# Documentos de projeto

## O que é e quando usar

Todo projeto tem uma lista de documentos para organizar sua operação.

Entra: uma frente nova ou uma frente viva sem arquivo. Sai: a pasta com os documentos da
fase, cada um com dono, data e prova. Dois documentos vivem só nesta skill porque não têm
skill própria: o **Status Report** (do Desafio de 7 Dias — o "pulso" curto de uma frente)
e o **Resumo do Ciclo** (fechamento de uma página).

Regra: projeto roda em ciclo; operação roda em fluxo (M06 A11). Dossiê é de **projeto**.
Processo recorrente tem briefing de processo + POP + quadro, sem plano de ciclo próprio.

## Fonte no método

- Fundamentos — visão de floresta e Lean: §1 (o que cada passo deixa pronto), §4.3 (Mapa da Jornada e próxima entrega).
- Passo 1 — Entender o contexto, §1: A3 como alicerce; OKR nasce da distância para a meta; backlog e ciclos vêm do plano.
- Passo 2 — Organizar o trabalho, §1: OKR → iniciativas → briefing → matriz → Backlog 2D → ciclo → Checkpoint do Plano.
- Passo 4 — Ritmo ágil: §4.5 (Plano do Ciclo v6), §4.7 (Revisão do Ciclo v6), §4.14 (Desafio de 7 Dias e Status Report). Status Report é template sem aula própria.
- Passo 5 — Melhoria contínua, §4.5: Resumo do Ciclo, Artefato 17 (v6 06/09), sem aula própria.
- Templates oficiais: Status Report do Desafio de 7 Dias (8 campos); legado editável do Módulo 04 (6 campos, semáforo, próxima ação); Resumo do Ciclo editável do Módulo 05 (5 campos); Plano e Revisão do Ciclo.
- Acréscimos do laboratório: registro durável dos rituais, estado com prova e reaproveitamento de pastas existentes. Os modelos em branco estão em `../assets/modelos/`.

## A cadeia — fase, documento, skill, arquivo


| #   | Fase            | Documento                                                                         | Skill                                                   | Arquivo em `<pasta-do-projeto>/`                 | Quem assina                  |
| --- | --------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------- | ---------------------------- |
| 0   | Escolher o caso | Canvas de Visão curto                                                             | `ga2-canvas-de-visao`                                   | `00-canvas-de-visao.md`                               | dono da frente               |
| 1   | Entender        | A3 (esquerdo + causa + direito)                                                   | `ga2-diagnostico`, `ga2-causa-raiz`, `ga2-relatorio-a3` | `01-a3.md` (+ `01a-ishikawa.md`)                      | dono; decisor se houver gate |
| 2   | Combinar        | Briefing da iniciativa (por tipo)                                                 | `ga2-briefing-iniciativa`                               | `02-briefing.md`                                      | dono + interessados          |
| 3   | Mirar           | OKR e iniciativas (ponte A3 → OKR)                                                | `ga2-okr-canvas`                                        | `03-okr.md`                                           | dono; responsável pelo portfólio se cruza área     |
| 4   | Planejar        | Backlog 2D (+ matriz esforço × impacto)                                           | `ga2-backlog-2d`                                        | `04-backlog-2d.md`                                    | dono                         |
| 5   | Fluir           | Kanban: colunas, políticas, WIP                                                   | `ga2-kanban-canvas`                                     | `05-kanban.md`                                        | dono; Gestor propõe WIP      |
| 6   | Ciclo           | Plano do ciclo (meta, período, itens com dono)                                    | `ga2-plano-do-ciclo` / `ga2-review-do-ciclo` / `ga2-retrospectiva`                                  | `ciclos/AAAA-Www/plano.md` (linha da frente) | dono                         |
| 7   | Pulso           | **Status Report** (onde estou, travou, aprendi, próximo passo)                    | **esta skill**                                          | `status/AAAA-MM-DD.md`                                | dono                         |
| 8   | Revisar         | Review do ciclo (combinado × entregue × prova) + Retro                            | `ga2-plano-do-ciclo` / `ga2-review-do-ciclo` / `ga2-retrospectiva`                                  | `ciclos/AAAA-Www/review.md`, `retro.md`      | Gestor + dono                |
| 9   | Fechar          | **Resumo do Ciclo** (uma página; vira A3 de melhoria?)                            | **esta skill**                                          | `90-resumo-ciclo-<n>.md`                              | dono                         |
| —   | Sempre          | `README.md` — dono, empresa, régua, estado de cada documento, cartão no portfólio | esta skill                                              | `README.md`                                           | Gestor                       |


Se o projeto já tiver uma pasta com definição, andamento e aprovações, use esse dossiê.
A definição equivale ao briefing; o andamento equivale ao Status Report. Não duplique: o índice aponta para os documentos existentes.

## Como conduzir

1. **Confirme a pasta escolhida pelo usuário**, local ou no destino autorizado. Reuse a estrutura existente; se precisar organizar uma nova, use `ga2-abrir-projeto`. Registre no índice dono, empresa, régua, data e identificador do cartão. Recuse frente sem dono.
2. **Diga em que fase a frente está** e qual é a "próxima entrega" (Mapa da Jornada). Frente que está na fase 6 sem os documentos 1–2 tem dívida: registre no README, não finja.
3. **Status Report** (fase 7) — quando: toda sexta para frente em ciclo, ou quando o dono pede ajuda. Pergunta ao dono: "Que dia/semana está? No ritmo? O que já entregou, com prova? O que travou? O que aprendeu? Próximo passo, com data?" Retrato de 2 minutos; recuse relatório longo e recuse "no prazo" sem prova.
4. **Resumo do Ciclo** (fase 9) — quando: no fim do ciclo da frente, depois de review e retro. Pergunta: "Qual era o problema ou objetivo? O que foi produzido ou melhorou, com evidência? O que ficou claro depois de executar? Continuar, ajustar, pausar ou escalar? Algum problema merece voltar ao A3?" Recuse lista de tarefas no lugar de evidência.
5. **Confira o dossiê** na cadência combinada: documento da fase existe? tem data dos últimos 10 dias? tem assinatura? Registre a falta, quem deve responder, prazo e critério de pronto; envie cobrança apenas quando autorizado.
6. **Feche**: quando a frente entrega (critério de pronto do briefing provado), `README.md` ganha estado "entregue — aceito por <dono do resultado> em dd/mm" e o cartão sai do quadro.

## Regras do método que valem aqui

- **Sete artefatos do seu caso real, não de exemplo de livro.** (v6 00, slide 16)
- **Ritual que não produziu arquivo não aconteceu.** (acréscimo do laboratório, cadência: registro do ritual)
- **Estado vem de arquivo, não de memória.** Arquivo velho = cartão parado. (acréscimo do laboratório, estado com prova)
- **Status: rápido e honesto.** "Um retrato de 2 minutos, não um relatório longo. Adiantado, no prazo ou atrasado — sem maquiar." (Status Report do Desafio)
- **Feche com o próximo passo.** "Sempre saia com a próxima ação clara." (Status Report)
- **Resumo do Ciclo: feche em uma página; se precisar, reutilize o A3.** (Artefato 17)
- **Review produz decisão; retro produz uma melhoria com dono e data.** (cadência, regras 2 e 3)
- **Briefings entram à medida que a operação ganha cadência, não tudo no dia 1.** (Kit, fecho) — a régua corta documento, não fase.

## Saída

Os caminhos `.md` abaixo são convenções do fluxo de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- `<pasta-do-projeto>/` com os arquivos da tabela; `README.md` atualizado a cada documento novo.
- `status/AAAA-MM-DD.md` referenciado na coluna "Última prova" do portfólio.
- `90-resumo-ciclo-<n>.md` alimenta o report ao responsável pelo portfólio e, se marcar "vira A3", abre `01-a3.md` novo (um caso, um A3).
- Se o usuário usar repositório, siga o fluxo de versionamento autorizado. Salvar um documento não autoriza publicar nem enviar mensagens.

## Formas de saída

Ao criar ou revisar um artefato, leia [entrega-editavel.md](entrega-editavel.md). O formato pedido e o documento existente orientam a entrega.
Padrão desta skill, sem formato definido: documento Word `.docx`; Google Docs quando esse for o destino escolhido.
Use ferramentas de arquivos ou a integração disponível para gerar e conferir a entrega real.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Os modelos abaixo atendem ao fluxo de geração de HTML e canvas quando essa for a entrega escolhida.


| Forma     | Arquivo                                                                   | Quando sai                                                                | Modelo                                   |
| --------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------- |
| Fonte     | `<nome>.md` (este `template.md` preenchido)                               | quando o fluxo precisar de fonte Markdown                                 | `template.md`                            |
| Documento | `<nome>.html` — documento corrido no design system da casa                | quando HTML for escolhido                                                 | `../assets/modelos/documento.html` (pronto)        |
| Canvas    | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-status-report-b-04.html` |


Modelos canvas desta skill (specs `status-report-b-04`, `resumo-ciclo-b-04`, `status-report-b-04-p2`, `resumo-ciclo-b-04-p2`):


| Modelo                                                | Origem                                                     | Pedido que o escolhe | Estado |
| ----------------------------------------------------- | ---------------------------------------------------------- | -------------------- | ------ |
| `../assets/modelos/canvas-status-report-b-04.html` **(padrão)** | Status Report — 7 dias (editável) · família b 04           | "no editável"        | pronto |
| `../assets/modelos/canvas-resumo-ciclo-b-04.html`               | Resumo do Ciclo (editável) · família b 04                  | "no editável"        | pronto |
| `../assets/modelos/canvas-status-report-b-04-p2.html`           | Status Report — 7 dias (editável), página 2 · família b 04 | "no editável"        | pronto |
| `../assets/modelos/canvas-resumo-ciclo-b-04-p2.html`            | Resumo do Ciclo (editável), página 2 · família b 04        | "no editável"        | pronto |


Como gerar (da raiz do repo; o construtor lê o `.md` pelas âncoras `<!-- c:id -->` deste template):

```bash
python3 construtor/construir.py status-report-b-04 --documento --md <nome>.md --saida <nome>.html
python3 construtor/construir.py status-report-b-04 --canvas --md <nome>.md --saida <nome>-canvas.html
# Confira o HTML renderizado: ids, campos preenchidos, nenhum conteúdo cortado e número de páginas esperado.
```

Sem o construtor: copie o modelo em branco e escreva dentro das `div[data-campo]`, mantendo os
ids; campos de lista (`class="postits"`) recebem um `div.postit` por item. Os ids e o texto-guia
de cada campo estão em `../assets/modelos/CAMPOS.md`. Preserve o modelo em branco e preencha uma cópia do caso; não altere o desenho oficial para corrigir preenchimento.

### Regras da forma HTML

Quando HTML for escolhido, use os modelos empacotados em `../assets/modelos/` e confira a renderização. Eles já trazem as cores da marca; preserve o desenho oficial.

**Cores do modelo GA 2.0:**
Teal `#3D9B9D` = marca e medido · laranja `#F97316` = risco e estimado · cinza `#576270` =
em aberto. Tipografia Manrope. Nenhuma cor solta no arquivo.

**Linguagem: curta e autoexplicativa.** Frase de até 20–25 palavras, uma ideia por frase.
Palavra comum vence a rebuscada. Jargão traduzido na primeira aparição, na própria linha
("ROAS = quanto de receita volta para cada R$ 1 gasto"). Sem inglês desnecessário. O título
diz a consequência, não o achado. Curto não é vago: corte a palavra, nunca o número nem a
fonte.

**Procedência:** todo número carrega selo (medido · estimado, com a premissa escrita · em
aberto) e fonte reconferível. O que o sistema *faria* é sempre "em aberto", nunca "medido".
Número sem fonte não vira pixel.

**Pessoas envolvidas:** todo artefato de projeto ou frente traz o bloco — quem responde pelo
resultado, quais **pessoas** participam (pelo nome), quais **agentes** executam, quem decide a
trava e quem confirma que serve. Separe pessoas de agentes de IA quando existirem. Sem nome na fonte, escreva "não definido" — nunca atribua responsabilidade por suposição.

No fluxo Markdown → HTML, gere o HTML da fonte atual.
Em Word, Docs ou planilhas, siga a fonte e a conferência de `SAIDA-EDITAVEL.md`.

## Adaptação


| Régua         | Quando                          | Documentos obrigatórios                                                                                 |
| ------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Leve          | 1 pessoa, &lt; 1 mês            | 00 canvas curto · 01 A3 de uma página · 05 kanban (3 colunas) · status semanal · resumo no fim          |
| Intermediária | área, 1–3 meses                 | 00–05 · linha no plano do ciclo · status semanal · review/retro · resumo                                |
| Robusta       | atravessa áreas, dinheiro, gate | tudo, com OKR de 2+ KRs, Backlog 2D completo, políticas escritas, status com semáforo, resumo por ciclo |


## Erros comuns

- Pasta criada e vazia: dossiê de nome, não de fato.
- Status Report que é lista de atividades — sem "no ritmo?", sem trava, sem próximo passo datado.
- "No prazo" sem prova pelo caminho real.
- Resumo do Ciclo com aprendizado genérico ("precisamos comunicar melhor") ou decisão sem verbo.
- Pular o resumo e emendar o próximo ciclo — o aprendizado morre.
- Duplicar um dossiê existente em outra pasta — aponte, não copie.
- Cobrar documento de fase robusta em frente leve — o dono abandona o método.
