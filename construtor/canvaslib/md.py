"""Lê valores de um .md preenchido pelas âncoras invisíveis `<!-- c:id -->`.

Regras (ver ferramentas/canvas/README.md):
- âncora dentro de uma célula de tabela → o valor é outra célula da mesma linha
  (a última, por padrão; ou a coluna nomeada pelo spec; ou um formato com nomes de coluna);
- âncora numa linha comum → o valor é o texto depois da âncora na mesma linha
  e, se não houver, o parágrafo, a citação ou a tabela que vem a seguir.
- regras: coluna (pelo cabeçalho) · coluna_n (pela posição, 1-based) · linha_tabela (n-ésima linha
  do corpo) · formato / formato_linha com {Nome da coluna} ou {#n} · item · extrair · literal · senao.
"""
import re
from pathlib import Path

ANC = re.compile(r"<!--\s*c:([a-zA-Z0-9_\-\.]+)\s*-->")


def limpar(t: str) -> str:
    t = re.sub(r"<!--.*?-->", "", t)
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"(?<![\w*])\*(?!\*)([^*]+?)\*(?![\w*])", r"\1", t)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"^\s*>\s?", "", t)
    return t.strip()


def celulas(linha: str):
    s = linha.strip()
    if not s.startswith("|"):
        return None
    partes = re.split(r"(?<!\\)\|", s.strip("|"))
    return [p.replace("\\|", "|").strip() for p in partes]


def eh_separador(linha: str) -> bool:
    s = linha.strip()
    return s.startswith("|") and set(s) <= set("|-: ")


def _cabecalho(linhas, i):
    """Cabeçalho da tabela que contém a linha i (a linha antes do separador)."""
    j = i - 1
    while j >= 0 and celulas(linhas[j]) is not None:
        if eh_separador(linhas[j]) and j - 1 >= 0 and celulas(linhas[j - 1]) is not None:
            return [limpar(c) for c in celulas(linhas[j - 1])]
        j -= 1
    return []


def _bloco_seguinte(linhas, i):
    """Parágrafo, citação ou tabela que vem depois da linha i (pula linhas em branco)."""
    j = i + 1
    while j < len(linhas) and linhas[j].strip() == "":
        j += 1
    bloco = []
    while j < len(linhas):
        l2 = linhas[j]
        if l2.strip() == "" or ANC.search(l2) or l2.startswith("#") or l2.strip() == "---":
            break
        bloco.append(l2.rstrip())
        j += 1
    return bloco


def brutos(md_path) -> dict:
    """Mapa id_md → {tipo: tabela|texto, ...}."""
    linhas = Path(md_path).read_text(encoding="utf-8").splitlines()
    out = {}
    for i, ln in enumerate(linhas):
        for m in ANC.finditer(ln):
            aid = m.group(1)
            cels = celulas(ln)
            if cels is not None and not eh_separador(ln):
                col = next((k for k, c in enumerate(cels) if f"c:{aid}" in c), 0)
                out[aid] = {"tipo": "tabela", "celulas": [limpar(c) for c in cels],
                            "cabecalho": _cabecalho(linhas, i), "coluna_ancora": col, "linha": i + 1}
            else:
                resto = limpar(ln[m.end():])
                if resto:
                    out[aid] = {"tipo": "texto", "bloco": [resto], "linha": i + 1}
                else:
                    out[aid] = {"tipo": "texto", "bloco": _bloco_seguinte(linhas, i), "linha": i + 1}
    return out


def _idx_coluna(cab, nome):
    alvo = nome.casefold()
    for k, c in enumerate(cab):
        if c.casefold() == alvo:
            return k
    for k, c in enumerate(cab):
        if alvo in c.casefold() or c.casefold() in alvo:
            return k
    return None


def _formatar(formato, cab, cels):
    def sub(m):
        nome = m.group(1)
        if nome.startswith("#") and nome[1:].isdigit():
            k = int(nome[1:]) - 1
            return cels[k] if 0 <= k < len(cels) else ""
        k = _idx_coluna(cab, nome)
        return cels[k] if k is not None and k < len(cels) else ""
    return re.sub(r"\{([^}]+)\}", sub, formato).strip(" ·—-")


def _tabela_para_linhas(bloco, formato_linha=None):
    linhas_tab = [l for l in bloco if celulas(l) is not None]
    if not linhas_tab:
        return None
    cab = [limpar(c) for c in celulas(linhas_tab[0])]
    corpo = [l for l in linhas_tab[1:] if not eh_separador(l)]
    saida = []
    for l in corpo:
        cels = [limpar(c) for c in celulas(l)]
        if not any(cels):
            continue
        if formato_linha:
            saida.append(_formatar(formato_linha, cab, cels))
        else:
            saida.append(" · ".join(c for c in cels if c))
    return "\n".join(s for s in saida if s)


def _pos(v: str, regra: dict) -> str:
    """Pós-processamento: 'item' pega a n-ésima linha; 'extrair' aplica regexes em ordem (grupo 1 ou o todo)."""
    if "item" in regra:
        linhas = [l for l in v.split("\n") if l.strip()]
        n = int(regra["item"])
        v = linhas[n - 1] if 0 < n <= len(linhas) else ""
    if "juntar" in regra:
        v = regra["juntar"].join(l.strip() for l in v.split("\n") if l.strip())
    if "extrair" in regra:
        padroes = regra["extrair"] if isinstance(regra["extrair"], list) else [regra["extrair"]]
        achou = False
        for pad in padroes:
            m = re.search(pad, v, re.S)
            if m:
                v = regra["literal"] if "literal" in regra else (m.group(1) if m.groups() else m.group(0))
                achou = True
                break
        if not achou:
            v = regra.get("senao", "")
    return v.strip()


def valor(brut: dict, campo_id: str, regra: dict | None = None) -> str:
    """Resolve o valor de um campo do canvas a partir dos brutos do .md."""
    regra = regra or {}
    return _pos(_valor_bruto(brut, campo_id, regra), regra)


def _valor_bruto(brut: dict, campo_id: str, regra: dict) -> str:
    aid = regra.get("ancora", campo_id)
    b = brut.get(aid)
    if b is None:
        return ""
    if b["tipo"] == "tabela":
        cab, cels = b["cabecalho"], b["celulas"]
        if "formato" in regra:
            return _formatar(regra["formato"], cab, cels)
        if "coluna_n" in regra:
            k = int(regra["coluna_n"]) - 1
            return cels[k] if 0 <= k < len(cels) else ""
        if "coluna" in regra:
            k = _idx_coluna(cab, regra["coluna"])
            return cels[k] if k is not None and k < len(cels) else ""
        if b["coluna_ancora"] == len(cels) - 1:
            return cels[-1]
        return next((c for c in reversed(cels) if c), "")
    bloco = b["bloco"]
    if "linha_tabela" in regra:
        linhas_tab = [l for l in bloco if celulas(l) is not None]
        if not linhas_tab:
            return ""
        cab = [limpar(c) for c in celulas(linhas_tab[0])]
        corpo = [l for l in linhas_tab[1:] if not eh_separador(l)]
        n = int(regra["linha_tabela"])
        if not (0 < n <= len(corpo)):
            return ""
        cels = [limpar(c) for c in celulas(corpo[n - 1])]
        if "formato" in regra:
            return _formatar(regra["formato"], cab, cels)
        if "coluna_n" in regra:
            k = int(regra["coluna_n"]) - 1
            return cels[k] if 0 <= k < len(cels) else ""
        k = _idx_coluna(cab, regra.get("coluna", ""))
        return cels[k] if k is not None and k < len(cels) else ""
    tab = _tabela_para_linhas(bloco, regra.get("formato_linha"))
    if tab is not None:
        return tab
    return "\n".join(limpar(l) for l in bloco if limpar(l))


def valores(md_path, spec: dict) -> dict:
    """Todos os campos do spec + metadados (_meta) lidos do .md."""
    brut = brutos(md_path)
    regras = (spec.get("md") or {}).get("ancoras", {})
    out = {}
    for c in spec.get("campos", []):
        out[c["id"]] = valor(brut, c["id"], regras.get(c["id"]))
    meta = {}
    for chave in ("pergunta", "resposta", "data", "empresa", "dono", "decide_com", "aceitante", "caso"):
        if chave in brut and chave not in out:
            meta[chave] = valor(brut, chave)
    out["_meta"] = meta
    out["_sem_ancora"] = [c["id"] for c in spec.get("campos", [])
                          if (regras.get(c["id"], {}).get("ancora", c["id"])) not in brut]
    return out
