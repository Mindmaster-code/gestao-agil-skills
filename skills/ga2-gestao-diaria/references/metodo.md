# Gestão diária (reunião diária / Daily Scrum)

## O que é e quando usar

A gestão diária é a segunda das quatro conversas do ritmo (planejar → **diária** → revisar →
melhorar). É um alinhamento curto entre quem faz o trabalho, todo dia, no mesmo horário, em
frente ao quadro, para inspecionar o avanço rumo à meta do ciclo e planejar as próximas 24 h.
Não é prestação de contas ao chefe; no minuto em que vira isso, ela morre.

Entra antes: Plano do Ciclo com meta escrita e quadro com cartões nomeados. Sai depois: quadro
atualizado, impedimentos com dono para resolver fora da reunião, e o registro do dia. No laboratório
não há reunião em pé: a diária é a **leitura por pulso e correio** que o Gestor faz ao abrir a
sessão, e a saída é carta de cobrança quando um cartão está parado.

## Fonte no método

- Base do método: Passo 4 — Ritmo Ágil §2.8 (Daily Scrum), §3 regras 7, 8, 12, 22, §4.9 (campos — sem
  template de equipe), §5 (linha "Reunião diária"), §6 item 3 (diária entre agentes), §8 itens 11 e 16.
- Base do método: Passo 3 — Gestão Visual §5 (daily em frente ao quadro, da direita para a esquerda).
- Aulas: M06 A14 (Reunião Diária), A15 (cópia da A14, "Gestão Diária na Prática"), A09
  (atualizar o Kanban todo dia); v6 pasta 05 aula 04.
- Template: só individual — folha individual «gestao-diaria-ga2.pdf» (artefato 09: semana
  de · por dia SEG–SEX: o que avancei · foco de hoje · o que me trava). Equipe: sem template;
  os campos desta skill são construção do laboratório a partir de A14 e v6 aula 04.
- Acréscimo do laboratório: acompanhamento assíncrono de 10 min; registro diário e cobrança em seis linhas, descritos em `template.md`.

## Como conduzir

### A. Reunião diária de equipe (pessoas)

1. **Fixe o ritual uma vez:** horário, lugar (ou link), facilitador, quadro que será olhado,
   teto de 15 min. Pergunta: "A que horas, onde, em frente a qual quadro?" Recuse "quando der".
2. **Meta do ciclo no alto.** Leia em voz alta (30 s) para que todos lembrem o porquê (A14).
3. **Percorra o quadro da direita para a esquerda** (Passo 3 §5): primeiro o que está quase
   pronto, depois o que está no limite, depois o que avançou.
4. **Três perguntas por pessoa, apontando o cartão:** o que entreguei desde ontem · o que vou
   puxar hoje · o que me trava. Recuse narrar a agenda; fala do cartão, não do dia.
5. **Impedimento vira lista, não debate.** Anote: o quê · dono · até quando. Resolva depois,
   fora da diária, só com quem precisa (v6 aula 04). Recuse resolver ali ("vira 40 minutos").
6. **Mova os cartões durante a reunião** (A09: atualizar todo dia). Marque bloqueio e idade.
7. **Registre o tempo real.** 15 min é teto; 7 min é bom. Se passou, a reunião virou relatório
   ou debate — pauta da retro.
8. **Quem participa:** quem trabalha nos itens. SM e PO (quem cuida do processo e quem dá o
   rumo) podem assistir; o dirigente responsável recomenda que participem, a v6 diz que a reunião não é
   para eles. O laboratório: participam calados, salvo impedimento que só eles destravam.

### B. Diária entre agentes (pulso e correio) — o que o Gestor lê todo dia

9. **Caixa:** canal de mensagens combinado pelo time — mensagem nova = o que "chegou desde ontem".
10. **Quadro:** portfólio do caso — três perguntas só: cartão mais parado? sem dono? gate sem decisor? Recuse ler todas as linhas sem selecionar o que exige ação.
11. **Pulsos:** resumos diários, registros de demandas e documentos de acompanhamento das áreas atualizados nos últimos 7 dias. Use só para atualizar "Última prova" de cartão que mexeu.
12. **Cadência:** registros de reporte e pasta do ciclo atual. Arquivo que não existe = ritual que não aconteceu.
13. **Responda as três perguntas por cartão do ciclo:** avançou (prova nova)? puxa hoje (próximo
    passo escrito)? trava (gate, dependência, dias parado)?
14. **Dispare carta quando:** cartão parado ≥3 dias úteis sem prova nova · compromisso do plano
    perdeu a data (marque `atrasado dd/mm` no plano no mesmo dia) · gate sem decisor nomeado ·
    cartão sem dono (vai ao dirigente responsável, não ao dono). Uma cobrança por dia; o resto espera a varredura de quarta.
15. **Escreva o registro do dia** em 5 linhas (formato em `template.md`), salve e registre a versão; commit quando houver repositório.

## Regras do método que valem aqui

- 15 minutos é teto, não meta; mesmo horário, mesmo lugar, em frente ao quadro; fala do cartão,
  não da agenda. (A14, v6 04)
- Diária não é prestação de contas ao chefe; é alinhamento entre pares. (v6 04)
- Problema levantado se anota e se resolve depois, só com quem precisa. (A14, v6 04)
- Atualize o quadro todo dia, antes ou durante a diária. Atrasar cria situação falsa. (A09)
- Diária sem meta é status disfarçado. (v6 09)
- "Um dia parado é 20% do ciclo." (v6 04)
- Equipes sem diária têm reunião o dia inteiro. (A14)
- Acréscimo do laboratório: cartão parado ≥3 dias úteis → carta; ≥10 dias → escala ao dirigente responsável. (registro do portfólio na pasta do caso)

## Saída

Os nomes abaixo são sugestões de organização, não dependências de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Equipe: registro diário em registro da diária na pasta do caso (acréscimo do laboratório),
  uma seção por dia; impedimentos com dono e prazo.
- Gestor: status de 5 linhas na sessão (formato de registro diário descrito em `template.md`) e, quando houver,
  cobrança com data e destinatário no canal combinado.
- registro do portfólio na pasta do caso atualizado: "Última prova", "Dias parado", marca de bloqueio.
- Depois: impedimento que passa de 2 diárias seguidas vira pauta da retro; urgência detectada
  segue `ga2-politicas-wip-urgencia`.

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
| Documento | `<nome>.html` — documento corrido no design system do laboratório | quando HTML for escolhido | modelo de documento HTML desta variante ainda indisponível no pacote; os canvas abaixo continuam disponíveis |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-gestao-diaria-v6.html` |

Modelos canvas desta skill (specs `gestao-diaria-v6`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-gestao-diaria-v6.html` **(padrão)** | Gestão Diária (folha individual) · família v6 | "no canvas v6" | pronto |

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
| Leve | uma pessoa | grid individual artefato 09: avancei · foco de hoje · me trava. 5 min, mesmo horário. |
| Intermediária | um time | reunião de 15 min, 3 perguntas por pessoa apontando o cartão, lista de impedimentos com dono, quadro movido na hora |
| Robusta | time com acompanhamento assíncrono | leitura por pulso e correio (passos 9–15), uma carta por dia, registro de 5 linhas, escalada por dias parado |

## Erros comuns

- Virar relatório para o chefe: cada um "presta contas" e ninguém planeja as 24 h.
- Entrar no problema: a diária vira reunião de 40 min.
- Narrar a agenda inteira em vez de apontar o cartão.
- Diária sem meta no alto: status disfarçado.
- Atualizar o quadro em lote na sexta: situação falsa a semana toda (A09).
- Impedimento anotado sem dono nem data: some até a review.
- Agente: ler tudo (21 cartões, todos os pulsos) e não cobrar nada — "Kanban no limbo" do próprio Gestor.
- Agente: cobrar cinco cartões num dia; uma cobrança por dia, a melhor.
