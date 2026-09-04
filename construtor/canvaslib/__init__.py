"""canvaslib — construtor de canvas do Gestão Ágil 2.0 (pacote do aluno).

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
