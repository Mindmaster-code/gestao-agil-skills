# Diagnóstico — exemplo fictício: erros na separação de pedidos

Exemplo fictício da Distribuidora Norte-Sul. Pessoas, datas, números e registros são sintéticos, criados para ensino; não são fontes reais verificadas.

**Caso:** pedidos com erro de separação · **Dona:** Mariana · **Empresa:** Distribuidora Norte-Sul · **Data:** 08/09/2026 · **Ciclo:** 08–14/09/2026 · **Régua:** intermediária.

## 0. Caso refinado

| Campo | Resposta |
|---|---|
| Caso escolhido | Pedidos da rota regional saem com item ou quantidade diferente do solicitado. |
| Entra neste ciclo | Separação e conferência dos pedidos da rota regional. |
| Fica de fora | Transporte, preços e troca do sistema de estoque. |
| Resultado desejado | Menos pedidos com erro, medidos com a mesma definição e amostra. |

## 1. Contexto <!-- c:contexto -->

Erros obrigam o cliente a pedir correção e atrasam a disponibilidade da mercadoria. Investigar agora permite comparar o ciclo de setembro com uma linha de base explícita.

## 2. Situação atual <!-- c:situacao_atual -->

| Fato do cenário | Número sintético | Fonte simulada | Data | Quem conferiria |
|---|---|---|---|---|
| Pedidos com item ou quantidade incorreta | 12 de 80 = 15% | S1: amostra fictícia dos pedidos de 01–07/09 | 08/09/2026 | Mariana |

Não há número financeiro neste diagnóstico.

### 2a. Mapa as-is — adaptação metodológica

Tempos abaixo são estimativas didáticas por pedido, não medições reais.

| # | Etapa | Quem faz | Entrada | Saída | Tempo / espera | Trava ou volta? |
|---|---|---|---|---|---|---|
| 1 | Receber pedido | Lucas | Pedido autorizado | Lista para separar | 5 min | Não observada |
| 2 | Separar | Lucas | Lista | Volumes separados | 15 min | Local a observar |
| 3 | Conferir | Mariana | Volumes e lista | Liberação ou correção | 8 min | Pode voltar à separação |
| 4 | Entregar à doca | Lucas | Volumes liberados | Registro de saída | 4 min | Não observada |

**Onde para:** o cenário sugere retorno da etapa 3 à 2; frequência e causa ainda precisam de observação.

### 2b. Linha de base — adaptação metodológica

| Métrica | Valor hoje | Data | Fonte | Frequência | Quem lê |
|---|---|---|---|---|---|
| Pedidos com erro ÷ pedidos conferidos | 15% (12/80) | 08/09/2026 | S1, sintética | Semanal | Mariana |

## 3. Situação desejada

Proposta: pedidos com erro de 15% para no máximo 5% até 30/09/2026, com a mesma definição de erro.

## 4. Gap <!-- c:gap -->

| Métrica | Hoje | Desejado | Gap: desejado − atual | Vale um A3? |
|---|---|---|---|---|
| Pedidos com erro | 15% | 5% | −10 pontos percentuais | Sim: muda a quantidade de pedidos que exigem correção do cliente. |

Contexto, situação atual e desejada usam a mesma medida: sim.

## 5. Histórico <!-- c:historico -->

| Quando | O que | Resultado |
|---|---|---|
| 04/09/2026 | Lembrete verbal, no cenário fictício | Efeito não medido; não há prova de melhora. |

## Antes de ir para a causa raiz

- [x] O cenário explicita número, origem sintética, data, meta e gap.
- [x] Nenhuma solução foi definida neste lado.
- [ ] Mariana valida o caso com dados reais e registra aceite até 10/09/2026.

Próximo: ga2-causa-raiz; o diagnóstico didático não autoriza mudar o processo.

