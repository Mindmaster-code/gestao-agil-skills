# Gestão diária (reunião diária / Daily Scrum)

## O que é e quando usar

A gestão diária é a segunda das quatro conversas do ritmo (planejar → **diária** → revisar →
melhorar). É um alinhamento curto entre quem faz o trabalho, todo dia, no mesmo horário, em
frente ao quadro, para inspecionar o avanço rumo à meta do ciclo e planejar as próximas 24 h.
Não é prestação de contas ao chefe; no minuto em que vira isso, ela morre.

Entra antes: Plano do Ciclo com meta escrita e quadro com cartões nomeados. Sai depois: quadro
atualizado, impedimentos com dono para resolver fora da reunião, e o registro do dia. No acréscimo do método
(diária entre agentes) não há reunião em pé: a diária é a **leitura dos resumos e da caixa de mensagens** que quem conduz o método faz ao abrir a
sessão, e a saída é cobrança por escrito, com data, quando um cartão está parado.

## Fonte no método

- Base do método: Passo 4 — Ritmo Ágil §2.8 (Daily Scrum), §3 regras 7, 8, 12, 22, §4.9 (campos — sem
  template de equipe), §5 (linha "Reunião diária"), §6 item 3 (diária entre agentes), §8 itens 11 e 16.
- Base do método: Passo 3 — Gestão Visual §5 (daily em frente ao quadro, da direita para a esquerda).
- Aulas: M06 A14 (Reunião Diária), A15 (cópia da A14, "Gestão Diária na Prática"), A09
  (atualizar o Kanban todo dia); v6 pasta 05 aula 04.
- Template: só individual — folha individual «gestao-diaria-ga2.pdf» (artefato 09: semana
  de · por dia SEG–SEX: o que avancei · foco de hoje · o que me trava). Equipe: sem template;
  os campos desta skill são construção deste pacote a partir de A14 e v6 aula 04.
- Acréscimo do método: acompanhamento assíncrono de 10 min; registro diário e cobrança em seis linhas, descritos em `template.md`.
- Fichas F05 (preparar o próximo dia de trabalho) e F06 (fechar o expediente e atualizar os acordos) do Guia completo de rotinas de gestão, para o modo pessoal (passos 16 a 26) `(adaptação metodológica)`.

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
   rumo) podem assistir; o responsável pela área recomenda que participem, a v6 diz que a reunião não é
   para eles. No acréscimo do método: participam calados, salvo impedimento que só eles destravam.

### B. Diária entre agentes (resumos e caixa de mensagens) — o que quem conduz o método lê todo dia

9. **Caixa:** canal de mensagens combinado pelo time — mensagem nova = o que "chegou desde ontem".
10. **Quadro:** carteira de iniciativas do caso — três perguntas só: cartão mais parado? sem dono? gate sem decisor? Recuse ler todas as linhas sem selecionar o que exige ação.
11. **Acompanhamento:** resumos diários, registros de demandas e documentos de acompanhamento das áreas atualizados nos últimos 7 dias. Use só para atualizar "Última prova" de cartão que mexeu.
12. **Cadência:** registros de reporte e pasta do ciclo atual. Arquivo que não existe = ritual que não aconteceu.
13. **Responda as três perguntas por cartão do ciclo:** avançou (prova nova)? puxa hoje (próximo
    passo escrito)? trava (gate, dependência, dias parado)?
14. **Dispare cobrança por escrito quando:** cartão parado ≥3 dias úteis sem prova nova · compromisso do plano
    perdeu a data (marque `atrasado dd/mm` no plano no mesmo dia) · gate sem decisor nomeado ·
    cartão sem dono (vai ao responsável pela área, não ao dono). Uma cobrança por dia; o resto espera a varredura de quarta.
15. **Escreva o registro do dia** em 5 linhas (formato em `template.md`), salve e registre a versão; commit quando houver repositório.

### C. Modo pessoal (fechar o expediente e preparar o próximo dia)

Serve a uma pessoa que organiza o próprio dia, sem reunião. São dois momentos curtos que se encaixam: o fechamento deixa o dia seguinte quase pronto, e o preparo o confirma. Cada pessoa usa o quadro e a agenda que já tem. O modo alimenta a diária do time e não a substitui. Você prepara os rascunhos de aviso e de retorno; quem envia é a pessoa. O roteiro pode ser conduzido no chat: gere arquivo só se a pessoa pedir ou quiser guardar o registro. Fonte: fichas F05 e F06 do Guia completo de rotinas de gestão `(adaptação metodológica)`; a regra do quadro em dia é da aula A09.

**Fechar o expediente (5 a 15 minutos, ao fim do expediente)**

16. **Atualize o estado das entregas no quadro:** mova o que avançou, marque o que travou e escreva o que ainda falta. Quadro em dia, todo dia, antes da diária.
17. **Prepare os retornos necessários** sobre compromissos ou riscos de prazo, para a pessoa enviar. Fato, efeito e data nova, e o nome de quem dará o próximo retorno.
18. **Capture o que ficou sem destino:** assuntos que surgiram e ainda não têm dono, data nem cartão. Cada um ganha um destino (cartão, outra pessoa ou lista) ou é descartado.
19. **Deixe a prioridade de amanhã e o primeiro passo escritos.** É o preparo do dia seguinte; feito aqui, os passos 22 e 23 viram só uma conferência.
20. **Encerre os recursos e deixe o ambiente pronto,** conforme a necessidade do trabalho. Havendo ocorrência urgente em andamento, combine a passagem de responsabilidade antes de encerrar. Não prolongue o fechamento com tarefas novas sem prioridade.

**Preparar o próximo dia (5 a 10 minutos, ao fim do expediente anterior ou no início do dia)**

21. **Confira os compromissos do dia seguinte** e o preparo que cada um pede. Pergunta: "Que horas, com quem, e o que preciso ter em mãos?"
22. **Escolha a entrega prioritária que dá para fazer com a capacidade do dia.** O foco do dia tem de 1 a 3 coisas, com a prioridade em primeiro lugar. Recuse lista diária maior que a capacidade.
23. **Defina o primeiro passo e os materiais.** O primeiro passo é uma ação que dá para começar sem reorganizar o trabalho, como abrir o arquivo na versão certa e deixar os dados à mão.
24. **Identifique as dependências** que precisam ser resolvidas antes: o que alguém tem de confirmar e o que depende de outra pessoa. Deixe pronto o aviso a essas pessoas, para ser enviado ainda hoje.
25. **Reserve o período de execução** e ajuste as expectativas quando necessário. Com trabalho imprevisível, mantenha a prioridade e uma alternativa de execução.
26. **No dia seguinte, observe** se a prioridade avançou, o que alterou o plano e se algo foi esquecido. Use isso para melhorar a confiabilidade do registro e a previsão.

Como o modo se liga ao resto: na folha individual (artefato 09), o fechamento preenche "O que avancei" e "O que me trava", e o preparo preenche "Foco de hoje". Na diária do time, o fechamento responde "entreguei desde ontem" e "me trava", e o preparo responde "puxo hoje".

## Regras do método que valem aqui

- 15 minutos é teto, não meta; mesmo horário, mesmo lugar, em frente ao quadro; fala do cartão,
  não da agenda. (A14, v6 04)
- Diária não é prestação de contas ao chefe; é alinhamento entre pares. (v6 04)
- Problema levantado se anota e se resolve depois, só com quem precisa. (A14, v6 04)
- Atualize o quadro todo dia, antes ou durante a diária. Atrasar cria situação falsa. (A09)
- Diária sem meta é status disfarçado. (v6 09)
- "Um dia parado é 20% do ciclo." (v6 04)
- Equipes sem diária têm reunião o dia inteiro. (A14)
- Acréscimo do método: cartão parado ≥3 dias úteis → cobrança por escrito; ≥10 dias → escala ao responsável pela área. (registro da carteira de iniciativas na pasta do caso)

## Saída

Os nomes abaixo são sugestões de organização, não dependências de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Equipe: registro diário em registro da diária na pasta do caso (acréscimo do método),
  uma seção por dia; impedimentos com dono e prazo.
- Quem conduz o método: status de 5 linhas na sessão (formato de registro diário descrito em `template.md`) e, quando houver,
  cobrança com data e destinatário no canal combinado.
- registro da carteira de iniciativas na pasta do caso atualizado: "Última prova", "Dias parado", marca de bloqueio.
- Pessoa (modo pessoal): fechamento do expediente (estado das entregas, retornos enviados, assuntos com destino) e preparo do dia seguinte (prioridade, primeiro passo, dependências), no registro que ela já usa; o quadro em dia.
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
| Documento | `<nome>.html` — documento corrido no design system dos modelos públicos | quando HTML for escolhido | modelo de documento HTML desta variante ainda indisponível no pacote; os canvas abaixo continuam disponíveis |
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
| Robusta | time com acompanhamento assíncrono | leitura dos resumos e da caixa de mensagens (passos 9–15), uma cobrança por escrito por dia, registro de 5 linhas, escalada por dias parado |
| Pessoal | uma pessoa que quer fechar e preparar o próprio dia, sem reunião | a folha da régua Leve, mais o fechamento (5 a 15 minutos) e o preparo (5 a 10 minutos) de cada dia, passos 16 a 26 |

## Erros comuns

- Virar relatório para o chefe: cada um "presta contas" e ninguém planeja as 24 h.
- Entrar no problema: a diária vira reunião de 40 min.
- Narrar a agenda inteira em vez de apontar o cartão.
- Diária sem meta no alto: status disfarçado.
- Atualizar o quadro em lote na sexta: situação falsa a semana toda (A09).
- Impedimento anotado sem dono nem data: some até a review.
- Agente: ler tudo (21 cartões, todos os resumos) e não cobrar nada — "Kanban no limbo" de quem conduz o método.
- Agente: cobrar cinco cartões num dia; uma cobrança por dia, a melhor.
- Modo pessoal: fechar o expediente sem atualizar o quadro; o atraso só aparece na diária.
- Modo pessoal: lista do dia maior que a capacidade, sem prioridade nem primeiro passo.
- Modo pessoal: deixar um compromisso em risco sem avisar quem espera o retorno.
- Modo pessoal: prolongar o fechamento com tarefas novas, até o expediente não acabar.
