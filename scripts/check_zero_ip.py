#!/usr/bin/env python3
"""
Menukaart-check (s25): faalt als er iets in deze publieke repo staat dat niet
door de generator is gemaakt of niet expliciet repo-eigen is.

Sinds s25 (26-08-2026) is deze check een ALLOWLIST, geen blacklist:

1. Elk getrackt bestand staat óf in plugin-manifest.json (gegenereerd door
   installer/build_plugin.py in agent-architecture) met een kloppende sha256,
   óf in REPO_EIGEN hieronder. Alles anders is een incident: het is niet uit
   de registry gegenereerd en hoort dus niet in de menukaart.
2. Elk bestand uit het manifest bestaat ook echt (geen halve release).
3. Als tweede laag blijven de patroonchecks staan (fase-markers,
   placeholders, Notion-IDs, sleutels, playbook-sectiekoppen) plus de
   grootte-limiet voor SKILL.md. Dezelfde lijst draait al in de generator
   (build_plugin.py, MENUKAART_PATRONEN) — hier als onafhankelijke laag.

Draait offline: agent-architecture is niet nodig. Of de gecommitte output
ook echt bij de gepinde arch-commit hoort, bewaakt plugin-drift.yml.
Vereist een git-clone: de lijst te controleren bestanden komt uit git.
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "plugin-manifest.json"

# s32: op een Windows-console met codepage 1252 laat print("✅ …") het
# script met een UnicodeEncodeError omvallen — dan lijkt een schone check
# gefaald. Zelfde aanpak als installer/registry.py in agent-architecture:
# encoding met rust laten, alleen de foutafhandeling op "replace".
for _stream in (sys.stdout, sys.stderr):
    _reconfigure = getattr(_stream, "reconfigure", None)
    if _reconfigure is None:
        continue
    try:
        "✅".encode(_stream.encoding or "utf-8")
    except (UnicodeEncodeError, LookupError):
        try:
            _reconfigure(errors="replace")
        except (ValueError, OSError):
            pass

# Repo-eigen bestanden: alles wat níet uit de generator komt en hier toch
# thuishoort. Bewust een korte, letterlijke lijst (geen globs voor content-
# mappen): een nieuw bestand buiten deze lijst moet een bewuste keuze zijn.
REPO_EIGEN = {
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "LICENSE.en.md",
    "NOTICE",
    "CONTRIBUTING.md",
    ".gitattributes",
    ".gitignore",
    "agent-architecture.lock.json",
    "plugin-manifest.json",
    ".github/dependabot.yml",
    ".github/pull_request_template.md",
    ".github/workflows/zero-ip.yml",
    ".github/workflows/plugin-drift.yml",
    ".github/workflows/dco.yml",
    "scripts/check_zero_ip.py",
    "scripts/sync_plugin.py",
}

# De literals zijn zo geschreven dat ze zichzelf niet matchen: dit bestand
# wordt door deze check ook gelezen, en een uitzonderingslijst voor het eigen
# script is precies het gat dat je niet wilt.
PATTERNS = [
    (re.compile(r"<!--\s*phase:"), "fase-marker (playbook-content!)"),
    (re.compile(r"\{\{[A-Z0-9_]+\}\}"), "prompt-placeholder"),
    (re.compile(r"notion\.so|notion\.site|api\.notion\.com"), "Notion-verwijzing"),
    (re.compile(r"\b[0-9a-f]{32}\b|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"), "UUID/database-ID"),
    (re.compile(r"atk_(?!\.\.\.)[A-Za-z0-9_-]{8,}"), "licentiesleutel"),
    (re.compile(r"secret_[A-Za-z0-9]{20,}|ntn_[A-Za-z0-9]{20,}|sk_" + "live|whsec" + "_"), "secret"),
    (re.compile(r"##\s*(Rol & Missie|Werkwijze per run|Escalatieprincipes|Session Output)"), "playbook-sectiekop"),
]

# Menukaart-skills zijn klein; groter = verdacht. 8KB laat ruimte voor de
# team-overzichtsskill — playbook-content wordt sowieso gevangen door de
# allowlist én de patroonchecks.
MAX_SKILL_BYTES = 8192


def getrackte_bestanden():
    """Alles wat git kent (staged + gecommit + niet-genegeerde nieuwe
    bestanden) — niet de werkmap-afvalbak, anders faalt een lokale run op
    editor-swapbestanden. Zonder git-clone is er geen betrouwbare lijst:
    dan stoppen we, in plaats van stil op een rglob terug te vallen."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            check=True, capture_output=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"❌ Menukaart-check vereist een git-clone van deze repo ({e}).")
        sys.exit(1)
    # Een geneste git-checkout (CI zet agent-architecture/ in de werkmap) komt
    # bij --others als één map-entry terug; dat is geen bestand van deze repo.
    return sorted(p for p in out.decode("utf-8").split("\0") if p and not (ROOT / p).is_dir())


failures = []

# ── 1 + 2: manifest-allowlist ─────────────────────────────────────────────
try:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest_bestanden = manifest["bestanden"]
    if not isinstance(manifest_bestanden, dict) or not manifest_bestanden:
        raise ValueError("'bestanden' ontbreekt of is leeg")
    manifest_versie = str(manifest["registryVersion"])
except (OSError, ValueError, KeyError, TypeError) as e:
    print(f"❌ plugin-manifest.json ontbreekt of is ongeldig ({e}) — genereer met scripts/sync_plugin.py")
    sys.exit(1)

bestanden = getrackte_bestanden()
inhoud = {}  # rel → bytes; één read per bestand voor hash, grootte en tekst
for rel in bestanden:
    try:
        inhoud[rel] = (ROOT / rel).read_bytes()
    except FileNotFoundError:
        # Getrackt in git maar weg uit de werkmap (verwijderd, nog niet gestaged).
        failures.append(f"{rel}: staat in git maar ontbreekt in de werkmap")
    except (PermissionError, IsADirectoryError) as e:
        failures.append(f"{rel}: onleesbaar ({e.__class__.__name__})")

for rel, data in inhoud.items():
    if rel in REPO_EIGEN:
        continue
    verwacht = manifest_bestanden.get(rel)
    if verwacht is None:
        failures.append(f"{rel}: staat niet in plugin-manifest.json en is niet repo-eigen — niet door de generator gemaakt")
    elif "sha256:" + hashlib.sha256(data).hexdigest() != verwacht:
        failures.append(f"{rel}: inhoud wijkt af van plugin-manifest.json — met de hand bewerkt of manifest verouderd")

for rel in manifest_bestanden:
    if rel not in inhoud:
        failures.append(f"{rel}: staat in plugin-manifest.json maar ontbreekt in de repo")

# plugin.json-versie moet het manifest volgen (één release, één versie).
try:
    plugin_json = json.loads((ROOT / "plugins" / "agentic-team" / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if str(plugin_json.get("version")) != manifest_versie:
        failures.append(f"plugin.json version {plugin_json.get('version')} ≠ manifest registryVersion {manifest_versie}")
except (OSError, ValueError):
    failures.append("plugins/agentic-team/.claude-plugin/plugin.json ontbreekt of is geen JSON")

# ── 3: patroonchecks (tweede laag) ────────────────────────────────────────
for rel, data in inhoud.items():
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        failures.append(f"{rel}: binair/onleesbaar bestand hoort hier niet")
        continue

    if rel.endswith("SKILL.md") and len(data) > MAX_SKILL_BYTES:
        failures.append(f"{rel}: {len(data)}B > {MAX_SKILL_BYTES}B — te groot voor een menukaart-skill")

    for pattern, label in PATTERNS:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            failures.append(f"{rel}:{line}: {label} — '{match.group(0)[:40]}'")

for failure in failures:
    print(f"❌ {failure}")

if failures:
    print(f"\n❌ Menukaart-check gefaald: {len(failures)} bevinding(en)")
    sys.exit(1)

print(f"✅ Menukaart-check schoon: {len(manifest_bestanden)} gegenereerde bestanden (registry {manifest_versie}), {len(bestanden) - len(manifest_bestanden)} repo-eigen")
