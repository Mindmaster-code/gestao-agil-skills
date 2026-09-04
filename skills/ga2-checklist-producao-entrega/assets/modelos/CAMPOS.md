# Campos dos modelos canvas — `ga2-checklist-producao-entrega`

Gerado pelo construtor (`construir.py --campos-md`). Não editar à mão.

## `dor-dod-lab` — Portões DoR / DoD (laboratório)

| id | rótulo no canvas | texto-guia | âncora no template |
|---|---|---|---|
| `cartao` | Cartão / frente |  | `<!-- c:cartao -->` |
| `dono` | Dono (um nome) |  | `<!-- c:dono -->` |
| `data` | Data |  | `<!-- c:data -->` |
| `dor` | PORTÃO 1 — DEFINITION OF READY | o cartão pode entrar em execução? um item por linha: [x] ou [ ] + o que falta | `<!-- c:dor -->` |
| `dod` | PORTÃO 2 — DEFINITION OF DONE | o cartão pode ser entregue e aceito? um item por linha, com a prova | `<!-- c:dod -->` |
| `veredito_entrada` | Veredito do portão 1 | pode entrar? o que falta, quem resolve, até quando | `<!-- c:veredito_entrada -->` |
| `veredito_saida` | Veredito do portão 2 | pode entregar? prova pelo caminho real, aceitante | `<!-- c:veredito_saida -->` |
