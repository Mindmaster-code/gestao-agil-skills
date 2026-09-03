#!/usr/bin/env python3
"""Atualiza SHA256SUMS.txt para os arquivos-fonte do repositório."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "SHA256SUMS.txt"
SKIP_PARTS = {".git", ".claude-plugin", "_to_delete", "dist", "__pycache__"}


def tracked_files() -> list[Path]:
    return sorted(
        (
            path
            for path in ROOT.rglob("*")
            if path.is_file()
            and path != OUTPUT
            and not SKIP_PARTS.intersection(path.relative_to(ROOT).parts)
        ),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )


def main() -> None:
    lines = []
    for path in tracked_files():
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Atualizados {len(lines)} checksums.")


if __name__ == "__main__":
    main()
