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
3. Als tweede laag blijven de oude patroonchecks staan (fase-markers,
   placeholders, Notion-IDs, sleutels, playbook-sectiekoppen) plus de
   grootte-limiet voor SKILL.md — een generator-bug mag hier niet doorheen.

Draait offline: agent-architecture is niet nodig. Of de gecommitte output
ook echt bij de gepinde arch-commit hoort, bewaakt plugin-drift.yml.
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
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
    "NOTICE",
    "agent-architecture.lock.json",
    "plugin-manifest.json",
    ".github/dependabot.yml",
    ".github/workflows/zero-ip.yml",
    ".github/workflows/plugin-drift.yml",
    "scripts/check_zero_ip.py",
    "scripts/sync_plugin.py",
}

PATTERNS = [
    (re.compile(r"<!--\s*phase:"), "fase-marker (playbook-content!)"),
    (re.compile(r"\{\{[A-Z0-9_]+\}\}"), "prompt-placeholder"),
    (re.compile(r"notion\.so|notion\.site|api\.notion\.com"), "Notion-verwijzing"),
    (re.compile(r"\b[0-9a-f]{32}\b|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"), "UUID/database-ID"),
    (re.compile(r"atk_(?!\.\.\.)[A-Za-z0-9_-]{8,}"), "licentiesleutel"),
    (re.compile(r"secret_[A-Za-z0-9]{20,}|ntn_[A-Za-z0-9]{20,}|sk_live|whsec_"), "secret"),
    (re.compile(r"##\s*(Rol & Missie|Werkwijze per run|Escalatieprincipes|Session Output)"), "playbook-sectiekop"),
]

# Menukaart-skills zijn klein; groter = verdacht. 8KB laat ruimte voor de
# team-overzichtsskill — playbook-content wordt sowieso gevangen door de
# allowlist én de patroonchecks.
MAX_SKILL_BYTES = 8192

# De sha256's in het manifest zijn géén secrets/IDs, maar de UUID-regex
# hierboven zou de 64-hex-strings kunnen raken; het manifest en de lock zijn
# gestructureerde JSON die we apart valideren.
PATROON_VRIJ = {"plugin-manifest.json", "agent-architecture.lock.json", "scripts/check_zero_ip.py"}


def getrackte_bestanden():
    """Alles wat git kent (staged + gecommit) — niet de werkmap-afvalbak,
    anders faalt een lokale run op editor-swapbestanden. Buiten git (bv. een
    kale uitpak) vallen we terug op de werkmap."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            check=True, capture_output=True,
        ).stdout
        return sorted(p for p in out.decode("utf-8").split("\0") if p)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return sorted(
            p.relative_to(ROOT).as_posix()
            for p in ROOT.rglob("*")
            if p.is_file() and ".git/" not in p.as_posix().replace(str(ROOT), "")
        )


def sha256_van(path):
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


failures = []

# ── 1 + 2: manifest-allowlist ─────────────────────────────────────────────
try:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest_bestanden = manifest["bestanden"]
    assert isinstance(manifest_bestanden, dict) and manifest_bestanden
    manifest_versie = str(manifest["registryVersion"])
except (OSError, ValueError, KeyError, AssertionError) as e:
    print(f"❌ plugin-manifest.json ontbreekt of is ongeldig ({e}) — genereer met scripts/sync_plugin.py")
    sys.exit(1)

bestanden = getrackte_bestanden()
for rel in bestanden:
    if rel in REPO_EIGEN:
        continue
    verwacht = manifest_bestanden.get(rel)
    if verwacht is None:
        failures.append(f"{rel}: staat niet in plugin-manifest.json en is niet repo-eigen — niet door de generator gemaakt")
        continue
    if sha256_van(ROOT / rel) != verwacht:
        failures.append(f"{rel}: inhoud wijkt af van plugin-manifest.json — met de hand bewerkt of manifest verouderd")

aanwezig = set(bestanden)
for rel in manifest_bestanden:
    if rel not in aanwezig:
        failures.append(f"{rel}: staat in plugin-manifest.json maar ontbreekt in de repo")

# plugin.json-versie moet het manifest volgen (één release, één versie).
try:
    plugin_json = json.loads((ROOT / "plugins" / "agentic-team" / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if str(plugin_json.get("version")) != manifest_versie:
        failures.append(f"plugin.json version {plugin_json.get('version')} ≠ manifest registryVersion {manifest_versie}")
except (OSError, ValueError):
    failures.append("plugins/agentic-team/.claude-plugin/plugin.json ontbreekt of is geen JSON")

# ── 3: patroonchecks (tweede laag) ────────────────────────────────────────
for rel in bestanden:
    path = ROOT / rel
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        failures.append(f"{rel}: binair/onleesbaar bestand hoort hier niet")
        continue

    if path.name == "SKILL.md" and path.stat().st_size > MAX_SKILL_BYTES:
        failures.append(f"{rel}: {path.stat().st_size}B > {MAX_SKILL_BYTES}B — te groot voor een menukaart-skill")

    if rel in PATROON_VRIJ:
        continue

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
