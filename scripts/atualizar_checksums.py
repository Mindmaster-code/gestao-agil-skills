#!/usr/bin/env python3
"""Atualiza SHA256SUMS.txt para os arquivos-fonte do repositório."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

from exportar_metodo import seal_distribution


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "SHA256SUMS.txt"
def tracked_files() -> list[Path]:
    result = subprocess.run(
        ("git", "ls-files", "-z"),
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [
        ROOT / relative
        for relative in sorted(
            (Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item),
            key=lambda path: path.as_posix(),
        )
        if ROOT / relative != OUTPUT
    ]


def index_bytes(path: Path) -> bytes:
    relative = path.relative_to(ROOT).as_posix()
    return subprocess.run(
        ("git", "show", f":{relative}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def main() -> None:
    seal_distribution(ROOT / "skills")
    lines = []
    for path in tracked_files():
        digest = hashlib.sha256(index_bytes(path)).hexdigest()
        lines.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Atualizados {len(lines)} checksums.")


if __name__ == "__main__":
    main()
