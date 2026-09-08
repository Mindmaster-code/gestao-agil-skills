# POP — Procedimento Operacional Padrão

## O que é e quando usar

"Documento formal que descreve as etapas de um processo, padronizando e trazendo clareza"
(M04 A13). É "um grande checklist" para alguém executar sem depender de interpretação —
"quando a gente fica refém da interpretação na hora de executar um processo, é um
problemão". Serve para férias, promoção, treinamento e onboarding; traz eficiência,
qualidade e rastreabilidade (auditoria).

Vive no Passo 2, **depois do Briefing de Processo**, para o **gargalo** escolhido — não para a
operação inteira. Entra: uma iniciativa classificada como processo (3 Ps), com o briefing
que mostrou onde o erro nasce. Sai: o POP aprovado, com versão, e um indicador que diz se o
padrão está sendo seguido. Nesta adaptação, processo recorrente ganha POP quando passa a depender de
um único executor.

## Fonte no método

- Passo 2 — Organizar o Trabalho: conceito de POP, regras e campos consolidados.
- Aula e slides: M04 A13 — “Padronizando Processos — POP”; não há aula v6 de POP.
- Template legado: M10 — “Canvas POP” (PDF estático, 11 blocos); sem editável nas fontes citadas.
- Exemplo da aula: M04 A13 — “Exemplo Canvas POP” (aprovação de projetos, APPROJ001).
- Exemplo do curso: Kit Implementação — “Conferência padrão de separação” (POP-SEP-001).
- Critério de qualidade e revisão são adaptações metodológicas; a origem de cada campo está na tabela abaixo.
## Campos — de onde vem cada um

| # | Campo | Origem | Nome usado nesta adaptação |
|---|---|---|---|
| 1 | Nome do processo | canvas | — |
| 2 | Identificação: data, código, versão | canvas | versão |
| 3 | Objetivo ("finalidade: dar um direcionamento claro a todos os envolvidos") | canvas | objetivo |
| 4 | Escopo (o que cobre e o que não cobre) | canvas | escopo |
| 5 | Responsabilidades (pessoas/papéis e o que cada um faz) | canvas | responsável |
| 6 | Entradas do processo ("descreva como o processo inicia") | canvas | **gatilho** — é o mesmo campo |
| 7 | Passos do processo, em sequência, com responsável | canvas | passos |
| 8 | Saídas (resultado esperado ou documentos gerados) | canvas | — |
| 9 | Indicadores do processo e onde acessá-los | canvas | — |
| 10 | Sistemas ou ferramentas — **e como acessar** | canvas | **materiais** — é o mesmo campo |
| 11 | Exceções e tratamento ("e aprovações") | canvas | exceções |
| 12 | Riscos do processo e ações de mitigação | canvas | — |
| 13 | Monitoramento contínuo para prevenir riscos | aula e slides A13; sem caixa no canvas | — |
| 14 | Aprovação (nome, cargo, data) | canvas | — |
| 15 | Critério de qualidade (como se sabe que um passo saiu certo) | `(adaptação metodológica)` — na aula vive diluído em indicadores e saídas | critério de qualidade |
| 16 | Revisão (quando e quem revisa o POP; vale até) | `(adaptação metodológica)` — a aula só tem versão e aprovação | revisão |

## Como conduzir

1. **Confira se é caso de POP.** Pergunta: "isso repete sem data fim? depende de uma pessoa
   (ou uma automação) só? é o gargalo achado no briefing?" Recusa: POP da operação inteira
   ("manual de 40 páginas que ninguém lê"); POP de projeto (projeto tem fim — vai para briefing).
2. **Nome e identificação.** Pergunta: "como todo mundo chama isso? qual código localiza?"
   Escreve nome, data, código mnemônico (ex.: `POP-COB-001`), versão `v1.0`.
3. **Objetivo e escopo.** Pergunta: "para que existe? o que fica fora?" Recusa: objetivo sem
   o resultado ("padronizar" não é objetivo; "todo pedido sai certo na primeira" é).
4. **Responsabilidades.** Pergunta por papel: "quem executa? quem é dono e cobra? quem aprova
   exceção? quem recebe a saída?" Recusa: passo sem responsável; dois donos.
5. **Entrada (gatilho).** Pergunta: "o que faz o processo começar — evento, insumo, data?"
   Recusa: "quando der" — precisa de gatilho observável.
6. **Passos.** Numerados, em sequência, um verbo por passo, com responsável e o que sai de
   cada um. Pergunta por passo: "quem faz? com o quê? o que sai? como sabe que saiu certo?"
   (critério de qualidade). Recusa: passo que só diz "analisar"; passo que depende de
   "bom senso".
7. **Saídas.** O que existe no fim que não existia no começo (documento, registro, mensagem).
8. **Sistemas e como acessar.** Caminho, comando, login (sem segredo no POP). Recusa:
   sistema citado sem instrução de acesso.
9. **Indicadores.** Quais e onde ver. Pelo menos um de adesão (o padrão está sendo seguido?)
   e um de resultado. Recusa: processo "que não dá para medir" — "todo processo pode ser medido".
10. **Exceções, riscos, monitoramento.** Pergunta: "o que sai do padrão e quem aprova? o que
    pode dar errado e o que se faz antes? quem olha isso toda semana?"
11. **Aprovação e revisão.** Nome, cargo, data de quem aprovou; data da próxima revisão.
    Recusa: POP sem versão nem aprovação — "é rascunho".
12. **Teste real.** Alguém que nunca fez executa só com o POP. Onde travou, o POP está errado.

## Regras do método que valem aqui

- **POP documenta passo a passo com dono, entrada, saída, sistema e como acessar** (M04 A13).
- **POP do gargalo, não da operação inteira.** "POP vira padrão quando descreve uma tarefa específica, mensurável e com dono" (Kit).
- **Todo processo pode ser medido** (M04 A12) — POP sem indicador não fecha.
- **Ao mapear processo, questione cada etapa:** "por que você faz isso? quem usa?" — a planilha que ninguém lê sai (M04 A12).
- **Estabeleça monitoramento contínuo para prevenir riscos** (A13).
- **Bem feito = uma pessoa nova executa do mesmo jeito que o veterano** (critério de bem feito do Passo 2).
- **Classifique antes:** POP é para processo; projeto e produto têm briefing próprio (M04 A10).

## Saída

- Salve o POP identificado por código, versão e nome na pasta escolhida pelo usuário. Se o responsável já mantém o documento, atualize-o ou faça referência a ele.
- Depois: o indicador de adesão entra no painel ou relatório do processo; a revisão entra na agenda; cada exceção aprovada recebe registro datado.
- Automação ou produção: a execução cabe ao responsável técnico autorizado. Antes de executar, registre custos, frequência e controles para não repetir trabalho sem mudança de estado.

## Formas de saída

Leia [Entrega editável](entrega-editavel.md). O pedido e o documento existente definem formato e destino.
Padrão desta skill, sem formato definido: documento Word `.docx`; Google Docs quando esse for o destino escolhido.
Gere e reabra a entrega real; em revisões, atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário. HTML sai quando escolhido; não é cópia obrigatória de Word, Docs ou planilhas.
Preserve os campos e a ordem de [template.md](template.md) e confira [checklist.md](checklist.md).

Modelos para HTML/canvas quando essa for a entrega escolhida:

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-pop-kit.html` **(padrão)** | POP - Procedimento Operacional Padrão · família kit | "no canvas do kit" | pronto |


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

- **Leve** (rotina de uma pessoa, 5 passos): nome, gatilho, passos com responsável, saída, onde acessar, aprovação. Indicador = "foi feito, sim ou não".
- **Intermediária** (processo de área com handoff): todos os 14 campos do canvas + critério de qualidade por passo; teste com alguém que nunca fez.
- **Robusta** (processo entre áreas, com dinheiro ou cliente no caminho): tudo acima + monitoramento nomeado, revisão trimestral, versão com histórico de mudança, exceção com aprovador e registro.

## Erros comuns

- Manual de 40 páginas (Kit).
- Passo sem responsável; "todo mundo" é ninguém (A13).
- Sistema sem instrução de acesso (A13: "login é com seu e-mail e senha, não existe senha corporativa").
- POP sem aprovação nem versão — rascunho que ninguém segue.
- POP de processo que ninguém questionou (a planilha de 2–3 h a cada dois dias que "mandaram fazer", A12).
- Indicador de esforço ("X POPs escritos") no lugar de adesão e resultado.
- Checklist que vira carimbo automático sem conferência real (Kit, risco 2) — a saída visível (etiqueta, registro) é o que denuncia.
