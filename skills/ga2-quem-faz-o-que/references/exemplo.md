# Quem faz o quê — Norte-Sul

Exemplo fictício, novo e independente. Pessoas, datas, números e registros abaixo são ilustrativos; não representam evidência real.

## Cabeçalho

| Campo | Valor |
|---|---|
| Frente / demanda <!-- c:frente --> | Conferência de pedidos da Distribuidora Norte-Sul |
| Entrega <!-- c:entrega --> | Checklist de conferência usado em cinco pedidos simulados, com divergências registradas |
| Empresa <!-- c:empresa --> | Norte-Sul — Expedição |
| Cartão no portfólio <!-- c:cartao --> | NS-01 |
| Data desta matriz <!-- c:data --> | 14/09/2026 |

## Matriz de papéis

<!-- c:matriz -->
| Papel | Nome | O que faz nesta frente | O que não faz |
|---|---|---|---|
| Dono / DRI | Mariana | responde pelo resultado; prioriza a frente; apresenta a prova consolidada | não promete a capacidade de Lucas; não amplia a própria alçada |
| Aceitante | Mariana | recebe o resultado; confere os cinco registros na review; marca Aceita | não executa o checklist nem aceita por impressão |
| Executor | Lucas | prepara e aplica o checklist; decide como executar | não muda a prioridade da frente |
| Apoio | Não necessário nesta frente | nenhum apoio previsto | não há co-dono |
| Decisor de gate | Mariana, se houver mudança de regra de expedição | decide a proposta dentro da alçada simulada de responsável pela expedição | autorização não substitui aceite |
| Dono do processo | Lucas | facilita o quadro e os rituais; registra impedimentos | não define o rumo nem aceita a entrega |
| Prioridade entre áreas | Não definido | caso restrito à expedição | não se presume autoridade fora da área |

## Papéis do ritmo

| Papel | Nome |
|---|---|
| Dono do ciclo <!-- c:dono_ciclo --> | Mariana |
| Quem faz <!-- c:quem_faz --> | Lucas |
| Quem recebe o resultado <!-- c:quem_recebe --> | Mariana, na review de 18/09/2026 às 16h |

## Acumulações declaradas

| Pessoa | Acumula | Permitido? |
|---|---|---|
| Mariana | dona do resultado + Aceitante + decisora de gate dentro da área | sim, conforme alçada simulada; não executa a entrega |
| Lucas | executor + facilitador do processo | sim; não acumula SM e PO |

## Gates desta frente

| Ação sensível | Decisor | Proposta escrita | Pedido em | Decidido em |
|---|---|---|---|---|
| Alterar a regra de conferência em produção | Mariana | estado: conferência livre; mudança: checklist; risco: atraso; reversão: regra anterior | 14/09/2026 | em aberto; decisão prevista para 21/09/2026 |

O ciclo usa somente pedidos simulados. A alteração em produção não está autorizada nem faz parte da entrega deste ciclo.

## Demandas filhas

| Filha | Dono | DoD | Aceitante | Por que é filha |
|---|---|---|---|---|
| Nenhuma | — | — | — | não existe apoio com entrega, acesso ou aceite próprio |

## Transferência de dono

| De | Para | Aceitou por escrito em | Contexto entregue |
|---|---|---|---|
| Não houve | — | — | Mariana continua responsável |

## Teste de fronteira

- [x] Um nome em Dono: Mariana.
- [x] Não há disputa de responsabilidade nem SM e PO na mesma pessoa.
- [x] Mariana consegue conferir os cinco registros sem depender da explicação de Lucas.
- [x] Gate tem pessoa, proposta e data; a produção permanece fora do ciclo.

## Linha para o cartão

```text
Dono: Mariana · Aceitante: Mariana · Gate: Mariana (mudança em produção, pedido 14/09, decisão prevista 21/09) · Executa: Lucas · Apoio: nenhum
```
