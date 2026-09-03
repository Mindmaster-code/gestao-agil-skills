#!/usr/bin/env python3
"""Valida estrutura, quantidade e ausência de referências internas."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
FORBIDDEN = (
    "/home/ubuntu",
    "~/",
    "operacao/",
    "gestor-agil-agent",
    "ceo-agent",
    "delivery-agent",
    "marketing-agent",
    "Denisson",
    "Otto",
    "Clara",
    "Maya",
    "Ciro",
    "Duda",
    "Bia",
)


def fail(message: str) -> None:
    print(f"ERRO: {message}", file=sys.stderr)
    raise SystemExit(1)


directories = sorted(path for path in SKILLS.glob("ga2-*") if path.is_dir())
if len(directories) != 30:
    fail(f"esperadas 30 skills; encontradas {len(directories)}")

for directory in directories:
    required = (
        directory / "SKILL.md",
        directory / "references/metodo.md",
        directory / "references/fontes.md",
        directory / "assets/template-artefato.html",
        directory / "agents/openai.yaml",
    )
    for path in required:
        if not path.is_file():
            fail(f"arquivo ausente: {path.relative_to(ROOT)}")

    content = (directory / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: .+\n---\n", content)
    if not match:
        fail(f"cabeçalho inválido: {directory.name}")
    if match.group(1) != directory.name:
        fail(f"nome do cabeçalho diverge da pasta: {directory.name}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.name == "validar.py":
        continue
    if path.suffix.lower() not in {".md", ".html", ".yaml", ".yml", ".txt"}:
        continue
    content = path.read_text(encoding="utf-8", errors="replace")
    for marker in FORBIDDEN:
        if marker in content:
            fail(f"referência interna {marker!r} em {path.relative_to(ROOT)}")
    if "TODO" in content or "[TODO" in content:
        fail(f"marcador pendente em {path.relative_to(ROOT)}")

print("OK: 30 skills válidas e sem referências internas conhecidas.")

