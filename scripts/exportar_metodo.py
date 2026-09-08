#!/usr/bin/env python3
"""Confere a integridade das skills mantidas neste repositório."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

MANIFEST = "procedencia.json"
SOURCE = "https://github.com/Mindmaster-code/gestao-agil-skills"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(root: Path, relative: str) -> Path:
    path = root / relative
    if not relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"caminho inválido: {relative}")
    path.resolve().relative_to(root.resolve())
    return path


def inventory(root: Path) -> dict[str, str]:
    files = {}
    for directory in sorted(root.glob("ga2-*")):
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError(f"skill precisa ser uma pasta real: {directory.name}")
        for path in sorted(directory.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"link não distribuível: {path.relative_to(root)}")
            if path.is_file():
                files[path.relative_to(root).as_posix()] = digest(path.read_bytes())
    if not files:
        raise ValueError("catálogo de skills vazio")
    return files


def seal_distribution(root: Path) -> dict:
    """Registra os bytes atuais; revisão de conteúdo precede esta atualização."""
    manifest = {"schema": 2, "source": SOURCE, "outputs": inventory(root)}
    (root / MANIFEST).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def verify(root: Path) -> dict:
    manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    if manifest.get("schema") != 2 or manifest.get("source") != SOURCE:
        raise ValueError("manifesto inválido: a fonte deve ser este repositório")
    actual = inventory(root)
    if actual != manifest["outputs"]:
        changed = sorted(k for k in actual.keys() | manifest["outputs"].keys()
                         if actual.get(k) != manifest["outputs"].get(k))
        raise ValueError(f"conteúdo divergiu do manifesto: {', '.join(changed[:5])}")
    resource = re.compile(r"`((?:references/|\.\./assets/modelos/)[^`<>\s]+\.(?:md|html|json|yaml))`")
    for relative in actual:
        path = safe_path(root, relative)
        if path.suffix != ".md":
            continue
        for target in resource.findall(path.read_text(encoding="utf-8")):
            resolved = (path.parent / target).resolve()
            resolved.relative_to(root.resolve())
            if not resolved.is_file():
                raise ValueError(f"referência ausente em {relative}: {target}")
    return manifest
