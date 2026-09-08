# Revisão do Ciclo (Sprint Review)

## O que é e quando usar

É a conversa que fecha a conta do ciclo: o que ficou pronto **contra a meta combinada**,
mostrado funcionando, na frente de quem recebe o resultado. Olha **produto**, não processo
(processo é a Retrospectiva, que vem logo depois).

Vive no **Passo 4 — Ritmo Ágil**: review e retro pertencem a esse passo.
Entra antes: `plano.md` do ciclo (a meta e os compromissos) e os reports de sexta dos
diretores. Sai depois: decisão por compromisso, cartões do próximo ciclo, sinal de resultado
para o Quadro Kaizen e a entrada da Retrospectiva.

Na cadeia: A3 → OKR → Backlog 2D → Kanban → **Plano do ciclo → Review** → Retro → PDCA.

## Fonte no método

- Base do método: Passo 4 — Ritmo Ágil §2.13, §4.7, regras 15, 16 e 22 — M06 A07 (ao vivo); v6 aula 07.
- Base do método: Passo 5 — Melhoria Contínua §2.3, regra 3 — M07 A02/A03 (professor).
- Templates: v6 «Canvas Editável — Revisão do Ciclo»;
  legado «M06 A07 — Canvas Sprint Review»;
  roteiro «Mod 05 — Roteiro de Review GA2 Editável»;
  individual folha individual «review-ciclo-ga2.pdf».
- Exemplo do curso: Kit Implementação, bloco 5 (Distribuidora Norte-Sul).

## Os 5 formatos, consolidados em um

| Campo deste template | A07 ao vivo | Legado A07 | v6 | Roteiro Mod 05 | `--help` 10 |
|---|---|---|---|---|---|
| Meta combinada (copiada sem maquiagem) | meta do sprint | — | sim | o que foi combinado | — |
| Ciclo e período | início/fim | — | sim | — | ciclo/período |
| Ficou pronto, com prova | entregas realizadas | resultados | mostre funcionando | o que foi entregue | o que entreguei |
| Não ficou e por quê (vira cartão) | — | — | sim | — | ficou pra depois |
| Números (de/para por KR) | métricas do briefing | — | OKR se mexeu? | antes/depois | — |
| Feedback de quem recebe | feedback do PO | positivos/negativos/mudanças | — | — | feedback que recebi |
| Decisão (continua / para / corta / escala) | — | — | — | decisões necessárias | — |
| Aprendizado | — | aprendizados | — | — | o que aprendi |
| O que muda no próximo ciclo | próximo sprint | — | sim | próximo ciclo | o que levo |

Variantes: o legado A07 não tem meta nem data; só o Roteiro Mod 05 traz "decisões
necessárias"; o `--help` 10 é individual. A consolidação é `(acréscimo do laboratório)`:
o campo "Decisão" generaliza "aprovar, ajustar, cortar" do Roteiro para
continua / para / corta / escala, que é o vocabulário de acordo de cadência do time regra 2.

## Como conduzir (30 min, sexta 12h)

1. **Reler a meta em voz alta** (30 s). Pergunta: "Qual foi a meta que combinamos na
   segunda?" Copie do `plano.md` **igual**. Recusa: meta reescrita para caber no resultado.
2. **Por compromisso, pedir a prova.** Pergunta: "Mostra funcionando — URL, log, arquivo,
   mensagem?" Escreve a prova na linha. Recusa: "está quase", "deveria funcionar",
   slide no lugar da coisa. Linha sem prova = **não entregue**.
3. **O que não ficou e por quê.** Pergunta: "O que travou e desde quando?" Escreve a causa
   (situação, não pessoa) e cria o cartão do próximo ciclo **na hora**, com dono.
4. **Números.** Pergunta: "Qual KR ou métrica do briefing se mexeu? De quanto para quanto?"
   Número sempre com a empresa (uma empresa ≠ outra empresa). Recusa: "foi bem" sem número.
5. **Feedback de quem recebe.** Quem usa o resultado (cliente, diretor ou outro destinatário nomeado) diz
   positivo, negativo e mudança necessária. Colete, não defenda.
6. **Decisão por compromisso:** continua / para / corta / escala — quem decide é quem recebe
   o resultado; o Gestor registra. Recusa: review sem decisão (vira relato de atividade).
7. **Próximo ciclo.** O que muda, em uma linha; o que fica de fora, dito pelo nome.
8. Salvar, atualizar registro de métricas na pasta do caso (data cumprida, aceite na 1ª) e abrir a Retro.

## Regras do método que valem aqui

- "Review mede contra a meta combinada, copiada sem maquiagem, e mostra funcionando, não em
  slide. Quem fez é quem mostra." (regra 15, A07 / v6 aula 07)
- "Nunca contra a expectativa que cresceu no meio do caminho." (Kit Implementação)
- "Review olha os números do negócio, não só as tarefas." (regra 16, A03/A07)
- "A pergunta não é 'o que a gente fez' — é 'isso serve?'" (v6 aula 07)
- "Feedback negativo é o mais valioso." (M07 A02)
- Review produz decisão (continua, para, corta, escala), não relato de atividade
  (acordo de cadência do time, regra 2). Linha sem prova conta como não entregue (regra 4).

## Saída

Os nomes abaixo são sugestões de organização, não dependências de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Arquivo: Revisão do Ciclo na pasta do caso (template em `template.md` desta skill).
- Depois: cartões novos em registro do portfólio na pasta do caso; métricas em registro de métricas na pasta do caso;
  KR parado há 2 semanas ou entrega recusada abre `ga2-quadro-kaizen`; a review é a entrada
  da `ga2-retrospectiva` (mesmo dia, 14h); resumo entra no report de sexta ao dirigente responsável.

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
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-revisao-kit-08.html` |

Modelos canvas desta skill (specs `revisao-kit-08`, `revisao-v6`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-revisao-kit-08.html` **(padrão)** | Revisão de Entregas | Debriefing · família kit 8 | "no canvas do kit" | pronto |
| `../assets/modelos/canvas-revisao-v6.html` | Canvas Editável — Revisão do Ciclo · família v6 | "no canvas v6" | pronto |

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

- **Leve** (um diretor, 1–3 compromissos): tabela prometido × entregue × prova × decisão,
  mais "o que muda". Sem feedback formal nem aprendizado.
- **Intermediária** (ciclo do laboratório): template completo.
- **Robusta** (projeto com cliente externo ou Conselho): acrescenta feedback por
  interessado, de/para de cada KR e aceite assinado por quem recebe.

## Erros comuns

- Apresentar em vez de mostrar; só o líder falar.
- Esconder o que não saiu; maquiar a meta.
- Medir tarefa e esquecer o número do negócio.
- Misturar com a retro ("por que atrasou" é assunto da retro).
- Review sem decisão e sem cartão para o que sobrou.
- Número sem dizer de qual empresa.
