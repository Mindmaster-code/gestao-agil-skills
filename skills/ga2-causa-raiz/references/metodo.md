# Causa raiz — 5 Porquês e Ishikawa

## O que é e quando usar

Causa raiz é o que deu origem ao problema, não o sintoma que grita. A skill preenche o
campo 5 do A3 ("Causa raiz — por que o problema acontece") com duas ferramentas: **5
Porquês** (uma cadeia, sempre sobre a resposta anterior, até uma causa de sistema) e
**Ishikawa** (problema com várias causas ao mesmo tempo, organizadas nas categorias 6M, com
5 Porquês em cada ramo que importa). Pareto decide qual ramo atacar primeiro.

Entra: o lado esquerdo do A3 com gap quantificado (`ga2-diagnostico`). Sai: a causa de
sistema provada, escrita como processo ou regra — nunca nome de pessoa — e a causa
prioritária. Cadeia: **Diagnóstico → Causa raiz → Contramedidas (A3 direito).**

Nesta adaptação, o relatório de incidente registra os cinco níveis e a regra proposta a partir da causa de sistema. Sem evidência suficiente, registre hipóteses e o teste necessário; não declare a causa provada.

## Fonte no método

- Passo 1 — Entender o Contexto: 5 Porquês e exemplo do farol (M03 A05); três ferramentas (M03 A07); cinco níveis e armadilhas (v6 aula 04).
- Passo 0 — Fundamentos: regra “métrica que cai vira A3, nunca cobrança”.
- Template oficial: Artefato 06 — “Causa raiz — 5 Porquês GA2 editável”: Problema observado · 5 Porquês · Evidências · Causa prioritária.
- v6 aula 04 — “Causa Raiz 5 Porquês”.
- Ishikawa e Pareto não têm template oficial nas fontes citadas. Os blocos desta skill são adaptações metodológicas identificadas como tal.
## Como conduzir

1. **Escreva o problema observado** em uma frase, com o número do lado esquerdo. Recuse problema sem fato ("a fila está grande" → "120 chamados abertos, resposta em 72h").
2. **Escolha a ferramenta.** Pergunta: "Há uma cadeia ou várias causas ao mesmo tempo?" Uma cadeia → 5 Porquês. Várias → Ishikawa, depois 5 Porquês nos ramos que importam. Se há contagem de ocorrências, Pareto ordena.
3. **Por quê 1 — causa imediata.** Pergunta: "Por que isso acontece?" E em seguida: **"Como você sabe que isso é verdade?"** Escreva a resposta e a evidência (log, arquivo, número, observação). Recuse resposta sem evidência.
4. **Por quês 2 a 5.** Cada pergunta é sobre a **resposta anterior**: causa do processo → causa da rotina → causa da regra → causa do sistema. Recuse pular nível e recuse voltar ao sintoma.
5. **Teste de pessoa.** Pergunta: "A causa que você escreveu é processo ou regra, ou é o nome de alguém?" "Fulano errou" encerra a investigação. Reescreva como "não existe X que impeça Y".
6. **Teste de retorno.** Pergunta: "Se corrigir só isso, o problema volta?" Se volta, ainda é sintoma — continue.
7. **Teste de controle.** Pergunta: "O dono controla essa causa?" Pare no nível mais profundo que o dono ainda controla; o nível acima vai como "depende de" (gate, verba, decisão).
8. **Ishikawa, se precisar.** Cabeça do peixe = problema. Uma espinha por categoria 6M (método, mão de obra, máquina, material, medição, meio ambiente). Brainstorm por categoria; depois 5 Porquês no ramo mais frequente ou de maior impacto. Recuse Ishikawa sem escolher ramo.
9. **Causa prioritária.** Pergunta: "Qual atacar primeiro — a mais frequente, a de maior impacto ou a acionável agora?" Escreva qual e por quê. Pode haver mais de uma causa; só uma é prioritária.
10. Leve a causa prioritária para o campo 5 do A3 e siga para `ga2-relatorio-a3`.

## Regras do método que valem aqui

- **Pergunte por quê pelo menos cinco vezes**, sempre sobre a resposta anterior, até uma causa de sistema. Parar cedo = tratar sintoma. (M03 A05, A07; v6 aula 04)
- **Cada porquê precisa de evidência** — Genchi Genbutsu: "como eu sei que isso é verdade?" (v6 aula 04)
- **Causa é processo ou regra, nunca pessoa.** "No momento que você diz 'fulano errou', a investigação morre." (v6 aula 04, slide 9)
- **Várias causas = Ishikawa + 5 Porquês em cada ramo. Pareto escolhe qual atacar primeiro.** (M03 A07; v6 aula 04)
- **A causa raiz não é o farol — é a falta de gestão do trabalho.** (apostila p.7)
- **Métrica que cai vira A3, nunca cobrança.** (v6 00, slide 13)
- **Cinco armadilhas:** parar cedo; pular nível; culpar pessoa; responder sem evidência; achar que há só uma causa. (v6 aula 04)

## Saída

- Atualize a seção “5. Causa raiz” do A3 na pasta escolhida pelo usuário: cadeia completa, evidências e causa prioritária. Anexe o Ishikawa se houver.
- Em incidentes, registre o mesmo bloco no relatório do responsável, incluindo a regra proposta a partir da causa de sistema.
- Depois: uma contramedida por causa em `ga2-relatorio-a3`. Regras de alcance organizacional vão para o local de padrões escolhido, após a aprovação competente.

## Formas de saída

Leia [Entrega editável](entrega-editavel.md). O pedido e o documento existente definem formato e destino.
Padrão desta skill, sem formato definido: documento Word `.docx`; Google Docs quando esse for o destino escolhido.
Gere e reabra a entrega real; em revisões, atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário. HTML sai quando escolhido; não é cópia obrigatória de Word, Docs ou planilhas.
Preserve os campos e a ordem de [template.md](template.md) e confira [checklist.md](checklist.md).

Modelos para HTML/canvas quando essa for a entrega escolhida:

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-cinco-porques-b-06.html` **(padrão)** | Causa raiz — 5 Porquês (editável) · família b 06 | "no editável" | pronto |
| `../assets/modelos/canvas-ishikawa-lab.html` | Ishikawa — espinha de peixe (laboratório) · família laboratorio | "no canvas do laboratório" | pronto |


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

| Régua | Quando | O que fazer |
|---|---|---|
| Leve | causa única evidente, gap pequeno | 5 Porquês em 5 linhas, evidência em cada, causa prioritária |
| Intermediária | área, causa incerta | 5 Porquês com evidência; teste de pessoa, retorno e controle por escrito |
| Robusta | atravessa áreas, incidente com dinheiro ou reputação, causa múltipla | Ishikawa 6M + 5 Porquês por ramo + Pareto com contagem + regra nova proposta |

## Perguntas para conduzir (do método)

18. Por que isso acontece? Como você sabe que essa resposta é verdade?
19. (Sobre a resposta) E por que isso? — repetir até o quinto nível.
20. A causa que você escreveu é um processo ou regra, ou é o nome de uma pessoa?
21. Se você corrigir só isso, o problema volta?
22. Há mais de uma causa ao mesmo tempo? Em qual categoria (6M) e qual é a mais frequente?

## Erros comuns

- Parar no segundo porquê porque "já deu para ver a solução".
- Responder com achismo: nível sem log, arquivo ou número.
- Culpar pessoa ou ferramenta ("a pessoa esqueceu", "a ferramenta falhou") em vez do processo que permitiu.
- Pular do sintoma para a causa de sistema sem os níveis do meio — fica sem plano acionável.
- Ishikawa com todas as espinhas cheias e nenhum ramo escolhido.
- Confundir causa prioritária com causa mais profunda: ataque a que o dono controla agora; registre a outra como dependência.
- Usar 5 Porquês para achar culpado numa cobrança — o método proíbe.
