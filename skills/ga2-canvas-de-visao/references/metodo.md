# Canvas de Visão

## O que é e quando usar

O Canvas de Visão é uma página que liga o ponto A (passado e hoje) ao ponto B (futuro
desejado) num horizonte de 3, 5 ou 10 anos, e fecha com uma frase de visão que cabe numa
linha. É o **primeiro documento** do Passo 1 (Entender o Contexto) e a âncora de tudo que
vem depois: sem ele, OKR, projeto e prioridade de ciclo ficam "sem âncora".

Entra: quem é o dono, números de hoje com fonte, o que já aconteceu. Sai: o canvas salvo,
comunicado ao time, e a lista do que a empresa ou frente **não** vai fazer. Cadeia:
**Canvas de Visão → A3 → Briefing → OKR → Backlog 2D → Kanban.**

Duas versões: **curta** (Artefato 02, para uma frente ou um caso — 5 campos) e **completa**
(M10, para empresa ou área — 7 campos). Escolha antes de preencher.

## Fonte no método

- Passo 1 — Entender o Contexto: Norte estratégico (M03 A03), Canvas (M03 A04); regras de visão antes das metas, diagnóstico honesto e comunicação.
- Apostila do Passo 1, p.4–6: Canvas como primeiro documento do projeto.
- Template completo: M10 — Kit de Ferramentas, Templates, Canvas e Exemplos, “Canvas Visão”.
- Template curto: Artefato 02 — “Canvas de Visão curto GA2 editável”.
- Exemplo do curso: Kit Implementação, Canvas de Visão da Norte-Sul.
- Diferenças entre versões: o Canvas não existe na v6; a versão curta é de caso, não de empresa.
## Como conduzir

Ordem da aula A04: **hoje → passado → tendências → futuro → como chegar → frase**.

1. **Escolha o objeto e o horizonte.** Pergunta: "É empresa, área, projeto ou frente? 3, 5 ou 10 anos?" Escreva no cabeçalho. Quando houver mais de uma empresa, faça um canvas **por empresa**, sem misturar números do grupo. Recuse canvas sem empresa no cabeçalho.
2. **Situação atual (Hoje).** Pergunta: "Como está hoje: produto, números, clientes, pessoas, desafios? Qual a fonte de cada número?" Escreva só número com fonte e data. Número financeiro vem do responsável financeiro da empresa. O que não tem fonte entra como `[a medir]`. Recuse "a gente acha".
3. **Passado.** Pergunta: "O que mudou até aqui: marcos, pivôs, crises, padrões que se repetem?" Escreva fato datado. Recuse copiar o exemplo da aula ("ficou lindo, mas não é o seu passado").
4. **Perspectivas e tendências.** Pergunta: "O que está mudando no mercado, no cliente, na tecnologia, na regra? O que é ameaça e o que é oportunidade?" Recuse canvas que ignora mercado e cliente ("não pode ser uma ilha").
5. **Futuro desejado.** Pergunta: "Em N anos, como quer ser reconhecido e com que números?" Escreva quantitativo e qualitativo. Recuse futuro sem número.
6. **Como chegar lá.** Pergunta: "Comparando hoje com o futuro, quais os buracos? Que ação, investimento, competência ou parceria fecha cada um?" Uma linha por buraco.
7. **Visão em uma frase.** Pergunta: "Cabe numa linha? Alguém de fora entende? Inspira?" Recuse frase longa.
8. **O que NÃO vamos fazer.** Pergunta: "O que a visão manda deixar de lado?" Pelo menos um item. Sem ele, o canvas não fechou.
9. **Comunicação.** Pergunta: "Para quem e com que frequência?" Time, sócios, fornecedores, clientes.

Na versão curta, os passos 2, 5, 7 viram "Como está hoje", "Como quero que fique", "Meu
Norte"; o passo 6 vira "Primeiro passo"; o resto é opcional.

## Regras do método que valem aqui

- **Visão antes de meta.** Sem canvas, OKR e projeto não têm âncora. (M03 A04; apostila p.6)
- **Comece pela situação atual e seja honesto:** nem minimizar problema nem exagerar sucesso. (M03 A04, A06)
- **A visão direciona especialmente o que vocês não farão.** (M03 A03)
- **Comunique a visão com frequência**, até para sócios, fornecedores e clientes. (M03 A04)
- **Horizonte de 3, 5 ou 10 anos**; revisitar uma vez por ano. (apostila p.6)
- **Cabe numa página.** A frase cabe numa linha.

## Saída

- Salve o canvas na pasta escolhida pelo usuário, identificando objeto, empresa e dono. A visão da empresa exige aprovação do decisor estratégico.
- Para cada frente, mantenha o seu canvas no documento escolhido; não misture números de empresas diferentes.
- Depois: o “Hoje” vira situação atual do A3 (`ga2-diagnostico`); o “Futuro desejado” vira objetivo do OKR; o “Não vamos fazer” vira política de entrada do quadro. Confirme com o dono e registre como comunicará ao time.

## Formas de saída

Leia [Entrega editável](entrega-editavel.md). O pedido e o documento existente definem formato e destino.
Padrão desta skill, sem formato definido: documento Word `.docx`; Google Docs quando esse for o destino escolhido.
Gere e reabra a entrega real; em revisões, atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário. HTML sai quando escolhido; não é cópia obrigatória de Word, Docs ou planilhas.
Preserve os campos e a ordem de [template.md](template.md) e confira [checklist.md](checklist.md).

Modelos para HTML/canvas quando essa for a entrega escolhida:

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-visao-kit-01.html` **(padrão)** | Canvas de Visão · família kit 1 | "no canvas do kit" | pronto |


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

| Régua | Quando | O que preencher |
|---|---|---|
| Leve | frente de 1 pessoa, < 1 mês | versão curta: caso, norte, hoje, como quero, primeiro passo |
| Intermediária | área ou frente de 1–3 meses | versão completa sem "Trajetória"; tendências em 3 linhas |
| Robusta | empresa, rumo, aprovação da direção ou do conselho | versão completa, todos os campos, número com fonte e responsável financeiro, lista do "não fazer", plano de comunicação |

A forma muda; a ordem (hoje → passado → tendências → futuro → como chegar → frase) não.

## Erros comuns

- Copiar o exemplo da aula e chamar de visão própria.
- Frase de visão longa demais (a própria aula reconhece isso no exemplo dela).
- Ser uma ilha: canvas sem mercado, cliente, concorrente.
- Foco excessivo no curto prazo: "futuro" que é a meta do trimestre.
- Número sem fonte, ou número de grupo sem dizer de qual empresa.
- Pular o "não vamos fazer" — canvas que autoriza tudo não direciona nada.
- Preencher e guardar: visão que ninguém comunicou não existe.
