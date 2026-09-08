# Matriz Esforço × Impacto

## O que é e quando usar

Grade 2×2 que ordena iniciativas: **impacto** (quanto move os KR) no eixo vertical, **esforço**
(tempo, custo, complexidade, curva de aprendizado) no horizontal. "Gestão é escolha;
priorizar é usar essa escolha de modo inteligente" (M04 A15). A matriz torna a escolha
"transparente e defensável": quando alguém pergunta por que algo está esperando, "está lá
um método para se provar".

Vive no Passo 2, **depois do OKR e antes do Backlog 2D**. Entra: a lista de iniciativas do
OKR Canvas. Sai: uma fila ordenada que vira a linha de cima do Backlog 2D. Nesta adaptação, alimenta a
fila do planejamento do ciclo.

## Fonte no método

- Passo 2 — Organizar o Trabalho: variante de objetivos (M04 A09), conceito e campos da matriz (M04 A15), diferenças de nomes.
- Aulas: M04 A15 (Esforço × Impacto), M04 A09 (Importância × Dificuldade sobre objetivos); v6, módulo 03, aula 07.
- Templates: Artefato 07 — “Matriz Esforço Impacto GA2 editável”; Ficha artefato 05 — “Esforço Impacto GA2”; slide M04 A15 — “Matriz de Priorização”.
- M10 não tem canvas próprio dessa matriz: ela aparece no “Template OKR Canvas”, com outros eixos.
- Exemplo do curso: Kit Implementação — “OKR Canvas — Planejamento”, bloco 2 (variante de objetivos, Norte-Sul).
## Como conduzir

1. **Confira a entrada.** Pergunta: "isso é iniciativa, objetivo ou KR?" Só iniciativa entra.
   Recusa: objetivo e KR na grade — "são direção e meta, não escolha".
2. **Liste tudo, sem filtro.** Inclua o que já roda hoje e as ideias que surgiram na hora.
   Recusa: lista com item sem dono ou sem o KR que move ("volta ao OKR").
3. **Impacto.** Pergunta por item: "quanto isso move o KR? qual número e quanto?" Escreve
   alto ou baixo com o motivo em uma linha. Nesta adaptação, impacto = quanto move o KR no período
   ou quanto destrava dinheiro, cliente, reputação ou decisão. Recusa: "é importante" sem número.
4. **Esforço.** Pergunta: "quanto custa em tempo, dinheiro, complexidade e aprendizado? tem
   gate humano pendente?" Nesta adaptação, esforço = dias de trabalho + espera por aprovações. Recusa:
   estimativa sem unidade.
5. **Posicione** cada item num quadrante:
   - alto impacto + baixo esforço → **Faça já** (resultado rápido; "o dinheiro fácil")
   - alto impacto + alto esforço → **Planeje** (estratégico; quebre em partes menores, escolha o momento)
   - baixo impacto + baixo esforço → **Encaixe** (apoio; só entra se não roubar foco)
   - baixo impacto + alto esforço → **Evite ou questione** (desperdício; "você vai trabalhar demais para não entregar nada de valor")
6. **Decida a sequência**, não o descarte: Faça já → Planeje (com data) → Encaixe (nas brechas)
   → Evite (fica fora do backlog, com o motivo escrito). Pergunta final: "o que você ia
   fazer primeiro antes da matriz? mudou?" e "o que caiu no Evite — tem coragem de tirar?"
7. **Entregue a fila.** Escreve a ordem numerada. Ela vira a linha de cima do Backlog 2D.

## Regras do método que valem aqui

- **Só iniciativas entram.** Objetivo e KR ficam fora (v6 07).
- **A matriz dá sequência, não descarte.** "Não é fazer só o Faça já e jogar o resto fora" (v6 07).
- **Ordem de leitura:** resultado rápido → estratégico → apoio nas brechas → questionar o desperdício (M04 A15; v6 07).
- **Planeje = quebre em partes menores** (editável Mod 2).
- **Encaixe só entra se não roubar foco** (editável Mod 2).
- **Evite fica fora do backlog** com o motivo escrito (v6 08: "a do Evite não entra no backlog").
- **Priorização transparente e defensável:** dá para explicar a um terceiro por que algo espera (M04 A15).
- **Nomes usados nesta adaptação:** Faça já / Planeje / Encaixe / Evite (v6), impacto na vertical, esforço na horizontal. As equivalências com outras fontes estão no template.

## Variante: Importância × Dificuldade sobre objetivos (M04 A09)

No fluxo do OKR Canvas estendido (M04 A09), a mesma grade serve para escolher **quais
objetivos** entram no trimestre: eixos Importância/Impacto × Dificuldade/Custo; quadrantes
1 Quick Wins ("alto valor"), 2 Estratégico ("tem que ter"), 3 Desejável ("quando puder"),
4 Distrações ("não priorizar"). "Normalmente a gente prioriza o 1 e o 2, e mais o número 1."
É a única variante que o Kit (Norte-Sul) preenche. Use-a **antes** do OKR, na lista inicial
de objetivos; use a de iniciativas **depois** do OKR. Não misture as duas numa grade só.

## Saída

- Salve a matriz datada na pasta escolhida pelo usuário. A fila também pode integrar o Plano do Ciclo existente.
- Depois: a fila numerada vira a linha de cima de `ga2-backlog-2d`; Faça já alimenta os compromissos do ciclo (adaptação: até três por responsável); Planeje ganha data; Evite fica fora com motivo.
- Se houver insistência em um item do Evite ou disputa entre áreas, registre e leve ao decisor de prioridades. O facilitador não altera a prioridade por conta própria.

## Formas de saída

Leia [Entrega editável](entrega-editavel.md). O pedido e o documento existente definem formato e destino.
Padrão desta skill, sem formato definido: planilha `.xlsx`; Google Sheets quando esse for o destino escolhido.
Gere e reabra a entrega real; em revisões, atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário. HTML sai quando escolhido; não é cópia obrigatória de Word, Docs ou planilhas.
Preserve os campos e a ordem de [template.md](template.md) e confira [checklist.md](checklist.md).

Modelos para HTML/canvas quando essa for a entrega escolhida:

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-matriz-v6.html` **(padrão)** | Canvas Editável — Matriz de Priorização · família v6 | "no canvas v6" | pronto |


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

- **Leve** (até 6 itens, uma pessoa): duas perguntas por item, posiciona de cabeça, escreve só a fila numerada com o quadrante de cada um.
- **Intermediária** (área, 6–15 itens): tabela com impacto e esforço justificados em uma linha cada, grade desenhada, fila numerada com data para o Planeje.
- **Robusta** (portfólio, várias áreas): impacto ligado ao KR com o número; esforço em dias de trabalho + espera por aprovações; item de área diferente na mesma grade exige o decisor de prioridades para desempatar; registro do que foi para o Evite e por quê.

## Erros comuns

- Pôr objetivo ou KR na matriz (v6 07).
- Fazer só o quadrante Faça já e descartar o resto (v6 07).
- Começar pelo item grande e caro — "sem a matriz talvez a Ana tivesse começado justamente por essa" (trocar o sistema; trocar o ERP no Kit).
- Impacto "alto" sem dizer qual número move.
- Esforço sem contar o gate humano: esperar uma aprovação custa dias parados, não apenas horas de execução.
- Misturar a grade de objetivos (A09) com a de iniciativas (A15) — eixos e nomes diferentes.
- Chamar tarefa de iniciativa: tarefa se ordena no Backlog 2D, não na matriz (a variante de objetivos está separada nesta skill).
