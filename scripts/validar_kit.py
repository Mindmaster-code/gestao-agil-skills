#!/usr/bin/env python3
"""Confere o contrato do kit definitivo e suas referências nas skills."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "modelos" / "kit"


def fail(message: str) -> None:
    raise SystemExit(f"ERRO: {message}")


def main() -> None:
    manifesto = json.loads((KIT / "kit.json").read_text(encoding="utf-8"))
    migracao = json.loads((KIT / "migracao.json").read_text(encoding="utf-8"))
    modelos = manifesto.get("modelos")
    if not isinstance(modelos, list) or len(modelos) != 28:
        fail("o manifesto deve conter exatamente 28 modelos")
    codigos = [modelo.get("codigo") for modelo in modelos]
    if len(set(codigos)) != 28 or any(not isinstance(codigo, str) for codigo in codigos):
        fail("os 28 códigos do manifesto devem ser únicos")
    for modelo in modelos:
        for chave in ("arquivo_html", "pdf", "docx"):
            rel = modelo.get(chave)
            if not isinstance(rel, str) or not (ROOT / "modelos" / rel).is_file():
                fail(f"arquivo ausente para {modelo['codigo']}: {chave}")
        for skill in [modelo.get("skill_primaria"), *modelo.get("skills_compartilhadas", [])]:
            if skill is None:
                continue
            path = ROOT / "skills" / skill / "SKILL.md"
            if not path.is_file():
                fail(f"skill sem código oficial {modelo['codigo']}: {skill}")
            linhas = path.read_text(encoding="utf-8").splitlines()
            contrato = next((linha for linha in linhas if "Modelo oficial do aluno:" in linha), "")
            if modelo["codigo"] not in contrato:
                fail(f"skill sem código oficial {modelo['codigo']}: {skill}")
    if not migracao.get("antigo_para_codigo"):
        fail("mapa de migração ausente")
    if not set(migracao["antigo_para_codigo"].values()).issubset(set(codigos)):
        fail("mapa de migração aponta para código inexistente")
    print(f"OK: kit {manifesto['versao']}; 28 modelos, arquivos e referências nas skills conferidos.")


if __name__ == "__main__":
    main()
