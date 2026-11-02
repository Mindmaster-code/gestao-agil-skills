#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o kit de modelos do GA 2.0 (especificação em ../../ESPEC-kit.md).

Cópia estendida de ../../../modelos/_build/gerar_modelo.py (o original não muda). O conteúdo mora em dados_kit.py. Por
modelo, na pasta de saída (KIT_SAIDA; padrão: a pasta kit/):

  Pxx-slug.html        páginas para imprimir e preencher à mão: o modelo em branco e, depois dele, as páginas do
                       "Exemplo preenchido" (../../estilo/ga.css + ../../modelos/modelos.css + kit.css)
  pdf/Pxx-slug.pdf     Chromium do Playwright: tamanho de página do CSS, printBackground
  docx/Pxx-slug.docx   editável: o modelo em branco e, depois de uma quebra de página, o exemplo preenchido
  previa/Pxx-pN.png    print de cada página (N = número da página, as de exemplo vêm depois das em branco)
  kit.json             o contrato que o construtor das skills lê: "versao", "data" e a lista "modelos", com codigo,
                       titulo, passo, tempo_min e tempo_fonte ("est." quando a aula não dá o tempo), skill_primaria
                       (null no modelo sem skill), skills_compartilhadas, campos (os rótulos, na ordem da folha),
                       formato ("A4 retrato", "A4 paisagem" ou "A3 paisagem"), paginas, arquivo_html, pdf e docx
                       (caminhos relativos a modelos-definitivos/) e exemplo (setor e caso)

O que o kit acrescenta ao gerador dos 14 modelos:
  1. cabeçalho com o passo, o tempo e a skill (sem "Ficha relacionada" e sem "Aula");
  2. rodapé "Gestão Ágil 2.0 · Kit de modelos" e "P2.1 · página x de y" (y conta as páginas em branco e as de exemplo);
  3. página de exemplo preenchido depois do modelo: faixa no topo, os mesmos blocos com o `ex=` de cada bloco escrito
     dentro do campo (Manrope, teal-700, 10,5 pt, sobre as linhas de escrever) e as linhas que sobram vazias; o campo
     cresce o quanto o texto pedir, e a página de exemplo se ajusta como a página em branco;
  4. formatos de página: A4 em pé (padrão), A4 deitado ("A4d") e A3 deitado ("A3d");
  5. DOCX com o modelo em branco e, depois da quebra de página, o exemplo preenchido;
  6. conferência também nas páginas de exemplo: letra de 10 pt no mínimo, nada cortado, nenhuma página quase vazia,
     sem travessão, aspas retas, vocabulário vetado; e todo bloco com valor de exemplo.

Etapas:
  1. escreve o HTML;
  2. mede cada página no Chromium e acrescenta linhas de escrever onde sobra espaço (e onde o texto do exemplo pede);
  3. gera o PDF e as prévias PNG;
  4. escreve um HTML simples por modelo e converte para DOCX pelo LibreOffice;
  5. confere o texto e o PDF.

Uso: python3 gerar_kit.py                    (tudo)
     python3 gerar_kit.py --so-html          (só HTML e medição)
     python3 gerar_kit.py --so P1.2,P2.1     (só estes modelos; não regrava o kit.json)
     python3 gerar_kit.py --conferir         (só mede e confere o que já está na pasta)
     python3 gerar_kit.py --dados arq.py     (outro arquivo de dados, para teste)
Variáveis: MODELOS_SCRATCH (pasta de trabalho temporária) e KIT_SAIDA (pasta de saída).
Não sobe nada ao Drive e não faz commit.
"""
import base64
import html
import importlib.util
import io
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path

from PIL import Image

AQUI = Path(__file__).resolve().parent                 # .../modelos-definitivos/kit/_build
sys.path.insert(0, str(AQUI))


def carregar_dados():
    if "--dados" in sys.argv:
        caminho = Path(sys.argv[sys.argv.index("--dados") + 1]).resolve()
        spec = importlib.util.spec_from_file_location("dados_alternativos", caminho)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    import dados_kit
    return dados_kit


D = carregar_dados()

KIT = AQUI.parent                                       # .../modelos-definitivos/kit
SAIDA = Path(os.environ.get("KIT_SAIDA", KIT)).resolve()
TRILHA = AQUI.parents[2]                                # .../trilha-ga-rotinas
ESTILO = TRILHA / "estilo"
CSS = [ESTILO / "ga.css", TRILHA / "modelos" / "modelos.css", KIT / "kit.css"]
LOGO_ABS = ESTILO / "logo-ga2-horizontal.png"
RODAPE = "Gestão Ágil 2.0 · Kit de modelos"
NODE = "node"
SCRATCH = Path(os.environ.get("MODELOS_SCRATCH", Path(tempfile.gettempdir()) / "ga-kit-build"))
SEGURANCA_MM = 1.2        # folga que fica sempre no fim da página
CAB_MM, ROD_MM = 19, 14   # altura do cabeçalho e do rodapé da página (modelos.css)

# Formatos de página (os mesmos nomes do kit.json). css: classe da página; pagina: valor do @page (None = A4 em pé, que
# o ga.css já traz); docx: tamanho da página do DOCX.
FORMATOS = {
    "A4 retrato": dict(css="", pagina=None, docx="21cm 29.7cm"),
    "A4 paisagem": dict(css="a4d", pagina="297mm 210mm", docx="29.7cm 21cm"),
    "A3 paisagem": dict(css="a3d", pagina="420mm 297mm", docx="42cm 29.7cm"),
}


def rel(caminho):
    """Caminho relativo à pasta de saída, com barras normais (para o link dentro do HTML)."""
    return Path(os.path.relpath(caminho, SAIDA)).as_posix()


# ------------------------------------------------------------------ texto
def esc(s):
    return html.escape(s, quote=False)


def plain(s):
    return re.sub(r"[{}]", "", s)


def rich(s):
    """{...} vira explicação em cinza dentro do rótulo."""
    out = []
    for parte in re.split(r"(\{[^}]*\})", s):
        if parte.startswith("{") and parte.endswith("}"):
            out.append('<span class="dica">' + esc(parte[1:-1]) + "</span>")
        else:
            out.append(esc(parte))
    return "".join(out)


def nome_arquivo(m):
    return f"{m['cod']}-{m['slug']}"


def rotulo_passo(m):
    p = m["passo"]
    return p if isinstance(p, str) else f"Passo {p[0]} · {p[1]}"


def rotulo_tempo(m):
    return f"Leva cerca de {m['tempo']['min']} minutos"


def cx(on=False, estilo=""):
    st = f' style="{estilo}"' if estilo else ""
    return f'<i class="cx{" on" if on else ""}"{st}></i>'


# ------------------------------------------------------------------ ids dos blocos que crescem
def atribuir_ids(m):
    """Dá um id a cada bloco que cresce ou que recebe texto de exemplo. O mesmo id vale na página em branco e na de
    exemplo: as linhas de escrever (e as linhas de tabela) são iguais nas duas páginas."""
    n = 0

    def passo(blocos):
        nonlocal n
        for b in blocos:
            t = b["t"]
            if t in ("f", "tres", "quad") or (t == "tab" and b["flex"]):
                n += 1
                b["_fid"] = f"{m['cod']}-{n}"
            if t == "agil":
                passo(b["filhos"])
            if t == "grid":
                passo(b["itens"])

    for pg in m["paginas"]:
        passo(pg)


def fid_de(b, E):
    return b.get("_fid")


# ------------------------------------------------------------------ HTML: blocos
def p_f(b, X, E=False, forcar_rotulo_acima=False):
    fid = fid_de(b, E)
    extra = X.get(fid, 0) if fid else 0
    n = b["n"] + extra
    texto = b.get("ex") if E else None
    attrs = ""
    if fid:
        attrs = (f' data-flex="linha" data-fid="{fid}" data-base="{b["n"]}" data-cur="{n}" data-cap="{b["cap"]}" '
                 f'data-w="{max(b["flex"], 1)}"')
    inline = b["inline"]
    if inline is None:
        inline = (b["n"] == 1 and not b["flex"] and not b["hint"] and not b["num"] and len(plain(b["label"])) <= 44)
    if forcar_rotulo_acima:
        inline = False
    ov = f'<span class="ex">{esc(texto)}</span>' if texto else ""
    if inline:
        return (f'<div class="campo em-linha"><span class="rot">{rich(b["label"])}</span>'
                f'<span class="trc">{ov}</span></div>')
    hint = f'<span class="dica bl">{rich(b["hint"])}</span>' if b["hint"] else ""
    corpo = (f'<div class="campo"{attrs}><span class="rot">{rich(b["label"])}</span>{hint}'
             f'<div class="lns">{"<i></i>" * n}{ov}</div></div>')
    if b["num"]:
        corpo = f'<div class="perg"><div class="num">{b["num"]}</div>{corpo}</div>'
    return corpo


def p_grid(b, X, E=False):
    itens = "".join(p_f(i, X, E, forcar_rotulo_acima=True) for i in b["itens"])
    return f'<div class="grade-c" style="grid-template-columns:{b["cols"]}">{itens}</div>'


def p_sec(b, X, E=False):
    return f'<h3 class="sec">{rich(b["texto"])}</h3>'


def p_p(b, X, E=False):
    return f'<p class="txt-p">{rich(b["texto"])}</p>'


def p_nota(b, X, E=False):
    return f'<p class="nota">{rich(b["texto"])}</p>'


def p_lbl(b, X, E=False):
    return f'<div class="campo rot-tab"><span class="rot">{rich(b["texto"])}</span></div>'


def sn_palavras(sn):
    return sn if isinstance(sn, (tuple, list)) else D.SN


def p_ck(b, X, E=False):
    marcados = (b.get("ex") or []) if E else []
    itens = []
    for idx, it in enumerate(b["itens"]):
        v = marcados[idx] if idx < len(marcados) else None
        if b["sn"]:
            a, c = sn_palavras(b["sn"])
            itens.append(f'<li><span>{rich(it)}</span><span class="sn-p">{cx(v == "a")}{esc(a)}{cx(v == "c")}{esc(c)}'
                         f'</span></li>')
        else:
            itens.append(f'<li>{cx(bool(v))}<span>{rich(it)}</span></li>')
    return f'<ul class="marcas{" sn" if b["sn"] else ""}">{"".join(itens)}</ul>'


def indices(v):
    if v is None:
        return []
    return list(v) if isinstance(v, (list, tuple)) else [v]


def p_opts(b, X, E=False):
    marc = indices(b.get("ex")) if E else []
    ops = "".join(f'<span class="op">{cx(i in marc)}{esc(o)}</span>' for i, o in enumerate(b["opcoes"]))
    return f'<div class="opts"><span class="rot">{rich(b["label"])}</span>{ops}</div>'


def p_agil(b, X, E=False):
    filhos = "".join(render_bloco(f, X, E) for f in b["filhos"])
    return f'<div class="caixa-agil"><div class="rotulo">{esc(b["titulo"])}</div>{filhos}</div>'


def sobre_linha(texto):
    return f'<span class="ex">{esc(texto)}</span>' if texto else ""


def p_formula(b, X, E=False):
    exs = (b.get("ex") or []) if E else []
    partes = []
    for i, nome in enumerate(b["partes"]):
        if i:
            partes.append(f'<span class="op">{esc(b["ops"][i - 1])}</span>')
        ov = sobre_linha(exs[i] if i < len(exs) else "")
        partes.append(f'<span class="par"><i>{ov}</i><small>{esc(nome)}</small></span>')
    return f'<div class="formula"><span class="rot">{rich(b["label"])}</span><div class="fl">{"".join(partes)}</div></div>'


def p_legenda(b, X, E=False):
    itens = "".join(f"<div><b>{esc(a)}</b>{esc(t)}</div>" for a, t in b["itens"])
    return f'<div class="legenda">{itens}</div>'


def p_duas(b, X, E=False):
    exs = (b.get("ex") or ([], [])) if E else ([], [])

    def col(tt, lista):
        linhas = "".join(
            f'<div class="l"><b>{i}</b><i>{sobre_linha(lista[i - 1] if i - 1 < len(lista) else "")}</i></div>'
            for i in range(1, b["n"] + 1))
        return f'<div><h5>{esc(tt[0])}</h5><span class="dica">{esc(tt[1])}</span>{linhas}</div>'
    return f'<div class="duas">{col(b["esq"], exs[0])}{col(b["dir"], exs[1])}</div>'


def p_tres(b, X, E=False):
    fid = fid_de(b, E)
    n = b["n"] + X.get(fid, 0)
    exs = (b.get("ex") or []) if E else []
    cols = []
    for i, (tt, sub) in enumerate(b["cols"], 1):
        ov = sobre_linha(exs[i - 1] if i - 1 < len(exs) else "")
        cols.append(f'<div class="c m{i}"><div class="cab">{esc(tt)}</div><div class="sub">{esc(sub)}</div>'
                    f'<div class="lns">{"<i></i>" * n}{ov}</div></div>')
    cls = f' {b["cls"]}' if b.get("cls") else ""
    return (f'<div class="tres{cls}" data-flex="linha" data-fid="{fid}" data-base="{b["n"]}" data-cur="{n}" '
            f'data-cap="{b["cap"]}" data-w="1">{"".join(cols)}</div>')


def p_quad(b, X, E=False):
    """Grade 2 x 2 (por exemplo esforço x impacto): quatro quadrantes com título, explicação e linhas de escrever.
    Os quadrantes vêm em ordem de leitura: linha de cima (esq., dir.), linha de baixo (esq., dir.)."""
    fid = fid_de(b, E)
    n = b["n"] + X.get(fid, 0)
    exs = (b.get("ex") or []) if E else []
    (colx, coly) = b["eixos"]
    partes = [f'<div class="eixo"></div><div class="eixo">{esc(colx[0])}</div><div class="eixo">{esc(colx[1])}</div>']
    for r in range(2):
        partes.append(f'<div class="eixo">{esc(coly[r])}</div>')
        for c in range(2):
            i = r * 2 + c
            tt, sub = b["quadrantes"][i]
            ov = sobre_linha(exs[i] if i < len(exs) else "")
            partes.append(f'<div class="c m{i + 1}"><div class="cab">{esc(tt)}</div><div class="sub">{esc(sub)}</div>'
                          f'<div class="lns">{"<i></i>" * n}{ov}</div></div>')
    return (f'<div class="quad" data-flex="linha" data-fid="{fid}" data-base="{b["n"]}" data-cur="{n}" '
            f'data-cap="{b["cap"]}" data-w="1">{"".join(partes)}</div>')


def texto_de(lista, i, j):
    try:
        return lista[i][j] or ""
    except (IndexError, TypeError):
        return ""


def p_quadro(b, X, E=False):
    """Quadro do time para imprimir: colunas com título, explicação e limite, cartões vazios (ou com o texto do exemplo)
    e uma faixa de cartões travados embaixo. Altura fixa (h, em mm)."""
    exs = (b.get("ex") or {}) if E else {}
    cartoes, lims, trav = exs.get("cartoes", []), exs.get("limites", []), exs.get("travado", [])
    cols = []
    for i, (tt, sub, lim) in enumerate(b["colunas"]):
        limite = ""
        if lim:
            v = lims[i] if i < len(lims) and lims[i] else ""
            limite = f'<span class="lim">limite <i class="li">{esc(v)}</i></span>'
        cards = "".join(
            (f'<div class="cart ex">{esc(texto_de(cartoes, i, j))}</div>' if texto_de(cartoes, i, j)
             else '<div class="cart"></div>') for j in range(b["n"]))
        ult = " ult" if i == len(b["colunas"]) - 1 else ""
        cols.append(f'<div class="qc{ult}"><div class="cab"><b>{esc(tt)}</b>{limite}<small>{esc(sub)}</small></div>'
                    f'<div class="cor">{cards}</div></div>')
    tt, sub = b["travado"]
    cards = "".join((f'<div class="cart ex">{esc(trav[j])}</div>' if j < len(trav) and trav[j] else '<div class="cart"></div>')
                    for j in range(b["n_trav"]))
    cols.append(f'<div class="qt"><b>{esc(tt)}</b><small>{esc(sub)}</small><div class="cartoes">{cards}</div></div>')
    return f'<div class="qd" style="height:{b["h"]}mm">{"".join(cols)}</div>'


def p_fichas(b, X, E=False):
    """Fichas para cortar: a mesma pergunta em cada ficha, uma escolha e uma frase de duas linhas."""
    exs = (b.get("ex") or []) if E else []
    cards = []
    for i in range(b["n"]):
        marc, frase = exs[i] if i < len(exs) else (None, "")
        ops = "".join(f'<span class="op">{cx(marc == k)}{esc(o)}</span>' for k, o in enumerate(b["opcoes"]))
        cards.append(f'<div class="fcard"><div class="fperg">{esc(b["pergunta"])}</div><div class="fops">{ops}</div>'
                     f'<div class="frot">{esc(b["frase"])}</div><div class="lns"><i></i><i></i>{sobre_linha(frase)}</div></div>')
    return f'<div class="fichas">{"".join(cards)}</div>'


def p_niveis(b, X, E=False):
    itens = "".join(f'<div><span class="n">{i}</span><span><b>{esc(t)}</b> {esc(d)}</span></div>'
                    for i, (t, d) in enumerate(b["itens"], 1))
    return f'<div class="niveis">{itens}</div>'


def celula_vazia(col, k):
    f = col["fill"]
    if f is None:
        return "<td></td>"
    if f == "num":
        return f'<td class="n">{k}</td>'
    if f == "sn":
        return '<td class="sn"><i class="cx"></i>Sim<i class="cx" style="margin-left:2.2mm"></i>Não</td>'
    if f == "c":
        return '<td class="c"></td>'
    if f == "cx":
        return '<td class="c"><i class="cx solo"></i></td>'
    if f == "datas":
        return '<td class="dts"><span><b>de</b><i></i></span><span><b>a</b><i></i></span></td>'
    if f == "bolas":
        return '<td class="c">' + '<i class="bol"></i>' * 10 + "</td>"
    if isinstance(f, tuple) and f[0] == "opts":
        ops = "".join(f'<span class="op"><i class="cx"></i>{esc(o)}</span> ' for o in f[1])
        return f'<td class="op2">{ops}</td>'
    return "<td></td>"


def celula_exemplo(col, v, k):
    """Célula do exemplo: texto em teal-700, ou caixa marcada quando a coluna é de marcar."""
    f = col["fill"]
    if f == "num":
        return f'<td class="n">{k}</td>'
    if f == "cx":
        return f'<td class="c"><i class="cx solo{" on" if v else ""}"></i></td>'
    if f == "sn":
        return f'<td class="sn">{cx(v == D.SN[0])}Sim{cx(v == D.SN[1], "margin-left:2.2mm")}Não</td>'
    if isinstance(f, tuple) and f[0] == "opts":
        marc = indices(v)
        ops = "".join(f'<span class="op">{cx(o in marc)}{esc(o)}</span> ' for o in f[1])
        return f'<td class="op2">{ops}</td>'
    return f'<td class="{"c ex" if f == "c" else "ex"}">{esc(v)}</td>'


def celula_escrita(col, valor, k, primeira, exv=None):
    if valor is None:
        if exv is not None:
            return celula_exemplo(col, exv, k)
        return celula_vazia(col, k)
    if isinstance(valor, dict):
        if valor.get("agil"):
            return f'<td class="rot agil">{rich(valor["txt"])}</td>'
        if "opts" in valor:
            ops = "".join(f'<span class="op"><i class="cx"></i>{esc(o)}</span> ' for o in valor["opts"])
            return f'<td class="op2">{ops}</td>'
        if valor.get("sn"):
            return celula_vazia({"fill": "sn"}, k)
    cls = "rot" if primeira else ""
    return f'<td class="{cls}">{rich(valor)}</td>' if cls else f"<td>{rich(valor)}</td>"


def th_html(texto, colspan=1, rowspan=1, agil=False):
    attrs = ""
    if colspan > 1:
        attrs += f' colspan="{colspan}"'
    if rowspan > 1:
        attrs += f' rowspan="{rowspan}"'
    cls = []
    if agil:
        cls.append("agil")
    if texto.strip().isdigit():
        cls.append("c")
    c = f' class="{" ".join(cls)}"' if cls else ""
    return f"<th{c}{attrs}>{rich(texto)}</th>"


def linhas_escritas(b):
    """As linhas já escritas da tabela, sem as bandas."""
    return [r for r in b["rows"] if not (isinstance(r, dict) and "banda" in r)]


def p_tab(b, X, E=False):
    cols = b["cols"]
    tot = sum(c["w"] for c in cols)
    fid = fid_de(b, E)
    extra = X.get(fid, 0) if fid else 0
    exrows = (b.get("ex") or []) if E else []
    n_pre = len(linhas_escritas(b))
    blank0 = b["blank"]
    so_escritas = b["flex"] and b["blank"] == 0
    attrs = ""
    h = b["h"]
    if fid:
        if so_escritas:
            attrs = (f' data-flex="altura-tab" data-fid="{fid}" data-base="0" data-cur="{extra}" '
                     f'data-cap="{b["cap"]}" data-w="1"')
            h = b["h"] + extra
        else:
            attrs = (f' data-flex="linha-tab" data-fid="{fid}" data-base="{blank0}" data-cur="{blank0 + extra}" '
                     f'data-cap="{max(b["cap"], blank0)}" data-w="1"')
    colgroup = "<colgroup>" + "".join(f'<col style="width:{c["w"] / tot * 100:.3f}%">' for c in cols) + "</colgroup>"
    if b["head"]:
        thead = "".join("<tr>" + "".join(th_html(t[0], t[1], t[2]) for t in linha) + "</tr>" for linha in b["head"])
    else:
        thead = "<tr>" + "".join(th_html(c["h"], agil=c["agil"]) for c in cols) + "</tr>"
    linhas = []
    k = b["num0"]
    ri = 0                      # posição entre as linhas que recebem exemplo (escritas e depois em branco)
    for r in b["rows"]:
        if isinstance(r, dict) and "banda" in r:
            dica = f'<span class="dica">{esc(r["dica"])}</span>' if r.get("dica") else ""
            linhas.append(f'<tr class="banda"><td colspan="{len(cols)}"><div class="bd"><b>{rich(r["banda"])}</b>'
                          f'{dica}</div></td></tr>')
            continue
        estilo = ""
        if isinstance(r, dict):
            estilo = f' style="--h:{r["h"] + (extra if so_escritas else 0)}mm"'
            r = r["r"]
        exr = exrows[ri] if ri < len(exrows) else None
        celulas = "".join(celula_escrita(cols[i], v, k, i == 0 and cols[i]["fill"] != "num",
                                         exr[i] if exr else None) for i, v in enumerate(r))
        linhas.append(f"<tr{estilo}>{celulas}</tr>")
        k += 1
        ri += 1
    for _ in range(blank0 + (0 if so_escritas else extra)):
        exr = exrows[ri] if ri < len(exrows) else None
        if exr is None:
            linhas.append('<tr class="l">' + "".join(celula_vazia(c, k) for c in cols) + "</tr>")
        else:
            linhas.append('<tr class="lx">' + "".join(
                celula_exemplo(c, exr[i], k) if exr[i] is not None else celula_vazia(c, k)
                for i, c in enumerate(cols)) + "</tr>")
        k += 1
        ri += 1
    return (f'<table class="tab grade"{attrs} style="--h:{h}mm">{colgroup}<thead>{thead}</thead>'
            f'<tbody>{"".join(linhas)}</tbody></table>')


PRINT = {"f": p_f, "grid": p_grid, "sec": p_sec, "p": p_p, "nota": p_nota, "lbl": p_lbl, "ck": p_ck, "opts": p_opts,
         "agil": p_agil, "formula": p_formula, "legenda": p_legenda, "duas": p_duas, "tres": p_tres, "quad": p_quad, "quadro": p_quadro, "fichas": p_fichas, "niveis": p_niveis, "tab": p_tab}


def render_bloco(b, X, E=False):
    return PRINT[b["t"]](b, X, E)


# ------------------------------------------------------------------ HTML: página e documento
def titulo_bloco(m):
    """Cabeçalho: selo, três etiquetas (passo, tempo e skill primária) e o título. Sem skill primária, sem a etiqueta."""
    etq = [f'<span class="etq passo">{esc(rotulo_passo(m))}</span>',
           f'<span class="etq tempo">{esc(rotulo_tempo(m))}</span>']
    if m["skill_primaria"]:
        etq.append(f'<span class="etq sk"><span class="k">Skill</span> {esc(m["skill_primaria"])}</span>')
    return (f'<div class="titulo"><div class="selo">{m["cod"]}</div><div class="txt">'
            f'<div class="etiquetas">{"".join(etq)}</div><h1>{esc(m["titulo"])}</h1></div></div>')


def faixa_exemplo(m):
    return (f'<div class="faixa-ex"><span class="rot-ex">Exemplo preenchido</span><span>·</span>'
            f'<b>{esc(m["setor"])}</b><span class="mod-ex">{esc(m["titulo"])}</span></div>')


def html_modelo(m, X):
    fmt = FORMATOS[m["formato"]]
    n = len(m["paginas"])
    total = 2 * n
    logo = rel(LOGO_ABS)
    paginas = []
    for k in range(total):
        E = k >= n
        i = k % n
        if E:
            topo = faixa_exemplo(m)
            cab_dir = f'Modelo {m["cod"]} · exemplo'
        elif i == 0:
            topo = (titulo_bloco(m) +
                    f'<div class="caixa-pet como"><div class="rotulo">Como usar</div><p>{esc(m["como"])}</p></div>')
            cab_dir = f'Modelo {m["cod"]}'
        else:
            topo = f'<div class="cont"><b>{esc(m["titulo"])}</b><span>continuação · Modelo {m["cod"]}</span></div>'
            cab_dir = f'Modelo {m["cod"]} · continuação'
        corpo = "".join(render_bloco(b, X, E) for b in m["paginas"][i])
        cls = "pg" + (f' {fmt["css"]}' if fmt["css"] else "")
        estilo_linha = f' style="--passo:{m["linha_mm"]}mm"' if m.get("linha_mm") else ""
        paginas.append(
            f'<section class="{cls}"{estilo_linha} data-pagina="{k + 1}" data-tipo="{"exemplo" if E else "branco"}">\n'
            f'<header class="pg-cab"><img class="logo-ga" src="{logo}" alt="Gestão Ágil 2.0"><span>{cab_dir}</span></header>\n'
            f'<div class="pg-corpo">{topo}{corpo}</div>\n'
            f'<footer class="pg-rod"><span>{RODAPE}</span><span><b class="num">{m["cod"]}</b> · página {k + 1} de {total}'
            f'</span></footer>\n</section>')
    estilo_pagina = f'<style>@page{{size:{fmt["pagina"]};margin:0}}</style>\n' if fmt["pagina"] else ""
    links = "".join(f'<link rel="stylesheet" href="{rel(c)}">\n' for c in CSS)
    return (f'<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{m["cod"]} {esc(m["titulo"])}</title>\n{links}{estilo_pagina}'
            f'</head>\n<body>\n' + "\n".join(paginas) + "\n</body>\n</html>\n")


# ------------------------------------------------------------------ medição e preenchimento
class Medidor:
    """Um Chromium que fica aberto durante a execução toda (medir.cjs --servir): cada medição reaproveita o navegador,
    em vez de abrir um novo a cada rodada. Fecha pela entrada (o Node encerra o navegador quando a entrada acaba)."""

    def __init__(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.erro = open(SCRATCH / "medir.err", "w", encoding="utf-8")
        self.p = subprocess.Popen([NODE, str(AQUI / "medir.cjs"), "--servir"], stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE, stderr=self.erro, text=True, bufsize=1)

    def medir(self, arquivos):
        self.p.stdin.write(json.dumps([str(a) for a in arquivos]) + "\n")
        self.p.stdin.flush()
        linha = self.p.stdout.readline()
        if not linha:
            raise SystemExit("medir.cjs parou sem responder (ver medir.err na pasta de trabalho)")
        res = json.loads(linha)
        if "__erro__" in res:
            raise SystemExit("medir.cjs falhou: " + res["__erro__"])
        return res

    def fechar(self):
        try:
            self.p.stdin.close()
            self.p.wait(timeout=60)
        except Exception:
            self.p.kill()     # só o processo que este script abriu
        self.erro.close()


_MEDIDOR = None


def medir(arquivos):
    global _MEDIDOR
    if _MEDIDOR is None:
        _MEDIDOR = Medidor()
    return _MEDIDOR.medir(arquivos)


def fechar_medidor():
    global _MEDIDOR
    if _MEDIDOR is not None:
        _MEDIDOR.fechar()
        _MEDIDOR = None


def distribuir(med, extras, modelos):
    """Reparte o espaço livre entre os elementos que crescem, de modo que a página em branco e a de exemplo tenham as
    mesmas linhas: o mesmo id vale nas duas, e cada acréscimo só entra se couber nas duas. O piso de cada campo é o
    maior entre as linhas do dado e as que o texto do exemplo pede. Devolve True se mudou algo."""
    mudou = False
    for m in modelos:
        X = extras[m["cod"]]
        pgs = med[nome_arquivo(m) + ".html"]
        livre = [pg["livre"] for pg in pgs]
        info = {}
        for pi, pg in enumerate(pgs):
            for f in pg["flex"]:
                d = info.setdefault(f["id"], dict(cur=f["cur"], base=f["base"], need=0, cap=0, w=f["w"], pgs=[]))
                d["need"] = max(d["need"], f["need"])
                d["cap"] = max(d["cap"], f["cap"])
                d["pgs"].append((pi, f["unit"]))
        for fid, d in info.items():
            d["piso"] = max(d["base"], d["need"])
            d["cap"] = max(d["cap"], d["piso"])
            if d["cur"] < d["piso"]:
                falta = d["piso"] - d["cur"]
                X[fid] = X.get(fid, 0) + falta
                for pi, u in d["pgs"]:
                    livre[pi] -= falta * u
                d["cur"] = d["piso"]
                mudou = True
        while True:   # estourou: devolve as unidades acrescentadas, sem passar do piso
            ruins = [pi for pi, l in enumerate(livre) if l < 0]
            cand = [(fid, d) for fid, d in info.items()
                    if d["cur"] > d["piso"] and any(pi in ruins for pi, _ in d["pgs"])]
            if not ruins or not cand:
                break
            fid, d = max(cand, key=lambda x: x[1]["cur"] - x[1]["piso"])
            X[fid] = X.get(fid, 0) - 1
            d["cur"] -= 1
            for pi, u in d["pgs"]:
                livre[pi] += u
            mudou = True
        if any(l < 0 for l in livre):
            continue
        add = {fid: 0 for fid in info}
        while True:
            # linha: cur = linhas atuais; linha-tab: cur = linhas vazias atuais; altura-tab: cur = mm extra por linha
            cand = [fid for fid, d in info.items() if d["cur"] + add[fid] < d["cap"]
                    and all(u <= livre[pi] - SEGURANCA_MM for pi, u in d["pgs"])]
            if not cand:
                break
            fid = min(cand, key=lambda k: (info[k]["cur"] + add[k]) / max(info[k]["w"], 1))
            add[fid] += 1
            for pi, u in info[fid]["pgs"]:
                livre[pi] -= u
        for fid, q in add.items():
            if q:
                X[fid] = X.get(fid, 0) + q
                mudou = True
    return mudou


def escrever_html(modelos, extras):
    SAIDA.mkdir(parents=True, exist_ok=True)
    arqs = []
    for m in modelos:
        p = SAIDA / (nome_arquivo(m) + ".html")
        p.write_text(html_modelo(m, extras[m["cod"]]), encoding="utf-8")
        arqs.append(p)
    return arqs


# ------------------------------------------------------------------ DOCX (HTML simples, tabelas com atributos legados)
PET_ESC, PET, PET_CL, PET_CL2 = "#1A4243", "#2B6F70", "#D4F1F2", "#F0FAFA"
TEAL_FORTE = "#225859"
DOUR, DOUR_TX, DOUR_CL = "#D4AF37", "#7A5F0E", "#FBF4DC"
TINTA, TINTA3, LINHA_D = "#1F2937", "#6B7280", "#94C8C9"
CORAL, CORAL_CL = "#C2410C", "#FFEDD5"
CREME = "#FAFAF8"
DOCX_ALTO = 8
PX_MM = 3.78 * 0.7   # altura mínima das linhas no DOCX: um pouco menor que a da folha, o texto aumenta a linha se precisar
CX = "&#9744;"
CXON = "&#9745;"


def dcx(on=False):
    return CXON if on else CX


def dh_label(s, cor_dica=TINTA3):
    out = []
    for parte in re.split(r"(\{[^}]*\})", s):
        if not parte:
            continue
        if parte.startswith("{") and parte.endswith("}"):
            out.append(f'<font size="2" color="{cor_dica}">{esc(parte[1:-1])}</font>')
        else:
            out.append(f"<b>{esc(parte)}</b>")
    return "".join(out)


def dh_texto(s, cor_dica=TINTA3):
    out = []
    for parte in re.split(r"(\{[^}]*\})", s):
        if parte.startswith("{") and parte.endswith("}"):
            out.append(f'<font size="2" color="{cor_dica}">{esc(parte[1:-1])}</font>')
        else:
            out.append(esc(parte))
    return "".join(out)


def d_exemplo(s):
    """Texto do exemplo no DOCX: teal-700, para se distinguir do que é do modelo."""
    return f'<font color="{PET}">{esc(s).replace(chr(10), "<br>")}</font>'


TAB_ATTR = f'border="1" bordercolor="{LINHA_D}" cellpadding="5" cellspacing="0" width="100%" style="border-collapse:collapse"'
TAB_JUNTA = (f'border="1" bordercolor="{LINHA_D}" cellpadding="5" cellspacing="0" width="100%" '
             f'style="border-collapse:collapse;page-break-inside:avoid"')
ESP = '<p class="sp">&nbsp;</p>'


def d_frow(b, bg=PET_CL2, compacto=False, E=False):
    n = b["n"]
    h = int((24 + (10 if compacto else 16) * (n - 1)) * DOCX_ALTO / 8)
    lab = dh_label(b["label"])
    if b.get("num"):
        lab = f'{b["num"]}. ' + lab
    hint = f'<br><font size="2" color="{TINTA3}">{esc(b["hint"])}</font>' if b.get("hint") else ""
    ex = b.get("ex") if E else None
    resp = d_exemplo(ex) if ex else "&nbsp;"
    return f'<tr><td width="36%" bgcolor="{bg}" valign="top">{lab}{hint}</td><td height="{h}" valign="top">{resp}</td></tr>'


def d_grid_linha(b, bg=PET_CL2, E=False):
    """Campos lado a lado no DOCX: uma linha só, com o rótulo e o espaço de cada campo, na proporção da grade."""
    fr = [float(x.replace("fr", "")) for x in b["cols"].split()]
    tot = sum(fr)
    cel = []
    for i, it in enumerate(b["itens"]):
        w = fr[i] / tot * 100
        ex = it.get("ex") if E else None
        resp = d_exemplo(ex) if ex else "&nbsp;"
        alt = 24 + 16 * (it["n"] - 1)
        hint = f'<br><font size="2" color="{TINTA3}">{esc(it["hint"])}</font>' if it.get("hint") else ""
        cel.append(f'<td width="{w * 0.4:.1f}%" bgcolor="{bg}" valign="top">{dh_label(it["label"])}{hint}</td>'
                   f'<td width="{w * 0.6:.1f}%" height="{alt}" valign="top">{resp}</td>')
    return f"<tr>{''.join(cel)}</tr>"


def d_campos(itens, bg=PET_CL2, E=False):
    """Campos em tabela de rótulo e resposta. Os campos de uma grade viram uma linha só (cada grade na sua tabela)."""
    saida, linhas = [], []

    def fechar():
        if linhas:
            saida.append(f"<table {TAB_ATTR}>{''.join(linhas)}</table>{ESP}")
            linhas.clear()

    for b in itens:
        if b["t"] == "grid":
            fechar()
            saida.append(f"<table {TAB_ATTR}>{d_grid_linha(b, bg, E)}</table>{ESP}")
        else:
            linhas.append(d_frow(b, bg, E=E))
    fechar()
    return "".join(saida)


def d_sec(b, X, E=False):
    return f"<h2>{dh_texto(b['texto'])}</h2>"


def d_p(b, X, E=False):
    return f"<p>{dh_texto(b['texto'])}</p>"


def d_nota(b, X, E=False):
    return f'<p><font size="2" color="{TINTA3}">{dh_texto(b["texto"])}</font></p>'


def d_lbl(b, X, E=False):
    # o rótulo de uma tabela fica na mesma página que a tabela (manter com o próximo)
    return f'<p style="page-break-after:avoid">{dh_label(b["texto"])}</p>'


def d_ck(b, X, E=False):
    marcados = (b.get("ex") or []) if E else []
    out = []
    for idx, it in enumerate(b["itens"]):
        v = marcados[idx] if idx < len(marcados) else None
        if b["sn"]:
            a, c = sn_palavras(b["sn"])
            out.append(f"<p>{esc(it)} &nbsp; {dcx(v == 'a')} {esc(a)} &nbsp; {dcx(v == 'c')} {esc(c)}</p>")
        else:
            out.append(f"<p>{dcx(bool(v))} {esc(it)}</p>")
    return "".join(out)


def d_opts(b, X, E=False):
    marc = indices(b.get("ex")) if E else []
    ops = " &nbsp; ".join(f"{dcx(i in marc)} {esc(o)}" for i, o in enumerate(b["opcoes"]))
    return f"<p><b>{esc(plain(b['label']))}</b> &nbsp; {ops}</p>"


def d_formula(b, X, E=False, bg=PET_CL2):
    exs = (b.get("ex") or []) if E else []
    cab = f"<p>{dh_label(b['label'])}</p>"
    linhas = "".join(
        f'<tr><td width="36%" bgcolor="{bg}" valign="top"><b>{esc(p)}</b></td>'
        f'<td height="34">{d_exemplo(exs[i]) if i < len(exs) and exs[i] else "&nbsp;"}</td></tr>'
        for i, p in enumerate(b["partes"]))
    return f"{cab}<table {TAB_ATTR}>{linhas}</table>{ESP}"


def d_legenda(b, X, E=False):
    cel = "".join(f'<td width="20%" valign="top" bgcolor="{PET_CL2}"><b>{esc(a)}</b><br><font size="2" color="{TINTA3}">{esc(t)}</font></td>'
                  for a, t in b["itens"])
    return f"<table {TAB_JUNTA}><tr>{cel}</tr></table>{ESP}"


def d_duas(b, X, E=False):
    exs = (b.get("ex") or ([], [])) if E else ([], [])
    linhas = [f'<tr><td width="50%" bgcolor="{PET_CL2}"><b>{esc(b["esq"][0])}</b> <font size="2" color="{TINTA3}">{esc(b["esq"][1])}</font></td>'
              f'<td width="50%" bgcolor="{PET_CL2}"><b>{esc(b["dir"][0])}</b> <font size="2" color="{TINTA3}">{esc(b["dir"][1])}</font></td></tr>']
    for i in range(1, b["n"] + 1):
        e = exs[0][i - 1] if i - 1 < len(exs[0]) else ""
        d = exs[1][i - 1] if i - 1 < len(exs[1]) else ""
        linhas.append(f'<tr><td height="34">{i}. {d_exemplo(e) if e else ""}</td>'
                      f'<td height="34">{i}. {d_exemplo(d) if d else ""}</td></tr>')
    return f"<table {TAB_JUNTA}>{''.join(linhas)}</table>{ESP}"


def d_tres(b, X, E=False):
    exs = (b.get("ex") or []) if E else []
    if b.get("cls") == "deg":
        cores, txt = [PET_CL, PET, PET_ESC], [PET_ESC, "#FFFFFF", "#FFFFFF"]
    else:
        cores, txt = [PET, DOUR, CORAL], ["#FFFFFF", PET_ESC, "#FFFFFF"]
    cab = "".join(f'<td width="33%" bgcolor="{cores[i]}"><font color="{txt[i]}"><b>{esc(tt)}</b></font><br>'
                  f'<font size="2" color="{txt[i]}">{esc(sub)}</font></td>' for i, (tt, sub) in enumerate(b["cols"]))
    alt = 22 * b["n"]
    corpo = "".join(f'<td height="{alt}" valign="top">{d_exemplo(exs[i]) if i < len(exs) and exs[i] else "&nbsp;"}</td>'
                    for i in range(len(b["cols"])))
    return f"<table {TAB_JUNTA}><tr>{cab}</tr><tr>{corpo}</tr></table>{ESP}"


def d_quad(b, X, E=False):
    exs = (b.get("ex") or []) if E else []
    (colx, coly) = b["eixos"]
    linhas = [f'<tr><td width="16%" bgcolor="{PET_CL2}">&nbsp;</td><td width="42%" bgcolor="{PET_CL2}"><b>{esc(colx[0])}</b></td>'
              f'<td width="42%" bgcolor="{PET_CL2}"><b>{esc(colx[1])}</b></td></tr>']
    alt = 22 * b["n"]
    for r in range(2):
        cel = f'<td bgcolor="{PET_CL2}" valign="top"><b>{esc(coly[r])}</b></td>'
        for c in range(2):
            i = r * 2 + c
            tt, sub = b["quadrantes"][i]
            ex = d_exemplo(exs[i]) if i < len(exs) and exs[i] else "&nbsp;"
            cel += (f'<td height="{alt}" valign="top"><font color="{PET_ESC}"><b>{esc(tt)}</b></font> '
                    f'<font size="2" color="{TINTA3}">{esc(sub)}</font><br>{ex}</td>')
        linhas.append(f"<tr>{cel}</tr>")
    return f"<table {TAB_JUNTA}>{''.join(linhas)}</table>{ESP}"


def d_quadro(b, X, E=False):
    exs = (b.get("ex") or {}) if E else {}
    cartoes, lims, trav = exs.get("cartoes", []), exs.get("limites", []), exs.get("travado", [])
    n = len(b["colunas"])
    cab, corpo = "", ""
    for i, (tt, sub, lim) in enumerate(b["colunas"]):
        limite = f" (limite: {d_exemplo(lims[i]) if i < len(lims) and lims[i] else '____'})" if lim else ""
        cab += (f'<td width="{100 // n}%" bgcolor="{PET_ESC if i < n - 1 else DOUR}"><font color="{CREME if i < n - 1 else PET_ESC}">'
                f'<b>{esc(tt)}</b>{limite}</font><br><font size="2" color="{CREME if i < n - 1 else PET_ESC}">{esc(sub)}</font></td>')
        itens = [texto_de(cartoes, i, j) for j in range(b["n"])]
        corpo += f'<td height="{18 * b["n"]}" valign="top">{"<br>".join(d_exemplo(t) if t else "&nbsp;" for t in itens)}</td>'
    tt, sub = b["travado"]
    tv = "<br>".join(d_exemplo(t) for t in trav if t) or "&nbsp;"
    return (f"<table {TAB_JUNTA}><tr>{cab}</tr><tr>{corpo}</tr>"
            f'<tr><td colspan="{n}" height="40" bgcolor="{CORAL_CL}" valign="top"><b>{esc(tt)}</b> '
            f'<font size="2" color="{TINTA3}">{esc(sub)}</font><br>{tv}</td></tr></table>{ESP}')


def d_fichas(b, X, E=False):
    exs = (b.get("ex") or []) if E else []
    cels = []
    for i in range(b["n"]):
        marc, frase = exs[i] if i < len(exs) else (None, "")
        ops = " &nbsp; ".join(f"{dcx(marc == k)} {esc(o)}" for k, o in enumerate(b["opcoes"]))
        cels.append(f'<td width="50%" height="150" valign="top"><b>{esc(b["pergunta"])}</b><br>{ops}<br>'
                    f'<font size="2" color="{TINTA3}">{esc(b["frase"])}</font><br>{d_exemplo(frase) if frase else ""}</td>')
    linhas = "".join(f"<tr>{''.join(cels[i:i + 2])}</tr>" for i in range(0, len(cels), 2))
    return f"<table {TAB_ATTR}>{linhas}</table>{ESP}"


def d_niveis(b, X, E=False):
    linhas = "".join(f'<tr><td width="22%" bgcolor="{PET_CL2}"><b>{i} · {esc(t)}</b></td><td>{esc(d)}</td></tr>'
                     for i, (t, d) in enumerate(b["itens"], 1))
    return f"<table {TAB_JUNTA}>{linhas}</table>{ESP}"


def d_opcoes(opcoes, marc=()):
    """Opções com caixa de marcar: cada uma não quebra por dentro, e a linha quebra entre as opções."""
    return " ".join(f"{dcx(o in marc)}&nbsp;{esc(o).replace(' ', '&nbsp;')}" for o in opcoes)


def d_celula(col, valor, k, primeira, h_px, exv=None):
    f = col["fill"]
    if valor is None and exv is not None:
        if f == "num":
            return f'<td height="{h_px}" align="center" valign="top"><b>{k}</b></td>'
        if f == "cx":
            return f'<td height="{h_px}" align="center" valign="middle">{dcx(bool(exv))}</td>'
        if f == "sn":
            return f'<td height="{h_px}" valign="top">{dcx(exv == D.SN[0])} Sim &nbsp; {dcx(exv == D.SN[1])} Não</td>'
        if isinstance(f, tuple) and f[0] == "opts":
            return f'<td height="{h_px}" valign="top">{d_opcoes(f[1], indices(exv))}</td>'
        return f'<td height="{h_px}" valign="top">{d_exemplo(exv)}</td>'
    if valor is None:
        if f == "num":
            return f'<td height="{h_px}" align="center" valign="top"><b>{k}</b></td>'
        if f == "sn":
            return f'<td height="{h_px}" valign="top">{CX} Sim &nbsp; {CX} Não</td>'
        if f == "cx":
            return f'<td height="{h_px}" align="center" valign="middle">{CX}</td>'
        if f == "datas":
            return f'<td height="{h_px}" valign="top">de ________<br>a ________</td>'
        if f == "bolas":
            return f'<td height="{h_px}" valign="top">{"&#9675; " * 10}</td>'
        if isinstance(f, tuple) and f[0] == "opts":
            return f'<td height="{h_px}" valign="top">{d_opcoes(f[1])}</td>'
        return f'<td height="{h_px}" valign="top">&nbsp;</td>'
    if isinstance(valor, dict):
        if valor.get("agil"):
            return f'<td height="{h_px}" bgcolor="{DOUR_CL}" valign="top">{dh_label(valor["txt"], DOUR_TX)}</td>'
        if "opts" in valor:
            return f'<td height="{h_px}" valign="top">{d_opcoes(valor["opts"])}</td>'
        if valor.get("sn"):
            return f'<td height="{h_px}" valign="top">{CX} Sim &nbsp; {CX} Não</td>'
    if primeira:
        return f'<td height="{h_px}" bgcolor="{PET_CL2}" valign="top">{dh_label(valor)}</td>'
    return f'<td height="{h_px}" valign="top">{dh_texto(valor)}</td>'


def d_tab(b, X, E=False):
    cols = b["cols"]
    tot = sum(c["w"] for c in cols)
    fid = fid_de(b, E)
    extra = X.get(fid, 0) if fid else 0
    so_escritas = b["flex"] and b["blank"] == 0
    exrows = (b.get("ex") or []) if E else []
    n_pre = len(linhas_escritas(b))
    blank0 = b["blank"]
    h_px = int(min(b["h"], 8) * DOCX_ALTO / 8 * PX_MM)      # no DOCX a linha pede no máximo DOCX_ALTO mm (padrão 8): o texto aumenta a linha se precisar
    larg = [f'{c["w"] / tot * 100:.1f}%' for c in cols]

    def th(texto, agil=False, w=None):
        bg = DOUR if agil else PET_ESC
        fg = PET_ESC if agil else "#FFFFFF"
        cor_d = PET_ESC if agil else "#D4F1F2"
        a = f' width="{w}"' if w else ""
        corpo = "".join(
            f'<font size="2" color="{cor_d}">{esc(p[1:-1])}</font>' if p.startswith("{") and p.endswith("}")
            else f'<font color="{fg}"><b>{esc(p)}</b></font>'
            for p in re.split(r"(\{[^}]*\})", texto) if p)
        return f'<th bgcolor="{bg}" align="left" valign="middle"{a}>{corpo}</th>'

    head = "<tr>" + "".join(th(c["h"], agil=c["agil"], w=larg[i]) for i, c in enumerate(cols)) + "</tr>"
    linhas = []
    k = b["num0"]
    ri = 0
    for r in b["rows"]:
        if isinstance(r, dict) and "banda" in r:
            dica = f' &nbsp; <font size="2" color="{TINTA3}">{esc(r["dica"])}</font>' if r.get("dica") else ""
            linhas.append(f'<tr><td colspan="{len(cols)}" bgcolor="{PET_CL}">{dh_label(r["banda"])}{dica}</td></tr>')
            continue
        hh = h_px
        if isinstance(r, dict):
            hh = int(r["h"] * PX_MM)
            r = r["r"]
        exr = exrows[ri] if ri < len(exrows) else None
        linhas.append("<tr>" + "".join(d_celula(cols[i], v, k, i == 0 and cols[i]["fill"] != "num", hh,
                                                exr[i] if exr else None) for i, v in enumerate(r)) + "</tr>")
        k += 1
        ri += 1
    for _ in range(blank0 + (0 if so_escritas else extra)):
        exr = exrows[ri] if ri < len(exrows) else None
        linhas.append("<tr>" + "".join(
            d_celula(c, None, k, False, h_px, exr[i] if exr else None) for i, c in enumerate(cols)) + "</tr>")
        k += 1
        ri += 1
    attr = TAB_JUNTA if b.get("junta") else TAB_ATTR
    return f"<table {attr}><thead>{head}</thead><tbody>{''.join(linhas)}</tbody></table>{ESP}"


def d_agil(b, X, E=False):
    """Caixa dourada: uma tabela simples, com o título na primeira linha. Blocos largos saem como tabela própria."""
    saida = []
    linhas = [f'<tr><td colspan="2" bgcolor="{DOUR}"><font color="{PET_ESC}"><b>{esc(b["titulo"])}</b></font></td></tr>']

    def fechar():
        if linhas:
            saida.append(f"<table {TAB_JUNTA}>{''.join(linhas)}</table>{ESP}")
            linhas.clear()

    for f in b["filhos"]:
        t = f["t"]
        if t == "p":
            linhas.append(f'<tr><td colspan="2" bgcolor="{DOUR_CL}">{dh_texto(f["texto"])}</td></tr>')
        elif t == "f":
            linhas.append(d_frow(f, DOUR_CL, E=E))
        elif t == "grid":
            linhas.extend(d_frow(i, DOUR_CL, E=E) for i in f["itens"])
        elif t == "ck":
            marcados = (f.get("ex") or []) if E else []
            for idx, it in enumerate(f["itens"]):
                v = marcados[idx] if idx < len(marcados) else None
                if f["sn"]:
                    a, c = sn_palavras(f["sn"])
                    linhas.append(f'<tr><td colspan="2" bgcolor="{DOUR_CL}">{esc(it)} &nbsp; {dcx(v == "a")} {esc(a)} &nbsp; {dcx(v == "c")} {esc(c)}</td></tr>')
                else:
                    linhas.append(f'<tr><td colspan="2" bgcolor="{DOUR_CL}">{dcx(bool(v))} {esc(it)}</td></tr>')
        elif t == "opts":
            marc = indices(f.get("ex")) if E else []
            ops = " &nbsp; ".join(f"{dcx(i in marc)} {esc(o)}" for i, o in enumerate(f["opcoes"]))
            linhas.append(f'<tr><td colspan="2" bgcolor="{DOUR_CL}"><b>{esc(plain(f["label"]))}</b> &nbsp; {ops}</td></tr>')
        elif t == "formula":
            exs = (f.get("ex") or []) if E else []
            linhas.append(f'<tr><td colspan="2" bgcolor="{DOUR_CL}">{dh_label(f["label"])}</td></tr>')
            for i, p in enumerate(f["partes"]):
                linhas.append(f'<tr><td width="36%" bgcolor="{DOUR_CL}" valign="top">{esc(p)}</td>'
                              f'<td height="34">{d_exemplo(exs[i]) if i < len(exs) and exs[i] else "&nbsp;"}</td></tr>')
        else:  # duas, lbl, tab, tres e outros blocos largos
            fechar()
            saida.append(DOCX[t](f, X, E))
    fechar()
    return "".join(saida)


DOCX = {"sec": d_sec, "p": d_p, "nota": d_nota, "lbl": d_lbl, "ck": d_ck, "opts": d_opts, "agil": d_agil,
        "formula": d_formula, "legenda": d_legenda, "duas": d_duas, "tres": d_tres, "quad": d_quad, "quadro": d_quadro, "fichas": d_fichas, "niveis": d_niveis, "tab": d_tab}


def docx_blocos(blocos, X, E=False):
    saida, buf = [], []

    def fechar():
        if buf:
            saida.append(d_campos(list(buf), E=E))
            buf.clear()

    for b in blocos:
        if b.get("so_a4"):
            continue
        if b["t"] in ("f", "grid"):
            buf.append(b)
        else:
            fechar()
            saida.append(DOCX[b["t"]](b, X, E))
    fechar()
    return "".join(saida)


def logo_docx_b64():
    im = Image.open(LOGO_ABS).convert("RGBA")
    im = im.crop(im.getbbox())
    im = im.resize((1100, round(im.height * 1100 / im.width)), Image.LANCZOS)
    fundo = Image.new("RGBA", im.size, (255, 255, 255, 255))
    fundo.alpha_composite(im)
    buf = io.BytesIO()
    fundo.convert("RGB").save(buf, "PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode(), fundo.width / fundo.height


DOCX_UNIR_TABELAS = set()   # códigos cujas tabelas de páginas seguidas, com as mesmas colunas, viram uma só no DOCX


def paginas_docx(m):
    """O DOCX é um fluxo contínuo. Nos modelos de DOCX_UNIR_TABELAS, as tabelas de páginas seguidas, com as mesmas
    colunas, viram uma só tabela, para o cabeçalho se repetir a cada página em vez de aparecer no meio dela."""
    if m["cod"] not in DOCX_UNIR_TABELAS:
        return m["paginas"]
    saida = []
    for b in [b for pg in m["paginas"] for b in pg]:
        ant = saida[-1] if saida else None
        if (ant and ant["t"] == "tab" and b["t"] == "tab" and [c["h"] for c in ant["cols"]] == [c["h"] for c in b["cols"]]):
            saida[-1] = dict(ant, rows=ant["rows"] + b["rows"], blank=ant["blank"] + b["blank"])
        else:
            saida.append(b)
    return [saida]


def html_docx(m, X, logo_b64):
    global DOCX_ALTO
    DOCX_ALTO = m.get("docx_alto") or 8
    fmt = FORMATOS[m["formato"]]
    partes = [esc(rotulo_passo(m)).upper(), esc(rotulo_tempo(m)).upper()]
    if m["skill_primaria"]:
        partes.append(f"SKILL: {esc(m['skill_primaria'])}")
    ref = f'<font size="2" color="{DOUR_TX}"><b>' + " &nbsp;·&nbsp; ".join(partes) + "</b></font>"
    em_branco = "\n".join(docx_blocos(blocos, X, False) for blocos in paginas_docx(m))
    exemplo = "\n".join(docx_blocos(blocos, X, True) for blocos in paginas_docx(m))
    while em_branco.rstrip().endswith(ESP):      # o espaço depois da última tabela não pode abrir uma página só para ele
        em_branco = em_branco.rstrip()[:-len(ESP)]
    faixa = (f'<p style="page-break-before:always;margin:0;font-size:1pt">&nbsp;</p>'
             f'<table border="0" cellpadding="6" cellspacing="0" width="100%">'
             f'<tr><td bgcolor="{PET_ESC}"><font color="{CREME}"><b>EXEMPLO PREENCHIDO &nbsp;·&nbsp; {esc(m["setor"])}</b>'
             f'</font></td></tr></table>{ESP}')
    css = f"""@page {{ size: {fmt['docx']}; margin: 1.2cm 1.5cm 1.5cm 1.5cm; }}
body {{ font-family: Arial, sans-serif; font-size: 10.5pt; color: {TINTA}; }}
h1 {{ font-family: Arial, sans-serif; font-size: 19pt; color: {PET_ESC}; margin-top: 0; margin-bottom: 4pt; }}
h2 {{ font-family: Arial, sans-serif; font-size: 12.5pt; color: {PET_ESC}; margin-top: 12pt; margin-bottom: 4pt; }}
p {{ font-family: Arial, sans-serif; font-size: 10.5pt; margin-top: 0; margin-bottom: 4pt; }}
p.sp {{ font-size: 5pt; margin: 0; }}
td, th {{ font-family: Arial, sans-serif; font-size: 10.5pt; vertical-align: top; }}"""
    altura = 22
    return (f'<!DOCTYPE html>\n<html lang="pt-BR"><head><meta charset="utf-8">'
            f'<meta http-equiv="content-language" content="pt-BR"><meta name="author" content="MindMaster Educação Profissional">'
            f'<title>{m["cod"]} {esc(m["titulo"])}</title><style>\n{css}\n</style></head><body>\n'
            f'<p><img src="data:image/png;base64,{logo_b64[0]}" width="{round(altura * logo_b64[1])}" height="{altura}" alt="Gestão Ágil 2.0"></p>\n'
            f'<p><font size="2" color="{DOUR_TX}"><b>MODELO {m["cod"]}</b></font><br>{ref}</p>\n'
            f'<h1>{esc(m["titulo"])}</h1>\n'
            f'<table border="0" cellpadding="6" cellspacing="0" width="100%"><tr><td bgcolor="{PET_CL}">'
            f'<font size="2" color="{TEAL_FORTE}"><b>COMO USAR</b></font><br>{esc(m["como"])}</td></tr></table>{ESP}\n'
            + em_branco + "\n" + faixa + exemplo +
            f'\n<div title="footer"><p align="center"><font size="1" color="{TINTA3}">{RODAPE} · {m["cod"]}</font></p></div>\n'
            f'</body></html>\n')


def rodar(cmd, tempo):
    """Roda um comando num grupo de processos próprio; se passar do tempo, encerra só esse grupo (nunca pkill)."""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        out, err = p.communicate(timeout=tempo)
    except subprocess.TimeoutExpired:
        os.killpg(p.pid, signal.SIGKILL)
        p.communicate()
        raise SystemExit(f"{cmd[0]} passou de {tempo} s e o grupo {p.pid} foi encerrado")
    return p.returncode, out, err


def converter_docx(modelos, extras):
    pasta_html = SCRATCH / "docx-html"
    pasta_out = SCRATCH / "docx-out"
    for p in (pasta_html, pasta_out):
        shutil.rmtree(p, ignore_errors=True)
        p.mkdir(parents=True)
    logo = logo_docx_b64()
    arqs = []
    for m in modelos:
        p = pasta_html / (nome_arquivo(m) + ".html")
        p.write_text(html_docx(m, extras[m["cod"]], logo), encoding="utf-8")
        arqs.append(p)
    perfil = SCRATCH / "lo-perfil"
    cmd = ["soffice", f"-env:UserInstallation=file://{perfil}", "--headless", "--infilter=HTML (StarWriter)",
           "--convert-to", "docx:MS Word 2007 XML", "--outdir", str(pasta_out), *map(str, arqs)]
    rc, out, err = rodar(cmd, 900)
    if rc != 0:
        raise SystemExit("soffice falhou:\n" + out + err)
    destino = SAIDA / "docx"
    destino.mkdir(parents=True, exist_ok=True)
    for m in modelos:
        origem = pasta_out / (nome_arquivo(m) + ".docx")
        if not origem.exists():
            raise SystemExit(f"DOCX não gerado: {origem}")
        ajustar_idioma(origem, destino / origem.name)


def ajustar_idioma(origem, destino):
    """Pós-processa o DOCX do LibreOffice: troca en-US por pt-BR em styles.xml e core.xml (o corretor não marca tudo de
    vermelho) e impede que uma linha de tabela se parta entre duas páginas (w:cantSplit em document.xml)."""
    with zipfile.ZipFile(origem) as zi, zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zo:
        for info in zi.infolist():
            dados = zi.read(info.filename)
            if info.filename in ("word/styles.xml", "docProps/core.xml"):
                dados = dados.replace(b"en-US", b"pt-BR")
            if info.filename == "word/document.xml":
                s = dados.decode("utf-8")
                s = re.sub(r"<w:trPr>(?!<w:cantSplit/>)", "<w:trPr><w:cantSplit/>", s)
                s = re.sub(r"<w:tr>(?!<w:trPr>)", "<w:tr><w:trPr><w:cantSplit/></w:trPr>", s)
                dados = s.encode("utf-8")
            zo.writestr(info, dados)


# ------------------------------------------------------------------ PDF, prévia e conferências
def arquivos_previa(m):
    return [SAIDA / "previa" / f"{m['cod']}-p{k + 1}.png" for k in range(2 * len(m["paginas"]))]


def gerar_pdf_previa(modelos):
    (SAIDA / "pdf").mkdir(parents=True, exist_ok=True)
    (SAIDA / "previa").mkdir(parents=True, exist_ok=True)
    lista = [{"html": str(SAIDA / (nome_arquivo(m) + ".html")), "pdf": str(SAIDA / "pdf" / (nome_arquivo(m) + ".pdf")),
              "pngs": [str(p) for p in arquivos_previa(m)]} for m in modelos]
    SCRATCH.mkdir(parents=True, exist_ok=True)
    spec = SCRATCH / "lista-render.json"
    spec.write_text(json.dumps(lista), encoding="utf-8")
    r = subprocess.run([NODE, str(AQUI / "render.cjs"), str(spec)], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("render.cjs falhou:\n" + r.stderr)
    return json.loads(r.stdout)


def paginas_pdf(caminho):
    r = subprocess.run(["pdfinfo", str(caminho)], capture_output=True, text=True)
    m = re.search(r"Pages:\s+(\d+)", r.stdout)
    t = re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", r.stdout)
    return int(m.group(1)), (float(t.group(1)), float(t.group(2)))


PROIBIDAS = ["fundamental", "essencial", "crucial", "além disso", "potencializar", "alavancar", "transformar",
             "simplesmente", "na verdade", "ilustrativo", "ilustrativa"]
# Regras de voz dos modelos: nada de "cabe/comporta", "capacidade disponível", "quem executa".
# Dia da semana abreviado nunca; por extenso só dentro de calendário ou grade de dias (tabela).
VOCABULARIO_VETADO = re.compile(
    r"\b(cabe|cabem|cabia|caber|comporta|comportam|absorve|acomoda|alocar|alocação|capacidade disponível|quem executa)\b")
# Abreviação de dia: "Seg", "Ter"... com inicial maiúscula (o verbo "ter" em minúscula não conta) ou qualquer uma seguida
# de ponto ("seg.").
DIAS_ABREVIADOS = re.compile(r"\b(Seg|Ter|Qua|Qui|Sex|Sáb|Sab|Dom)\b|\b(seg|ter|qua|qui|sex|sáb|sab|dom)\.")
DIAS_POR_EXTENSO = re.compile(r"\b(segunda|terça|terca|quarta|quinta|sexta|sábado|sabado|domingo)(?:-feira)?\b")


def conferir_texto(modelos, med):
    problemas = []
    for m in modelos:
        liberadas = set(m.get("permitir", ()))
        for pg in med[nome_arquivo(m) + ".html"]:
            t = pg["texto"]
            rot = f"{m['cod']} p{pg['pagina']}"
            for ch, nome in (("—", "travessão"), ("–", "meia-risca"), ("“", "aspas curvas"),
                             ("”", "aspas curvas"), ("‘", "aspas curvas"), ("’", "aspas curvas")):
                if ch in t:
                    problemas.append(f"{rot}: {nome}")
            if re.search(r"\s-\s", t):
                problemas.append(f"{rot}: hífen solto como travessão")
            low = t.lower()
            for w in PROIBIDAS:
                if w in low and w not in liberadas:
                    problemas.append(f"{rot}: palavra '{w}'")
            if re.search(r"não é [^.;]{1,40}[,;] é ", low):
                problemas.append(f"{rot}: 'não é X, é Y'")
            for achado in VOCABULARIO_VETADO.findall(low):
                if achado not in liberadas:
                    problemas.append(f"{rot}: vocabulário vetado '{achado}'")
            for achado in DIAS_ABREVIADOS.findall(t):
                problemas.append(f"{rot}: dia da semana abreviado '{''.join(achado)}'")
            for achado in DIAS_POR_EXTENSO.findall(pg["textoSemTabela"].lower()):
                problemas.append(f"{rot}: dia da semana por extenso fora de calendário '{achado}'")
    return problemas


def conferir_layout(modelos, med):
    """Estouro, texto que escapou da caixa, letra abaixo de 10 pt e faixa "Como usar" com mais de 3 linhas, em todas as
    páginas (as em branco e as de exemplo)."""
    problemas = []
    for m in modelos:
        for pg in med[nome_arquivo(m) + ".html"]:
            rot = f"{m['cod']} p{pg['pagina']} ({pg['tipo']})"
            if pg["estouro"]:
                problemas.append(f"{rot}: conteúdo passou do fim da página")
            if pg["largura"]:
                problemas.append(f"{rot}: texto escapou da caixa {pg['largura'][:3]}")
            if pg["menorPt"] < 9.95:
                problemas.append(f"{rot}: letra de {pg['menorPt']:.1f} pt")
            if pg["comoLinhas"] > 3:
                problemas.append(f"{rot}: 'Como usar' com {pg['comoLinhas']} linhas (o máximo é 3)")
            if pg["titLinhas"] > 1:
                problemas.append(f"{rot}: título com {pg['titLinhas']} linhas")
    return problemas


def blocos_planos(blocos):
    for b in blocos:
        yield b
        if b["t"] == "agil":
            yield from blocos_planos(b["filhos"])
        if b["t"] == "grid":
            yield from blocos_planos(b["itens"])


def conferir_dados(modelos):
    """Todo bloco que a pessoa preenche tem o valor de exemplo (ex=). ex="" quer dizer vazio de propósito."""
    problemas = []
    for m in modelos:
        c = m["cod"]
        for campo in ("passo", "tempo", "setor", "como", "caso"):
            if not m.get(campo):
                problemas.append(f"{c}: falta {campo}")
        if m["formato"] not in FORMATOS:
            problemas.append(f"{c}: formato '{m['formato']}' desconhecido (use {list(FORMATOS)})")
        t = m.get("tempo") or {}
        if not isinstance(t.get("min"), int) or t["min"] <= 0:
            problemas.append(f"{c}: tempo sem minutos")
        if not (isinstance(t.get("fonte"), str) and t["fonte"].strip()):
            problemas.append(f"{c}: tempo sem fonte (a aula de onde veio, ou 'est.')")
        if m["skill_primaria"] is not None and not (isinstance(m["skill_primaria"], str) and m["skill_primaria"].strip()):
            problemas.append(f"{c}: skill_primaria precisa ser um texto ou None")
        if not isinstance(m["skills_compartilhadas"], list) or not all(isinstance(s, str) for s in m["skills_compartilhadas"]):
            problemas.append(f"{c}: skills_compartilhadas precisa ser uma lista de textos")
        if m["skill_primaria"] is None and m["skills_compartilhadas"]:
            problemas.append(f"{c}: sem skill primária e com skills compartilhadas")
        for pg in m["paginas"]:
            for b in blocos_planos(pg):
                t = b["t"]
                rot = f"{c}: bloco {t}"
                if t in ("f", "ck", "opts", "formula", "duas", "tres", "quad", "quadro", "fichas", "tab") and b.get("ex") is None:
                    nome = b.get("label") or (b.get("cols") and b["cols"][0] if t != "tab" else b["cols"][0]["h"]) or ""
                    problemas.append(f"{rot} '{str(nome)[:40]}' sem exemplo (ex=)")
                if t == "tab" and b.get("ex") is not None:
                    pre = linhas_escritas(b)
                    if len(b["ex"]) > len(pre) + b["blank"]:
                        problemas.append(f"{rot} com mais linhas de exemplo ({len(b['ex'])}) do que linhas "
                                         f"({len(pre) + b['blank']})")
                    for i, exr in enumerate(b["ex"]):
                        if len(exr) != len(b["cols"]):
                            problemas.append(f"{rot}: linha {i + 1} do exemplo com {len(exr)} valores para "
                                             f"{len(b['cols'])} colunas")
                        elif i < len(pre):
                            r = pre[i]["r"] if isinstance(pre[i], dict) else pre[i]
                            for j, v in enumerate(exr):
                                if v is not None and r[j] is not None:
                                    problemas.append(f"{rot}: exemplo escrito sobre célula já escrita (linha {i + 1}, "
                                                     f"coluna {j + 1})")
    return problemas


def cor_teal_700(cor):
    """O teal-700 do kit (2B6F70). O PDF do Chromium arredonda os canais em até 1 ponto; aceita até 3."""
    r, g, b = (cor >> 16) & 255, (cor >> 8) & 255, cor & 255
    return abs(r - 0x2B) <= 3 and abs(g - 0x6F) <= 3 and abs(b - 0x70) <= 3


def conferir_pdfs(modelos, med):
    """Confere cada PDF: páginas iguais às do HTML, letra de 10 pt ou mais no corpo, texto todo presente e dentro da
    página, página quase vazia, e o texto do exemplo em Manrope teal-700 de 10,5 pt. Devolve (linhas, problemas)."""
    import fitz
    linhas, problemas = [], []
    topo = CAB_MM / 25.4 * 72
    for m in modelos:
        arq = SAIDA / "pdf" / (nome_arquivo(m) + ".pdf")
        doc = fitz.open(arq)
        paginas_html = med[nome_arquivo(m) + ".html"]
        if len(doc) != len(paginas_html):
            problemas.append(f"{m['cod']}: PDF com {len(doc)} páginas e HTML com {len(paginas_html)}")
        for i, page in enumerate(doc):
            base = page.rect.height - ROD_MM / 25.4 * 72
            menor, ymax, fora = 99.0, 0.0, []
            exemplo = []
            texto_pdf = re.sub(r"\s+", "", unicodedata.normalize("NFKC", page.get_text("text")).lower())
            for bl in page.get_text("dict")["blocks"]:
                for ln in bl.get("lines", []):
                    for sp in ln["spans"]:
                        if not sp["text"].strip():
                            continue
                        x0, y0, x1, y1 = sp["bbox"]
                        if x0 < -0.5 or x1 > page.rect.width + 0.5 or y0 < -0.5 or y1 > page.rect.height + 0.5:
                            fora.append(sp["text"][:30])
                        if cor_teal_700(sp["color"]) and "Manrope" in sp["font"]:
                            exemplo.append(round(sp["size"], 1))
                        if y0 < topo or y1 > base:
                            continue
                        menor = min(menor, sp["size"])
                        ymax = max(ymax, y1)
            for d in page.get_drawings():
                r = d["rect"]
                if r.y0 >= topo and r.y1 <= base:
                    ymax = max(ymax, r.y1)
            ocupacao = (ymax - topo) / (base - topo)
            html_pg = paginas_html[i] if i < len(paginas_html) else None
            faltam = []
            if html_pg:
                tokens = set(re.findall(r"\w{3,}", unicodedata.normalize("NFKC", html_pg["texto"]).lower()))
                faltam = sorted(w for w in tokens if w not in texto_pdf)
            eh_exemplo = bool(html_pg and html_pg["tipo"] == "exemplo")
            linhas.append(f"{m['cod']} p{i + 1} ({'exemplo' if eh_exemplo else 'branco '}): menor letra {menor:.1f} pt | "
                          f"ocupação {ocupacao * 100:3.0f}% | fora da página {len(fora)} | "
                          f"palavras do HTML ausentes {len(faltam)}"
                          + (f" | texto do exemplo: {len(exemplo)} trechos, {sorted(set(exemplo))} pt" if eh_exemplo else ""))
            if menor < 9.95:
                problemas.append(f"{m['cod']} p{i + 1}: letra de {menor:.1f} pt no corpo")
            if ocupacao < 0.55:
                problemas.append(f"{m['cod']} p{i + 1}: página quase vazia ({ocupacao * 100:.0f}% do corpo)")
            if fora:
                problemas.append(f"{m['cod']} p{i + 1}: texto fora da página {fora[:3]}")
            if faltam:
                problemas.append(f"{m['cod']} p{i + 1}: palavras do HTML ausentes no PDF {faltam[:6]}")
            if eh_exemplo and not exemplo:
                problemas.append(f"{m['cod']} p{i + 1}: nenhum texto do exemplo em Manrope teal-700")
            if eh_exemplo and any(abs(s - 10.5) > 0.15 for s in exemplo):
                problemas.append(f"{m['cod']} p{i + 1}: texto do exemplo fora de 10,5 pt {sorted(set(exemplo))}")
    return linhas, problemas


def conferir_docx(modelos):
    """Converte cada DOCX em PDF pelo LibreOffice e aplica as mesmas regras do PDF do modelo: o mesmo número de páginas,
    nenhuma página quase vazia e o exemplo começando em página nova (logo depois das páginas em branco)."""
    import fitz
    pasta = SCRATCH / "docx-check"
    shutil.rmtree(pasta, ignore_errors=True)
    pasta.mkdir(parents=True)
    docs = [SAIDA / "docx" / (nome_arquivo(m) + ".docx") for m in modelos]
    cmd = ["soffice", f"-env:UserInstallation=file://{SCRATCH / 'lo-perfil-check'}", "--headless", "--convert-to", "pdf",
           "--outdir", str(pasta), *map(str, docs)]
    rc, out, err = rodar(cmd, 900)
    if rc != 0:
        return [], ["soffice falhou na conferência do DOCX: " + (out + err)[-200:]]
    linhas, problemas = [], []
    for m in modelos:
        base = nome_arquivo(m)
        pdf = pasta / (base + ".pdf")
        if not pdf.exists():
            problemas.append(f"{m['cod']}: DOCX não virou PDF")
            continue
        doc = fitz.open(pdf)
        n_modelo = len(fitz.open(SAIDA / "pdf" / (base + ".pdf")))
        if len(doc) != n_modelo:
            problemas.append(f"{m['cod']}: DOCX com {len(doc)} páginas e PDF do modelo com {n_modelo}")
        for i, page in enumerate(doc):
            topo = 12 / 25.4 * 72
            limite = page.rect.height - 22 / 25.4 * 72      # o rodapé do DOCX mora abaixo disso
            ymax = 0.0
            for bl in page.get_text("dict")["blocks"]:
                for ln in bl.get("lines", []):
                    for sp in ln["spans"]:
                        if sp["text"].strip() and sp["bbox"][3] <= limite:
                            ymax = max(ymax, sp["bbox"][3])
            for d in page.get_drawings():
                if d["rect"].y1 <= limite:
                    ymax = max(ymax, d["rect"].y1)
            ocup = (ymax - topo) / (limite - topo)
            linhas.append(f"{m['cod']} DOCX p{i + 1}: ocupação {ocup * 100:3.0f}%")
            if ocup < 0.55:
                problemas.append(f"{m['cod']} DOCX p{i + 1}: página quase vazia ({ocup * 100:.0f}% do corpo)")
        n_branco = len(m["paginas"])
        if len(doc) > n_branco and not doc[n_branco].get_text("text").strip().upper().startswith("EXEMPLO PREENCHIDO"):
            problemas.append(f"{m['cod']}: o exemplo do DOCX não começa na página {n_branco + 1}")
        linhas.append(f"{m['cod']} DOCX: {len(doc)} páginas (PDF do modelo: {n_modelo})")
    return linhas, problemas


def relatorio(modelos, med):
    linhas = []
    for m in modelos:
        for pg in med[nome_arquivo(m) + ".html"]:
            linhas.append(f"{m['cod']} p{pg['pagina']} ({pg['tipo']:7}): livre {pg['livre']:5.1f} mm | estouro "
                          f"{pg['estouro']!s:5} | menor {pg['menorPt']:.1f} pt | como {pg['comoLinhas']} linhas | "
                          f"título {pg['titLinhas']} | largura {pg['largura'] or '-'}")
    return "\n".join(linhas)


def rotulo_limpo(s):
    """Rótulo como está impresso na folha, sem a explicação em cinza ({...})."""
    return re.sub(r"\s+", " ", re.sub(r"\{[^}]*\}", "", s)).strip()


def campos_do_modelo(m):
    """Os rótulos dos campos, na ordem da folha (as páginas em branco, de cima para baixo). Vale cada rótulo impresso de
    campo, de rótulo de tabela, de escolha, de conta, de lista de marcar e de colunas com título. A tabela que tem
    rótulo, ou que vem logo depois de um campo, é desse rótulo; a tabela solta entra pelos títulos das colunas."""
    campos = []
    ultimo = [None]

    def anda(blocos):
        for b in blocos:
            t = b["t"]
            if t == "agil":
                anda(b["filhos"])
            elif t == "grid":
                anda(b["itens"])
            elif t == "f":
                campos.append(rotulo_limpo(b["label"]))
                ultimo[0] = "f"
            elif t == "lbl":
                campos.append(rotulo_limpo(b["texto"]))
                ultimo[0] = "lbl"
            elif t in ("opts", "formula"):
                campos.append(rotulo_limpo(b["label"]))
                ultimo[0] = t
            elif t == "ck":
                campos.extend(rotulo_limpo(i) for i in b["itens"])
                ultimo[0] = t
            elif t == "duas":
                campos.extend([rotulo_limpo(b["esq"][0]), rotulo_limpo(b["dir"][0])])
                ultimo[0] = t
            elif t == "tres":
                campos.extend(rotulo_limpo(c[0]) for c in b["cols"])
                ultimo[0] = t
            elif t == "quad":
                campos.extend(rotulo_limpo(q[0]) for q in b["quadrantes"])
                ultimo[0] = t
            elif t == "quadro":
                campos.extend(rotulo_limpo(c[0]) for c in b["colunas"])
                campos.append(rotulo_limpo(b["travado"][0]))
                ultimo[0] = t
            elif t == "fichas":
                campos.append(rotulo_limpo(b["pergunta"]))
                ultimo[0] = t
            elif t == "tab":
                if ultimo[0] not in ("lbl", "f"):
                    campos.append(" / ".join(rotulo_limpo(c["h"]) for c in b["cols"]))
                ultimo[0] = "tab"
            # sec, p, nota e legenda não são campos

    for pg in m["paginas"]:
        anda(pg)
    return campos


def caminho_modelos(caminho):
    """Caminho relativo a modelos-definitivos/ (a pasta acima de kit/)."""
    return Path(os.path.relpath(caminho, KIT.parent)).as_posix()


def gravar_json(modelos):
    """kit.json: o contrato que o construtor das skills lê. Os nomes dos campos são fixos."""
    lista = []
    for m in modelos:
        base = nome_arquivo(m)
        t = m["tempo"]
        lista.append({
            "codigo": m["cod"],
            "titulo": m["titulo"],
            "passo": rotulo_passo(m),
            "tempo_min": t["min"],
            "tempo_fonte": t["fonte"],
            "skill_primaria": m["skill_primaria"],
            "skills_compartilhadas": m["skills_compartilhadas"],
            "campos": campos_do_modelo(m),
            "formato": m["formato"],
            "paginas": {"branco": len(m["paginas"]), "exemplo": len(m["paginas"])},
            "arquivo_html": caminho_modelos(SAIDA / f"{base}.html"),
            "pdf": caminho_modelos(SAIDA / "pdf" / f"{base}.pdf"),
            "docx": caminho_modelos(SAIDA / "docx" / f"{base}.docx"),
            "exemplo": {"setor": m["setor"], "caso": m["caso"]},
        })
    saida = {"versao": getattr(D, "VERSAO", "lote-1-piloto"), "data": getattr(D, "DATA", ""), "modelos": lista}
    (SAIDA / "kit.json").write_text(json.dumps(saida, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return saida


def so_conferir(modelos):
    """Mede o HTML que já está na pasta e confere os dados, o texto, o layout e os PDFs, sem regenerar nada."""
    arqs = [SAIDA / (nome_arquivo(m) + ".html") for m in modelos]
    med = medir(arqs)
    print(relatorio(modelos, med))
    problemas = conferir_dados(modelos)
    print("Conferência dos dados:", problemas or "sem problemas")
    p2 = conferir_texto(modelos, med)
    print("Conferência de texto:", p2 or "sem problemas")
    p3 = conferir_layout(modelos, med)
    print("Conferência de layout:", p3 or "sem problemas")
    linhas, p4 = conferir_pdfs(modelos, med)
    print("\n".join(linhas))
    print("Conferência dos PDFs:", p4 or "sem problemas")
    linhas_d, p5 = conferir_docx(modelos)
    print("\n".join(linhas_d))
    print("Conferência dos DOCX:", p5 or "sem problemas")
    return 1 if (problemas or p2 or p3 or p4 or p5) else 0


def main():
    so_html = "--so-html" in sys.argv
    filtro = None
    if "--so" in sys.argv:
        filtro = set(sys.argv[sys.argv.index("--so") + 1].split(","))
    modelos = [m for m in D.MODELOS if filtro is None or m["cod"] in filtro]
    if "--conferir" in sys.argv:
        for m in modelos:
            atribuir_ids(m)
        return so_conferir(modelos)
    for m in modelos:
        atribuir_ids(m)
    problemas_dados = conferir_dados(modelos)
    print("Conferência dos dados:", problemas_dados or "sem problemas")
    extras = {m["cod"]: {} for m in modelos}
    SCRATCH.mkdir(parents=True, exist_ok=True)
    med = None
    for _ in range(8):
        arqs = escrever_html(modelos, extras)
        med = medir(arqs)
        if not distribuir(med, extras, modelos):
            break
    arqs = escrever_html(modelos, extras)
    med = medir(arqs)
    print(relatorio(modelos, med))
    problemas_texto = conferir_texto(modelos, med)
    print("Conferência de texto:", problemas_texto or "sem problemas")
    problemas_layout = conferir_layout(modelos, med)
    print("Conferência de layout:", problemas_layout or "sem problemas")
    json.dump(extras, open(SCRATCH / "extras.json", "w"), ensure_ascii=False, indent=1)
    if problemas_dados or problemas_layout:
        print("PARADO: corrija os dados ou o texto antes de gerar PDF, DOCX e prévias.")
        return 1
    if so_html:
        return 1 if problemas_texto else 0
    print(gerar_pdf_previa(modelos))
    converter_docx(modelos, extras)
    for m in modelos:
        n, tam = paginas_pdf(SAIDA / "pdf" / (nome_arquivo(m) + ".pdf"))
        ok = "ok" if n == 2 * len(m["paginas"]) else "DIFERENTE do HTML"
        print(f"{m['cod']}: PDF com {n} páginas ({ok}), tamanho {tam[0]:.0f} x {tam[1]:.0f} pt")
    linhas, probs = conferir_pdfs(modelos, med)
    print("\n".join(linhas))
    print("Conferência dos PDFs:", probs or "sem problemas")
    linhas_d, probs_d = conferir_docx(modelos)
    print("\n".join(linhas_d))
    print("Conferência dos DOCX:", probs_d or "sem problemas")
    probs = probs + probs_d
    if filtro is None or "--json-tudo" in sys.argv:
        saida = gravar_json(D.MODELOS if "--json-tudo" in sys.argv else modelos)
        print("kit.json:", saida["versao"], saida["data"], [(s["codigo"], s["paginas"]) for s in saida["modelos"]])
    return 1 if (problemas_texto or probs) else 0


if __name__ == "__main__":
    try:
        codigo = main()
    finally:
        fechar_medidor()
    sys.exit(codigo)
