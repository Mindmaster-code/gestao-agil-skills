# Retrospectiva

## O que é e quando usar

É a única conversa do ciclo sobre o **jeito de trabalhar**, só com quem faz o trabalho. Olha
processo, não produto; situação, não pessoa. Sai **uma** ação, com dono e prazo — "duas viram
nenhuma".

Vive no **Passo 4 — Ritmo Ágil**, logo depois da Revisão do Ciclo, no mesmo dia. Entra antes:
`review.md` e registro de métricas na pasta do caso. Sai depois: a ação registrada como PDCA (e, se precisar
de passos, 5W2H); a próxima retro abre conferindo a ação desta.

Na cadeia: Plano do ciclo → Review → **Retro** → PDCA / Quadro Kaizen → padrão (POP).

## Fonte no método

- Base do método: Passo 4 — Ritmo Ágil §2.14, §4.8, regras 18, 19 e 22 — M06 A08 (ao vivo); v6 aula 08.
- Base do método: Passo 5 — Melhoria Contínua §2.4, §2.9 (filtro de ideias), regras 1, 2, 5, 8, 9 e 15 — M07 A02/A04 (professor); v6 A01/A04.
- Templates: v6 «Canvas Editável — Retrospectiva»;
  legado «M06 A08 — Canvas Retrospectiva»;
  «Mod 05 — Retrospectiva GA2 Editável»;
  individual folha individual «retrospectiva-ga2.pdf».

## As 4 versões do formato

| Versão | Colunas | Ação |
|---|---|---|
| A08 ao vivo / v6 | Manter · Melhorar · **Parar** | uma, dono e prazo (o exemplo v6 tem dono, não tem data) |
| Legado A08 "Reflexões da Equipe" | Funcionou bem · Podia ser melhor · **Vamos tentar** | uma mudança por sprint (Kit) |
| Mod 05 editável | Funcionou · Atrapalhou · Manter · Ajustar | uma, dono e prazo |
| `--help` 11 (individual) | Foi bem · Não foi bem · Vou mudar | "1 ou 2 experimentos" — contradiz a v6 |

O Gestor usa **Manter / Melhorar / Parar** (v6) e aceita "começou / parou / continuou" como
leitura da mesma folha olhando para trás. A regra de uma ação vence o `--help` 11.

## Como conduzir (20–30 min, sexta 14h)

1. **Abrir conferindo a ação da retro anterior.** Pergunta: "A ação da semana passada
   aconteceu? Qual o número?" Escreve Do/Check/Act no PDCA anterior. Recusa: passar adiante
   sem fechar.
2. **5 minutos em silêncio, todo mundo escreve.** Por carta ou pulso: cada participante manda
   as três colunas antes de ler as dos outros. Recusa: o líder preencher sozinho.
3. **Manter** — começar pelo que foi bem. Pergunta: "O que funcionou e queremos de novo?"
4. **Melhorar** — "O que atrapalhou o jeito de trabalhar?" Escreve a situação com fonte
   ("cartão P-04 ficou 21 dias sem dono"). Recusa: nome de pessoa como causa.
5. **Parar** — "O que decidimos deixar de fazer?"
6. **Filtrar as ideias** (v6 A04): está sob controle do time? cabe em um ciclo? move um atrito
   que apareceu mais de uma vez? A primeira que passa nas três vira ação. As outras vão para o
   estacionamento (lista de ideias estacionadas na pasta do caso), sem promessa.
7. **Uma ação, dono, data, como medimos.** Recusa: duas ações; ação sem data; "em breve".
8. **Clima** (Happiness Metric, 1 a 5, tendência do time, nunca nota individual). Opcional na
   time com acompanhamento assíncrono — registre só se houver humano no ciclo.
9. Salvar; abrir o PDCA em PDCA da melhoria na pasta do caso com o Plan preenchido.

## Regras do método que valem aqui

- "Processo, não produto; situação, não pessoa; começa pelo que foi bem; todo mundo escreve
  antes de falar; uma ação por ciclo com dono e prazo; a próxima retrô abre conferindo a ação
  da anterior." (regra 18, A08 / v6 aula 08)
- "Uma mudança por ciclo. Duas viram nenhuma." (v6 aula 08) · "Se duas coisas mudam juntas,
  você perde a chance de saber qual delas funcionou." (v6 A01)
- "Não pule a retrospectiva. É a parte mais negligenciada do processo." (M07 A01)
- "O que funcionou vira padrão escrito onde o time trabalha." (v6 A04)
- "Problemas quase sempre têm causa raiz no processo, não nas pessoas." (M07 A12)
- Retro produz uma melhoria só, com dono e data, registrada como PDCA (acordo de cadência do time, regra 3).

## Saída

Os nomes abaixo são sugestões de organização, não dependências de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Arquivo: Retrospectiva na pasta do caso (template em `template.md`).
- Depois: `ga2-pdca` aberto com o Plan; se a ação tem mais de um passo, `ga2-5w2h`; se o
  atrito se repetiu e tem número, `ga2-quadro-kaizen`. Lição que vale para a organização vai para
  registro compartilhado de aprendizados da organização (seguindo o README). Ação e dono entram
  no report de sexta ao dirigente responsável.

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
| Documento | `<nome>.html` — documento corrido no design system do laboratório | quando HTML for escolhido | `../assets/modelos/documento.html` (pronto) |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-retrospectiva-kit-09.html` |

Modelos canvas desta skill (specs `retrospectiva-kit-09`, `retrospectiva-v6`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-retrospectiva-kit-09.html` **(padrão)** | Retrospectiva | Reflexões da Equipe · família kit 9 | "no canvas do kit" | pronto |
| `../assets/modelos/canvas-retrospectiva-v6.html` | Canvas Editável — Retrospectiva · família v6 | "no canvas v6" | pronto |

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

- **Leve** (um agente, ciclo individual): três linhas (manter / melhorar / parar) e uma ação com data.
- **Intermediária** (ciclo do laboratório): template completo, sem clima.
- **Robusta** (time com humanos): acrescenta clima por pessoa (tendência), ata distribuída e
  ação anterior conferida com número na abertura.

## Erros comuns

- Desabafo sem ação; lista de doze melhorias.
- Caça ao culpado; "fulano esqueceu" em vez de "o cartão ficou três dias sem dono".
- Assunto que cabia na review (resultado do produto).
- Ação sem dono ou sem data; ação que o time não controla.
- Não conferir a ação da retro anterior — a melhoria fica aberta para sempre.
