# Kanban Canvas

## O que é e quando usar

Kanban (japonês: cartão visual, sinal) é um método de gestão visual de processos: o trabalho
vira cartão, o fluxo vira colunas, e cada coluna tem teto de cartões. É o Passo 3 do método
(Colocando Gestão Visual). Entra depois do Backlog 2D (o cartão nasce da **tarefa** do mapa, não
da iniciativa) e antes do Ritmo (o quadro é o que a diária, a review e a retro olham).

Cadeia: contramedida do A3 → iniciativa do OKR → entrega do Backlog 2D → tarefa → **cartão**.

Três produtos desta skill: (1) o **Kanban Canvas completo** de uma frente ou área; (2) o
**quadro mínimo** de 3 colunas (v6, artefato 07) para caso pequeno; (3) o **Kanban de
portfólio** do laboratório, que é registro do portfólio na pasta do caso.

## Fonte no método

- Base do método: Passo 3 — Gestão Visual §2.10–2.20 (Kanban, cinco passos, não dá ré, três erros, raias),
  §4.3–4.9 (artefatos), §6.1 (Kanban de portfólio do laboratório), §8 item 4 (bloqueio).
- Aulas: M05 A07 (Kanban, professor), A08 (Kanban Canvas), A09–A13 (fluxo, quadro vivo,
  hierarquia), A14 (tipos de demanda e raias), A17 (cartão e WIP no Trello); v6 pasta 04 aulas
  03 (Kanban mínimo), 04 (montar o quadro do caso), 05 (políticas).
- Templates: folha individual «kanban-canvas-ga2.pdf» (artefato 07, v6) e
  `kanban-quadro-imprimir-ga2.pdf`; «Mod 03 — Kanban Mínimo GA2 Editável»;
  legado «M10 — Kanban Canvas» (A08) e `Canvas Kanban Avançado.pdf` (7.1).
- Modelo operacional do laboratório: modelo operacional de demandas (acréscimo do laboratório, com regras incorporadas nesta referência) §7–8
  (estados comuns, condições, Kanbans hierárquicos).

## Como conduzir

1. **Nomeie o quadro e o dono.** Pergunta: "Qual caso este quadro mostra? Quem atualiza?"
   Escreva nome, dono e onde vai morar. Recuse quadro sem dono de atualização (vira "Kanban no limbo").
2. **Desenhe o fluxo atual, não o ideal.** Pergunta: "Como a demanda chega hoje? Por onde passa
   até alguém receber?" Escreva as colunas na ordem. Recuse copiar "a fazer / fazendo / feito"
   sem olhar o fluxo real (Kanban melancia). Toda equipe tem pelo menos fila, fazendo e pronto.
3. **Separe tipos de demanda em raias.** Pergunta: "Que tipos de trabalho entram? Têm caminhos
   diferentes?" Mais de um tipo = raias horizontais, não quadros soltos. Colunas comuns
   (Feito) são compartilhadas. No laboratório: `Empresa A · Empresa B · Compartilhado · Processo interno`.
4. **Fixe o cartão padrão.** Campos: origem (etiqueta do OKR/entrega), o que é numa frase,
   dono (nome de pessoa, nunca área), prazo, idade em dias, checklist de pronto, marca de
   bloqueio, prova. Recuse cartão maior que uma semana ("quando fica pronto?" sem resposta = quebra no mapa).
5. **Ponha o limite de trabalho em andamento (WIP)** no topo de cada coluna de execução.
   Ponto de partida: conte o que está em andamento hoje e tire um. Detalhe em `ga2-politicas-wip-urgencia`.
6. **Escreva as políticas no próprio quadro**: entrada, pronto, prioridade, bloqueio,
   atualização. Mínimo das três da v6: feito, limite, ritmo de revisão.
7. **Escolha a representação de bloqueio** (ver seção abaixo) e escreva: "bloqueado há mais de N
   dias sobe para quem".
8. **Combine o ritmo de atualização**: quem move, quando, e a revisão semanal fixa (dia, hora, 15 min).
9. **Monte** onde o time já abre todo dia, em formato escolhido com o usuário. O quadro deve caber na tela usada pelo time. Use uma ferramenta de quadro quando o usuário pedir interação por ela.
10. **Teste de bem feito:** alguém decide sem perguntar; as três políticas estão no quadro;
    cada cartão tem dono, idade e prova.

## Bloqueio — três representações, uma escolhida

O acervo tem três jeitos de mostrar cartão travado (Base do método: Passo 3 — Gestão Visual §8.4):

| Representação | Onde aparece | Como funciona |
|---|---|---|
| A. Marca no cartão, coluna mantida | M05 A07 (professor: "Kanban não dá ré"), Trello A17 | cartão fica onde estava, sinalizado em vermelho; métricas de tempo na coluna continuam válidas |
| B. Coluna "Bloqueados" | template GA 2.0 `04-quadro-de-execucao` | cartão sai do fluxo para uma coluna própria, com "o que travou e quem destrava" |
| C. Área "Impedimentos" separada | Canvas 7/7.1 e M05 A13 | o impedimento vira post-it numa área fora do fluxo; o cartão não se move |

**O laboratório adota A**, por três motivos: é a única compatível com "Kanban não dá ré" (regra 13);
o modelo operacional aprovado diz que "Bloqueada, Gate pendente e Apta para integração são
condições, não colunas" (§7–8); e preserva a medida de dias parado por coluna. O cartão ganha a
marca na coluna "Gate / trava" do portfólio, com motivo, decisor e data do pedido.
A escolha da representação nos materiais do curso permanece uma divergência editorial; esta referência explicita a opção A do laboratório e preserva as três origens.

## Regras do método que valem aqui

- Desenhe o fluxo **atual**, com o time; não copie modelo da internet. (A07, v6 04)
- Quadro mínimo: a fazer, fazendo, feito — e não pare nele. (A07, A12)
- Defina "pronto" por escrito antes de usar a coluna Feito. (A07, v6 05)
- Puxe, não empurre: só começa quando termina o anterior. (A07, A12)
- Kanban não dá ré: cartão travado fica parado e sinalizado, nunca volta. (A07)
- Políticas escritas no próprio quadro, onde valem. (A11, v6 05)
- Mais de um tipo de demanda = raias, não quadros soltos. (A14)
- Cartão do tamanho de uma semana; vem do Backlog 2D, não se inventa no quadro. (v6 04)
- Um quadro por contexto; quadros se conversam em hierarquia (portfólio → área → projeto → pessoa). (A11)
- "Um quadro que mente é pior que quadro nenhum." (v6 05)

## Saída

Os nomes abaixo são sugestões de organização, não dependências de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Quadro de uma frente ou área: quadro Kanban na pasta do caso (acréscimo do laboratório:
  a aula não fixa caminho). Nome: `<area>-kanban.md`, ex.: `delivery-kanban.md`.
- Kanban de portfólio do laboratório: registro do portfólio na pasta do caso (já existe; esta skill é quem o mantém).
- Cartão novo no portfólio entra com as 6 linhas do padrão de comunicação
  (registro de demanda em seis linhas — o que, por que, dono, pronto é, prazo, onde trava (acréscimo do laboratório) §1).
- Depois: políticas de WIP e urgência (`ga2-politicas-wip-urgencia`), plano do ciclo
  (`ga2-plano-do-ciclo`), diária (`ga2-gestao-diaria`).

## Formas de saída

Ao criar ou revisar um artefato, leia [entrega-editavel.md](entrega-editavel.md). O formato pedido e o documento existente orientam a entrega.
Padrão desta skill, sem formato definido: documento Word `.docx`; Google Docs quando esse for o destino escolhido. PDF serve para leitura; HTML apenas para visualização solicitada.
Use ferramentas de arquivos ou a integração disponível para gerar e conferir a entrega real.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Os modelos abaixo atendem ao fluxo de geração de HTML e canvas quando essa for a entrega escolhida.

| Forma | Arquivo | Quando sai | Modelo |
|---|---|---|---|
| Fonte | `<nome>.md` (este `template.md` preenchido) | quando o fluxo precisar de fonte Markdown | `template.md` |
| Documento | `<nome>.html` — documento corrido no design system do laboratório | quando HTML for escolhido | modelo de documento HTML desta variante ainda indisponível no pacote; os canvas abaixo continuam disponíveis |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-kanban-kit-07.html` |

Modelos canvas desta skill (specs `kanban-kit-07`, `kanban-avancado-kit-7-1`, `kanban-politicas-kit-7-2`, `kanban-canvas-v6`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-kanban-kit-07.html` **(padrão)** | Kanban | Quadro de Acompanhamento Simples · família kit 7 | "no canvas do kit" | pronto |
| `../assets/modelos/canvas-kanban-avancado-kit-7-1.html` | Kanban | Quadro de Acompanhamento Avançado · família kit 7.1 | "no canvas do kit" | pronto |
| `../assets/modelos/canvas-kanban-politicas-kit-7-2.html` | Políticas do Kanban | "Combinados" da Equipe · família kit 7.2 | "no canvas do kit" | pronto |
| `../assets/modelos/canvas-kanban-canvas-v6.html` | Kanban Canvas (jornada v6) · família v6 | "no canvas v6" | pronto |

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
| Leve | uma pessoa, um caso, fila curta | quadro mínimo v6: 3 colunas, limite em Fazendo, "feito" escrito, revisão semanal de 15 min. Sem raias. |
| Intermediária | uma área, 2–5 tipos de demanda | colunas do fluxo real, raias por tipo, cartão padrão completo, 5 políticas, marca de bloqueio |
| Robusta | portfólio de várias áreas | tudo acima + hierarquia de quadros, estados comuns do modelo operacional, dias parado e gate medidos, report semanal |

Corte o que não tem dono de atualização. Coluna que ninguém move não existe.

## Erros comuns

- **Kanban melancia:** a fazer/fazendo/feito genérico, nunca adaptado ao fluxo real.
- **Kanban no limbo:** ninguém atualiza; "está lá só para tirar foto".
- **Kanban congestionado:** sem limite; tudo em andamento.
- Cartão com nome de área ("Marketing") em vez de pessoa.
- Mover cartão para trás quando trava — estraga a métrica.
- Política num documento que ninguém abre, em vez de no quadro.
- Cartão de iniciativa inteira (seis semanas) em vez de tarefa de uma semana.
- Quadro com 14 colunas para impressionar; o dirigente responsável lê no celular.
