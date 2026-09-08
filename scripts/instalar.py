#!/usr/bin/env python3
"""Instala as skills do pacote e registra versão, revisão e hashes verificáveis."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from exportar_metodo import SOURCE, digest, inventory, verify

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ".gestao-agil-2.json"


def revision(root: Path) -> str | None:
    if not (root / ".git").exists():
        return None
    try:
        return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def install(root: Path, destination: Path, check: bool = False) -> dict:
    source = (root / "skills").resolve()
    destination = destination.expanduser().resolve()
    if destination == source or source in destination.parents or destination in source.parents:
        raise ValueError("destino sobrepõe a fonte; instalações não são pastas de edição")
    manifest = verify(source)
    files = manifest["outputs"]
    receipt = {"schema": 1, "repository": SOURCE,
               "version": (root / "VERSION").read_text().strip(),
               "base_commit": revision(root),
               "content_sha256": digest(json.dumps(files, sort_keys=True).encode()),
               "files": files}
    # base_commit identifica a base Git; content_sha256 identifica os bytes, mesmo em teste local.
    receipt_path = destination / RECEIPT
    existing = sorted(destination.glob("ga2-*"))
    old = json.loads(receipt_path.read_text()) if receipt_path.exists() else None
    if existing:
        if not old:
            raise ValueError("skills existentes sem registro; preserve e migre essas pastas antes de instalar")
        if inventory(destination) != old["files"]:
            raise ValueError("instalação alterada localmente; leve as mudanças ao repositório antes de atualizar")
    elif old:
        raise ValueError("instalação incompleta: faltam skills registradas")
    if check:
        if not old or old["files"] != files or old["version"] != receipt["version"]:
            raise ValueError("instalação não corresponde ao pacote selecionado")
        return old
    if old and old["files"] == files and old["version"] == receipt["version"]:
        return old
    destination.mkdir(parents=True, exist_ok=True)
    names = sorted({name.split("/")[0] for name in files})
    # Prepare tudo antes de trocar a instalação. A reserva temporária permite rollback.
    with tempfile.TemporaryDirectory(prefix=".ga2-install-", dir=destination.parent) as tmp:
        staging = Path(tmp) / "new"
        backup = Path(tmp) / "old"
        staging.mkdir(); backup.mkdir()
        for name in names:
            shutil.copytree(source / name, staging / name)
        if inventory(staging) != files:
            raise ValueError("cópia divergiu da fonte")
        moved = []
        placed = []
        previous_receipt = receipt_path.read_bytes() if receipt_path.exists() else None
        try:
            for path in existing:
                path.rename(backup / path.name)
                moved.append(path.name)
            for name in names:
                (staging / name).rename(destination / name)
                placed.append(name)
            receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
            if inventory(destination) != files:
                raise ValueError("instalação divergiu da fonte")
        except BaseException:
            for name in placed:
                shutil.rmtree(destination / name)
            for name in moved:
                (backup / name).rename(destination / name)
            if previous_receipt is None:
                receipt_path.unlink(missing_ok=True)
            else:
                receipt_path.write_bytes(previous_receipt)
            raise
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destino", type=Path, action="append", default=[])
    for flag in ("todos", "claude", "codex", "cursor", "opencode", "agents"):
        parser.add_argument("--" + flag, action="store_true")
    parser.add_argument("--conferir", action="store_true")
    args = parser.parse_args()
    home = Path.home()
    targets = {"claude": home / ".claude/skills",
               "codex": Path(os.environ.get("CODEX_HOME", home / ".codex")) / "skills",
               "cursor": home / ".cursor/skills", "opencode": home / ".config/opencode/skills",
               "agents": home / ".agents/skills"}
    selected = args.destino + [path for name, path in targets.items() if args.todos or getattr(args, name)]
    if not selected:
        parser.error("escolha --destino ou um ambiente")
    for target in dict.fromkeys(path.expanduser().resolve() for path in selected):
        try:
            receipt = install(ROOT, target, args.conferir)
        except (OSError, ValueError, KeyError) as error:
            parser.exit(1, f"ERRO: {error}\n")
        print(f"OK: {target}; versão {receipt['version']}; conteúdo {receipt['content_sha256']}")


if __name__ == "__main__":
    main()
