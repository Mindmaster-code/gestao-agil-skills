#!/usr/bin/env python3
"""Gera um arquivo ZIP reproduzível para validar ou enviar o plug-in."""

from __future__ import annotations

import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
OUTPUT_DIR = ROOT / "dist"
OUTPUT = OUTPUT_DIR / f"gestao-agil-2-plugin-{VERSION}.zip"
INCLUDE_ROOTS = (".codex-plugin", "assets", "skills", "docs", "tests")
INCLUDE_FILES = (
    "README.md",
    "LICENSE.md",
    "PRIVACY.md",
    "TERMS.md",
    "SUPPORT.md",
    "VERSION",
)


def included_files() -> list[Path]:
    files: list[Path] = []
    for directory in INCLUDE_ROOTS:
        files.extend(path for path in (ROOT / directory).rglob("*") if path.is_file())
    files.extend(ROOT / filename for filename in INCLUDE_FILES)
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def add_file(archive: ZipFile, path: Path) -> None:
    relative = path.relative_to(ROOT).as_posix()
    info = ZipInfo(relative, date_time=(2026, 9, 3, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, path.read_bytes())


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with ZipFile(OUTPUT, "w") as archive:
        for path in included_files():
            add_file(archive, path)

    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    checksum = OUTPUT.with_suffix(OUTPUT.suffix + ".sha256")
    checksum.write_text(f"{digest}  {OUTPUT.name}\n", encoding="utf-8")
    print(f"Pacote: {OUTPUT}")
    print(f"SHA-256: {digest}")


if __name__ == "__main__":
    main()
