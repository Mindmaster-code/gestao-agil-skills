# Quadro de Delegação

## O que é e quando usar

Quadro que diz **quem decide o quê**: assuntos do time nas linhas, níveis de delegação
nas colunas, nome de quem decide dentro da célula. "O nível diz como a decisão acontece;
o nome diz quem decide."

Vive no Passo 6 (Liderando Times). Entra antes: o diagnóstico do estágio do time
(Tuckman) — o quadro é a jogada do **storming**, quando "ninguém sabe quem decide e tudo
volta para a mesa do gestor". Sai depois: quadro pendurado ao lado do Kanban, data de
revisão, e o assunto que virou os 70% de um PDI.

Dispara quando: alguém vem perguntar "posso?" mais de uma vez por semana; dois donos acham
que a decisão é deles; demanda que volta ao líder em duas semanas; célula sem nome.

## Fonte no método

- Base do método — Passo 6: Liderança de Times §2.8 (Management 3.0: Delegation Board / Poker), §2.10 (storming → Delegation Poker), §4.3 (campos v6 e ao vivo), §6.1–6.2 (aplicação à operação e a agentes), §8.1 (divergência 4 × 7 níveis).
- Aulas: ao vivo M08 A09 (Management 3.0) e A11 (Tuckman); v6 pasta 07 aula 02 ("Management 3.0 e Quadro de Delegação", caso da Ana).
- Templates: v6 Canvas Editável — Quadro de Delegação, v6, Passo 6; ao vivo Canvas Matriz Delegação, Kit M10 e slides GA — Aula — Matriz Delegação, M08; exemplo Matriz de Delegação preenchida, Kit de Implementação (referência bibliográfica).

## Os dois esquemas (documentados; esta referência adota o de 7)

| | Ao vivo / M10 / Kit (4 níveis) | v6 / A09 / Management 3.0 (7 níveis) |
|---|---|---|
| Colunas | N1 Decide Sozinho · N2 Consulta Equipe · N3 Consulta o Líder · N4 Líder Decide | 1 Dizer · 2 Vender · 3 Consultar · 4 Concordar · 5 Aconselhar · 6 Perguntar · 7 Delegar |
| Autonomia do time | à **esquerda** (N1) | à **direita** (7) |
| Faixas | — | Você decide (1–3) · Juntos (4) · O time decide (5–7) |
| Regra de ajuste | "suba uma decisão de nível só quando o time errar nela" (Kit) | "cada um marca sozinho antes de comparar" (v6) |

Leitura invertida e escala diferente entre a aula (A09, 7) e o template que o aluno baixa
(M10, 4). A fonte registra a divergência: declare a versão usada; não presuma que as escalas foram unificadas.

**Adotado nesta referência: 7 níveis**, com tradução de cada um:

| Nível | Nome | Tradução |
|---|---|---|
| 1 | Dizer | o líder decide e comunica |
| 2 | Vender | o líder decide e explica o porquê |
| 3 | Consultar | o líder ouve antes e decide |
| 4 | Concordar | decidem juntos, por acordo |
| 5 | Aconselhar | o time decide depois de ouvir o líder |
| 6 | Perguntar | o time decide e conta depois |
| 7 | Delegar | o time decide e nem precisa contar |

Conversão para quem tem o template de 4: N4 Líder Decide = 1–2 · N3 Consulta o Líder = 3–5 · N2 Consulta Equipe = 4 · N1 Decide Sozinho = 6–7.

## Como conduzir (1 hora, v6 02)

1. **Liste os assuntos.** "Quais quatro assuntos fazem alguém vir te perguntar 'posso?'" Um por linha, **no verbo**: "responder reclamação fora do padrão". Recusa: assunto largo ("atendimento"); mais de 6 linhas na primeira rodada.
2. **Cada um marca sozinho, calado** — inclusive o líder. Recusa: líder marcando primeiro em voz alta ("o time repete").
3. **Compare linha a linha.** Conversa só onde discordou: "a linha em que vocês discordaram é a conversa que faltava".
4. **Combine o nível e escreva o nome** na célula. Recusa: célula com X e sem nome ("volta para você em duas semanas"); dois nomes na mesma célula (fronteira mal escrita — conserte a linha, não o caso).
5. **Preencha o rodapé:** Combinado em (data da reunião) · Visível em ("onde o time vê, não na sua gaveta") · Revisamos em (data). Recusa: "revisamos em" em branco — "é a que todo mundo deixa em branco".
6. **Pendure ao lado do quadro de tarefas.** Na data de revisão, reabra só as linhas em que a decisão voltou ao líder ou o time errou.

## Aplicação aos agentes (acréscimo do laboratório)

Para agente, delegação por nível não é boa prática, é enforcement: "gente intui limite;
agente executa o que o prompt permitir" (Base do método — Passo 6 §6.2). Tradução dos níveis para uma operação com agentes; os papéis devem ter autoridade registrada, não presumida:

| Nível | Quem decide | Onde está escrito | Exemplo |
|---|---|---|---|
| 1–2 | autoridade humana competente decide e explica | política de autorização, controle técnico e registro da aprovação do projeto | preço, verba, contrato, estrutura, produto, pessoa, deploy em produção, DNS, exclusão de dado, mídia paga |
| 3 | autoridade de coordenação ouve o diretor e decide | acordo de autoridade da organização | prioridade entre áreas, mudança de dono, fronteira entre diretores |
| 4 | coordenação e diretor por acordo | demanda com o que, por quê, dono, pronto é, prazo, onde trava; status com gate e decisor nomeado | prazo de negócio, corte de escopo |
| 5 | Diretor decide depois de ouvir a coordenação | STATUS do projeto | sequência de entregas dentro da área |
| 6 | Diretor/head decide e conta no report de sexta | identidade canônica do agente | "diretor pede direto ao time técnico, dentro da autoridade registrada" |
| 7 | Agente decide sem contar | identidade canônica, "Autoridade" | formato de artefato interno, pauta de ritual, classificar cartão como parado |

Célula sem nome = agente que age sem autoridade ou trava sem motivo. Autoridade só viaja
com fonte (arquivo, linha, hora, texto).

## Regras do método que valem aqui

- Autonomia sem limite declarado não é autonomia, é armadilha. Empoderar = limite claro + devolver a decisão dentro dele. (M08 A09; v6 02)
- O nível diz como a decisão acontece; o nome diz quem decide. (v6 02)
- Cada um marca sozinho antes de comparar. (v6 02)
- Storming não se abafa, se medeia: o acordo escrito vira a regra do norming. (M08 A11; v6 01)
- Suba uma decisão de nível só quando o time errar nela — delegação se ajusta pela confiança. (Kit)
- "Os melhores gestores são como magos: ajudam o herói, nunca fazem por ele." (M08 A09)

## Saída

Os caminhos `.md` abaixo são convenções do fluxo de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Organização: um quadro pelo `template.md`, no destino escolhido e vinculado ao portfólio. Por frente, crie um quadro próprio apenas quando necessário.
- Aluno: canvas v6 preenchido, pendurado ao lado do Kanban, foto no STATUS.
- Depois: o assunto que subiu para 6–7 vira os 70% do PDI da pessoa (`ga2-pdi`); linha em que dois donos discordam vai à autoridade de coordenação como fronteira, não como caso.

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
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-delegacao-kit-11.html` |

Modelos canvas desta skill (specs `delegacao-kit-11`, `delegacao-v6`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-delegacao-kit-11.html` **(padrão)** | Matriz de Delegação · família kit 11 | "no canvas do kit" | pronto |
| `../assets/modelos/canvas-delegacao-v6.html` | Canvas Editável — Quadro de Delegação · família v6 | "no canvas v6" | pronto |

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

- **Leve** (time de 2–3, uma dor): 3 linhas, rodapé completo, revisão em 30 dias.
- **Intermediária** (área da organização): 4–8 linhas, nome de agente na célula, fonte da autoridade ao lado.
- **Robusta** (organização inteira, gates humanos): quadro único com os 7 níveis, coluna "onde está escrito" e revisão por ciclo de OKR; mudança de nível 1–2 só com "sim" da autoridade humana competente registrado.

## Erros comuns

- Líder marca primeiro. Assunto largo demais. X sem nome. Quadro na gaveta. Sem data de revisão.
- Tratar o quadro como organograma: organograma diz quem reporta; o quadro diz quem decide cada assunto.
- Dois nomes na célula para "não brigar". É a fronteira mal escrita — a linha vai à autoridade de coordenação.
- Subir de nível por desconfiança geral, e não por erro naquele assunto.
- Para agente: célula 1–2 sem hook ou gate escrito — vira só texto, e texto não segura agente.
