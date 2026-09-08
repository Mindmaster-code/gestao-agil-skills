#!/usr/bin/env python3
"""Copia as skills canônicas sem reescrever método, instruções ou recursos."""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil

from exportar_metodo import verify

ROOT = Path(__file__).resolve().parents[1]


def build(output: Path) -> None:
    source = ROOT / "skills"
    verify(source)
    source, output = source.resolve(), output.resolve()
    if output == source:
        return
    if source in output.parents or output in source.parents:
        raise ValueError("destino sobrepõe a fonte")
    if output.exists() and any(output.iterdir()):
        raise ValueError("use um destino vazio; não sobrescreva uma distribuição")
    shutil.copytree(source, output, dirs_exist_ok=True)
    verify(output)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destino", type=Path, required=True)
    args = parser.parse_args()
    build(args.destino)
    print(f"Skills copiadas e conferidas em {args.destino}")


if __name__ == "__main__":
    main()
