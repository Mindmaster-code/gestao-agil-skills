#!/usr/bin/env python3
"""Exporta o método canônico com adaptações públicas explícitas e rastreáveis."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

MANIFEST = "procedencia.json"
PUBLIC_ONLY = {"ga2-abrir-projeto"}
PRIVATE = re.compile(r"/home/|~/|operacao/|ceo-agent|delivery-agent|marketing-agent|\b(?:Denisson|Otto|Clara|Maya|Ciro|Duda|Bia|Caio|Vera)\b")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def public_text(text: str, relative: str) -> None:
    match = PRIVATE.search(text)
    if match:
        raise ValueError(f"referência interna em {relative}: {match.group()}")


def safe_path(root: Path, relative: str) -> Path:
    path = root / relative
    if not relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"caminho inválido: {relative}")
    path.resolve().relative_to(root.resolve())
    return path


def prepare(project: Path, names: set[str]) -> tuple[dict[str, bytes], dict]:
    source = project / ".claude/skills"
    if not source.is_dir():
        raise ValueError("--fonte deve apontar ao projeto com skills canônicas em .claude/skills; pacotes legados de GPTs não são fonte")
    config = project / "laboratorio/publicacao"
    files: dict[str, bytes] = {}
    entries = {}
    for name in sorted(names):
        if not re.fullmatch(r"ga2-[a-z0-9-]+", name):
            raise ValueError(f"nome inválido: {name}")
        directory = source / name
        adaptation_path = config / "adaptacoes" / f"{name}.json"
        adaptation_bytes = adaptation_path.read_bytes()
        adaptation = json.loads(adaptation_bytes)
        if adaptation.get("skill") != name:
            raise ValueError(f"adaptação de outra skill: {name}")
        required = {p.name for p in directory.iterdir() if p.name in {"SKILL.md", "template.md", "checklist.md"}}
        required.update(p.relative_to(directory).as_posix() for p in (directory / "references").glob("*.md"))
        if "SKILL.md" not in required or "template.md" not in required:
            raise ValueError(f"skill canônica incompleta: {name}")
        adaptations = adaptation.get("files", {})
        if set(adaptations) != required:
            raise ValueError(f"recurso sem adaptação ou inexistente em {name}: {sorted(required ^ set(adaptations))}")
        inputs = {}
        for relative in sorted(required):
            path = safe_path(directory, relative)
            raw = path.read_bytes()
            inputs[path.relative_to(project).as_posix()] = digest(raw)
            text = raw.decode("utf-8")
            for change in adaptations[relative]["replacements"]:
                before, after = change["from"], change["to"]
                if not before or not change.get("reason"):
                    raise ValueError(f"adaptação sem texto ou motivo: {name}/{relative}")
                if before not in text:
                    raise ValueError(f"adaptação desatualizada em {name}/{relative}: {before[:100]!r}")
                text = text.replace(before, after)
            if relative == "SKILL.md":
                text = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S).lstrip("\n")
                filename = "metodo.md"
            else:
                filename = Path(relative).name
            output = f"{name}/references/{filename}"
            public_text(text, output)
            files[output] = text.encode("utf-8")
        # Exemplos operacionais não são anonimizações: só o exemplo didático separado é exportado.
        example_path = safe_path(config, adaptation["example"])
        example = example_path.read_bytes()
        if not re.search(r"fict[ií]ci[oa]", example.decode(), re.I):
            raise ValueError(f"exemplo sem indicação de ficção: {name}")
        public_text(example.decode(), f"{name}/references/exemplo.md")
        files[f"{name}/references/exemplo.md"] = example
        inputs[adaptation_path.relative_to(project).as_posix()] = digest(adaptation_bytes)
        inputs[example_path.relative_to(project).as_posix()] = digest(example)
        entries[name] = {"origin": "canonical-skill", "inputs": inputs,
                         "checklist": "references/checklist.md" if "checklist.md" in required else "criteria-in-method",
                         "example": "independent-fiction"}
    manifest = {"schema": 1, "source": "project-skills", "entries": entries,
                "outputs": {name: digest(data) for name, data in sorted(files.items())}}
    return files, manifest


def write_export(output: Path, files: dict[str, bytes], manifest: dict) -> None:
    for relative, data in sorted(files.items()):
        path = safe_path(output, relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    (output / MANIFEST).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def seal_distribution(output: Path, manifest: dict) -> None:
    """Inclui roteadores e modelos públicos no gate; não declara origem interna para exceções."""
    manifest["public_only"] = sorted(PUBLIC_ONLY)
    manifest["outputs"] = {
        path.relative_to(output).as_posix(): digest(path.read_bytes())
        for directory in sorted(output.glob("ga2-*")) if directory.is_dir()
        for path in sorted(directory.rglob("*")) if path.is_file()
    }
    (output / MANIFEST).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def verify(output: Path, project: Path | None = None) -> None:
    manifest = json.loads((output / MANIFEST).read_text(encoding="utf-8"))
    if manifest.get("schema") != 1 or manifest.get("source") != "project-skills":
        raise ValueError("manifesto de procedência inválido")
    expected_names = set(manifest["entries"]) | set(manifest.get("public_only", []))
    actual_names = {path.name for path in output.glob("ga2-*") if path.is_dir()}
    if actual_names != expected_names:
        raise ValueError("catálogo divergiu do manifesto de procedência")
    for relative, expected in manifest["outputs"].items():
        path = safe_path(output, relative)
        if not path.is_file() or digest(path.read_bytes()) != expected:
            raise ValueError(f"arquivo divergiu do manifesto: {relative}")
    actual_files = {path.relative_to(output).as_posix() for name in actual_names
                    for path in (output / name).rglob("*") if path.is_file()}
    if actual_files != set(manifest["outputs"]):
        raise ValueError("arquivo fora do manifesto de procedência")
    # Só caminhos declarados como recursos do pacote; citações de aula e arquivos do caso não são dependências.
    resource = re.compile(r"`((?:references/|\.\./assets/modelos/)[^`<>\s]+\.(?:md|html|json|yaml))`")
    for relative in manifest["outputs"]:
        path = output / relative
        if path.suffix != ".md":
            continue
        for target in resource.findall(path.read_text(encoding="utf-8")):
            resolved = (path.parent / target).resolve()
            resolved.relative_to(output.resolve())
            if not resolved.is_file():
                raise ValueError(f"referência ausente em {relative}: {target}")
    if project is not None:
        names = {path.name for path in (project / ".claude/skills").glob("ga2-*") if path.is_dir()}
        if names != set(manifest["entries"]):
            raise ValueError("catálogo da fonte divergiu; revise a distribuição")
        for entry in manifest["entries"].values():
            for relative, expected in entry["inputs"].items():
                path = safe_path(project, relative)
                if not path.is_file() or digest(path.read_bytes()) != expected:
                    raise ValueError(f"fonte divergiu; regenere a distribuição: {relative}")
        files, _ = prepare(project, names)
        for relative, data in files.items():
            if (output / relative).read_bytes() != data:
                raise ValueError(f"exportação divergiu da fonte: {relative}")
