"""Gera um template.md mínimo e limpo a partir do spec: cada campo do canvas ganha um lugar com âncora
`<!-- c:id -->` compatível com as regras de md.ancoras (linha de tabela, tabela inteira, coluna).

É o template que vai com o pacote do aluno: só rótulos e textos-guia do canvas oficial, sem contexto
interno. O construtor lê o .md preenchido do mesmo jeito que lê os templates da casa.
"""
import re

CHAVES_TABELA = ("linha_tabela", "formato", "formato_linha", "item")


def simplificar_regras(spec: dict) -> dict:
    """Cópia do spec em que todo campo lido por `extrair` (um pedaço de um valor compartilhado) vira uma
    linha própria com a âncora igual ao id. É a forma que o template mínimo usa: uma célula, um campo."""
    import copy
    sp = copy.deepcopy(spec)
    regras = sp.setdefault("md", {}).setdefault("ancoras", {})
    for c in sp.get("campos", []):
        r = regras.get(c["id"], {})
        if "extrair" in r:
            regras[c["id"]] = {"ancora": c["id"]}
    return sp


def _humano(anc: str) -> str:
    return anc.replace("_", " ").strip().capitalize()


def _agrupar(spec: dict) -> tuple:
    """Classifica as âncoras: 'valor' (uma célula), 'tabela' (bloco de tabela) ou 'coluna' (linha com colunas)."""
    regras = (spec.get("md") or {}).get("ancoras", {})
    grupos = {}
    ordem = []
    for c in spec.get("campos", []):
        r = regras.get(c["id"], {})
        if "literal" in r and "extrair" not in r:
            continue
        anc = r.get("ancora", c["id"])
        g = grupos.get(anc)
        if g is None:
            g = grupos[anc] = {"tipo": "valor", "campos": [], "colunas": [], "n_linhas": 1, "posicional": 0}
            ordem.append(anc)
        g["campos"].append(c)
        if any(k in r for k in CHAVES_TABELA):
            g["tipo"] = "tabela"
            if "linha_tabela" in r:
                g["n_linhas"] = max(g["n_linhas"], int(r["linha_tabela"]) if int(r["linha_tabela"]) < 50 else g["n_linhas"])
            if "item" in r and int(r["item"]) < 50:
                g["n_linhas"] = max(g["n_linhas"], int(r["item"]))
            for fmt in (r.get("formato"), r.get("formato_linha")):
                for nome in re.findall(r"\{([^}]+)\}", fmt or ""):
                    if nome.startswith("#"):
                        g["posicional"] = max(g["posicional"], int(nome[1:]) if nome[1:].isdigit() and int(nome[1:]) < 50 else 0)
                    elif nome not in g["colunas"]:
                        g["colunas"].append(nome)
        if "coluna" in r:
            if g["tipo"] == "valor":
                g["tipo"] = "coluna"
            if r["coluna"] not in g["colunas"]:
                g["colunas"].append(r["coluna"])
        if "coluna_n" in r:
            if g["tipo"] == "valor":
                g["tipo"] = "coluna"
            g["posicional"] = max(g["posicional"], int(r["coluna_n"]))
    return grupos, ordem


def _colunas(g: dict) -> list:
    cols = list(g["colunas"])
    if g["posicional"]:
        while len(cols) < g["posicional"]:
            cols.append(f"Coluna {len(cols) + 1}")
    return cols or ["Item"]


def _rotulo(g: dict, anc: str) -> str:
    rots = [c.get("rotulo") for c in g["campos"] if c.get("rotulo")]
    if len(g["campos"]) == 1 and rots:
        return rots[0]
    if g["tipo"] == "tabela" and len(g["campos"]) > 3:
        return _humano(anc)                                           # tabela grande: o nome do bloco, não o da 1ª célula
    comum = rots[0] if rots else _humano(anc)
    m = re.match(r"^(.*?)(?: — | \(| \d+$| #\d+)", comum)
    return (m.group(1) if m and len(m.group(1)) > 3 else comum).strip()


def _guia(g: dict) -> str:
    gs = [c.get("guia") for c in g["campos"] if c.get("guia")]
    return (gs[0] if gs else "").replace("|", "/").strip()


def montar(spec: dict) -> str:
    grupos, ordem = _agrupar(spec)
    leitura = spec.get("leitura") or {}
    capitulos = leitura.get("capitulos") or [{"titulo": "Campos do canvas", "campos": [c["id"] for c in spec.get("campos", [])]}]
    campo_para_anc = {}
    for anc, g in grupos.items():
        for c in g["campos"]:
            campo_para_anc[c["id"]] = anc
    usados = set()
    secoes = []
    # cabeçalho: âncoras cujos campos não aparecem em capítulo nenhum
    em_capitulos = {cid for cap in capitulos for cid in cap.get("campos", [])}
    cabecalho = [anc for anc in ordem if not any(c["id"] in em_capitulos for c in grupos[anc]["campos"])]
    blocos = [("Cabeçalho", cabecalho)] if cabecalho else []
    for cap in capitulos:
        ancs = []
        for cid in cap.get("campos", []):
            anc = campo_para_anc.get(cid)
            if anc and anc not in ancs and anc not in usados and anc not in cabecalho:
                ancs.append(anc)
        if ancs:
            blocos.append((cap.get("titulo", "Campos"), ancs))
    out = [f"<!-- spec: {spec['id']} · gerado pelo construtor (construir.py --template); preencha as células e os blocos sem apagar as marcas de campo (os comentários c:...) -->",
           "", f"# {spec.get('titulo', spec['id'])}", "",
           "Preencha este arquivo e gere o canvas ou o documento com o construtor. Regras: um dono por artefato (nome de pessoa); todo número com fonte e data; o que não souber fica em branco, nunca inventado.", ""]
    for titulo, ancs in blocos:
        out += [f"## {titulo}", ""]
        valores = [a for a in ancs if grupos[a]["tipo"] == "valor" and a not in usados]
        if valores:
            out += ["| Campo | Resposta |", "|---|---|"]
            for anc in valores:
                g = grupos[anc]; usados.add(anc)
                guia = _guia(g)
                out.append(f"| **{_rotulo(g, anc)}**{' — ' + guia if guia else ''} <!-- c:{anc} --> | |")
            out.append("")
        colunas = [a for a in ancs if grupos[a]["tipo"] == "coluna" and a not in usados]
        for chave, grupo in _agrupar_por_colunas(colunas, grupos).items():
            cols = list(chave)
            out += ["| | " + " | ".join(cols) + " |", "|---|" + "---|" * len(cols)]
            for anc in grupo:
                g = grupos[anc]; usados.add(anc)
                out.append(f"| **{_rotulo(g, anc)}** <!-- c:{anc} --> | " + " | ".join("" for _ in cols) + " |")
            out.append("")
        for anc in [a for a in ancs if grupos[a]["tipo"] == "tabela" and a not in usados]:
            g = grupos[anc]; usados.add(anc)
            cols = _colunas(g)
            guia = _guia(g)
            out += [f"**{_rotulo(g, anc)}**{' — ' + guia if guia else ''} (uma linha por item):", f"<!-- c:{anc} -->",
                    "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
            for _ in range(max(1, g["n_linhas"])):
                out.append("| " + " | ".join("" for _ in cols) + " |")
            out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def _agrupar_por_colunas(ancs: list, grupos: dict) -> dict:
    por = {}
    for anc in ancs:
        por.setdefault(tuple(_colunas(grupos[anc])), []).append(anc)
    return por
