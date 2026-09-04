"""Monta a forma DOCUMENTO: o conteúdo do canvas em documento corrido, no template da casa.

Obedece o padrão de documento da casa (SAIDA-HTML): h1 é a pergunta, lede responde em uma frase com um
único trecho grifado, 3 a 5 números-âncora, selo de procedência em todo valor, bloco Pessoas
envolvidas, seção Em aberto fechando e data de corte no rodapé. Só tokens da casa no CSS.
"""
import html as H
import re
from datetime import date

from . import TEMPLATE_ARTEFATO

CSS_EXTRA = """
/* ---------- forma documento (acréscimos; só tokens) ---------- */
section p.guia{font-family:var(--mono);font-size:12px;color:var(--ink-3);margin-top:6px}
section .valor{margin-top:10px;color:var(--ink-2);font-size:15.5px}
section .valor p{margin-top:8px}
section .valor ul{margin:8px 0 0;padding-left:20px}
section .valor li{margin:4px 0}
.claim.vazio{border-style:dashed;box-shadow:none}
.claim.vazio p{color:var(--ink-3)}
.scroll{margin-top:22px}
table td .seal{margin-left:6px}
.pessoas td:first-child{font-weight:620;color:var(--ink);width:38%}
"""


def _selo(v: str):
    t = (v or "").lower()
    if not v:
        return '<span class="seal o">em aberto</span>'
    if "(fato" in t or "(medido" in t or "fonte:" in t:
        return '<span class="seal v">medido</span>'
    if "(estim" in t:
        return '<span class="seal e">estimado</span>'
    if "(opini" in t:
        return '<span class="seal o">opinião</span>'
    return '<span class="seal o">sem fonte</span>'


def _valor_html(v: str) -> str:
    linhas = [l.rstrip() for l in (v or "").split("\n")]
    itens = [l for l in linhas if l.strip()]
    if not itens:
        return '<p>não preenchido</p>'
    if all(re.match(r"^\s*(?:[-•·]|\d+[.)])\s+", l) for l in itens) and len(itens) > 1:
        return "<ul>" + "".join(f"<li>{H.escape(re.sub(r'^\s*(?:[-•·]|\d+[.)])\s+', '', l))}</li>" for l in itens) + "</ul>"
    return "".join(f"<p>{H.escape(l.lstrip('-•· '))}</p>" for l in itens)


def _lista_html(v: str) -> str:
    itens = [l.strip(" -•·\t") for l in (v or "").split("\n") if l.strip(" -•·\t")]
    if not itens:
        return '<p>não preenchido</p>'
    return "<ul>" + "".join(f"<li>{H.escape(i)}</li>" for i in itens) + "</ul>"


def _campo_bloco(c: dict, v: str, lista=False) -> str:
    vazio = not (v or "").strip()
    guia = f'<p class="guia">{H.escape(c["guia"])}</p>' if c.get("guia") else ""
    corpo = _lista_html(v) if lista else _valor_html(v)
    return (f'<div class="claim{" vazio" if vazio else ""}"><div class="claim-top"><h3>{H.escape(c["rotulo"] or c["id"])}</h3>{_selo(v)}</div>'
            f'{guia}<div class="valor">{corpo}</div></div>')


def _tabela(cap: dict, campos: dict, valores: dict) -> str:
    cols = cap.get("colunas") or []
    n = cap.get("por_linha") or len(cols) or 1
    ids = cap["campos"]
    linhas = [ids[i:i + n] for i in range(0, len(ids), n)]
    out = ['<div class="scroll"><table><thead><tr>' + "".join(f"<th>{H.escape(c)}</th>" for c in cols) + "</tr></thead><tbody>"]
    algum = False
    for ln in linhas:
        vals = [valores.get(i, "") for i in ln]
        if not any(v.strip() for v in vals):
            continue
        algum = True
        out.append("<tr>" + "".join(f"<td>{H.escape(v)} {_selo(v) if v else ''}</td>" for v in vals) + "</tr>")
    if not algum:
        out.append(f'<tr><td colspan="{max(1, len(cols))}" class="dim">não preenchido</td></tr>')
    out.append("</tbody></table></div>")
    return "\n".join(out)


def montar(spec: dict, valores: dict | None = None, meta: dict | None = None) -> str:
    valores = dict(valores or {})
    meta = dict(meta or valores.get("_meta", {}) or {})
    for k, v in (valores.get("_meta") or {}).items():
        meta.setdefault(k, v)
    tpl = TEMPLATE_ARTEFATO.read_text(encoding="utf-8")
    cabeca = tpl[:tpl.index('<div class="wrap">') + len('<div class="wrap">')]
    cauda = tpl[tpl.index("</div>\n\n<script>"):]
    cabeca = cabeca.replace("<title>{{TITULO_CURTO}}</title>", f"<title>{H.escape(spec.get('titulo', spec['id']))}</title>")
    cabeca = cabeca.replace("</style>", CSS_EXTRA + "</style>", 1)

    campos = {c["id"]: c for c in spec.get("campos", [])}
    leitura = spec.get("leitura") or {}
    hoje = date.today().strftime("%d/%m/%Y")
    pergunta = (meta.get("pergunta") or leitura.get("pergunta_padrao") or f"O que diz o {spec.get('titulo', spec['id'])}?").strip()
    if not pergunta.endswith("?"):
        pergunta += "?"
    resposta = (meta.get("resposta") or "").strip()
    if resposta:
        lede = f"<em>{H.escape(resposta)}</em>" if "<em>" not in resposta else resposta
    else:
        lede = 'A resposta em uma frase ainda não foi escrita: <em>em aberto</em>.'

    total = [c for c in spec.get("campos", []) if not c.get("opcional")]
    cheios = [c for c in total if (valores.get(c["id"]) or "").strip()]
    facts = [
        ("Empresa", meta.get("empresa") or "não definida", "" if meta.get("empresa") else "em aberto"),
        ("Responde pelo resultado", meta.get("dono") or "não definido", "" if meta.get("dono") else "em aberto"),
        ("Data de corte", meta.get("data") or "sem data", "" if meta.get("data") else "em aberto"),
        ("Campos preenchidos", f"{len(cheios)} de {len(total)}", "contagem do construtor"),
    ]
    facts_html = "".join(f'<div class="fact"><dt>{H.escape(a)}</dt><dd>{H.escape(str(b))}<small>{H.escape(c)}</small></dd></div>' for a, b, c in facts)

    secoes = []
    for n, cap in enumerate(leitura.get("capitulos", []), 1):
        corpo = []
        if cap.get("forma") == "tabela":
            corpo.append(_tabela(cap, campos, valores))
        else:
            for cid in cap["campos"]:
                c = campos.get(cid)
                if not c:
                    continue
                v = valores.get(cid, "")
                if c.get("opcional") and not (v or "").strip():
                    continue
                corpo.append(_campo_bloco(c, v, lista=(cap.get("forma") == "lista")))
        secoes.append(f'<section><div class="s-head"><p class="eyebrow">Capítulo {n}</p></div><h2>{H.escape(cap["titulo"])}</h2>'
                      f'<div class="stack stack-tight" style="margin-top:22px">{"".join(corpo)}</div></section>')

    pessoas = [("Responde pelo resultado", meta.get("dono") or "não definido"),
               ("Pessoas que participam", meta.get("participantes") or "não definido"),
               ("Agentes que executam", meta.get("agentes") or "não definido"),
               ("Quem decide a trava", meta.get("decide_com") or "não definido"),
               ("Quem confirma que serve", meta.get("aceitante") or "não definido")]
    pessoas_html = ('<section><div class="s-head"><p class="eyebrow">Quem</p></div><h2>Pessoas envolvidas</h2>'
                    '<div class="scroll"><table class="pessoas"><tbody>' +
                    "".join(f"<tr><td>{H.escape(a)}</td><td>{H.escape(b)}</td></tr>" for a, b in pessoas) +
                    "</tbody></table></div><p class=\"s-sub\">Pessoa e agente nunca na mesma linha. Sem nome na fonte, fica \"não definido\".</p></section>")

    abertos = [c for c in total if not (valores.get(c["id"]) or "").strip()]
    itens_abertos = "".join(f'<div class="claim vazio"><div class="claim-top"><h3>{H.escape(c["rotulo"] or c["id"])}</h3><span class="seal o">não preenchido</span></div>'
                            f'<p>{H.escape(c.get("guia") or "Campo do canvas ainda sem resposta no .md.")}</p></div>' for c in abertos)
    if not itens_abertos:
        itens_abertos = '<div class="claim"><div class="claim-top"><h3>Nenhum campo em branco</h3><span class="seal v">completo</span></div><p>Todos os campos obrigatórios do canvas têm valor no .md. O que ainda depende de decisão humana está marcado como opinião ou estimativa.</p></div>'
    em_aberto = (f'<section><div class="s-head"><p class="eyebrow">Em aberto</p></div><h2>O que ainda não está respondido</h2>'
                 f'<p class="s-sub">Nenhum artefato da casa finge completude. Cada item abaixo tem um dono a nomear.</p>'
                 f'<div class="stack stack-tight" style="margin-top:22px">{itens_abertos}</div></section>')

    origem = spec.get("origem", {})
    rodape = (f'<footer><b>fonte</b> {H.escape(str(meta.get("md") or "—"))} · canvas oficial {H.escape(str(origem.get("arquivo", "—")))} '
              f'· spec <code>{H.escape(spec["id"])}</code> · <b>corte</b> {H.escape(str(meta.get("data") or "sem data"))} · <b>gerado</b> {hoje}<br>'
              f'Forma documento gerada pelo construtor (construir.py --documento) a partir do .md, que é a fonte da verdade. Selo "sem fonte" = valor sem marca (fato/estimativa) no .md.</footer>')

    mes = date.today().strftime("%b/%Y").lower()
    header = (f'<header><p class="eyebrow">Gestão Ágil 2.0 · {H.escape(spec.get("titulo", spec["id"]))} · forma documento · {mes}</p>'
              f'<h1>{H.escape(pergunta)}</h1><p class="lede">{lede}</p><dl class="facts">{facts_html}</dl></header>')

    return cabeca + "\n\n" + header + "\n\n" + "\n".join(secoes) + "\n" + pessoas_html + "\n" + em_aberto + "\n\n" + rodape + "\n\n" + cauda
