#!/usr/bin/env python3
"""Gera um arquivo ZIP reproduzível para validar ou enviar o plug-in."""

from __future__ import annotations

import argparse
import hashlib
import io
import re
import subprocess
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
OUTPUT_DIR = ROOT / "dist"
OUTPUT = OUTPUT_DIR / f"gestao-agil-2-plugin-{VERSION}.zip"
INCLUDE_ROOTS = (".codex-plugin", ".claude-plugin", "assets", "skills", "docs", "tests", "construtor")
SKIP_PARTS = {"__pycache__", ".git"}
INCLUDE_FILES = (
    "README.md",
    "LICENSE.md",
    "PRIVACY.md",
    "TERMS.md",
    "SUPPORT.md",
    "VERSION",
    "instalar.sh",
    "instalar.ps1",
)


def included_files() -> list[Path]:
    files: list[Path] = []
    for directory in INCLUDE_ROOTS:
        source = ROOT / directory
        if not source.is_dir():
            raise FileNotFoundError(f"Pasta ausente: {source}")
        files.extend(path for path in source.rglob("*")
                     if path.is_file() and not SKIP_PARTS.intersection(path.relative_to(ROOT).parts))
    files.extend(ROOT / filename for filename in INCLUDE_FILES)
    for path in files:
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Arquivo ausente ou link não empacotável: {path}")
        path.resolve().relative_to(ROOT.resolve())
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def add_file(archive: ZipFile, path: Path) -> None:
    relative = path.relative_to(ROOT).as_posix()
    info = ZipInfo(relative, date_time=(2026, 9, 3, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, path.read_bytes())


def package(output_dir: Path, source: Path) -> tuple[Path, str]:
    # Um ZIP novo só nasce depois de conferir a fonte atual, não apenas os hashes antigos.
    subprocess.run([sys.executable, str(ROOT / "scripts/validar.py"), "--fonte", str(source)], check=True)
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", VERSION):
        raise ValueError("VERSION precisa conter uma versão semântica válida")
    buffer = io.BytesIO()
    with ZipFile(buffer, "w") as archive:
        for path in included_files():
            add_file(archive, path)
    data = buffer.getvalue()
    digest = hashlib.sha256(data).hexdigest()
    output = output_dir / OUTPUT.name
    checksum = output.with_suffix(output.suffix + ".sha256")
    expected = f"{digest}  {output.name}\n".encode()
    # Compare antes de gravar: uma versão existente é imutável.
    for path, content in ((output, data), (checksum, expected)):
        if path.exists() and path.read_bytes() != content:
            raise ValueError(f"Versão existente tem conteúdo diferente: {path}; use uma nova versão")
    output_dir.mkdir(parents=True, exist_ok=True)
    for path, content in ((output, data), (checksum, expected)):
        if not path.exists():
            with path.open("xb") as stream:
                stream.write(content)
    return output, digest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fonte", type=Path, required=True, help="projeto canônico atual; obrigatório para impedir pacote desatualizado")
    parser.add_argument("--saida-dir", type=Path, default=OUTPUT_DIR,
                        help="Destino; use uma pasta temporária para testar antes da versão final")
    args = parser.parse_args()
    output, digest = package(args.saida_dir, args.fonte)
    print(f"Pacote: {output}")
    print(f"SHA-256: {digest}")


if __name__ == "__main__":
    main()
