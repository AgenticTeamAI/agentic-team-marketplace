#!/usr/bin/env python3
"""
Ververst deze marketplace-repo uit agent-architecture en zet de pin (s25).

  plugins/, .claude-plugin/marketplace.json, plugin-manifest.json
      ← installer/build_plugin.py, gedraaid op een schone uitpak van de
        gepinde commit (nooit op een werkmap met lokale wijzigingen)
  agent-architecture.lock.json ← commit + registryVersion

Zelfde patroon als arch-sync in de site en sync-schema in het dashboard:
alleen commits op origin/main van agent-architecture mogen als pin dienen —
CI checkt de pin uit op de remote en zou een lokale commit niet vinden.

Gebruik:
    python3 scripts/sync_plugin.py                     # origin/main van ../agent-architecture
    python3 scripts/sync_plugin.py --commit <sha>      # specifieke commit (moet op origin/main staan)
    python3 scripts/sync_plugin.py --arch <pad>        # andere locatie van de arch-clone (of env ARCH_PATH)
    python3 scripts/sync_plugin.py --commit <sha> --buiten-main
        # alleen om een PR voor te bereiden vóór de arch-merge; CI blijft
        # rood tot de pin opnieuw op een main-commit staat.
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

ROOT = Path(__file__).parent.parent
LOCK = ROOT / "agent-architecture.lock.json"
GEGENEREERD = ["plugins", ".claude-plugin", "plugin-manifest.json"]


def git(arch, *args):
    return subprocess.run(["git", "-C", str(arch), *args], check=True, capture_output=True, text=True).stdout


def main():
    ap = argparse.ArgumentParser(description="Bouw de plugin op een gepinde arch-commit en schrijf de lock")
    ap.add_argument("--arch", default=os.environ.get("ARCH_PATH", str(ROOT.parent / "agent-architecture")))
    ap.add_argument("--commit", default="origin/main")
    ap.add_argument("--buiten-main", action="store_true", help="sta een commit toe die (nog) niet op origin/main staat")
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
        if not args.buiten_main:
            print(f"sync_plugin: {commit} staat niet op origin/main van agent-architecture; CI zou de pin niet accepteren. (--buiten-main om toch te bouwen)")
            sys.exit(1)
        print(f"⚠️  {commit} staat NIET op origin/main — bouw gaat door, maar CI blijft rood tot de pin op main staat.")

    # Schone uitpak van precies die commit: build_plugin.py leest core/agents.json
    # en installer/registry.py, dus beide komen uit dezelfde boom.
    with tempfile.TemporaryDirectory(prefix="arch-pin-") as tmp:
        tmp = Path(tmp)
        tar_path = tmp / "arch.tar"
        with open(tar_path, "wb") as f:
            subprocess.run(["git", "-C", str(arch), "archive", "--format=tar", commit, "core", "installer"], check=True, stdout=f)
        with tarfile.open(tar_path) as tar:
            tar.extractall(tmp / "arch", filter="data")
        registry = json.loads((tmp / "arch" / "core" / "agents.json").read_text(encoding="utf-8"))
        versie = registry["registryVersion"]

        out = tmp / "out"
        subprocess.run([sys.executable, str(tmp / "arch" / "installer" / "build_plugin.py"), "--output", str(out)], check=True)

        for naam in GEGENEREERD:
            doel = ROOT / naam
            if doel.is_dir():
                shutil.rmtree(doel)
            elif doel.exists():
                doel.unlink()
            bron = out / naam
            if bron.is_dir():
                shutil.copytree(bron, doel)
            else:
                shutil.copy2(bron, doel)

    LOCK.write_text(json.dumps({
        "_doc": (
            "Gepinde commit van AgenticTeamAI/agent-architecture waaruit plugins/, "
            ".claude-plugin/marketplace.json en plugin-manifest.json zijn gegenereerd "
            "(installer/build_plugin.py, backlog s25). CI bouwt opnieuw op precies deze "
            "commit en faalt bij verschil, en faalt ook zodra de registry of de generator "
            "op arch-main verder is dan de pin. Bijwerken: python3 scripts/sync_plugin.py. "
            "Niet met de hand bewerken."
        ),
        "repository": "AgenticTeamAI/agent-architecture",
        "commit": commit,
        "registryVersion": versie,
        "bijgewerkt": date.today().isoformat(),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"✅ plugin gebouwd op {commit[:12]} (registry {versie}); lock geschreven. Controleer met: python3 scripts/check_zero_ip.py")


if __name__ == "__main__":
    main()
