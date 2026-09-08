# 5W2H — plano de ação

## O que é e quando usar

5W2H é a estrutura de plano de ação: **o quê** (What), **por quê** (Why), **quem** (Who),
**quando** (When), **onde** (Where), **como** (How), **quanto custa** (How much). Uma linha
por ação; cada linha responde as sete perguntas.

Nesta adaptação, é o bloco "plano de ação" do **lado direito do A3**, o plano de um PDCA com mais de
um passo e qualquer lista de ação que precise de dono e data. Entra antes: causa raiz e
contramedidas (A3) ou a ação da retro (PDCA). Sai depois: execução (Do), acompanhamento
(Check) e cartões no Kanban.

Vive no **Passo 0** (conceito, M02 A07) e no **Passo 1** (lado direito do A3, M03 A08).

## Fonte no método

- Passo 0 — Fundamentos: 5W2H (M02 A07), incluindo quem, quando, onde e quanto custa.
- Passo 1 — Entender o Contexto: 5W2H no lado direito do A3 (M03 A08/A09; v6 aula 05).
- Passo 5 — Melhoria Contínua: exemplo da Ana.
- Não há template oficial de 5W2H nas fontes citadas; a aula menciona quatro dos sete campos. O [template desta skill](template.md) é uma adaptação metodológica, com essa origem explicitada.
## Ligação com o A3 e com as contramedidas

| Pergunta | De onde vem no A3 | Onde a aula pede |
|---|---|---|
| Por quê | causa raiz (lado esquerdo) | contramedidas atacam a causa (M03 A08) |
| O quê | contramedida escolhida | plano de ação: "o quê · quem · quando" (v6 aula 05) |
| Quem · Quando | plano de ação | "sem isto não é plano" |
| Como · Quanto | briefing do projeto | "como o projeto será feito", "quando e quanto custa" (M03 A09) |
| Onde | contexto (lado esquerdo) / briefing | "descreva o ambiente onde o problema ocorre" (A05) |

Regra desta adaptação: **o quê / quem / quando** são obrigatórios em toda linha; **por quê** vem da
causa raiz; **como / onde / quanto** completam quando o plano vai rodar sem briefing. As sete
colunas são extensão do método `(adaptação metodológica identificada)`.

## Como conduzir

1. **Ligar ao diagnóstico.** Pergunta: "Qual causa raiz este plano ataca?" Escreve no
   cabeçalho. Recusa: plano solto, sem A3, PDCA ou retro de origem.
2. **Uma linha por contramedida.** "O que será feito?" — verbo no infinitivo, resultado
   verificável. Recusa: linha com "e" juntando duas ações.
3. **Por quê.** "Como esta ação mexe na causa?" Recusa: "porque é importante".
4. **Quem.** "Um nome." Recusa: dois nomes, "time", "a área". Apoio não vira co-dono.
5. **Quando.** "Que data?" Recusa: "em breve", "próximo ciclo" sem dia, "ASAP".
6. **Onde.** Passo do fluxo, local, ferramenta ou documento.
7. **Como.** Dois ou três passos. Se não cabe na célula, a ação é grande demais — cortar.
8. **Quanto.** Horas de trabalho ou R$ (material, ferramenta ou serviço). "Quanto em branco volta — é o que
   liga ao ROI." Custo que exige verba depende da aprovação do decisor competente.
9. **Conferir os seis campos de acompanhamento** (adaptação metodológica): o quê, por quê, dono,
   "pronto é", prazo, onde trava. O 5W2H já responde cinco; falta "pronto é" — acrescente na
   coluna Status/prova.
10. Salvar; cada linha vira cartão no Kanban ou compromisso do plano do ciclo.

## Regras do método que valem aqui

- "Sem isto não é plano: o quê · quem · quando." (v6 aula 05)
- "Um dono por demanda. Apoio não vira co-dono." (adaptação metodológica: responsabilidade única)
- "Cobrança sem data não é cobrança." (adaptação metodológica: prazo explícito) — linha sem data não é plano.
- "Contramedidas atacam a causa raiz, não o sintoma." (M02 A07, regra 20 do Passo 5)
- "Um cartão, uma semana." Ação maior que isso é cortada antes de entrar.

## Saída

- Salve o plano na pasta escolhida pelo usuário, junto do A3 ou do ciclo de PDCA/retrospectiva de origem.
- Depois: cada linha vira cartão no Kanban ou compromisso do Plano do Ciclo. O PDCA aponta para o 5W2H no campo Plano; atualize o acompanhamento na revisão do ciclo.

## Formas de saída

Leia [Entrega editável](entrega-editavel.md). O pedido e o documento existente definem formato e destino.
Padrão desta skill, sem formato definido: planilha `.xlsx`; Google Sheets quando esse for o destino escolhido.
Gere e reabra a entrega real; em revisões, atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário. HTML sai quando escolhido; não é cópia obrigatória de Word, Docs ou planilhas.
Preserve os campos e a ordem de [template.md](template.md) e confira [checklist.md](checklist.md).

Modelos para HTML/canvas quando essa for a entrega escolhida:

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-5w2h-lab.html` **(padrão)** | 5W2H — plano de ação (laboratório) · família laboratorio | "no canvas do laboratório" | pronto |


Use uma cópia do modelo de documento em `../assets/modelos/documento.html`. Para o canvas solicitado, copie o modelo correspondente e preencha os campos, preservando IDs e âncoras `<!-- c:id -->`.
Consulte `../assets/modelos/CAMPOS.md` para os campos; listas em `div[data-campo]` com `class="postits"` recebem um `div.postit` por item. Não altere o modelo original.
Confira IDs, campos sem preencher, ausência de `{{` residual, conteúdo sem estouro e uma página quando o modelo exigir.

### Regras da forma HTML

Use as cores e a tipografia do modelo, sem CSS criado do zero nem paleta genérica. Teal `#3D9B9D` indica marca e medido; laranja `#F97316`, risco e estimado; cinza `#576270`, em aberto; tipografia Manrope.
Linguagem curta e autoexplicativa: frases de 20–25 palavras, uma ideia por frase, termos comuns e jargão traduzido na primeira aparição. O título diz a consequência. Corte palavras, nunca números ou fontes.
Todo número tem estado (medido, estimado com premissa, ou em aberto) e fonte reconferível. O que o sistema faria permanece em aberto, não medido. Não apresente número sem fonte.
Identifique dono do resultado, participantes, decisor e quem aceita a entrega. Se houver agentes de IA, separe-os das pessoas. Sem nome na fonte, escreva “não definido”.
No fluxo Markdown → HTML, gere da fonte atual; nos demais formatos, siga a conferência de Entrega editável.

## Adaptação

- **Leve**: três colunas (o quê · quem · quando) — o mínimo da v6.
- **Intermediária** (retrospectiva da equipe): cinco (+ por quê, quanto).
- **Robusta** (A3 com várias contramedidas, projeto): as sete colunas e acompanhamento datado.

## Erros comuns

- "Quem" com dois nomes.
- "Quando" sem data.
- "Quanto" em branco.
- Lista de tarefas sem ligação com a causa raiz.
- Ação grande demais para caber em "como" de três passos.
- Plano de ação antes de fechar o lado esquerdo do A3.
