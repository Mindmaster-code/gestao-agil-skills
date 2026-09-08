# Quadro Kaizen do Ciclo

## O que é e quando usar

Kaizen = mudança + melhoria: "o hábito de melhorar o trabalho em passos pequenos, frequentes
e sustentados. A força vem do acúmulo." O Quadro Kaizen é uma página que leva um **sinal
real** até uma **decisão**: fato com número → uma aposta → medir → manter, ajustar ou
descartar. É a "folha de passagem entre os rituais": abre no check-in, ganha evidência na
Review, recebe ação na Retro, fecha quando o número volta (≤ 30 dias).

É o registro das melhorias pequenas do **lado 80–90%** do barbell (o jeito comprovado, feito
um pouco melhor). O lado 10–20% (a aposta diferente) tem outro registro: a **folha de
experimento**. Não duplicar: um experimento não vira Kaizen nem o contrário.

Vive no **Passo 5 — Melhoria Contínua** (artefato central da v6, aula 01).

## Fonte no método

- Base do método — Passo 5: Melhoria Contínua §2.9, §2.6 (barbell), §4.1, §4.7 (folha de experimento),
  §6.3, regras 5–9, divergência 22 — v6 aulas 01, 03, 04 (não há aula ao vivo).
- Template oficial: Canvas Editável — Quadro Kaizen do Ciclo, v6, Passo 5 (referência de origem; modelo público nos assets).
- Folha de experimento (lado 10–20): skill `ga2-folha-de-experimento`; as seis perguntas e os limites estão na referência de método dessa skill.

## Kaizen × folha de experimento

| | Quadro Kaizen (80–90) | Folha de experimento (10–20) |
|---|---|---|
| Pergunta | como fazer o de sempre um pouco melhor? | qual é a ideia mais diferente possível? |
| Origem | sinal: KR parado, entrega recusada, atrito repetido, 360, Gemba | dor de pessoa real com prova |
| Risco | baixo; não arrisca a operação | alto; "o pior dia custa uma semana" |
| Decisão | manter / ajustar / descartar | mata / ajusta / escala |
| Onde | pasta de melhorias escolhida pelo usuário ou junto do ciclo | registro de experimento da área, com data e nome |
| Cobrança | uma por ciclo, o Gestor registra | placar quinzenal, o Gestor cobra, a pessoa responsável pela coordenação compila |

A fonte registra uma divergência de nomenclatura entre Kaizen e experimento (divergência 22). Nesta skill, preserve a separação explicitada acima; não presuma que as versões foram fundidas.

## Gatilhos que abrem um Kaizen

- KR parado por duas semanas (check-in / review).
- Entrega concluída e recusada por quem recebe.
- Resultado subiu com efeito colateral (tempo menor, qualidade pior).
- Atrito que apareceu mais de uma vez na retro.
- Padrão no feedback 360.
- Fato do Gemba com causa clara.

## Como conduzir

1. **Registrar o sinal antes de pensar em solução.** Pergunta: "O que aconteceu, qual métrica,
   qual o número de hoje, qual a meta?" Escreve fato sem culpado. "Segure a vontade de
   escolher a solução agora." Recusa: sinal que é opinião do chefe — o quadro vira lista de ideias.
2. **Passar as ideias pelo filtro** (v6 A04): sob controle do time? cabe em um ciclo? move um
   atrito repetido? A primeira que passa vira aposta; as outras vão para a **fila**.
3. **Uma aposta, dono, prazo, o que esperamos.** Recusa: duas mudanças juntas; teste grande
   que arrisca a operação.
4. **Rodar dentro do ciclo**, no lado 80–90. Registrar desvios.
5. **Voltar ao número** no fim do ciclo. "O que aconteceu de fato?" com evidência.
6. **Decidir com verbo:** manter (escrever o padrão onde o time trabalha), ajustar (nova dose,
   novo Kaizen), descartar (registrar; "não procurar duas vezes no mesmo lugar").
7. **Fechar** com próximo passo e data. Quadro aberto há mais de 30 dias entra no relatório ao responsável pela coordenação.

## A fila de melhorias `(acréscimo do laboratório)`

O canvas v6 é uma folha por melhoria. Mantenha uma **fila** no documento escolhido:
ID · sinal · métrica e número · origem · dono · status (fila / em teste / fechado) · decisão.
Uma em teste por ciclo por dono; o resto espera. Ideia sem número de hoje não entra na fila.

## Regras do método que valem aqui

- "Sem número de hoje não existe melhoria — existe opinião. Anote mesmo estimado." (canvas Painel v6)
- "Uma mudança por ciclo, uma variável por vez." (v6 A01)
- "Toda melhoria termina num verbo: manter, ajustar ou descartar. Sem essa decisão, a
  melhoria fica aberta para sempre." (v6 A01)
- "O que funcionou vira padrão escrito onde o time trabalha." (v6 A04)
- "Reserve 10–20% do ciclo para a aposta; 80–90% fica no comprovado; o meio morno fica
  vazio." (v6 A02; política de inovação descrita neste método)
- "Uma melhoria em 30 dias: semana 1 sinal e número; 2 teste; 3 evidência; 4 decisão." (v6 A09)

## Saída

Os caminhos `.md` abaixo são convenções do fluxo de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Registro: uma folha por melhoria, com data e nome, no destino escolhido; inclua uma linha na fila de melhorias.
- Depois: decisão "manter" → POP ou política escrita onde o time trabalha; "ajustar" → novo Kaizen ou PDCA ciclo 2; fechamento entra no relatório de sexta. Se a causa é incerta ou atravessa áreas → abre A3, não Kaizen.

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
| Documento | `<nome>.html` — documento corrido no design system dos modelos públicos | quando HTML for escolhido | `../assets/modelos/documento.html` (pronto) |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-kaizen-v6.html` |

Modelos canvas desta skill (specs `kaizen-v6`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-kaizen-v6.html` **(padrão)** | Canvas Editável — Quadro Kaizen do Ciclo · família v6 | "no canvas v6" | pronto |

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

- **Leve**: sinal com número · aposta · dono · prazo · decisão — cinco linhas.
- **Intermediária** (ciclo da equipe): template completo, fila mantida.
- **Robusta** (melhoria de resultado com KR): acrescenta de/para por KR e ligação ao check-in
  semanal do OKR; fecha em até 30 dias com decisão escrita e padrão.

## Erros comuns

- Duas mudanças juntas.
- Sinal que é opinião, não número.
- Teste grande que arrisca a operação (isso é experimento, e nem assim sem gate).
- Decisão fechada por sensação em vez de número.
- Quadro que nunca fecha.
- Registrar como Kaizen uma aposta do lado 10–20 (ou vice-versa).
