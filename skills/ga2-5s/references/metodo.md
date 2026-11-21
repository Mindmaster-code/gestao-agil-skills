# 5S — método completo

## O que é e quando usar

5S são cinco palavras em japonês que começam com S. Cada uma é um senso de cuidado com o lugar
de trabalho:

| S | Japonês | Senso | Em uma frase |
|---|---|---|---|
| 1 | Seiri | Utilização | Só o necessário à mão; o resto sai da frente, guardado e catalogado. |
| 2 | Seiton | Organização | Um lugar para cada coisa, com nome, para achar de primeira. |
| 3 | Seiso | Limpeza | Limpar é inspecionar: tirar a sujeira e achar de onde ela vem. |
| 4 | Seiketsu | Padronização | Fazer os três primeiros todo dia, do mesmo jeito, por todos. |
| 5 | Shitsuke | Disciplina | Manter sem precisar de mutirão: rotina, dono e medida. |

Nasceu no chão de fábrica da Toyota: "das 500 ferramentas, o cara só usa 3". As três ficam à mão;
as outras 497 vão para um lugar catalogado, de onde se pega quando precisar. Vale para mesa
física e digital. "Os três primeiros S são coisas que a gente tem que fazer; o quarto e o quinto
são de comportamento."

O 5S é o último dos oito passos para começar no Lean, porque sustenta todos os outros: sem lugar
arrumado, o desperdício volta. Use quando procurar algo virou rotina; quando ninguém sabe qual é a
versão certa; quando um sistema, uma pasta ou uma lista cresceu sem dono; antes de entregar um
projeto a outra pessoa; no fim de um projeto ou de um ciclo; e, como rotina, todo dia em pequena dose.

**Entra:** um alvo nomeado pelo usuário. **Sai:** o alvo arrumado, a foto do antes e do depois, o
padrão de uma página e a rotina que mantém.

## O alvo é o parâmetro

O mesmo método serve para qualquer alvo: mesa, pasta, caixa de e-mail, agenda, backlog, planilha,
processo, repositório de código, estrutura de agentes de IA, campanhas de anúncio, funil comercial.
O que muda de um alvo para outro é só a tradução de cinco perguntas. A tradução dos alvos comuns
está em `alvos.md`:

1. O que é um **item** aqui?
2. Como se **prova que ele é usado**?
3. Onde fica o **lugar certo** de cada tipo de item?
4. Qual é a **sujeira** típica, e de onde ela costuma **vir**?
5. Qual **padrão** e qual **rotina** mantêm o alvo arrumado?

Para alvo que não está em `alvos.md`, responda as cinco perguntas antes de começar e mostre a
tradução ao usuário.

## Enquadramento (antes de tocar em qualquer coisa)

Escreva em poucas linhas:

- **Alvo e fronteira:** o que entra e o que fica de fora desta rodada.
- **Para que serve:** o trabalho que o alvo apoia. Utilidade é sempre utilidade para esse propósito.
- **Dono e usuários:** quem decide o destino dos itens e quem usa no dia a dia.
- **Risco:** sistema vivo (em produção, no ar, com dado de cliente ou com dinheiro) pede leitura do
 estado antes, menor mudança possível, conferência depois e caminho para desfazer. Em período
 crítico (dia de venda, campanha no ar, fechamento do mês), há **janela de congelamento**: o que
 mexe no que está rodando vai marcado "só depois de <data>".
- **Pronto quando:** o que fica mais fácil. Exemplo: "qualquer pessoa do time acha o contrato de um
 cliente em 30 segundos".

Alvo grande vira fatias. Comece pela fatia mais usada ou pela que mais dói, faça uma por rodada e
deixe a próxima marcada. Regra de 80/20: a parte pequena que todo mundo usa todo dia vale mais que
o arquivo morto inteiro.

## Os quatro modos

| Modo | Quando | O que faz | Mexe no alvo? |
|---|---|---|---|
| Diagnóstico | primeira vez, ou "como está isso?" | inventário, nota de 0 a 4 por S, os achados que mais pesam | não |
| Arrumação | depois do diagnóstico, com o sim do dono | os cinco S, com aprovação numa rodada só | sim, só o aprovado |
| Manutenção | na data da auditoria | refaz a nota, compara, trata só o que voltou | só o aprovado |
| Rotina | quando a arrumação já foi feita | escreve ou revisa padrão, rotina e vigia | não no conteúdo |

Sem modo definido: diagnóstico primeiro, depois ofereça a arrumação.

O diagnóstico sai curto: enquadramento, foto do antes, achados, fontes da sujeira (como hipótese) e
decisões do dono. Padrão e rotina entram só como proposta, e o "depois" fica para a arrumação.

## Foto do antes

1. **Inventário da fatia:** cada item com nome, tipo, onde está, quando foi usado ou alterado pela
 última vez, quem usa e quem aponta para ele. Em alvo digital, liste pelo próprio sistema; não
 confie na memória de ninguém.
 - **Alvo grande ou sistema com limite de consulta:** conte por tipo e por estado e meça uma
 amostra; item a item, só nos achados. Leia o que está ativo primeiro. O que ficou sem ler vira
 ponto em aberto, com a cobertura escrita ("700 de 843 lidos").
 - **Varredura automática erra.** Busca por nome acha o que não é e perde o que é. Toda contagem de
 varredura entra como **estimada** até alguém conferir uma amostra.
2. **Três medidas** que vão se repetir no fim:
 - **itens no total e itens à mão.** À mão é o que se usa sem procurar: a primeira tela, o primeiro
 nível, o que está no ar, o que o sistema carrega sozinho. `alvos.md` diz o que é em cada alvo.
 - **teste de achar:** três itens que o usuário mais procura (sem ele, os três padrão do alvo em
 `alvos.md`), sempre com um que fica no fundo. Meça o tempo; em sistema, conte comandos, chamadas
 ou cliques e diga a unidade. O ideal é medir com quem não arrumou.
 - **problemas abertos, por tipo:** quebrado ou com erro, duplicado, parado, fora do padrão, sem dono.
3. **Nota de 0 a 4 por S** (tabela abaixo), total de 0 a 20.
4. Quando ajudar, um registro visual do antes: foto da mesa, captura da pasta, árvore do repositório.

### Nota 5S

| Nota | O que significa (vale para cada S) |
|---|---|
| 0 | Nada feito. O problema é visível para quem chega. |
| 1 | Feito uma vez, num mutirão. Não há regra; já começou a voltar. |
| 2 | Feito, com lugar e critério definidos, mas depende de uma pessoa lembrar. |
| 3 | Padrão escrito e à vista; a rotina roda e alguém confere. |
| 4 | A rotina roda sozinha e é medida; a fonte da sujeira foi tratada; há guarda automática ou à prova de erro. |

O que olhar em cada S:

| S | Pergunta da nota |
|---|---|
| Utilização | O que está à mão é usado de fato? O que não é usado saiu, guardado e catalogado? |
| Organização | Cada tipo de item tem um lugar só, com nome previsível? Alguém de fora passa no teste de achar? |
| Limpeza | Há item quebrado, errado, duplicado ou desatualizado? As fontes de sujeira estão nomeadas e tratadas? |
| Padronização | O padrão existe em uma página, está onde se trabalha e todo mundo segue o mesmo? |
| Disciplina | A rotina tem dono, frequência e data? A nota é medida a cada auditoria? |

**Nota só com fato.** Cada nota cita o fato que a sustenta. Quando o S tem proporção que se mede
(itens fora do padrão, duplicados, parados), ancore a nota nela: até 5% fora vale 4; até 20%, 3; até
50%, 2; mais da metade, 1; sem regra nenhuma, 0. Sem como verificar (rotina que não se vê daqui, uso
sem contador), escreva "não verificado" ou marque a nota como provisória e diga onde procurou. Sem
prova de uso, a Utilização vai no máximo a 2.

A nota mede o alvo, nunca a pessoa. Use a mesma régua no antes e no depois.

**Achados:** liste os que mais pesam, de 3 a 10 (padrão 5; o pedido manda). Um achado pode ser um lote
("141 campanhas pausadas há mais de 90 dias"), com a contagem como prova.

## S1 — Utilização (Seiri)

**Objetivo:** só o necessário à mão. O resto sai da frente sem se perder.

Decida o destino de cada item pela **prova de uso**, não pela opinião de quem gosta dele. Prova de
uso é data de último acesso ou alteração, frequência, quem aponta para o item, quantas vezes rodou,
quanto gastou. A pergunta é: "isto serve ao propósito do alvo, e com que frequência?"

| Destino | Para quê | Critério típico |
|---|---|---|
| À mão | o que se usa todo dia ou toda semana | uso frequente comprovado |
| Guardado com catálogo | o que se usa raramente, mas precisa existir (as 497 ferramentas) | uso raro, obrigação legal, histórico que se consulta |
| Devolvido ao dono | o que é de outra pessoa, área ou projeto | dono identificado |
| Quarentena | dúvida: ninguém sabe se serve | sem prova de uso e sem dono claro |
| Descarte | sem uso, sem dono, sem obrigação de guardar, e com o sim do dono | só depois da quarentena, ou por pedido explícito |

**Etiqueta vermelha (quarentena).** Item duvidoso não vai direto para o lixo. Ele ganha uma etiqueta
vermelha e vai para uma área de quarentena (uma pasta, uma lista, um estado "pausado", uma prateleira)
com estes campos:

| Campo | Exemplo |
|---|---|
| Item | "Relatório semanal de visitas" |
| Por que está aqui | ninguém abriu desde março |
| Quem marcou e quando | Marcos, 04/05 |
| Prazo de decisão | 04/06 (de 2 a 6 semanas, conforme o risco) |
| Destino se ninguém reclamar | arquivar / descartar / devolver |

No prazo, quem sentiu falta pede de volta; o resto segue para o destino combinado, com o sim do dono.
Assim ninguém precisa decidir na hora, e nada importante some.

**Duplicatas e versões.** Quando há várias cópias, escolha uma fonte única e marque as outras como
cópia ou mande para a quarentena. Sempre com prova: compare data, tamanho ou conteúdo.

**Armadilhas:** jogar fora por impulso; guardar tudo "porque um dia pode servir" (estoque é
desperdício); decidir pelo dono; confundir "pouco usado" com "inútil" (as 497 ferramentas existem).

## S2 — Organização (Seiton)

**Objetivo:** um lugar para cada coisa e cada coisa no seu lugar, de modo que qualquer pessoa ache
de primeira.

1. **Defina os lugares** antes de mover: a estrutura (pastas, colunas, categorias, prateleiras,
 etiquetas) que espelha o jeito como o trabalho acontece, não o jeito como as coisas foram chegando.
2. **Um lugar só por tipo de item.** Dois lugares possíveis viram dois lugares usados.
3. **O mais usado mais perto:** no topo, na primeira tela, no primeiro nível, ao alcance da mão.
 Poucos níveis: se precisa de mais de três ou quatro cliques para chegar, a estrutura está funda.
4. **Nome previsível:** um padrão de nome que diga o que é sem abrir (data no formato ano-mês-dia,
 assunto, versão). Rótulo visível no físico; nome e descrição no digital.
5. **Mova preservando a identidade:** no digital, mover não é copiar. Copiar cria duplicata e quebra
 os links. Antes de mover, veja quem aponta para o item. O que é lido por um caminho fixo (uma
 automação, uma fórmula, um atalho) fica onde está ou muda junto com quem o lê.
6. **Teste de achar:** peça a alguém que não arrumou para achar os mesmos três itens da foto do antes.
 Se demorar, o lugar ou o nome ainda não é óbvio.

**Armadilhas:** estrutura bonita que ninguém entende; categoria "Diversos" ou "Outros" (vira o novo
lixo); reorganizar o que é de outra pessoa; copiar em vez de mover.

## S3 — Limpeza (Seiso)

**Objetivo:** o lugar fica limpo e passa a avisar quando algo dá errado. Limpar é inspecionar.

1. **Limpe:** corrija ou retire o que está quebrado, errado ou desatualizado. Link morto, versão velha,
 automação que falha, cartão parado há meses, dado inconsistente, poeira e lixo.
2. **Inspecione enquanto limpa:** cada sujeira é um sinal. Anote o que achou, mesmo o que não deu para
 resolver agora.
3. **Ache a fonte da sujeira.** Para cada tipo de sujeira que se repete, pergunte "de onde isto vem?"
 até chegar a um hábito, um processo ou uma ferramenta. Limpar sem tratar a fonte é marcar o próximo
 mutirão.

| Sujeira | Pergunta | Fonte típica | Contramedida na fonte |
|---|---|---|---|
| arquivo solto na raiz | quem salva ali e por quê? | o programa salva no lugar padrão | mudar o destino padrão; modelo de pasta |
| cópias da mesma coisa | por que alguém copiou em vez de abrir? | não achou o original | fonte única com link fixo |
| item sem dono | quem criou? | ninguém registra o dono ao criar | campo de dono obrigatório |
| nome fora do padrão | o padrão estava à vista? | padrão só na cabeça de alguém | modelo de nome e validação |

4. **Confira a guarda que já existe.** Se havia uma regra automática, um prazo no nome, uma validação
 ou um aviso que devia ter pego a sujeira, ver por que ele falhou vale mais que limpar. Guarda que
 existe e não funcionou é achado de primeira linha.
5. Quando a fonte não é óbvia ou atravessa áreas, abra uma análise de causa raiz (`ga2-causa-raiz`).
6. Prefira contramedidas **à prova de erro** (poka-yoke): o jeito certo vira o caminho mais fácil e o
 errado fica difícil ou impossível. Um modelo pronto, um destino padrão, uma validação que recusa o
 nome errado valem mais que um aviso pedindo cuidado.

**Armadilhas:** limpar só o que aparece; tratar a sujeira como culpa de alguém; resolver na hora o que
pede decisão do dono.

## S4 — Padronização (Seiketsu)

**Objetivo:** fazer os três primeiros S todo dia, do mesmo jeito, por todos.

Escreva o **padrão em uma página**, onde o trabalho acontece (no topo da pasta, no quadro, no
arquivo de instruções do repositório, na parede):

1. Para que serve o alvo e quem é o dono.
2. Onde fica cada tipo de item (o mapa dos lugares).
3. Como dar nome.
4. O que não fica aqui e para onde vai.
5. Quando e como se faz a manutenção.

Torne o padrão **visível e fácil de seguir**: modelo pronto para criar coisa nova, nome sugerido,
cores ou etiquetas, lugar de "entrada" para o que ainda não foi classificado. Quando der, transforme
regra em **guarda automática**: o modelo já nasce no padrão, a validação recusa o que sai dele, a
automação avisa o desvio. Padrão que depende só de memória não se sustenta.

Se o padrão virar procedimento com passos, use `ga2-pop`.

**Armadilhas:** padrão longo que ninguém lê; padrão escondido num documento à parte; um padrão
para cada pessoa.

## S5 — Disciplina (Shitsuke)

**Objetivo:** o alvo continua arrumado sem precisar de outro mutirão.

Combine a **rotina** em doses pequenas, com dono e frequência:

| Frequência | Dose | O que fazer |
|---|---|---|
| Diária | 5 minutos no fim do dia | o que entrou vai para o lugar; nada novo fica na área de entrada |
| Semanal | 15 a 20 minutos | quarentena vencida decide destino; duplicatas novas; nomes fora do padrão |
| Mensal | 20 a 40 minutos | auditoria com a mesma nota; poda do que perdeu sentido |
| Por evento | fim de projeto, ciclo ou campanha; entrada ou saída de pessoa | arrumação da fatia afetada antes de seguir |

Encaixe a rotina na agenda real (`ga2-sistema-de-rotinas`). Na auditoria, use a mesma nota de 0 a 4
e as mesmas três medidas; a tendência da nota diz se o 5S está vivo. A liderança dá o exemplo: vai ao
lugar (`ga2-gemba-walk`), olha a nota e reconhece quem mantém. A melhoria que sai da auditoria pode ir
para o `ga2-quadro-kaizen`.

**Vigia para alvo digital.** Quando o alvo é um sistema, uma rotina automática pode conferir o
padrão no lugar das pessoas:

- só lê e avisa; quem arruma é uma pessoa, com o sim do dono;
- avisa só o que é novo, uma vez, no canal de resumo que o dono já lê;
- lembra de tempos em tempos o que segue aberto, sem repetir todo dia;
- cala sobre o que o dono decidiu deixar como está (lista de exceções com motivo e data);
- avisa quando ele próprio para de funcionar.

**Armadilhas:** rotina grande demais para caber na semana; auditoria que vira cobrança de pessoa;
padrão que ninguém revisa quando o trabalho muda.

## Nome técnico do sistema

Ramo, versão guardada, conjunto de anúncios, automação agendada: quando o sistema tem nome próprio
para o item, use esse nome, com uma explicação curta na primeira vez. Traduzir o rótulo que a pessoa
vê na tela atrapalha mais do que ajuda.

## A decisão do dono numa rodada só

Depois do enquadramento e da foto do antes, junte tudo o que depende do dono e leve de uma vez:

- a tabela **item → de onde → para onde → por quê**;
- o que vai para a quarentena, com prazo, e o que vai para o descarte;
- o que fica no lugar de propósito e por quê (por exemplo, é lido por uma automação);
- o padrão proposto e a rotina.

Cada pergunta precisa se explicar sozinha. Aplique só o aprovado. Mova, não copie. Depois, refaça a
foto e compare.

## O 5S e os 7 desperdícios

Cada achado do 5S costuma esconder um dos sete desperdícios. Marcar o desperdício ajuda a explicar
por que vale arrumar:

| Achado | Desperdício |
|---|---|
| procurar o que deveria estar à mão | movimentação |
| esperar alguém dizer onde está ou qual é a versão certa | espera |
| relatório, ferramenta ou cópia que ninguém usa | inventário (estoque) |
| fazer de novo porque não achou o que já existia | produção excessiva |
| passos a mais para chegar ao que se usa todo dia | processamento excessivo |
| usar a versão errada, o dado velho, a automação quebrada | defeito |
| levar coisa de um lugar para outro sem necessidade | transporte |

## Erros comuns

- Mutirão sem padrão nem rotina: em um mês volta tudo.
- Começar pelo arquivo morto em vez da parte que se usa todo dia.
- Descartar sem quarentena e sem o sim do dono.
- Copiar em vez de mover e criar duplicata nova.
- Mover o que uma automação lê por caminho fixo e quebrá-la.
- Arrumar o que é de outra pessoa ou área.
- Nota que vira avaliação de pessoa.
- Limpar o sintoma e deixar a fonte da sujeira ligada.
