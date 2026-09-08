# Painel do Gestor

## O que é e quando usar

O Painel do Gestor é o retrato de um ciclo em uma tela, lido por quem decide, uma vez por
ciclo, "provavelmente no celular, entre duas reuniões". Pergunta que ele responde: "essa
área está sob controle?". Todo número vem com **meta, tendência e leitura** — número
solto "trabalha contra você".

Vive no Passo 7 (Painel do Gestor e IA). Entra antes: o Painel de Métricas do Ciclo do
Passo 5 (o mesmo dado, para o time) e os KRs do OKR do Passo 2. Sai depois: o Relatório
Executivo de uma página e a reunião de 15 minutos.

Não confundir com o painel de métricas do ciclo: aquele é do time, toda semana, número
cru serve. Este é de quem decide, uma vez por ciclo, número com régua e frase.

## Fonte no método

- Base do método — Passo 7: Ferramentas, IA e Painel do Gestor §2.6–2.7 (dois painéis; meta, tendência e leitura), §3 regras 11–13, §4.3 (campos do HTML e da planilha), §4.9 (cockpit em Sheets, referência).
- Base do método — Passo 5: Melhoria Contínua §2.10 (Teoria do Caiaque: os três pilares) e §2.12 (North Star Metric).
- Aulas: ao vivo M07 A06–A11 (métricas de sucesso, p1–p5); v6 pasta 08 aula 02 ("Painel do Gestor").
- Templates oficiais: `painel-do-gestor-ga2-PREENCHER.html` (editável, salva PDF), `Painel-do-Gestor.xlsx` / `painel-do-gestor-ga2-scorecard.xlsx` (abas Modelo, Exemplo, Evolução), `painel-do-gestor-ga2-exemplo-preenchido.pdf`. PDF do curso: `painel-do-gestor-ga2.pdf`.
- Métricas de fluxo derivadas pelo laboratório: apêndice de `template.md` (ver adaptação).

## Os blocos (v6, HTML oficial)

| Bloco | O que entra |
|---|---|
| Cabeçalho | ciclo e período; contadores no alvo / quase / abaixo (automático) |
| Entregas do ciclo | objetivo do OKR em uma frase; entregues / planejadas / meta % |
| Pilar Saúde do negócio | um número: nome, atual, unidade, meta, frase de contexto, direção ▲/▼ |
| Pilar Saúde do time | idem |
| Pilar Produtividade | idem |
| OKR — KR1..KR3 | resultado-chave, atual, meta, direção |
| Evolução | % de cumprimento de entregas nos últimos 4 ciclos |
| Feedback do ciclo | cliente e time, o que ouvi (uma frase cada) |
| Leitura e próximo passo | sua frase, duas linhas |

A planilha acrescenta uma linha **North Star** (métrica-estrela: a que responde negócio,
time e produtividade de uma vez) acima do OKR. O HTML não a tem. Ver divergência abaixo.

**Régua de cor (HTML e planilha):** direção ▲ (maior é melhor) = `atual / meta`; direção ▼
(menor é melhor) = `meta / atual`. ≥100% verde (no alvo), 80–99% âmbar (quase), <80%
vermelho (abaixo). No relatório, a cor vira palavra: no alvo / atenção / fora da meta.

## Como conduzir (40 min, v6 02 slide 11)

1. **Pergunte o ciclo.** "Qual ciclo e qual período?" Escreva no cabeçalho. Recusa: painel sem período.
2. **Um número por bloco.** Para cada pilar, pergunte as três do caiaque: o negócio entrega valor e dá lucro? as pessoas estão engajadas? o processo entrega produtividade? Escolha **um** indicador por pilar entre os seis que quase sempre servem: entregas do ciclo, tempo de entrega, retrabalho, satisfação de quem recebe, carga por pessoa, o que está parado esperando. Recusa: 14 números ("é lista"); sigla sem tradução (MTTR, SLA); número que ninguém coleta ("morre no 2º ciclo").
3. **A régua.** Para cada número: meta e valor do ciclo anterior. "É onde você descobre que não sabia a sua própria meta." Recusa: número sem meta. Se a meta não existe, o campo fica `falta meta` e isso entra na leitura.
4. **KRs.** Copie os KRs do OKR vigente com atual e meta. Recusa: KR inventado para o painel; KR sem número.
5. **Evolução.** Os quatro últimos ciclos de cumprimento de entregas. Primeiro ciclo: só um ponto, sem inventar histórico.
6. **Feedback.** Uma frase do cliente, uma do time, citadas como vieram. Recusa: resumo adjetivado ("o time está feliz").
7. **Leitura em duas linhas.** O que está no alvo, o que não está, o próximo passo. Recusa: desculpa, narrativa de processo, adjetivo.
8. **Escolha o formato e não troque.** Siga `entrega-editavel.md`: HTML para o visual; Word/Docs ou planilha quando solicitados; PDF para leitura. Markdown só quando o fluxo precisar. "Trocar toda hora muda: o leitor perde o hábito."

## Regras do método que valem aqui

- Número sempre com meta, tendência e leitura. (v6 02 slide 05)
- Quatro blocos, nada mais; 14 números é lista; número que ninguém coleta morre. (v6 02 slides 03 e 06)
- Faça as três perguntas do caiaque antes de escolher métrica; nunca copie template da internet. (M07 A07, A09)
- "Três linhas — não trinta": uma métrica por esfera. (Passo 5, v6 07)
- Status do KR é uma palavra: no alvo, atenção, fora da meta. (v6 03 slide 08)
- Métrica com mais de uma fonte: declare a canônica antes de reportar. Número de dinheiro vem com a empresa correta e a fonte é o responsável financeiro dela.

## Divergência registrada: HTML × planilha

As duas versões oficiais não batem (Base do método — Passo 7 §8.4–8.5):

| | HTML `painel-do-gestor-ga2-PREENCHER.html` | Planilha `Painel-do-Gestor.xlsx` |
|---|---|---|
| North Star | não existe | linha "CSAT 0–10" (7,9 / 8,5) |
| Indicadores por pilar | um (NPS · Clima · Tempo de entrega) | dois (NPS + ROI · Clima + Permanência · Entregas + Tempo) |
| Evolução | % de entregas por ciclo | CSAT e Clima por ciclo |
| Atingimento | mostra 110%, 103%, 125% em anéis | status numérico `=H/J*100` |
| Roteiro v6 02 | slide 08 "NPS 3,8 meta 4,3"; slide 09 "NPS 55 meta 50" | — |

Contradição de fundo: a aula 03 diz "quem decide não quer atingimento, quer palavra", e o
HTML exibe porcentagem. **Adaptação do laboratório preservada nesta referência:** o template usa um
indicador por pilar (HTML), mantém a linha North Star (planilha) e mostra a **palavra** de
status, com a % só entre parênteses. A fonte registra divergência na escala NPS/CSAT;
não presuma que escalas distintas foram unificadas.

## Saída

Os caminhos `.md` abaixo são convenções do fluxo de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Registro: um painel por ciclo pelo `template.md`, no destino escolhido. Painel por área ou diretor apenas quando pedido.
- Inclua a medição no histórico do painel.
- Depois: o Relatório Executivo (bloco 1 copia os três pilares) e o relatório de sexta à coordenação, no bloco de métricas.
- Aluno: HTML oficial salvo em PDF, ou planilha com aba duplicada para histórico.

## Formas de saída

Ao criar ou revisar um artefato, leia [entrega-editavel.md](entrega-editavel.md). O formato pedido e o documento existente orientam a entrega.
Padrão desta skill, sem formato definido: visual HTML; Word `.docx`, Google Docs, Excel `.xlsx` ou Google Sheets quando solicitados.
Use ferramentas de arquivos ou a integração disponível para gerar e conferir a entrega real.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Os modelos abaixo atendem ao fluxo de geração de HTML e canvas quando essa for a entrega escolhida.

| Forma | Arquivo | Quando sai | Modelo |
|---|---|---|---|
| Fonte | `<nome>.md` (este `template.md` preenchido) | quando o fluxo precisar de fonte Markdown | `template.md` |
| Documento | `<nome>.html` — documento corrido no design system dos modelos públicos | quando HTML for escolhido | `../assets/modelos/documento.html` (pronto) |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-painel-metricas-v6.html` |

Modelos canvas desta skill (specs `painel-metricas-v6`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-painel-metricas-v6.html` **(padrão)** | Canvas Editável — Painel de Métricas · família v6 | "no canvas v6" | pronto |

Como gerar HTML ou canvas quando escolhido:

1. Copie o modelo público em branco de `../assets/modelos/`; preserve a matriz original.
2. Preencha as `div[data-campo]` na cópia, mantendo os IDs e os campos do `template.md`.
3. Campos de lista (`class="postits"`) recebem um `div.postit` por item. Consulte `../assets/modelos/CAMPOS.md`.
4. No fluxo Markdown, preserve as âncoras `<!-- c:id -->` e gere a partir da fonte atual.
5. Confira IDs, nenhum `{{` restante, campos sem estouro e canvas em uma página.
6. Não altere o modelo distribuído. Mudança na matriz exige revisão do modelo e nova conferência.

### Regras da forma HTML

Padrão público, leia antes de gerar: `gestao-visual.md`. O documento nasce do
template público, que já traz as cores da marca aplicadas — **não escreva CSS do zero e não use
paleta genérica**.

**Cores: preserve o design system MindMaster incorporado nos modelos públicos**.
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
trava e quem confirma que serve. Pessoa e agente nunca na mesma linha. Sem nome na fonte,
escreva "não definido" — nunca atribua tudo ao usuário.

No fluxo Markdown → HTML, gere o HTML da fonte atual.
Em Word, Docs ou planilhas, siga a fonte e a conferência de `entrega-editavel.md`.

## Adaptação

- **Leve** (área pequena, ciclo semanal): só cabeçalho, três pilares e leitura. Sem evolução até ter 4 ciclos.
- **Intermediária** (diretor de área): blocos completos + linha North Star + métricas de fluxo como apêndice (tempo de ciclo, bloqueado, em gate, data cumprida, aceite na 1ª, retrabalho, parados, relatórios). As métricas de fluxo são **acréscimo do laboratório** — a aula não as lista; origem: Modelo Operacional de Demandas, §17, transcritas no apêndice do template.
- **Robusta** (aluno com número de sistema): planilha oficial, aba Evolução, exportar PDF, relatório executivo junto.

## Erros comuns

- Número demais. Número bonito que ninguém coleta. Sigla.
- Número sem meta, sem tendência ou sem leitura — o leitor "assume que você está se defendendo".
- Meta em legenda em vez de grudada no número.
- Trocar de formato a cada ciclo.
- Reportar total do grupo sem identificar a empresa ou a composição da soma.
- Painel com tese de que está tudo bem enquanto o portfólio mostra 8 cartões parados: leitura tem que bater com o quadro.
