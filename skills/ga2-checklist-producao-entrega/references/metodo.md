# Checklist de produção e entrega (Definition of Ready / Definition of Done)

## O que é e quando usar

A aula M06 A09 entrega um checklist de 9 etapas que percorre o método inteiro — do Canvas de
Planejamento ao próximo trimestre. Esta skill corta o checklist em dois portões que o quadro usa
todo dia:

- **Definition of Ready (DoR, "pronto para começar")** — o que um cartão precisa ter para sair
  de "A fazer / Apta" e entrar em "Em execução". Vem das etapas 1–4 do checklist.
- **Definition of Done (DoD, "pronto para entregar")** — o que um cartão precisa mostrar para ir
  a "Entregue" e depois "Aceito". Vem das etapas 5–8 e da regra do laboratório: prova pelo caminho real.

Vive entre o Passo 3 (política de entrada e de pronto do quadro) e o Passo 4 (checklist do
ritmo). Entra antes do Plano do Ciclo (item sem DoR não é puxado) e fecha a review (linha sem
DoD conta como não entregue).

## Fonte no método

- Base do método: Passo 4 — Ritmo Ágil §4.12 (as 9 etapas e as 6 perguntas da v6), §3 regras 15, 17, §8 item 13.
- Base do método: Passo 3 — Gestão Visual §4.7 (Quadro de Execução: "Concluídos — entrega **e evidência**"),
  §4.8 (política de Entrada e de Pronto; DoD genérico + por tipo de tarefa, Canvas 7.2), §3 regra 10.
- Aulas: M06 A09 (checklist), A07 (review mede contra a meta), M05 A07 e A11 (definir "pronto"
  por escrito); v6 pasta 05 aula 07 ("defina pronto uma vez, com o time, e cole ao lado da
  coluna Pronto") e aula 09 (checklist de 6 perguntas reproduzido em `template.md`).
- Template: «M06 A09 — Checklist Planejamento e Execução Processo GA» (9 etapas, sem
  campos preenchíveis); «M10 — Canvas Kanban — Políticas» (DoD genérico e por tipo);
  «Mod 03 — Quadro de Execução GA2 Editável» (evidência na coluna Concluídos).
- Acréscimo do laboratório: modelo operacional de demandas (acréscimo do laboratório, com regras incorporadas nesta referência) §5 (contrato mínimo para ficar Apta =
  o DoR do laboratório), §11 (DoD, Entregue, Aceita, gate); regra de entrega verificada (acréscimo do laboratório) "Entrega verificada";
  registro de demanda em seis linhas — o que, por que, dono, pronto é, prazo, onde trava (acréscimo do laboratório) §1 ("pronto é"); registro do portfólio na pasta do caso (políticas).

## Como conduzir

### Portão 1 — DoR: o cartão pode entrar em execução?

1. **Origem.** Pergunta: "De qual contramedida do A3 / iniciativa do OKR / entrega do Backlog 2D
   este cartão vem?" (etapas 1–3 do checklist). Recuse cartão órfão.
2. **Dono único e Aceitante.** Pergunta: "Quem responde? Quem confere?" (§5, `ga2-quem-faz-o-que`).
3. **"Pronto é" escrito.** Pergunta: "Como vamos saber que acabou, pelo caminho real?" URL,
   login, log, arquivo, mensagem. Recuse "quando estiver pronto" e "buildei local".
4. **Tamanho.** Cabe em uma semana? Quebrado em tarefas de um dia? (etapa 4; v6 04).
5. **Compromisso, classe e data** (§9): Comprometida? Crítica / Com prazo / Normal? Data comprometida?
6. **Gates mapeados de uma vez.** Pergunta: "Que ação sensível esta entrega pede? Quem autoriza?"
   Liste todos agora (regra de ouro: bloqueio que só o humano resolve se mapeia de uma vez).
7. **Riscos com resposta** (etapa 4: "ações para riscos do briefing").
8. **Contexto suficiente**: a pessoa que vai executar acha tudo sem perguntar (§5 "Pacote de Contexto").
9. **Capacidade**: o dono está abaixo do WIP (3)? Se não, o cartão espera ou outro cede.

Tudo marcado → cartão vai para "Em execução". Falta algo → volta a "Em preparação" com o que falta escrito.

### Portão 2 — DoD: o cartão pode ser entregue?

10. **Executou no ritmo** (etapa 5): esteve no quadro, passou pela diária, cartão atualizado.
11. **Prova pelo caminho real** (etapa 7 + regra do laboratório): URL de produção, login real (aluno e
    admin quando for produto), reload da feature, curl autenticado, log. Cite no cartão: o quê,
    onde, quando (HH:MM). Recuse "deveria funcionar".
12. **Checklist por tipo de tarefa** (Canvas 7.2): veja `template.md` — código/deploy, conteúdo
    de aula, campanha, relatório/número, carta/cobrança, decisão.
13. **Métrica de negócio olhada** (etapa 6): o número que a entrega deveria mover foi lido, com
    empresa rotulada (uma empresa ≠ outra empresa). Demanda cumprida ≠ objetivo atingido (§12) — registre os dois.
14. **Gate da DoD aprovado** (§11): nenhuma entrega com gate exigido pendente.
15. **Registro durável**: acompanhamento/diário/arquivo atualizado, versão registrada e resposta enviada a quem pediu. Use commit quando houver repositório. "Ritual que não produziu arquivo não aconteceu."
16. **Verbo honesto**: "validado em produção às HH:MM" / "código alterado, não validado em
    runtime". Nunca "feito" sem verificar.
17. **Aceite** (etapa 8): o dono marca Entregue; o **Aceitante** confere a DoD e marca Aceita. Rejeição
    do que já estava na DoD → volta a "Em execução"; correção fora da DoD → demanda filha.

## Regras do método que valem aqui

- Defina "pronto" por escrito, uma vez, com o time, e cole ao lado da coluna Pronto. (M05 A07, v6 07)
- Concluído = entrega **e evidência**. (artefato 04)
- Review mede contra a meta combinada, sem maquiagem; mostra funcionando, não em slide. (A07, v6 07)
- DoD genérico + DoD por tipo de tarefa. (Canvas 7.2)
- Checklist da v6: nenhuma pergunta aceita "mais ou menos". (v6 09)
- Acréscimo do laboratório: toda demanda tem DoD e Aceitante antes de executar; nenhuma é Entregue com gate pendente;
  urgência não elimina DoD. (§1, §11)
- Acréscimo do laboratório: "pronto" só pelo caminho real; linha sem prova conta como não entregue. (regra de entrega verificada (acréscimo do laboratório), `cadencia.md` regra 4)

## Saída

Os nomes abaixo são sugestões de organização, não dependências de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- DoR e DoD colados no quadro: seção "Políticas" de registro do portfólio na pasta do caso (portfólio) ou de
  quadro Kanban na pasta do caso; DoD por tipo em checklist por tipo na pasta do caso
  (acréscimo do laboratório).
- No cartão: campo "Pronto é" (DoR) e campo "Prova" (DoD) preenchidos.
- Resultado da checagem: Revisão do Ciclo na pasta do caso (linha prometido × entregue × prova).
- Depois: cartão sem DoR volta a Em preparação; cartão sem DoD fica em "Em prova" com marca, sem
  ré; checklist de 6 perguntas do ritmo vai para acordo de cadência do time toda sexta.

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
| Documento | `<nome>.html` — documento corrido no design system do laboratório | quando HTML for escolhido | `../assets/modelos/documento.html` (em produção) |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-dor-dod-lab.html` |

Modelos canvas desta skill (specs `dor-dod-lab`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-dor-dod-lab.html` **(padrão)** | Portões DoR / DoD (laboratório) · família laboratorio | "no canvas do laboratório" | pronto |

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
| Leve | uma pessoa | DoR: dono, "pronto é", cabe na semana. DoD: prova citada, verbo honesto. |
| Intermediária | um time | DoR completo (9 itens) + DoD genérico + DoD por tipo das 2–3 tarefas mais comuns |
| Robusta | organização / produção | tudo + gates mapeados de uma vez, Aceitante separado, métrica de negócio rotulada por empresa, registro durável e versão; commit quando houver repositório; checklist das 9 etapas no fechamento do trimestre |

## Erros comuns

- "Pronto" sem definição escrita: cada um entrega uma coisa.
- Cartão puxado sem dono, sem "pronto é" ou sem origem — e descoberto na sexta.
- Gate descoberto no dia da entrega (um por vez) em vez de mapeado no DoR.
- "Buildei local / deveria funcionar" como prova.
- Prova sem hora e sem caminho: "testei e funciona".
- Medir só tarefas e esquecer a meta do produto (A03, A07).
- Entregar com gate exigido ainda pendente.
- Aceite pelo próprio executor, ou "GO" local tomado por aceite.
- Entrega sem arquivo, sem versão registrada, sem resposta a quem pediu: aconteceu só na memória.
- Checklist das 9 etapas aplicado a cada cartão, inteiro — é do trimestre, não do cartão.
