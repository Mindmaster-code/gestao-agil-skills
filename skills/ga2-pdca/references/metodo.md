# PDCA — o ciclo de toda melhoria

## O que é e quando usar

PDCA = Plan, Do, Check, Act (planejar, executar, verificar, agir). É o ciclo que está por
baixo de todo método ágil: "Scrum, Kanban, OKR, XP, tudo segue essa linha". **Sprint é um
PDCA:** planejamento = P, execução = D, review = C, retrospectiva e ajuste = A.

É o **registro de qualquer melhoria de processo** que não mereça um A3 inteiro. Entra
antes: a ação da Retrospectiva, a contramedida de um A3, ou um sinal do Quadro Kaizen. Sai
depois: padrão escrito (POP) ou novo ciclo com dose diferente.

Vive no **Passo 0 — Fundamentos** (conceito) e é usado no Passo 4 (retro) e Passo 5 (Kaizen).

## Fonte no método

- Base do método — Passo 0: Fundamentos, Visão de Floresta e Lean §2.17, §4.5, regra 12, §8.7 — M02 A07.
- Base do método — Passo 1: Entender o Contexto §2.10 e "Como o A3 contém o PDCA" — M03 A05.
- Base do método — Passo 5: Melhoria Contínua §2.17, §4.9, regras 7, 8 e 9 — M07 A13; v6 Quadro Kaizen.
- A aula não fornece formulário oficial (lacuna L-02). O template derivado pelo laboratório está em `template.md`; os acréscimos continuam marcados.

## Como o A3 contém o PDCA

| PDCA | Lado do A3 | Campos do A3 |
|---|---|---|
| Plan | esquerdo (+ fim do direito) | contexto · situação atual · ideal · gap e causa raiz · contramedidas · plano |
| Do | direito | plano de ação executado |
| Check | direito | acompanhamento com a mesma medida da situação atual |
| Act | direito | aprendizado → ajustar e estabilizar; levar ao próximo ciclo |

"Um A3 é um relatório para dar início a um PDCA." Quando o problema tem A3, o PDCA aponta
para ele e não repete o diagnóstico.

## Como conduzir

1. **Plan — o sinal com número de hoje.** Pergunta: "Qual o fato e o número de hoje?" Escreve
   o problema sem culpado. Recusa: "sem número de hoje não existe melhoria — existe opinião".
2. **Plan — causa e linha de base.** "Por que isso acontece?" (5 porquês ou A3). A linha de
   base é o número que o Check vai comparar; escreva **antes** de executar. Recusa: plano sem
   linha de base — não há como checar.
3. **Plan — uma ação, dono, prazo, meta.** "O que muda, quem faz, até quando, que número
   esperamos?" Mais de um passo → abre `ga2-5w2h`. Recusa: duas ações no mesmo PDCA.
4. **Do — executar como escrito e registrar.** "O que foi feito, quando, por quem, com que
   prova?" Desvio do plano é registrado, não escondido.
5. **Check — medir durante, não só no fim.** "O número medido bateu com a linha de base?"
   Evidência pelo caminho real. Recusa: Check por sensação ("parece que melhorou").
6. **Act — decidir com verbo.** Três saídas:
   - **padronizar**: funcionou → escrever o padrão onde o time trabalha (POP, política do
     quadro, registro da cadência). "Sem padrão novo, o ganho fica preso na memória."
   - **ajustar**: funcionou em parte → novo ciclo com dose ou formato diferente, mesmo
     registro, ciclo nº +1.
   - **descartar**: não funcionou → registrar para não procurar duas vezes no mesmo lugar.
7. **Registrar o ciclo** na tabela de ciclos e fechar com data. PDCA sem Act escrito está aberto.

## Critério "Act = padronizar ou ajustar"

| Situação no Check | Act |
|---|---|
| Número bateu a meta e a causa foi a prevista | padronizar (POP / política) |
| Número mexeu na direção certa, mas não chegou | ajustar — mesma ação, dose maior ou formato diferente |
| Número mexeu por outra causa ou com efeito colateral | ajustar — nova ação no mesmo sinal |
| Número não mexeu após um ciclo completo | descartar e registrar; reabrir o 5 porquês |

## Regras do método que valem aqui

- "Todo ciclo de melhoria contínua tem que obedecer essas quatro etapas." (M02 A07)
- "Verificar = medir o sucesso relativo em relação à linha de base." (M02 A07)
- "É ciclo que não acaba nunca, por isso se chama melhoria contínua." (M02 A07) — mas cada
  ciclo **fecha** com um Act escrito.
- "Toda melhoria termina num verbo: manter, ajustar ou descartar." (v6 A01)
- "Uma mudança por ciclo, uma variável por vez." (v6 A01)
- Mudança em agendamento automático, integração ou rotina entra com linha de base, execução, verificação pelo caminho real e ajuste. Observe também a política de mudança em produção do projeto.

## Saída

Os caminhos `.md` abaixo são convenções do fluxo de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Registro: PDCA da melhoria, com ciclo, data e nome, junto da retrospectiva ou do A3 no destino escolhido.
- Depois: Act = padronizar → POP em um documento de procedimento operacional padrão aplicado ou linha nova em
  registro da cadência; Act = ajustar → ciclo nº +1 no mesmo arquivo; a retro seguinte abre
  conferindo o Check e o Act. Resumo vai no relatório de sexta ao responsável pela coordenação.

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
| Documento | `<nome>.html` — documento corrido no design system dos modelos públicos | quando HTML for escolhido | `../assets/modelos/documento.html` (em produção) |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-pdca-lab.html` |

Modelos canvas desta skill (specs `pdca-lab`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-pdca-lab.html` **(padrão)** | PDCA (laboratório) · família laboratorio | "no canvas do laboratório" | pronto |

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

- **Leve**: quatro linhas (P com número de hoje e meta, D, C com número, A com verbo).
- **Intermediária** (retrospectiva da equipe): template completo, um ciclo.
- **Robusta** (A3 ou mudança de produção): PDCA aponta para o A3, 5W2H anexo, registro de
  ciclos preenchido até o padrão ficar escrito.

## Erros comuns

- Pular o Check e ir direto para o próximo Plan.
- Plano sem linha de base; Check com número diferente do que o P prometia medir.
- Act que não padroniza — o ganho some quando a pessoa muda.
- PDCA que não acaba nunca: ciclo sem data de fechamento.
- Tratar como evento único — é ciclo.
- Confundir Check (review: produto) com Act (retro: processo) — erro de fala da própria aula.
