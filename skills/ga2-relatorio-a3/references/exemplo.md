# Relatório A3 — exemplo fictício: pedidos separados sem erro

Exemplo fictício da Distribuidora Norte-Sul. Pessoas, datas, números e registros são sintéticos, criados para ensino; não são fontes reais verificadas. Rascunho didático: a causa não foi validada e o plano de mudança não está liberado.

| Campo | Resposta |
|---|---|
| Caso / desafio <!-- c:caso --> | Pedidos com erro de separação |
| Responsável <!-- c:dono --> | Mariana |
| Data <!-- c:data --> | 08/09/2026 |
| Ciclo <!-- c:ciclo --> | 08–14/09/2026 |
| Empresa <!-- c:empresa --> | Distribuidora Norte-Sul |
| Régua | Intermediária |

## Lado esquerdo — Plan

### 1. Contexto <!-- c:contexto -->

Pedidos errados exigem correção e prejudicam o abastecimento do cliente. O ciclo de setembro precisa de uma linha de base e uma investigação antes de mudar o padrão.

### 2. Situação atual

<!-- c:situacao_atual -->
| Fato do cenário | Número | Fonte simulada | Data |
|---|---|---|---|
| Pedidos com item ou quantidade incorreta | 12/80 = 15% | S1, amostra sintética de 01–07/09 | 08/09/2026 |

### 3. Situação desejada <!-- c:situacao_desejada -->

Proposta: reduzir pedidos com erro de 15% para 5% até 30/09/2026.

### 4. Gap

<!-- c:gap -->
| Métrica | Hoje | Desejado | Gap | Vale um A3? |
|---|---|---|---|---|
| Pedidos com erro | 15% | 5% | −10 pontos percentuais | Sim: menos correções para o cliente. |

### 5. Causa raiz <!-- c:causa_raiz -->

Não comprovada. Hipótese prioritária do 5 Porquês: a regra de conferência pode deixar passar códigos divergentes. Mariana investiga até 11/09; sem evidência, o lado direito permanece proposta.

## Lado direito — proposta condicionada à causa

### 6. Contramedidas — fim do Plan

<!-- c:contramedidas -->
| # | Contramedida candidata | Causa que precisa ser confirmada |
|---|---|---|
| C1 | Comparação por código antes de liberar o pedido | Hipótese de conferência incompleta |
| C2 | Revisão do padrão alimentada pelos erros encontrados | Hipótese de revisão sem dados de erro |

### 7. Plano de ação — Do

<!-- c:plano -->
| # | O quê | Por quê | Quem | Quando | Onde | Como | Quanto |
|---|---|---|---|---|---|---|---|
| 1 | Observar 10 conferências | Validar ou refutar a hipótese de C1 | Mariana | 09/09/2026 | Bancada de conferência | Observar; registrar; comparar | Estimativa: 2 h |
| 2 | Decidir o piloto de C1 | Evitar mudar sem causa confirmada | Lucas | 11/09/2026 | Reunião da operação | Ler evidências; registrar decisão | Estimativa: 30 min |
| 3 | Experimentar C1 em um lote, se aprovado | Testar a contramedida ligada à causa | Mariana | 14/09/2026 | Uma rota regional | Aplicar; contar erros; comparar | Estimativa: 3 h |

Nenhuma ação supera uma semana. C2 será detalhada após a primeira revisão; não há verba adicional autorizada.

### 8. Métricas — Check

<!-- c:metricas -->
| Métrica | Hoje | Alvo | Frequência | Onde mora | Quem lê |
|---|---|---|---|---|---|
| Pedidos com erro ÷ pedidos conferidos | 15%, sintético | 5% até 30/09 | Semanal | Registro de conferência escolhido pela equipe | Mariana |

### 9. Acompanhamento — Check

Revisão com Lucas em 14/09/2026.

<!-- c:acompanhamento -->
| Data | Número medido | O que travou | Ajuste |
|---|---|---|---|
| 08/09/2026 | Só linha de base sintética: 15% | Causa sem validação | Investigar; não liberar mudança |
| 14/09/2026 | A medir após investigação | A registrar na revisão | Decidir manter, ajustar ou descartar |

### 10. Aprendizado — Act <!-- c:aprendizado -->

A preencher em 14/09/2026: o que confirmou ou refutou a hipótese e se o próximo ciclo exige outro ramo de investigação. Não padronizar antes de verificar.

## Fechamento

Estrutura e unidades conferidas para o exercício. Causa, aceite e execução continuam pendentes.
**Decisor:** Lucas, operação; pedido de piloto previsto em 11/09/2026.
**Assinatura da dona:** Mariana, pendente de dados reais e leitura conjunta.

