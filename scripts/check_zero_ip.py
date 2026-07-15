#!/usr/bin/env python3
"""
Nul-IP-check: faalt als er iets in deze publieke repo staat dat op
playbook-content, interne IDs of secrets lijkt.

Deze repo mag uitsluitend menukaart-tekst bevatten (naam + beschrijving +
ophaal-instructie). De playbooks zelf leven server-side; elk spoor daarvan
hier is een incident.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

PATTERNS = [
    (re.compile(r"<!--\s*phase:"), "fase-marker (playbook-content!)"),
    (re.compile(r"\{\{[A-Z0-9_]+\}\}"), "prompt-placeholder"),
    (re.compile(r"notion\.so|notion\.site|api\.notion\.com"), "Notion-verwijzing"),
    (re.compile(r"\b[0-9a-f]{32}\b|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"), "UUID/database-ID"),
    (re.compile(r"atk_(?!\.\.\.)[A-Za-z0-9_-]{8,}"), "licentiesleutel"),
    (re.compile(r"secret_[A-Za-z0-9]{20,}|ntn_[A-Za-z0-9]{20,}|sk_live|whsec_"), "secret"),
    (re.compile(r"##\s*(Rol & Missie|Werkwijze per run|Escalatieprincipes|Session Output)"), "playbook-sectiekop"),
]

MAX_SKILL_BYTES = 4096  # menukaart-skills zijn klein; groter = verdacht

failures = []

for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or ".git/" in str(path):
        continue
    rel = path.relative_to(ROOT)
    if str(rel).startswith(".git"):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        failures.append(f"{rel}: binair/onleesbaar bestand hoort hier niet")
        continue

    if path.name == "SKILL.md" and path.stat().st_size > MAX_SKILL_BYTES:
        failures.append(f"{rel}: {path.stat().st_size}B > {MAX_SKILL_BYTES}B — te groot voor een menukaart-skill")

    if path.name == "check_zero_ip.py":
        continue  # de patronen hieronder staan letterlijk in dit script

    for pattern, label in PATTERNS:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            failures.append(f"{rel}:{line}: {label} — '{match.group(0)[:40]}'")

for failure in failures:
    print(f"❌ {failure}")

if failures:
    print(f"\n❌ Nul-IP-check gefaald: {len(failures)} bevinding(en)")
    sys.exit(1)

print("✅ Nul-IP-check schoon")
