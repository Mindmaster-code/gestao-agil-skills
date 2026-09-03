#!/usr/bin/env python3
"""Valida estrutura, quantidade e ausência de referências internas."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PLUGIN_MANIFEST = ROOT / ".codex-plugin/plugin.json"
SUBMISSION_CASES = ROOT / "tests/plugin-submission-cases.json"
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

if not PLUGIN_MANIFEST.is_file():
    fail("manifesto do plug-in ausente")

try:
    plugin = json.loads(PLUGIN_MANIFEST.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as error:
    fail(f"manifesto do plug-in inválido: {error}")

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
if plugin.get("name") != "gestao-agil-2":
    fail("nome inválido no manifesto do plug-in")
if plugin.get("version") != version:
    fail("versão do manifesto diverge de VERSION")
if plugin.get("skills") != "./skills/":
    fail("caminho de habilidades inválido no manifesto")
if "apps" in plugin or "mcpServers" in plugin:
    fail("o plug-in educacional não pode declarar Apps ou MCP")

interface = plugin.get("interface", {})
for field in ("composerIcon", "logo"):
    relative = interface.get(field)
    if not isinstance(relative, str) or not (ROOT / relative).is_file():
        fail(f"recurso visual ausente no manifesto: {field}")

try:
    cases = json.loads(SUBMISSION_CASES.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as error:
    fail(f"casos de submissão inválidos: {error}")

case_types = [case.get("type") for case in cases]
if case_types.count("positive") != 5 or case_types.count("negative") != 3:
    fail("esperados cinco testes positivos e três negativos")

trails = (ROOT / "docs/TRILHAS.md").read_text(encoding="utf-8")
documented = set(re.findall(r"`(ga2-[a-z0-9-]+)`", trails))
expected = {directory.name for directory in directories}
if documented != expected:
    fail("o mapa das trilhas não cobre exatamente as 30 habilidades")

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

print("OK: plug-in, 30 habilidades, seis trilhas e oito testes válidos.")
