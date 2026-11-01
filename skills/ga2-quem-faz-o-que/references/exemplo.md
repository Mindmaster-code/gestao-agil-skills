# Quem faz o quê — Norte-Sul

Exemplo fictício, novo e independente. Pessoas, datas, números e registros abaixo são ilustrativos; não representam evidência real.

## Cabeçalho

| Campo | Valor |
|---|---|
| Frente / demanda <!-- c:frente --> | Conferência de pedidos da Distribuidora Norte-Sul |
| Entrega <!-- c:entrega --> | Checklist de conferência usado em cinco pedidos simulados, com divergências registradas |
| Área <!-- c:empresa --> | Norte-Sul — Expedição |
| Cartão no quadro <!-- c:cartao --> | NS-01 |
| Data desta matriz <!-- c:data --> | 14/09/2026 |

## Matriz de papéis

<!-- c:matriz -->
| Papel | Nome | O que faz nesta frente | O que não faz |
|---|---|---|---|
| Dono | Mariana | responde pelo resultado; prioriza a frente; apresenta a prova consolidada | não promete a capacidade de Lucas; não amplia a própria alçada |
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

## Revisão de responsabilidades (exemplo de outro ramo)

Beatriz gerencia uma loja de papelaria. Vanessa foi contratada como vendedora, mas há oito meses cuida também do estoque e do pedido semanal ao fornecedor. Na revisão semestral, em 28/11/2026, Beatriz abriu o registro reservado.

| Responsabilidade ou entrega | Papel previsto | Papel assumido | Desde quando | Evidência de contribuição |
|---|---|---|---|---|
| Atendimento no balcão | Vanessa | Vanessa | contratação | Sem queixa de cliente no semestre |
| Estoque | Beatriz | Vanessa | março de 2026 | Contagem mensal feita por ela, com as diferenças anotadas |
| Pedido semanal ao fornecedor | Beatriz | Vanessa | abril de 2026 | Pedidos feitos no prazo, com ruptura de estoque menor |

Beatriz comparou com o caso de outra loja da rede, em que o estoque é uma responsabilidade própria com enquadramento próprio, e levou a proposta a quem decide na rede em 30/11/2026, com a evidência, o impacto e a justificativa. Não prometeu reajuste a Vanessa. Depois da decisão, comunicou o resultado a ela individualmente, com os critérios que podiam ser explicados.

## Transição de responsabilidades (exemplo de outro ramo)

Eduardo, analista de compras de uma distribuidora de hortifruti, muda de função em 30/11/2026. Fernanda, líder da área, planejou a transição em 40 minutos e alinhou antes a condução com a área de pessoas.

| Entrega | POP escrito | Novo dono | Aceitou por escrito em | Trabalho feito uma vez com quem sai ao lado |
|---|---|---|---|---|
| Pedido semanal aos fornecedores | POP-COMP-01, v1.0 | Daniela | 16/11/2026 | 18/11/2026 |
| Conferência das notas de entrada | POP-COMP-02, v1.0 | Daniela | 16/11/2026 | 23/11/2026 |
| Cadastro de fornecedor novo | POP-COMP-03, v1.0 | Marcelo | 17/11/2026 | 25/11/2026 |

Nas duas primeiras execuções, Daniela perguntou onde ficava a lista de preços combinada. A resposta entrou no POP-COMP-01, e Eduardo confirmou o texto. Até o aceite escrito de cada um, Eduardo continuou respondendo pela entrega. Os acessos foram tratados pela área responsável, no dia combinado com ela.
