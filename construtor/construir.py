#!/usr/bin/env python3
"""spec (+ .md preenchido) → HTML da forma canvas ou da forma documento.

  construir.py ID|spec.json --canvas [--md ARQ.md | --valores ARQ.json] [--modo normal|conferencia] [--debug] [--fontes link|nenhuma] --saida ARQ.html
  construir.py ID|spec.json --documento [--md ARQ.md | --valores ARQ.json] --saida ARQ.html
  construir.py --campos-md SKILL --saida CAMPOS.md
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canvaslib import REPO, SPECS  # noqa: E402
from canvaslib import html_canvas, md as mdlib  # noqa: E402


def carregar_spec(ref: str) -> dict:
    p = Path(ref)
    if not p.exists():
        p = SPECS / f"{ref}.json"
    return json.loads(p.read_text(encoding="utf-8"))


def valores_de(a, spec):
    if a.md:
        v = mdlib.valores(a.md, spec)
        if v.get("_sem_ancora"):
            print(f"  aviso: campos sem âncora em {a.md}: {v['_sem_ancora']}", file=sys.stderr)
        return v
    if a.valores:
        return json.loads(Path(a.valores).read_text(encoding="utf-8"))
    return {}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", nargs="?")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--canvas", action="store_true")
    g.add_argument("--documento", action="store_true")
    g.add_argument("--campos-md", metavar="SKILL")
    g.add_argument("--template", action="store_true", help="template.md mínimo e limpo do spec (regras simplificadas; pacote do aluno)")
    ap.add_argument("--md")
    ap.add_argument("--valores")
    ap.add_argument("--modo", default="normal", choices=["normal", "conferencia"])
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--fontes", default="link", choices=["link", "nenhuma"])
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()
    saida = Path(a.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)

    if a.campos_md:
        specs = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(SPECS.glob("*.json"))]
        specs = [s for s in specs if s.get("skill") == a.campos_md]
        saida.write_text(html_canvas.campos_md(specs, a.campos_md), encoding="utf-8")
        print(f"ok {saida} ({len(specs)} specs)")
        return

    if not a.spec:
        ap.error("informe o spec")
    spec = carregar_spec(a.spec)
    valores = valores_de(a, spec)
    meta = dict(valores.get("_meta", {}))
    if a.md:
        try:
            meta["md"] = str(Path(a.md).resolve().relative_to(REPO))
        except ValueError:
            meta["md"] = a.md

    if a.template:
        from canvaslib import template_md
        saida.write_text(template_md.montar(template_md.simplificar_regras(spec)), encoding="utf-8")
        print(f"ok {saida} · template mínimo · {len(spec['campos'])} campos")
        return

    if a.canvas:
        svg_txt = html_canvas.carregar_svg(spec)
        html = html_canvas.montar(spec, svg_txt, valores, modo=a.modo, fontes=a.fontes, debug=a.debug, meta=meta)
        saida.write_text(html, encoding="utf-8")
        cheios = sum(1 for c in spec["campos"] if valores.get(c["id"]))
        print(f"ok {saida} · {len(spec['campos'])} campos, {cheios} preenchidos · {saida.stat().st_size // 1024} KB")
        return

    if a.documento:
        from canvaslib import html_doc
        html = html_doc.montar(spec, valores, meta=meta)
        saida.write_text(html, encoding="utf-8")
        print(f"ok {saida} · documento · {saida.stat().st_size // 1024} KB")
        return

    ap.error("escolha --canvas, --documento ou --campos-md")


if __name__ == "__main__":
    main()
