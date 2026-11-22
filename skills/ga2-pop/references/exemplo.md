# POP — exemplo fictício: conferência por código antes da doca

Exemplo fictício da Distribuidora Norte-Sul. Pessoas, datas, números e registros são sintéticos, criados para ensino; não são fontes reais verificadas. Rascunho do procedimento candidato; não aprovado nem executado.

## Cabeçalho

| Campo | Resposta |
|---|---|
| Nome do processo <!-- c:nome --> | Conferência de código e quantidade antes da doca |
| Identificação <!-- c:identificacao --> | 08/09/2026 · POP-CON-002 · v0.1 |
| Área / empresa | Operação · Distribuidora Norte-Sul |
| Briefing de origem | Processo de conferência; a confirmar após o piloto de setembro. |

## 1. Objetivo <!-- c:objetivo -->

Cada pedido segue para a doca com código e quantidade conferidos, reduzindo entregas incorretas ao cliente.

## 2. Escopo <!-- c:escopo -->

Cobre a conferência dos pedidos da rota regional entre separação e doca. Não cobre transporte, preço nem troca do sistema.

## 3. Responsabilidades

<!-- c:responsabilidades -->
| Papel / pessoa | Responsabilidade |
|---|---|
| Mariana — executa | Conferir e registrar divergências |
| Lucas — dono | Tratar desvios e manter o padrão |
| Lucas — aprova exceção | Decidir destino do pedido bloqueado |
| Lucas — recebe saída | Receber o lote liberado para a doca |

## 4. Entrada / gatilho <!-- c:gatilho -->

Pedido separado chega à bancada com lista autorizada e identificação do lote.

## 5. Passos

<!-- c:passos -->
| # | Passo | Responsável | Com o quê | Saída | Critério de qualidade |
|---|---|---|---|---|---|
| 1 | Identificar | Mariana | Lista e etiqueta do lote | Pedido associado ao lote | Mesmo identificador nos dois registros |
| 2 | Comparar | Mariana | Código de cada item e lista | Códigos conferidos | Código exato, não aparência |
| 3 | Contar | Mariana | Itens e quantidade solicitada | Quantidades conferidas | Quantidade igual à lista |
| 4 | Registrar | Mariana | Registro de conferência | Aceite ou divergência | Data, pedido, diferença e nome |
| 5 | Encaminhar | Lucas | Resultado da conferência | Pedido à doca ou correção | Só pedido sem divergência vai à doca |

## 6. Saídas <!-- c:saidas -->

Registro de conferência por pedido; lote liberado ou bloqueio identificado, com responsável pela correção.

## 7. Indicadores

<!-- c:indicadores -->
| Indicador | Tipo | Base sintética | Meta proposta | Frequência | Onde ver | Quem mede |
|---|---|---|---|---|---|---|
| Pedidos com registro completo | Adesão | A medir antes do piloto | 100% | Por lote | Registro de conferência | Mariana |
| Pedidos com erro ÷ conferidos | Resultado | 15% (12/80; S1) | Até 5% em 30/09 | Semanal | Amostra de pedidos | Lucas |

## 8. Sistemas ou ferramentas <!-- c:sistemas -->

| Ferramenta | Para quê | Como acessar |
|---|---|---|
| Lista autorizada de pedidos | Referência de código e quantidade | Solicitar a Lucas a versão liberada do lote |
| Registro de conferência | Guardar resultado e divergências | Pasta escolhida pela equipe; pedir acesso individual a Lucas |
| Etiqueta de identificação | Associar pedido e lote | Junto ao lote na bancada; ilegível significa bloqueio |

Nenhuma senha entra no POP.

## 9. Exceções <!-- c:excecoes -->

| Exceção | Tratamento | Quem aprova |
|---|---|---|
| Código ilegível ou lista ausente | Bloquear pedido; obter referência correta | Lucas |
| Divergência de quantidade | Voltar à separação e conferir novamente | Lucas |

## 10. Riscos <!-- c:riscos -->

| Risco | Mitigação |
|---|---|
| Marcar conferido sem comparar | Teste com pessoa nova e revisão de amostra |
| Confundir listas de lotes | Passo 1 obrigatório antes de comparar |

## 11. Monitoramento

| O que olhar | Quando | Quem |
|---|---|---|
| Bloqueios e registros incompletos | Ao fim de cada lote | Lucas |
| Erros e adesão | Toda revisão semanal | Mariana |

## 12. Aprovação <!-- c:aprovacao -->

Pendente: Lucas, responsável pela operação, decidirá após o piloto e o teste em 15/09/2026. A data é proposta, não aprovação.

## 13. Revisão

| Versão | Data | O que mudou | Quem | Próxima revisão |
|---|---|---|---|---|
| v0.1 | 08/09/2026 | Rascunho didático | Mariana | 15/09/2026 |

## Teste de bem feito

- [ ] Lucas, sem executar a conferência habitual, tentará o POP com um lote de teste em 15/09.
- [ ] Mariana registrará bloqueios e corrigirá o documento antes de pedir aprovação.
- [ ] Resultado ainda não existe; não declarar que alguém executou.

## 14. Cobertura e substituto (exemplo de outro ramo)

Rosângela coordena o departamento pessoal de um escritório de contabilidade. A analista Telma fecha a folha de pagamento e vai tirar férias de 14/12/2026 a 02/01/2027. Rosângela fez a pergunta das férias. Resposta: Só em parte. O POP existe, mas ninguém além de Telma fechou a folha de verdade.

| Atividade crítica | Titular | Substituto | Última vez que o substituto fez (data) | Observado por | Teste marcado (data) | Preparo e limite de decisão na cobertura |
|---|---|---|---|---|---|---|
| Fechamento da folha do mês | Telma | Júlio | nunca | | 27/11/2026 | Júlio fecha a folha de novembro com Telma ao lado. Na cobertura, decide sozinho os ajustes de rotina e leva a Rosângela qualquer pagamento fora da folha. |
| Envio das guias de recolhimento | Telma | Priscila | 10/10/2026 | Telma | 10/12/2026 | Priscila envia sozinha. Dúvida de valor sobe a Rosângela. |

| Campo | Resposta |
|---|---|
| Execução que vai demonstrar o preparo | Júlio fecha a folha de novembro em 27/11/2026, e o POP é corrigido onde ele parar |
| Contatos de escalada | Rosângela e o sócio responsável pelo departamento |
| Lição para compartilhar | O setor fiscal também depende de uma pessoa só para as guias; Rosângela leva a lição à reunião do setor |
