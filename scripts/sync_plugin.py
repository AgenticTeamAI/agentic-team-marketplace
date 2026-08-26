#!/usr/bin/env python3
"""
Ververst deze marketplace-repo uit agent-architecture en zet de pin (s25).

  plugins/, .claude-plugin/marketplace.json, plugin-manifest.json
      ← installer/build_plugin.py, gedraaid op een schone uitpak van de
        gepinde commit (nooit op een werkmap met lokale wijzigingen)
  agent-architecture.lock.json ← commit + registryVersion

Zelfde patroon als arch-sync in de site en sync-schema in het dashboard:
alleen commits op origin/main van agent-architecture mogen als pin dienen —
CI checkt de pin uit op de remote en zou een lokale of branch-commit niet
accepteren. Dus: altijd ná de merge in arch, op de main-SHA, nooit vanaf een
feature-branch.

Volgorde bij een release: eerst de site deployen die de velden uit
`serverContract` in plugin-manifest.json serveert, dán dit script.

Gebruik:
    python3 scripts/sync_plugin.py                     # origin/main van ../agent-architecture
    python3 scripts/sync_plugin.py --commit <sha>      # specifieke commit (moet op origin/main staan)
    python3 scripts/sync_plugin.py --arch <pad>        # andere locatie van de arch-clone (of env ARCH_PATH)
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "agent-architecture.lock.json"
MANIFEST = "plugin-manifest.json"


def git(arch, *args):
    return subprocess.run(["git", "-C", str(arch), *args], check=True, capture_output=True, text=True).stdout


def uitpakken(tar_path, doel):
    """tarfile.extractall met het 'data'-filter (Python ≥ 3.12, of 3.8+ met de
    security-backport); oudere interpreters kennen het argument niet — daar
    is de tar afkomstig van ons eigen `git archive`, dus veilig genoeg."""
    with tarfile.open(tar_path) as tar:
        try:
            tar.extractall(doel, filter="data")
        except TypeError:
            tar.extractall(doel)


def main():
    ap = argparse.ArgumentParser(description="Bouw de plugin op een gepinde arch-main-commit en schrijf de lock")
    ap.add_argument("--arch", default=os.environ.get("ARCH_PATH", str(ROOT.parent / "agent-architecture")))
    ap.add_argument("--commit", default="origin/main")
    args = ap.parse_args()

    arch = Path(args.arch).resolve()
    if not (arch / ".git").exists():
        print(f"sync_plugin: geen git-repo op {arch}. Clone AgenticTeamAI/agent-architecture ernaast of geef --arch <pad>.")
        sys.exit(1)
    remote = git(arch, "remote", "get-url", "origin").strip()
    if not re.search(r"github\.com[/:]AgenticTeamAI/agent-architecture(\.git)?$", remote):
        print(f"sync_plugin: origin van {arch} is {remote}, geen AgenticTeamAI/agent-architecture.")
        sys.exit(1)

    git(arch, "fetch", "-q", "origin", "main")
    commit = git(arch, "rev-parse", "--verify", f"{args.commit}^{{commit}}").strip()
    op_main = subprocess.run(["git", "-C", str(arch), "merge-base", "--is-ancestor", commit, "origin/main"]).returncode == 0
    if not op_main:
        print(f"sync_plugin: {commit} staat niet op origin/main van agent-architecture. Merge eerst in arch en sync daarna op de main-SHA; CI accepteert geen andere pin.")
        sys.exit(1)

    # Schone uitpak van precies die commit: build_plugin.py leest core/agents.json
    # en installer/registry.py, dus beide komen uit dezelfde boom.
    with tempfile.TemporaryDirectory(prefix="arch-pin-") as tmp:
        tmp = Path(tmp)
        tar_path = tmp / "arch.tar"
        with open(tar_path, "wb") as f:
            subprocess.run(["git", "-C", str(arch), "archive", "--format=tar", commit, "core", "installer"], check=True, stdout=f)
        uitpakken(tar_path, tmp / "arch")
        registry = json.loads((tmp / "arch" / "core" / "agents.json").read_text(encoding="utf-8"))
        versie = registry["registryVersion"]

        out = tmp / "out"
        subprocess.run([sys.executable, str(tmp / "arch" / "installer" / "build_plugin.py"), "--output", str(out)], check=True)

        # Wat er in de repo hoort = precies de manifest-sleutels + het manifest
        # zelf; geen eigen lijst die uit de pas kan lopen met de generator.
        nieuw_manifest = json.loads((out / MANIFEST).read_text(encoding="utf-8"))
        nieuwe_paden = sorted(nieuw_manifest["bestanden"])
        oude_paden = []
        if (ROOT / MANIFEST).exists():
            try:
                oude_paden = sorted(json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))["bestanden"])
            except (ValueError, KeyError):
                oude_paden = []

        # Eerst schrijven (nieuwe bestanden + manifest), dán pas opruimen wat
        # niet meer in het manifest staat: een fout halverwege laat zo nooit
        # een repo zonder manifest achter.
        for rel in nieuwe_paden:
            doel = ROOT / rel
            doel.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(out / rel, doel)
        shutil.copyfile(out / MANIFEST, ROOT / MANIFEST)
        for rel in oude_paden:
            if rel not in nieuw_manifest["bestanden"] and (ROOT / rel).exists():
                (ROOT / rel).unlink()
        # Lege mappen onder plugins/ opruimen (een verwijderde agent of map).
        for d in sorted((ROOT / "plugins").rglob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()

    LOCK.write_text(json.dumps({
        "_doc": (
            "Gepinde commit van AgenticTeamAI/agent-architecture waaruit plugins/, "
            ".claude-plugin/marketplace.json en plugin-manifest.json zijn gegenereerd "
            "(installer/build_plugin.py, backlog s25). CI bouwt opnieuw op precies deze "
            "commit en faalt bij verschil, en faalt ook zodra de registry of de generator "
            "op arch-main verder is dan de pin. Bijwerken: python3 scripts/sync_plugin.py "
            "(altijd ná de merge in arch, op de main-SHA). Niet met de hand bewerken."
        ),
        "repository": "AgenticTeamAI/agent-architecture",
        "commit": commit,
        "registryVersion": versie,
        "bijgewerkt": date.today().isoformat(),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"✅ plugin gebouwd op {commit[:12]} (registry {versie}, buildHash {nieuw_manifest.get('buildHash')}); lock geschreven. Controleer met: python3 scripts/check_zero_ip.py")


if __name__ == "__main__":
    main()
