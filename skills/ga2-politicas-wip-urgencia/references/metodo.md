# Políticas de WIP e urgência

## O que é e quando usar

Duas políticas que todo quadro precisa ter escritas antes de rodar. **Limite de WIP** (trabalho
em andamento) é o teto de cartões por etapa; sem ele a fila se espalha, o gargalo some e
ninguém termina nada. **Política de urgência** é a regra, escrita antes do incêndio, que diz o
que é urgente, quem pode chamar, quantas cabem e o que acontece com o cartão pausado.

Vive no Passo 4 (Ritmo Ágil), aulas de limite e de urgência, e se aplica ao quadro do Passo 3.
Entra depois do quadro desenhado (`ga2-kanban-canvas`); sai como texto no topo do quadro e
como decisão de calibragem na retrospectiva.

## Fonte no método

A procedência desta skill está em `fontes.md`, nesta mesma pasta.

- Política de urgência v6: cinco linhas transcritas em `template.md` — o que é, quem chama, quantas, pausado e onde fica escrito.
- Templates: só slides. «Políticas do Quadro GA2 Editável» e

## Como conduzir

### Parte 1 — Limite de WIP

1. **Conte o que está em andamento hoje, por coluna e por pessoa.** Pergunta: "Quantos cartões
 cada um tem começados e não terminados?" Escreva o número real.
2. **Ponto de partida: o que está em andamento menos um** (material de referência). O material sugere
 "pessoas ÷ 2 por etapa" — não está em aula; use só como segunda referência.
 Recuse "vamos sem limite por enquanto": nunca Kanban sem limite, inclusive dentro do ciclo.
3. **Escreva o limite no topo de cada coluna de execução.** Fila (A fazer) e Feito não têm
 limite (ver erro do exemplo Norte-Sul "4·4·4").
4. **Escreva a regra da coluna cheia:** "coluna cheia, ninguém puxa; quem ficou sem trabalho
 ajuda a terminar o que está lá." É o "parar a linha" da Toyota.
5. **Leia os três sinais toda semana** (material de referência): coluna mais cheia · cartão mais velho ·
 vazão (cartões que saíram). Pergunta: "Onde a fila se forma? Há quantos dias o mais velho está ali?"
6. **Calibre na retrospectiva, nunca no meio do ciclo.** Gente ociosa → limite baixo demais.
 Cartões parados na etapa ou na fila antes dela → limite alto demais **ou** etapa invisível
 (crie a coluna, ex.: "Validação" do departamento X). Decisão do time, registrada com data e motivo.
7. **Contratar é a última saída**, e só depois de provar o gargalo. Criar agente ou contratar requer os critérios e a autoridade definidos pela organização; nunca só "para aliviar fila".

### Parte 2 — Política de urgência (cinco linhas, material de referência)

8. **O que é urgente aqui.** Pergunta: "O que conta como incêndio?" Escreva em uma linha.
 Modelo v6: "cliente parado, receita parada ou risco legal; o resto entra na fila".
9. **Quem pode chamar.** Uma pessoa só. "Urgência que qualquer um decreta deixa de ser urgência."
10. **Quantas cabem por vez.** Uma. A segunda espera a primeira terminar. Na prática, a carteira de iniciativas
 reserva **2 vagas** na raia de urgência (uma por área, porque
 as duas áreas têm donos diferentes; revisar na retro do primeiro mês).
11. **O que acontece com o pausado.** Ganha marca de pausa com motivo e data; volta na frente da
 fila quando a urgente sai. "Se alguém perguntar por que atrasou, você sabe".
12. **Onde fica escrito.** No alto do quadro, à vista. Recuse política em mensagem escrita ou chat.
13. **Escolha a mecânica:** cartão vermelho que pausa o item em curso **ou** raia inferior só
 para urgências (colunas iguais ou menos: fila → execução → feito). A raia permite contar.
 Na prática usa raia.
14. **Ligue o contador.** Por ciclo: quantas urgências entraram · o que tiraram do plano · quem foi
 avisado. Uma ou duas o ritmo absorve; metade do quadro em vermelho é sintoma → pauta da retro.

### Parte 3 — Classe Crítica

15. Neste modelo, toda demanda tem **classe de atendimento**: Crítica, Com prazo ou Normal. Crítica =
 "dano relevante acontecendo agora". O solicitante pode sugerir; quem valida e interrompe é o
 responsável pela área, uma política de incidente aprovada ou a Autoridade competente por Prioridade explícita.
16. Se a Crítica ultrapassar o WIP, **registre qual trabalho foi deslocado**. É o mesmo
 "cartão pausado com marca" da aula, com nome do modelo.
17. Pedido direto do responsável pela área entra na fila normal; só **Prioridade explícita** manda interromper,
 com o custo da troca registrado. Mensagem escrita com comando no escopo do remetente é executada e
 arquivada; não vira urgência por si.

### Parte 4: antes de abrir vaga

O bloco **"Antes de abrir vaga: redistribuir, mudar o processo ou desenvolver alguém resolve?"** vem antes de qualquer pedido de contratação. Serve a quem responde pela área, antes de abrir vaga ou mudar a estrutura, e a cada revisão trimestral. Conversa com a operação, o financeiro e a área de pessoas, conforme a decisão.

18. **Ache a etapa em que a fila se forma,** com os três sinais do passo 5: a coluna mais cheia, o cartão mais velho e quanto o time entrega por semana. Se faltarem dados, observe o trabalho antes de assumir um quadro definitivo.
19. **Pergunte, uma de cada vez:**
 - **Redistribuir:** há gente com folga em outra etapa? "Quem ficou sem trabalho ajuda a terminar o que está lá."
 - **Mudar o processo:** a espera é por aprovação, informação ou retrabalho, e não por falta de mãos? Cotações paradas à espera da assinatura de uma só pessoa se resolvem com um critério escrito, não com mais um comprador.
 - **Desenvolver alguém:** falta uma competência específica, embora a quantidade de horas pareça suficiente?
20. **Só então descreva o perfil necessário e o benefício esperado** da contratação, ligados a resultados e a uma capacidade que dá para verificar. Contratação depende de orçamento e de autoridade aprovados: leve a decisão a quem a tem.
21. **Revise o efeito da decisão** sobre entrega, carga e custo, e atualize a previsão quando a demanda mudar.

### Parte 5: canal oficial por tipo de pedido

Complementa a regra Entrada das políticas do quadro (seção 1.6 do `template.md`) e a política de urgência da Parte 2. Define onde os pedidos entram, onde as decisões ficam registradas e como o assunto urgente chega às pessoas, para que a equipe responda com previsibilidade. Dono: o gestor da equipe ou quem cuida da comunicação. Definição inicial de 30 a 45 minutos; revisão mensal ou quando houver falhas recorrentes. Escolher o aplicativo de mensagem em si fica fora desta habilidade.

22. **Liste os tipos de pedido e os canais que usam hoje** (conversa de corredor, mensagem, e-mail, ligação). Pergunta: "Por onde chegou o último pedido de cada tipo?"
23. **Defina um canal oficial de entrada por tipo de pedido** e onde a decisão fica registrada. A demanda entra pelo quadro.
24. **Combine o prazo de resposta** de cada canal, compatível com a operação. Recuse exigir disponibilidade contínua sem acordo. Funções de plantão ou de atendimento precisam de cobertura antes de limitar a consulta a mensagens.
25. **Ligue o caminho da urgência** às cinco linhas da Parte 2: quem pode chamar (uma pessoa), por qual canal e para quê.
26. **Escreva as regras ao lado do quadro.** Quando alguém pedir por outro caminho, aponte a regra e leve o pedido para o canal oficial.
27. **Teste o acordo em casos reais** e ajuste a comunicação aos solicitantes. Acompanhe pedidos perdidos, duplicados e urgências fora do critério.

## Regras do método que valem aqui

- Nunca Kanban sem limite de WIP, inclusive dentro do ciclo.
- O limite não acerta de primeira; calibre observando; ajuste é decisão do time, na retro.
- Coluna cheia: ninguém puxa; quem sobrou ajuda a terminar. Contratar é a última saída.
- "Pare de começar, comece a terminar."
- Política de urgência escrita antes, no alto do quadro: o que é, quem, quantas, pausado, onde.
- Conte as urgências por ciclo; muitas = causa a investigar.
- Urgência não elimina a definição de pronto.
- "Você nunca mais vai fazer Kanban sem limite de WIP."
- Antes de abrir vaga, pergunte se redistribuir, mudar o processo ou desenvolver alguém resolve.
- Cada tipo de pedido tem um canal oficial de entrada e um prazo de resposta combinado; o pedido que chega por outro caminho volta ao canal.

## Saída

Os nomes abaixo são sugestões de organização, não dependências de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Texto das políticas no topo do quadro da área (quadro Kanban na pasta do caso) ou da
 carteira de iniciativas (registro na pasta do caso, seção "Políticas do quadro").
- Registro de calibragem: histórico de limites na pasta do caso, uma linha
 por mudança: data · coluna · limite antigo → novo · sinal observado · quem decidiu.
- Contador de urgências do ciclo: campo no Retrospectiva na pasta do caso.
- Canal oficial por tipo de pedido: tabela com o canal de entrada, o registro da decisão, o prazo de resposta e o caminho da urgência, ao lado das políticas do quadro.
- Depois: retrospectiva (`ga2-plano-do-ciclo`, `ga2-review-do-ciclo` e `ga2-retrospectiva`) decide a calibragem; urgência demais vira A3.

## Formas de saída

Ao criar ou revisar um artefato, leia [entrega-editavel.md](entrega-editavel.md). O formato pedido e o documento existente orientam a entrega.
Padrão desta skill, sem formato definido: documento Word `.docx`; Google Docs quando esse for o destino escolhido.
Use ferramentas de arquivos ou a integração disponível para gerar e conferir a entrega real.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Os modelos abaixo atendem ao fluxo de geração de HTML e canvas quando essa for a entrega escolhida.

| Forma | Arquivo | Quando sai | Modelo |
|---|---|---|---|
| Fonte | `<nome>.md` (este `template.md` preenchido) | quando o fluxo precisar de fonte Markdown | `template.md` |
| Documento | `<nome>.html` — documento corrido no design system dos modelos públicos | quando HTML for escolhido | `../assets/modelos/documento.html` (pronto) |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-politicas-quadro-b-05.html` |

Modelos canvas desta skill (specs `politicas-quadro-b-05`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-politicas-quadro-b-05.html` **(padrão)** | Políticas do quadro (editável) · família b 05 | "no editável" | pronto |

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
resultado, quais **pessoas** participam (pelo nome), quais **agentes** executam, quem decide o bloqueio e quem confirma que serve. Pessoa e agente nunca na mesma linha: identifique explicitamente o tipo de participante. Sem nome na fonte, escreva "não definido" — nunca atribua tudo a uma única pessoa por suposição.

No fluxo Markdown → HTML, gere o HTML da fonte atual.
Em Word, Docs ou planilhas, siga a fonte e a conferência de [entrega-editavel.md](entrega-editavel.md).

## Adaptação

| Régua | WIP | Urgência |
|---|---|---|
| Leve (uma pessoa) | um número em Fazendo (começa em 2) | uma linha: "só eu chamo urgente; uma por vez; a pausada volta na frente" |
| Intermediária (área) | limite por coluna de execução + por pessoa; três sinais lidos na sexta | cinco linhas + raia ou cartão vermelho + contador |
| Robusta (carteira de iniciativas) | limite por dono (3) e por raia; registro de calibragem com data; gargalo no report ao responsável pela área | cinco linhas + raia com 2 vagas + classe Crítica + trabalho deslocado registrado |

## Erros comuns

- Limite em todas as colunas, inclusive fila e Feito (exemplo Norte-Sul "4·4·4").
- Subir o limite porque "cabe mais" — esconde a etapa que emperra.
- Mudar o limite no meio da semana, por pressão.
- Urgência sem dono que chama: vira "tudo urgente".
- Duas urgências ao mesmo tempo, sem pausar nada: o plano morre em silêncio.
- Pausar sem marca: três semanas depois ninguém sabe por que atrasou.
- Não contar: metade do quadro em vermelho e ninguém leva para a retro.
- Confundir pedido direto (fila normal) com Prioridade explícita (interrompe).
- Abrir vaga antes de testar se redistribuir, mudar o processo ou desenvolver alguém resolve.
- Vários canais oficiais para o mesmo tipo de pedido: pedidos duplicados e perdidos.
- Prazo de resposta que exige disponibilidade contínua, sem acordo nem cobertura.
