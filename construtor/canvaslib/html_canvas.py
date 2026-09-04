"""Monta o HTML da forma canvas: o SVG vetorizado do PDF oficial + os campos sobrepostos."""
import html as H
import re
from datetime import date
from pathlib import Path

from . import RAIZ, TEMPLATE_ARTEFATO
from . import svg as svgmod


def tokens_da_casa() -> str:
    """Copia os tokens de cor do template da casa (tema claro e escuro) para o corpo da página."""
    try:
        t = TEMPLATE_ARTEFATO.read_text(encoding="utf-8")
        return t[t.index(":root{"):t.index("*{box-sizing")]
    except Exception:
        return ":root{--paper:#FAFAF8;--panel:#FFFFFF;--ink:#1F2937;--ink-2:#4B5563;--ink-3:#6B7280;--rule:#E4E7EB;--rule-2:#D2D7DE;--brand:#3D9B9D}"


def carregar_svg(spec: dict) -> str:
    p = RAIZ / spec["estatico"]["svg"]
    return p.read_text(encoding="utf-8")


def _google_fonts(spec: dict, modo_fontes: str) -> str:
    gf = (spec.get("preenchimento") or {}).get("google_fonts")
    if modo_fontes != "link" or not gf:
        return ""
    familias = "&family=".join(f.strip() for f in gf.split("|") if f.strip())
    return f"@import url('https://fonts.googleapis.com/css2?family={familias}&display=swap');\n"


CORES_POSTIT = ("amarelo", "verde", "azul", "rosa", "laranja")


def _postits(v: str, campo: dict) -> str:
    """Cada linha do valor vira um post-it; prefixo [cor] escolhe a cor (amarelo, verde, azul, rosa, laranja)."""
    itens = [i.strip(" -•·\t") for i in re.split(r"\n+", v) if i.strip(" -•·\t")]
    largura = campo.get("postit_largura_pt", 110)
    cor_padrao = campo.get("postit_cor", "amarelo")
    saida = []
    for i in itens:
        m = re.match(r"^\[(amarelo|verde|azul|rosa|laranja)\]\s*", i)
        cor = m.group(1) if m else cor_padrao
        if m:
            i = i[m.end():]
        saida.append(f'<div class="postit {cor}" style="width:{largura}pt">{H.escape(i)}</div>')
    return "".join(saida)


def montar(spec: dict, svg_txt: str, valores: dict | None = None, modo: str = "normal",
           fontes: str = "link", debug: bool = False, meta: dict | None = None) -> str:
    W = spec["pagina"]["largura_pt"]; Hp = spec["pagina"]["altura_pt"]
    pref = "c" + re.sub(r"[^a-z0-9]", "", spec["id"].lower())[:14]
    svg_in = svgmod.preparar(svg_txt, pref, W, Hp)
    pre = spec.get("preenchimento") or {}
    familia = pre.get("fonte", "Roboto")
    cor = pre.get("cor", "#1A1A1A")
    tam = pre.get("tamanho_pt", 10)
    minimo = pre.get("minimo_pt", 6.5)
    valores = valores or {}
    meta = meta or {}

    campos = []
    dbg = []
    for c in spec.get("campos", []):
        x0, y0, x1, y1 = c["area_util"]
        v = valores.get(c["id"], "") or ""
        ftam = c.get("tamanho_pt", tam)
        alin = c.get("alinhamento", "left")
        peso = c.get("peso", 400)
        estilo = (f"left:{x0}pt;top:{y0}pt;width:{x1 - x0:.2f}pt;height:{y1 - y0:.2f}pt;"
                  f"font-size:{ftam}pt;text-align:{alin};font-weight:{peso}" + (f";color:{c['cor']}" if c.get("cor") else ""))
        if c.get("apresentacao") == "postit":
            campos.append(f'<div class="campo postits" data-campo="{H.escape(c["id"])}" data-min="{c.get("minimo_pt", minimo)}" '
                          f'data-postit-w="{c.get("postit_largura_pt", 110)}" style="{estilo}">{_postits(v, c)}</div>')
        else:
            campos.append(f'<div class="campo" data-campo="{H.escape(c["id"])}" data-min="{c.get("minimo_pt", minimo)}" '
                          f'style="{estilo}">{H.escape(v)}</div>')
        if debug:
            bx0, by0, bx1, by1 = c.get("caixa", c["area_util"])
            dbg.append(f'<div class="dbg-caixa" style="left:{bx0}pt;top:{by0}pt;width:{bx1 - bx0:.2f}pt;height:{by1 - by0:.2f}pt"></div>')
            dbg.append(f'<div class="dbg-area" style="left:{x0}pt;top:{y0}pt;width:{x1 - x0:.2f}pt;height:{y1 - y0:.2f}pt"></div>')
            dbg.append(f'<div class="dbg-id" style="left:{x0}pt;top:{y0 - 9}pt">{H.escape(c["id"])}</div>')

    titulo = spec.get("titulo", spec["id"])
    origem = spec.get("origem", {})
    familia_canvas = origem.get("familia", "")
    numero = spec.get("numero_oficial") or ""
    hoje = date.today().strftime("%d/%m/%Y")

    css_fontes = _google_fonts(spec, fontes)
    css = f"""{css_fontes}{tokens_da_casa()}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:Manrope,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.barra{{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:baseline;padding:12px 22px;border-bottom:1px solid var(--rule);background:var(--panel);font-size:13.5px}}
.barra .eyebrow{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3)}}
.barra b{{font-weight:700}}
.barra .acoes{{margin-left:auto;display:flex;gap:8px}}
.barra button{{font:inherit;font-size:12.5px;padding:4px 11px;border:1px solid var(--rule-2);border-radius:6px;background:var(--panel);color:var(--ink);cursor:pointer}}
.barra button:focus-visible{{outline:2px solid var(--brand);outline-offset:2px}}
.scroll{{overflow:auto;padding:24px}}
.moldura{{position:relative}}
.page{{position:relative;width:{W}pt;height:{Hp}pt;background:#FFFFFF;box-shadow:0 2px 14px rgba(0,0,0,.14);transform-origin:top left;overflow:hidden}}
.page>svg{{position:absolute;left:0;top:0;width:{W}pt;height:{Hp}pt;display:block}}
.campo{{position:absolute;margin:0;overflow:hidden;white-space:pre-wrap;overflow-wrap:break-word;line-height:1.28;font-family:'{familia}',Arimo,'Liberation Sans',Arial,sans-serif;color:{cor}}}
.campo.postits{{display:flex;flex-wrap:wrap;gap:6pt;align-content:flex-start;padding:2pt;white-space:normal}}
.postit{{position:relative;padding:6pt 7pt;min-height:46pt;font-size:.92em;line-height:1.25;color:#1F2937;background:#FFF3A0;box-shadow:1px 2px 4px rgba(0,0,0,.18);white-space:pre-wrap;overflow-wrap:break-word;transform:rotate(-.6deg)}}
.postit:nth-child(2n){{transform:rotate(.7deg)}}
.postit:nth-child(3n){{transform:rotate(-.3deg)}}
.postit.verde{{background:#CFF4D6}}.postit.azul{{background:#CFE8FF}}.postit.rosa{{background:#FFD6E7}}.postit.laranja{{background:#FFE0B3}}
.meta{{padding:8px 24px 32px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:var(--ink-3);line-height:1.7;max-width:1200px}}
.meta b{{color:var(--ink-2);font-weight:500}}
.dbg-caixa{{position:absolute;border:1px solid rgba(37,99,235,.75);pointer-events:none}}
.dbg-area{{position:absolute;border:1px dashed rgba(220,38,38,.95);background:rgba(220,38,38,.06);pointer-events:none}}
.dbg-id{{position:absolute;font:8pt ui-monospace,monospace;color:#B91C1C;background:rgba(255,255,255,.9);padding:0 3px;pointer-events:none;white-space:nowrap}}
@page{{size:{W}pt {Hp}pt;margin:0}}
@media print{{.barra,.meta{{display:none!important}}.scroll{{overflow:visible;padding:0}}.moldura{{width:auto!important;height:auto!important}}.page{{transform:none!important;box-shadow:none}}body{{background:#FFFFFF}}}}
"""
    if modo == "conferencia":
        css += f"\nbody{{background:#FFFFFF}}.scroll{{padding:0;overflow:visible}}.page{{box-shadow:none;transform:none!important}}\n"

    script_encolher = """
(function(){
  document.querySelectorAll('.campo').forEach(function(el){
    if(!el.textContent.trim()) return;
    var min=parseFloat(el.dataset.min||'6.5');
    var fs=parseFloat(getComputedStyle(el).fontSize)*0.75; var guard=0;
    var pw=parseFloat(el.dataset.postitW||'110'); var notas=el.querySelectorAll('.postit');
    while(el.scrollHeight>el.clientHeight+1 && guard<120){
      if(fs>min){ fs-=0.5; el.style.fontSize=fs+'pt'; }
      else if(notas.length && pw>56){ pw=Math.max(56,pw*0.9); notas.forEach(function(p){p.style.width=pw+'pt';p.style.minHeight='0';}); }
      else break;
      guard++; }
    if(el.scrollHeight>el.clientHeight+1){ el.setAttribute('data-estourou','1'); }
  });
})();"""
    script_ajustar = """
(function(){
  var page=document.getElementById('page'),moldura=document.getElementById('moldura'),scroll=document.getElementById('scroll'),btn=document.getElementById('btn-ajustar');
  if(!btn) return;
  var W=page.offsetWidth,Hh=page.offsetHeight,ajustar=true;
  function aplicar(){var disp=scroll.clientWidth-48;var s=ajustar?Math.min(2.5,disp/W):1;page.style.transform='scale('+s+')';moldura.style.width=(W*s)+'px';moldura.style.height=(Hh*s)+'px';btn.textContent=ajustar?'ver em 1:1':'ajustar à tela';}
  btn.addEventListener('click',function(){ajustar=!ajustar;aplicar();});
  document.getElementById('btn-imprimir').addEventListener('click',function(){window.print();});
  window.addEventListener('resize',aplicar);aplicar();
})();"""

    barra = meta_html = ""
    if modo != "conferencia":
        fonte_md = meta.get("md") or "—"
        legenda = " · ".join(f"<b>{H.escape(k)}</b> {H.escape(str(v))}" for k, v in meta.items() if k not in ("md",) and v)
        barra = (f'<div class="barra"><span class="eyebrow">Gestão Ágil 2.0 · forma canvas · {H.escape(familia_canvas)}'
                 f'{(" " + H.escape(numero)) if numero else ""}</span><b>{H.escape(titulo)}</b>'
                 f'<span class="acoes"><button id="btn-ajustar" type="button">ajustar à tela</button>'
                 f'<button id="btn-imprimir" type="button">imprimir / PDF</button></span></div>')
        meta_html = (f'<p class="meta"><b>origem do canvas</b> {H.escape(str(origem.get("arquivo", "—")))} · '
                     f'<b>fonte do conteúdo</b> {H.escape(str(fonte_md))} · <b>gerado</b> {hoje}'
                     f'{("<br>" + legenda) if legenda else ""}<br>'
                     f'Réplica literal do canvas oficial; o texto preenchido vem do arquivo .md. '
                     f'Modelo gerado por ferramentas/canvas/construir.py — não editar à mão.</p>')

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{H.escape(titulo)}</title>
<style>
{css}</style>
</head>
<body>
{barra}
<div class="scroll" id="scroll"><div class="moldura" id="moldura"><div class="page" id="page" data-spec="{H.escape(spec['id'])}" data-largura-pt="{W}" data-altura-pt="{Hp}">
{svg_in}
{''.join(campos)}
{''.join(dbg)}
</div></div></div>
{meta_html}
<script>{script_encolher}
{script_ajustar}
</script>
</body>
</html>
"""


def campos_md(specs: list, skill: str) -> str:
    """Tabela CAMPOS.md: id · rótulo · texto-guia · onde está no template.md."""
    linhas = [f"# Campos dos modelos canvas — `{skill}`", "",
              "Gerado pelo construtor (`construir.py --campos-md`). Não editar à mão.", ""]
    for sp in specs:
        linhas += [f"## `{sp['id']}` — {sp.get('titulo', '')}", "",
                   "| id | rótulo no canvas | texto-guia | âncora no template |", "|---|---|---|---|"]
        regras = (sp.get("md") or {}).get("ancoras", {})
        for c in sp.get("campos", []):
            r = regras.get(c["id"], {})
            anc = r.get("ancora", c["id"])
            extra = f" (coluna: {r['coluna']})" if "coluna" in r else (f" (formato: `{r['formato']}`)" if "formato" in r else "")
            linhas.append(f"| `{c['id']}` | {c.get('rotulo', '')} | {(c.get('guia') or '')[:120]} | `<!-- c:{anc} -->`{extra} |")
        linhas.append("")
    return "\n".join(linhas)
