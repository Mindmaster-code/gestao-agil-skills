"""Prepara o SVG do pdftocairo para viver dentro de um HTML: ids únicos e tamanho em pt."""
import re


def preparar(svg: str, prefixo: str, largura_pt: float, altura_pt: float) -> str:
    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
    ids = set(re.findall(r'\bid="([^"]+)"', svg))

    svg = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{prefixo}-{m.group(1)}"', svg)
    svg = re.sub(r'((?:xlink:)?href=")#([^"]+)"',
                 lambda m: f'{m.group(1)}#{prefixo}-{m.group(2)}"' if m.group(2) in ids else m.group(0), svg)
    svg = re.sub(r"url\(#([^)]+)\)",
                 lambda m: f"url(#{prefixo}-{m.group(1)})" if m.group(1) in ids else m.group(0), svg)

    def dims(m):
        return f'<svg{m.group(1)} width="{largura_pt}pt" height="{altura_pt}pt"'
    svg = re.sub(r'<svg([^>]*?)\swidth="[^"]*"\sheight="[^"]*"', dims, svg, count=1)
    return svg.strip()
