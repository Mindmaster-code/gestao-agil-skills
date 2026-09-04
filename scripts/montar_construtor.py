#!/usr/bin/env python3
"""Leva o construtor de canvas para o pacote do aluno e gera os modelos de cada skill.

Duas etapas, nesta ordem (a segunda depende de `skills/` já montada por montar_distribuicao.py):

  python3 scripts/montar_construtor.py --exportar --fonte /caminho/do/repositorio-do-metodo
  python3 scripts/montar_construtor.py --modelos

--exportar copia o construtor (construir.py e canvaslib), os specs e os SVGs dos canvas, o template do
documento e o manifesto, tirando qualquer referência interna. --modelos roda o construtor exportado e
grava, em skills/<skill>/assets/modelos/, o canvas em branco, o documento em branco, o template.md
com as marcas e o CAMPOS.md.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONSTRUTOR = ROOT / "construtor"
SKILLS = ROOT / "skills"
MODULOS = ("__init__.py", "md.py", "html_canvas.py", "html_doc.py", "svg.py", "manifesto.py", "template_md.py")
CHAVES_SPEC = ("id", "skill", "titulo", "origem", "pagina", "estatico", "campos", "preenchimento", "md", "leitura")
FORBIDDEN = ("/home/ubuntu", "~/", "operacao/", "gestor-agil-agent", "ceo-agent", "delivery-agent", "marketing-agent",
             "Denisson", "Otto", "Clara", "Maya", "Ciro", "Duda", "Bia", "Téo", ".claude/skills")

INIT = '''"""canvaslib — construtor de canvas do Gestão Ágil 2.0 (pacote do aluno).

A camada estática de cada canvas é o PDF oficial vetorizado; o construtor só sobrepõe os campos
preenchíveis e gera a forma documento a partir do mesmo spec.
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]      # construtor/
REPO = RAIZ.parent                              # raiz do pacote
SPECS = RAIZ / "specs"
BRUTO = SPECS / "_bruto"
ESTATICO = RAIZ / "estatico"
CONFERENCIAS = RAIZ / "conferencias"
LIMIARES = RAIZ / "limiares.json"
TEMPLATE_ARTEFATO = RAIZ / "template-artefato.html"
'''

README = '''# Construtor de canvas e documento

Gera, a partir de um arquivo `.md` preenchido, o **canvas oficial** do curso (réplica do PDF, com o
texto por cima) e a **forma documento** (o mesmo conteúdo em documento corrido). Só precisa de
Python 3.10 ou mais novo; não instala nada.

## Como usar

1. Copie o template da skill: `skills/<skill>/assets/modelos/template-<id>.md`.
2. Preencha as células e os blocos. Não apague as marcas `<!-- c:... -->`: elas dizem ao construtor onde
   está cada campo. O que você não souber fica em branco.
3. Gere:

```bash
python3 construtor/construir.py <id> --documento --md meu-caso.md --saida meu-caso.html
python3 construtor/construir.py <id> --canvas    --md meu-caso.md --saida meu-caso-canvas.html
```

`<id>` é o identificador do canvas (tabela abaixo). Abra o HTML no navegador; o botão "imprimir / PDF"
sai em uma página no tamanho do canvas original.

Sem Python: copie `canvas-<id>.html` e escreva dentro das `div[data-campo]`, mantendo os ids.
Os ids e o texto-guia de cada campo estão em `assets/modelos/CAMPOS.md` da skill.

## Canvas disponíveis

{TABELA}

Família: **kit** = canvas do kit do curso (padrão quando existe); **v6** = canvas editável da versão v6;
**módulo** = editável por módulo; **jornada** = folha individual da jornada; **laboratório** = canvas que
não existe no curso, desenhado no mesmo estilo do kit e marcado como acréscimo.

## Como o construtor lê o `.md`

- marca numa célula de tabela → o valor é a última célula da mesma linha;
- marca num título ou rótulo → o texto depois dela na mesma linha ou o bloco seguinte;
- marca sozinha numa linha, antes de uma tabela → a tabela inteira (linha por linha).
'''

FAMILIA = {"kit": "kit", "v6": "v6", "b": "módulo", "c": "jornada", "laboratorio": "laboratório"}


def _scan(texto: str) -> list[str]:
    return [m for m in FORBIDDEN if m in texto]


def exportar(fonte: Path) -> None:
    src = fonte / "ferramentas" / "canvas"
    if not (src / "construir.py").is_file():
        raise SystemExit(f"fonte sem construtor: {src}")
    if CONSTRUTOR.exists():
        shutil.rmtree(CONSTRUTOR)
    for sub in ("canvaslib", "specs", "estatico", "oficiais"):
        (CONSTRUTOR / sub).mkdir(parents=True)
    shutil.copyfile(src / "construir.py", CONSTRUTOR / "construir.py")
    for m in MODULOS:
        texto = (src / "canvaslib" / m).read_text(encoding="utf-8")
        if m == "__init__.py":
            texto = INIT
        (CONSTRUTOR / "canvaslib" / m).write_text(texto, encoding="utf-8")
    tpl = (fonte / "operacao" / "_padrao" / "template-artefato.html").read_text(encoding="utf-8")
    tpl = re.sub(r"<!--(?:(?!-->).)*?(?:/home/ubuntu|~/|operacao/)(?:(?!-->).)*?-->", "", tpl, flags=re.S)   # comentários com caminho da casa
    tpl = re.sub(r"/\*(?:(?!\*/).)*?(?:/home/ubuntu|~/|operacao/)(?:(?!\*/).)*?\*/", "", tpl, flags=re.S)
    (CONSTRUTOR / "template-artefato.html").write_text(tpl, encoding="utf-8")

    sys.path.insert(0, str(CONSTRUTOR))
    from canvaslib import template_md  # noqa: E402  (a cópia recém-exportada)

    manifesto = json.loads((src / "oficiais" / "manifesto.json").read_text(encoding="utf-8"))
    itens = []
    linhas = ["| id | canvas | skill | família | padrão |", "|---|---|---|---|---|"]
    problemas = []
    for it in manifesto["oficiais"]:
        sid, skill = it["id"], it.get("skill")
        spec_path = src / "specs" / f"{sid}.json"
        if not skill or not spec_path.is_file():
            continue
        sp = json.loads(spec_path.read_text(encoding="utf-8"))
        sp = {k: sp[k] for k in CHAVES_SPEC if k in sp}
        arq = sp.get("origem", {}).get("arquivo")
        sp["origem"] = {"familia": sp.get("origem", {}).get("familia"), "arquivo": Path(arq).name if arq else None,
                        "pagina": sp.get("origem", {}).get("pagina", 1), "numero": sp.get("origem", {}).get("numero", "")}
        sp["estatico"] = {"svg": f"estatico/{sid}.svg"}
        sp = template_md.simplificar_regras(sp)
        sp["md"]["template"] = f"skills/{skill}/assets/modelos/template-{sid}.md"
        texto = json.dumps(sp, ensure_ascii=False, indent=1) + "\n"
        for marca in _scan(texto):
            problemas.append(f"spec {sid}: {marca!r}")
        (CONSTRUTOR / "specs" / f"{sid}.json").write_text(texto, encoding="utf-8")
        shutil.copyfile(src / "estatico" / f"{sid}.svg", CONSTRUTOR / "estatico" / f"{sid}.svg")
        itens.append({"id": sid, "familia": it["familia"], "arquivo": Path(it["arquivo"]).name if it.get("arquivo") else None,
                      "pagina": it.get("pagina", 1), "numero": it.get("numero", ""), "titulo": it["titulo"], "skill": skill,
                      "padrao": bool(it.get("padrao")), "largura_pt": it.get("largura_pt"), "altura_pt": it.get("altura_pt")})
        linhas.append(f"| `{sid}` | {it['titulo']} | `{skill}` | {FAMILIA.get(it['familia'], it['familia'])} | {'sim' if it.get('padrao') else ''} |")
    (CONSTRUTOR / "oficiais" / "manifesto.json").write_text(json.dumps({"oficiais": itens}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (CONSTRUTOR / "README.md").write_text(README.replace("{TABELA}", "\n".join(linhas)), encoding="utf-8")
    for path in CONSTRUTOR.rglob("*"):
        if path.is_file() and path.suffix in {".py", ".md", ".html", ".json"}:
            for marca in _scan(path.read_text(encoding="utf-8", errors="replace")):
                problemas.append(f"{path.relative_to(ROOT)}: {marca!r}")
    print(f"exportado: {len(itens)} canvas, {len(list((CONSTRUTOR / 'estatico').glob('*.svg')))} svgs")
    if problemas:
        print("REFERÊNCIAS INTERNAS A LIMPAR:")
        for pr in sorted(set(problemas)):
            print("  ", pr)
        raise SystemExit(1)


def modelos() -> None:
    manifesto = json.loads((CONSTRUTOR / "oficiais" / "manifesto.json").read_text(encoding="utf-8"))
    construir = [sys.executable, str(CONSTRUTOR / "construir.py")]
    por_skill: dict[str, list[dict]] = {}
    for it in manifesto["oficiais"]:
        por_skill.setdefault(it["skill"], []).append(it)
    n = 0
    for skill, itens in por_skill.items():
        pasta = SKILLS / skill / "assets" / "modelos"
        if not (SKILLS / skill).is_dir():
            print(f"  aviso: skill {skill} não está em skills/; pulada")
            continue
        if pasta.exists():
            shutil.rmtree(pasta)
        pasta.mkdir(parents=True)
        itens.sort(key=lambda i: (not i["padrao"], i["id"]))
        for k, it in enumerate(itens):
            sid = it["id"]
            sp = json.loads((CONSTRUTOR / "specs" / f"{sid}.json").read_text(encoding="utf-8"))
            subprocess.run(construir + [sid, "--canvas", "--saida", str(pasta / f"canvas-{sid}.html")], check=True, capture_output=True)
            subprocess.run(construir + [sid, "--template", "--saida", str(pasta / f"template-{sid}.md")], check=True, capture_output=True)
            le = sp.get("leitura") or {}
            if le.get("capitulos") and not le.get("sem_documento"):
                nome = "documento.html" if k == 0 else f"documento-{sid}.html"
                subprocess.run(construir + [sid, "--documento", "--saida", str(pasta / nome)], check=True, capture_output=True)
            n += 1
        subprocess.run(construir + ["--campos-md", skill, "--saida", str(pasta / "CAMPOS.md")], check=True, capture_output=True)
    print(f"modelos gerados: {n} canvas em {len(por_skill)} skills")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--exportar", action="store_true")
    ap.add_argument("--modelos", action="store_true")
    ap.add_argument("--fonte", type=Path)
    a = ap.parse_args()
    if a.exportar:
        if not a.fonte:
            ap.error("--exportar precisa de --fonte")
        exportar(a.fonte.resolve())
    if a.modelos:
        modelos()
    if not (a.exportar or a.modelos):
        ap.error("escolha --exportar e/ou --modelos")


if __name__ == "__main__":
    main()
