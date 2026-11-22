# OKR Canvas

## O que é e quando usar

OKR = Objetivo (aonde queremos chegar, sem número) + Resultados-chave (KR: o número que
prova que chegamos) + Iniciativas (o que vamos iniciar para mover cada número). É a pedra
grande do Passo 2: vem **depois do A3** (o diagnóstico do Passo 1) e **antes** da Matriz
Esforço × Impacto e do Backlog 2D. Cadeia: A3 → **OKR** → Matriz → Backlog 2D → Kanban.

Use no começo de cada período, um por nível
(empresa, área, pessoa). Entra: o A3 com problema e causa raiz. Sai: o canvas preenchido,
a lista de iniciativas para a matriz e o check-in semanal na agenda.

## Fonte no método

A procedência desta skill está em `fontes.md`, nesta mesma pasta.

- Exemplo do curso: Kit Implementação — OKR Canvas (Norte-Sul).

## Como conduzir

1. **Ponte A3 → OKR.** Pergunta: "qual problema do A3 este OKR precisa mover? qual causa vai
 ser atacada? qual mudança mensurável prova avanço? o que fica de fora neste ciclo?"
 Escreve os quatro campos da ponte (template, bloco 1). Recusa: OKR inventado do zero sem
 A3 — "volta e faz o diagnóstico".
2. **Período e nível.** Pergunta: "trimestre, semestre ou ano? empresa, área ou pessoa?
 Qual empresa?" Escreve no cabeçalho. Recusa: OKR de um grupo sem dizer
 de qual empresa é o número.
3. **Objetivo.** Pergunta: "aonde você quer chegar? lê em voz alta — dá vontade de ir
 atrás?" Escreve uma frase qualitativa, com prazo, sem verbo operacional. Recusa:
 objetivo com "implementar", "executar", "criar" — isso é tarefa. Objetivo com número é KR.
4. **Resultados-chave.** Para cada KR, três perguntas: "de quanto para quanto, até quando?";
 "isso mede resultado ou esforço?"; "se bater esse número, o objetivo está cumprido?"
 Escreve no formato **de/para com prazo**, com a fonte do número de partida e quem é o
 dono do número (responsável nomeado pela medida). Recusa: KR sem número de
 partida ("o problema é medição — pede ao responsável pela medição antes"); KR que é entrega ("publicar 20
 respostas" é iniciativa; "resolver 80% no primeiro contato" é KR).
5. **Quantidade.** A aula permite 2 a 5 KR por objetivo e 1 a 3 objetivos. Os templates
 editáveis e o Kit mandam começar com 1 objetivo e até 3 KR. Regra desta adaptação: **comece com
 até 3; aceite até 5 só se cada um tiver dono do número e fonte**. Recusa: 6 ou mais —
 "você vai gastar mais tempo medindo do que fazendo".
6. **Comprometido ou aspiracional.** Pergunta por KR: "tem que bater 100% ou 70% já é
 ótimo?" Marca no canvas. Um bom ciclo mistura os dois.
7. **Iniciativas.** Pergunta por KR: "para mover esse número, o que precisamos iniciar?" e
 "o que já roda hoje que não aponta para nenhum KR?" Escreve 2 ou 3 apostas por KR, cada
 uma com dono. Recusa: lista de 30 tarefas; iniciativa que não diz qual número move
 ("é ocupação").
8. **Divulga.** OKR é público. Pergunta: "quem precisa ler isso e onde vai ficar?"
9. **Checkpoint do Plano** (uma vez, ao fim do planejamento, depois da matriz e do backlog):
 as cinco perguntas do template, bloco 4. Sai "solta para executar" ou "volta e conserta".
10. **Check-in semanal** (toda semana, 5–15 min, do 1º dia ao fim do ciclo): número de hoje
 por KR, nota 0–1 pelo de/para, o que mexeu, o que impede, ação até a próxima com dono.
 Template, bloco 3. Recusa: check-in sem número ("OKR escrito, não feito").

## Regras do método que valem aqui

- **Pedra grande primeiro.** OKR antes de iniciativa, iniciativa antes de backlog.
- **Poucos OKR:** 1 a 3 objetivos; 2 a 5 KR por objetivo. No primeiro ciclo, 1 objetivo e até 3 KR (Kit, modelo editável).
- **Objetivo é direção sem número; KR é número sem atividade**.
- **KR em formato de/para com prazo**.
- **Prefira medir resultado, não esforço**. "Lançar 4 produtos" é KR; "criar reunião de inovação" é tarefa.
- **Toda iniciativa aponta para um KR.** Se não move número, é ocupação.
- **OKR se deriva por escolha, não por ordem:** a área responde "como contribuo?", não copia o KR da empresa.
- **OKR é público**.
- **Nota do KR é conta, não achismo:** caminho andado ÷ caminho total, de 0 a 1. Em KR aspiracional, 0,7 é excelente.
- **Iniciativa pronta e número parado = aposta errada: troca a iniciativa, não o KR**.
- **OKR sem check-in semanal é OKR escrito, não feito**.
- **O plano só passa se responder "o que faço segunda de manhã?"**.

## Saída

- Salve o OKR na pasta escolhida pelo usuário. Se já há documento oficial, atualize-o ou faça referência a ele; não mantenha cópias concorrentes dos números.
- Registre o check-in semanal no mesmo documento, uma linha por semana, ou no relatório já adotado pela equipe.
- Depois: iniciativas vão para `ga2-matriz-esforco-impacto`; a fila ordenada vira a linha de cima de `ga2-backlog-2d`; cada frente entra no Kanban com o KR que move.
- KR inviável: registre a evidência e recomende a revisão ao responsável pela meta. Só o decisor competente pode aprovar um alvo novo.

## Formas de saída

Leia [Entrega editável](entrega-editavel.md). O pedido e o documento existente definem formato e destino.
Padrão desta skill, sem formato definido: planilha `.xlsx`; Google Sheets quando esse for o destino escolhido.
Gere e reabra a entrega real; em revisões, atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário. HTML sai quando escolhido; não é cópia obrigatória de Word, Docs ou planilhas.
Preserve os campos e a ordem de [template.md](template.md) e confira [checklist.md](checklist.md).

Modelos para HTML/canvas quando essa for a entrega escolhida:

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-okr-kit-02.html` **(padrão)** | OKR Canvas | Objetivos e Resultados-Chaves · família kit 2 | "no canvas do kit" | pronto |
| `../assets/modelos/canvas-okr-v6.html` | Canvas Editável — OKR · família v6 | "no canvas v6" | pronto |
| `../assets/modelos/canvas-ponte-a3-okr-b-01.html` | Ponte A3 → OKR (editável) · família b 01 | "no editável" | pronto |
| `../assets/modelos/canvas-checkpoint-b-07.html` | Checkpoint do Plano (editável) · família b 07 | "no editável" | pronto |

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

- **Leve** (pessoa, frente pequena, 30 dias): 1 objetivo, 1–2 KR, 1 iniciativa por KR. Pula a ponte se o A3 é de uma linha; mantém o de/para e o check-in.
- **Intermediária** (área, trimestre): 1 objetivo, 2–3 KR, ponte A3→OKR preenchida, checkpoint antes de executar, check-in semanal registrado no canal combinado.
- **Robusta** (empresa, semestre ou ano): até 3 objetivos, até 5 KR cada, fonte oficial por KR, com responsável nomeado, comprometido × aspiracional marcado, cascata por área com a pergunta "como contribuo?", placar automático e revisão mensal.

## Erros comuns

- Objetivo que é tarefa ("implementar CRM") — o mais frequente.
- KR que é entrega ("criar o repositório") — é iniciativa.
- KR sem número de partida ou sem fonte: ninguém sabe a nota.
- Três colunas de objetivo preenchidas no primeiro trimestre (Kit).
- OKR imposto de cima, copiado da empresa para a área.
- Usar como modelo de KR exemplos que são tarefas; use os exemplos do Kit.
- Número de grupo sem rotular a empresa: cada empresa tem sua fonte e seu responsável pelo número.
- Plano sem check-in na agenda: "separa quem faz OKR de quem só escreveu OKR".

## Divergências anotadas

- Limite de KR: aula 2–5; modelo editável, Ficha e Kit 3; `Template+OKR+Canvas` 4. Adaptação desta skill: até 3 para começar, teto 5. Essa escolha não elimina as diferenças entre fontes.
- Template o modelo editável é defeituoso (só campo para KR 1). Use o o modelo editável.
- Check-in e Checkpoint só existem na v6; não há aula ao vivo nem template de check-in. O template desta skill (bloco 3) é a partir do roteiro.
