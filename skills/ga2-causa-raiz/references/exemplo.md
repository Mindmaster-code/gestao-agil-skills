# Causa raiz — exemplo fictício: erros na separação

Exemplo fictício da Distribuidora Norte-Sul. Pessoas, datas, números e registros são sintéticos, criados para ensino; não são fontes reais verificadas. As relações causais abaixo são hipóteses, não causas provadas.

| Campo | Resposta |
|---|---|
| Caso / desafio <!-- c:caso --> | Pedidos com erro de separação |
| Responsável <!-- c:dono --> | Mariana |
| Data <!-- c:data --> | 08/09/2026 |
| Ferramenta <!-- c:ferramenta --> | Ishikawa + 5 Porquês no ramo Método |

## A. 5 Porquês

**Problema observado** <!-- c:problema -->: na amostra sintética S1, 12 de 80 pedidos têm erro de item ou quantidade (15%).

<!-- c:porques -->
| Nível | Pergunta | Resposta provisória | Evidência necessária |
|---|---|---|---|
| Sintoma | O que acontece? | Pedidos divergem do solicitado. | S1 é dado didático; substituir por amostra real. |
| 1 · imediata | Por que o pedido diverge? | Hipótese: item parecido foi separado. | Lucas compara códigos de item e pedido em 09/09. |
| 2 · processo | Por que o item parecido passa? | Hipótese: conferência usa aparência, não código. | Mariana observa 10 conferências em 09/09. |
| 3 · rotina | Por que a conferência usa aparência? | Hipótese: a instrução não exige comparar códigos. | Mariana lê a instrução vigente em 10/09. |
| 4 · regra | Por que a instrução omite a comparação? | Hipótese: aprovação não exige teste dos erros conhecidos. | Lucas consulta o histórico de revisão em 10/09. |
| 5 · sistema | Por que não se exige esse teste? | Hipótese: revisão do padrão não recebe dados de erro. | Mariana compara responsáveis e registros em 11/09. |

## Testes antes de fechar

| Teste | Resposta |
|---|---|
| Pessoa | A cadeia descreve regras e processo, não culpa uma pessoa. |
| Retorno | Em aberto: corrigir só o item pode deixar o erro reaparecer. Testar o mecanismo antes de concluir. |
| Controle | Mariana pode investigar e propor o padrão. Mudança na aprovação depende de Lucas, responsável pela operação. |

**Evidências** <!-- c:evidencias -->: só há números sintéticos. Ausência de comparação por código ainda não foi observada; achar conferência correta enfraqueceria a hipótese.

**Causa prioritária** <!-- c:causa_prioritaria -->: investigar primeiro o ramo Método, porque a conferência está no recorte e pode ser observada. Não é conclusão causal.

**Depende de:** acesso autorizado aos registros e decisão de Lucas sobre mudança de padrão, após a investigação de 11/09.

## B. Ishikawa — adaptação metodológica

<!-- c:ishikawa -->
| Categoria | Causa levantada | Subcausa | Evidência | Frequência / impacto |
|---|---|---|---|---|
| Método | Hipótese: conferência incompleta | Código não comparado | Observação em 09/09 | A medir |
| Mão de obra | Nenhuma hipótese priorizada | Não culpar sem observar | Capacidade a observar | A medir |
| Máquina | Hipótese: leitura de código indisponível | Equipamento ou acesso | Teste em 10/09 | A medir |
| Material | Hipótese: etiquetas pouco legíveis | Impressão apagada | Amostra em 10/09 | A medir |
| Medição | Hipótese: erros não chegam à revisão | Registro sem rotina de leitura | Histórico em 11/09 | A medir |
| Meio ambiente | Nenhuma hipótese levantada | Examinar bancada | Observação em 09/09 | A medir |

**Ramo escolhido** <!-- c:ramos_escolhidos -->: Método; a cadeia acima é um roteiro de investigação, não um Ishikawa encerrado.

## C. Pareto

Não aplicado: ainda não há contagem real por causa. Não transformar a contagem de erros em contagem de causas.

## Para o campo 5 do A3

> Hipótese prioritária: a regra de conferência pode permitir divergências de código. Causa de sistema em aberto; Mariana reúne as evidências até 11/09/2026.

Próximo: completar a investigação antes de aprovar contramedidas em ga2-relatorio-a3.

