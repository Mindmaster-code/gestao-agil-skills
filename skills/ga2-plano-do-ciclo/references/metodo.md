# Plano do Ciclo (Sprint Plan)

## O que é e quando usar

Plano do Ciclo (no mercado: Sprint Plan, Sprint Planning) é a primeira conversa do ciclo. Dela
sai uma meta escrita, o período, quem faz, quando são a diária, a review e a retro, e a lista
do que entra — puxada do Backlog 2D, na ordem, cada item com dono. É o Passo 4 (Ritmo Ágil).

Entra antes: Backlog 2D com fatia fina marcada e quadro Kanban montado. Sai depois: a coluna
"A fazer / Sprint Backlog" do quadro cheia, a diária rodando, e a review de sexta lendo a meta
copiada "sem maquiagem".

## Fonte no método

- Base do método: Passo 4 — Ritmo Ágil §2.4 (ciclo), §2.6 (planejamento), §2.7 (sistema puxado), §3
  regras 2–6, §4.5 (campos dos três templates), §6 item 2, §8 itens 2, 5, 6, 7.
- Base do método: Passo 3 — Gestão Visual §2.23 (ponte Backlog 2D → cartão; fatia fina).
- Aulas: M06 A05 (Canvas Sprint Plan), A11 (tamanho do ciclo), A13 (Sprint Planning); v6
  pasta 05 aulas 02 (ciclo) e 03 (planejamento do ciclo).
- Templates: v6 «Canvas Editável — Plano do Ciclo» (campos e exemplo da versão v6); ao vivo
  «M06 A05 — Canvas Sprint Plan»; individual folha individual «sprint-plano-ciclo-ga2.pdf».
- Acréscimo do laboratório: plano segunda 09h, até 3 compromissos por diretor; variante consolidada em `template.md`.

## Como conduzir

1. **Confirme o ciclo.** Pergunta: "Qual a duração? Está fixa desde quando?" Acréscimo do laboratório: uma semana,
   segunda a sexta. Recuse mudar o tamanho no meio ("o time precisa repetir para aprender a capacidade").
2. **Escreva a meta, uma só.** Pergunta: "O que fica pronto na sexta, numa frase, e por que
   isso é valioso?" Três testes (v6 aula 03): dá para mostrar pronto na sexta? cabe com folga?
   alguém fora do time nota? Recuse duas metas ("duas metas é nenhuma meta") e meta sem fim
   visível ("é atividade, não entrega").
3. **Ligue a meta ao OKR.** Pergunta: "De qual iniciativa do OKR essa meta vem?" Escreva a
   etiqueta. Recuse meta órfã sem iniciativa nem A3.
4. **Calcule a capacidade e planeje 70%.** Pergunta: "Quantos dias-pessoa você tem de verdade
   esta semana?" Planeje cerca de 70%; os outros 30% somem em imprevisto — sempre somem (v6).
   No laboratório: **até 3 compromissos por diretor** (acordo de cadência do time).
5. **Puxe da fatia fina, na ordem.** Pergunta: "Quais tarefas da primeira entrega do mapa
   entram?" Quem executa escolhe o que cabe; o PO (dono do rumo) só diz a prioridade. Recuse
   item "de presente" (empurrado) e item que não está no Backlog 2D.
6. **Cada item com dono, data e "pronto é".** Nome de pessoa, nunca área. "Pronto é" = como se
   verifica pelo caminho real (URL, arquivo, log, mensagem). Recuse item sem "pronto é": a
   demanda ainda não está pensada. Recuse item maior que uma semana — volta ao mapa e quebra.
7. **Quebre em tarefas de um dia ou menos** (A13). Tarefa de cinco dias fica a semana inteira
   em "fazendo" e ninguém vê progresso.
8. **Marque os rituais**: diária (hora, lugar), review e retro (dia, hora). No laboratório: diária por
   pulso e correio; review sexta 12h; retro sexta 14h.
9. **Leve os riscos do briefing** e escreva a resposta de cada um (A03, checklist etapa 4).
10. **Feche e registre.** Sprint backlog no quadro; plano salvo no destino escolhido, com data e versão. Use commit quando houver repositório.

## Duração da reunião — divergência registrada

| Fonte | Duração |
|---|---|
| M06 A13 (ao vivo) | ~2 h: 10 min abertura + 10 min meta + ~40 min o que entra + decomposição ("parte mais longa") + revisão |
| Apostila §12 | 60 min |
| v6 aula 03 | 15 a 30 min, segunda de manhã |
| Apostila p.15 (colada do Scrum Guide) | até 8 h para sprint de um mês |

**O laboratório usa 15 minutos por diretor, por carta** (acordo de cadência do time). Motivo: ciclo de uma
semana, até 3 compromissos, itens já quebrados no Backlog 2D. A decomposição em tarefas de um
dia é feita pelo dono no quadro da área, não na reunião. A escolha editorial de duração entre versões permanece em aberto (Base do método, Passo 4, §8.5); não esconda essa divergência.

## Regras do método que valem aqui

- Ciclo = o menor tempo que entrega algo de valor. Comece com uma semana; depois não mude. (A11, v6 02)
- Todo ciclo abre com uma meta escrita, uma só. (A13, v6 03)
- Quem executa escolhe o que cabe; ninguém recebe cartão de presente. Planeje ~70%. (A13, v6 03)
- Quebre em tarefas de um dia ou menos. (A13)
- Cartão com nome de pessoa, não de área. (v6 03)
- Cartão vem do Backlog 2D; cabe em uma semana; fatia fina entra primeiro. (v6 04, Passo 3)
- A meta do plano é a que a review lê, copiada sem maquiagem. (v6 07)
- Erro mais comum: distribuir tarefa até encher a agenda. (v6 03)

## Saída

Os nomes abaixo são sugestões de organização, não dependências de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Arquivo: Plano do Ciclo na pasta do caso (organização inteira) ou `plano-<diretor>.md` (por
  área). `AAAA-Www` = `date +%G-W%V`, ex.: `2026-W35`.
- Cada linha do plano vira ou atualiza um cartão em registro do portfólio na pasta do caso (coluna
  "Priorizado no ciclo" / "Em execução").
- Depois: `ga2-gestao-diaria` todo dia útil; review e retro na sexta (`ga2-plano-do-ciclo`, `ga2-review-do-ciclo` e `ga2-retrospectiva`);
  compromisso que perder a data é marcado no mesmo dia, não na sexta.

## Formas de saída

Ao criar ou revisar um artefato, leia [entrega-editavel.md](entrega-editavel.md). O formato pedido e o documento existente orientam a entrega.
Padrão desta skill, sem formato definido: planilha `.xlsx`; Google Sheets quando esse for o destino escolhido.
Use ferramentas de arquivos ou a integração disponível para gerar e conferir a entrega real.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Os modelos abaixo atendem ao fluxo de geração de HTML e canvas quando essa for a entrega escolhida.

| Forma | Arquivo | Quando sai | Modelo |
|---|---|---|---|
| Fonte | `<nome>.md` (este `template.md` preenchido) | quando o fluxo precisar de fonte Markdown | `template.md` |
| Documento | `<nome>.html` — documento corrido no design system do laboratório | quando HTML for escolhido | `../assets/modelos/documento.html` (pronto) |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-plano-ciclo-v6.html` |

Modelos canvas desta skill (specs `plano-ciclo-v6`, `sprint-plano-ciclo-c`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-plano-ciclo-v6.html` **(padrão)** | Canvas Editável — Plano do Ciclo · família v6 | "no canvas v6" | pronto |
| `../assets/modelos/canvas-sprint-plano-ciclo-c.html` | Sprint / Plano do Ciclo (jornada) · família c | "na folha da jornada" | pronto |

Como preencher os modelos quando HTML ou canvas for solicitado:

Copie o modelo empacotado para o destino escolhido. Preencha as `div[data-campo]` sem alterar os IDs; campos de lista (`class="postits"`) recebem um `div.postit` por item. Preserve as âncoras `<!-- c:id -->` da fonte quando houver Markdown. Consulte `../assets/modelos/CAMPOS.md` para IDs e textos-guia.

Confira IDs intactos, ausência de marcadores `{{` pendentes, campos completos, ausência de estouro e uma página no canvas. Preserve o modelo original em branco. O pacote também oferece o construtor em `construtor/construir.py`, na raiz; use suas instruções de uso quando disponível.

### Regras da forma HTML

Quando HTML for solicitado, use os modelos empacotados e a política [entrega-editavel.md](entrega-editavel.md). O documento nasce do modelo com estilos aplicados — **não escreva CSS do zero e não use paleta genérica**.

**Cores: preserve as do design system da MindMaster incorporadas nos modelos empacotados.**
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
trava e quem confirma que serve. Pessoa e agente nunca na mesma linha: identifique explicitamente o tipo de participante. Sem nome na fonte, escreva "não definido" — nunca atribua tudo a uma única pessoa por suposição.

No fluxo Markdown → HTML, gere o HTML da fonte atual.
Em Word, Docs ou planilhas, siga a fonte e a conferência de [entrega-editavel.md](entrega-editavel.md).

## Adaptação

| Régua | Quando | O que fica |
|---|---|---|
| Leve | uma pessoa, um caso | artefato individual "Meu Sprint": período, objetivo, o que vou fazer, como vou saber que foi bom, o que pode atrapalhar. 10 min. |
| Intermediária | um time, uma frente | canvas v6 completo: meta, período, quem responde, diária, review/retro, itens com dono. 15–30 min. |
| Robusta | portfólio de várias áreas | um plano por diretor por carta + plano consolidado do laboratório; cada item ligado a cartão do portfólio, com "pronto é", data e risco. Gestor recusa o 4º compromisso. |

## Erros comuns

- Duas metas, ou meta que é lista de tarefas.
- Planejar 100% da capacidade; na sexta, cinco coisas em setenta por cento.
- Cartão sem dono ou com nome de área.
- Item que não está no Backlog 2D, inventado na reunião.
- Tarefa de 4–5 dias que some em "fazendo".
- "Pronto é" vago ("entregar a campanha") em vez de verificável ("anúncio ativo na conta X, print").
- Mudar o tamanho do ciclo toda semana.
- Esquecer de marcar review e retro — depois "não deu tempo".
- Plano sem arquivo: ritual que não produziu arquivo não aconteceu.
