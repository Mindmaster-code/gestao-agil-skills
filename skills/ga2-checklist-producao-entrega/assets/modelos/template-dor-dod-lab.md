<!-- spec: dor-dod-lab · gerado pelo construtor (construir.py --template); preencha as células e os blocos sem apagar as marcas de campo (os comentários c:...) -->

# Portões DoR / DoD (laboratório)

Preencha este arquivo e gere o canvas ou o documento com o construtor. Regras: um dono por artefato (nome de pessoa); todo número com fonte e data; o que não souber fica em branco, nunca inventado.

## Cabeçalho

| Campo | Resposta |
|---|---|
| **Cartão / frente** <!-- c:cartao --> | |
| **Dono (um nome)** <!-- c:dono --> | |
| **Data** <!-- c:data --> | |

## Portão de entrada

| Campo | Resposta |
|---|---|
| **Veredito do portão 1** — pode entrar? o que falta, quem resolve, até quando <!-- c:veredito_entrada --> | |

**PORTÃO 1 — DEFINITION OF READY** — o cartão pode entrar em execução? um item por linha: [x] ou [ ] + o que falta (uma linha por item):
<!-- c:dor -->
| OK | Item |
|---|---|
|  |  |

## Portão de saída

| Campo | Resposta |
|---|---|
| **Veredito do portão 2** — pode entregar? prova pelo caminho real, aceitante <!-- c:veredito_saida --> | |

**PORTÃO 2 — DEFINITION OF DONE** — o cartão pode ser entregue e aceito? um item por linha, com a prova (uma linha por item):
<!-- c:dod -->
| OK | Item | Prova |
|---|---|---|
|  |  |  |
