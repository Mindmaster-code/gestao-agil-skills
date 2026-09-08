#!/usr/bin/env python3
"""Gera modelos usando exclusivamente o construtor e specs deste repositório."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONSTRUTOR = ROOT / "construtor"
SKILLS = ROOT / "skills"


def modelos() -> None:
    manifesto = json.loads((CONSTRUTOR / "oficiais" / "manifesto.json").read_text(encoding="utf-8"))
    construir = [sys.executable, str(CONSTRUTOR / "construir.py")]
    por_skill: dict[str, list[dict]] = {}
    for it in manifesto["oficiais"]:
        por_skill.setdefault(it["skill"], []).append(it)
    n = 0
    for skill, itens in por_skill.items():
        pasta = SKILLS / skill / "assets" / "modelos"
        if not (SKILLS / skill).is_dir():
            print(f"  aviso: skill {skill} não está em skills/; pulada")
            continue
        if pasta.exists():
            shutil.rmtree(pasta)
        pasta.mkdir(parents=True)
        itens.sort(key=lambda i: (not i["padrao"], i["id"]))
        for k, it in enumerate(itens):
            sid = it["id"]
            sp = json.loads((CONSTRUTOR / "specs" / f"{sid}.json").read_text(encoding="utf-8"))
            subprocess.run(construir + [sid, "--canvas", "--saida", str(pasta / f"canvas-{sid}.html")], check=True, capture_output=True)
            subprocess.run(construir + [sid, "--template", "--saida", str(pasta / f"template-{sid}.md")], check=True, capture_output=True)
            le = sp.get("leitura") or {}
            if le.get("capitulos") and not le.get("sem_documento"):
                nome = "documento.html" if k == 0 else f"documento-{sid}.html"
                subprocess.run(construir + [sid, "--documento", "--saida", str(pasta / nome)], check=True, capture_output=True)
            n += 1
        subprocess.run(construir + ["--campos-md", skill, "--saida", str(pasta / "CAMPOS.md")], check=True, capture_output=True)
    print(f"modelos gerados: {n} canvas em {len(por_skill)} skills")



def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--modelos", action="store_true", required=True)
    parser.parse_args()
    modelos()


if __name__ == "__main__":
    main()
