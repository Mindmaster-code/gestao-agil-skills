# Vá e Veja (Gemba Walk)

## O que é e quando usar

Gemba = o lugar onde as coisas acontecem. Genchi genbutsu = "vá e veja" com os próprios
olhos. "Vá para o local do problema, veja, sinta, execute junto, converse com quem faz — e não
só olhe relatórios ou o relato de outras pessoas." É comportamento, não técnica.

Use quando o número caiu e ninguém sabe por quê; antes de escrever um A3; no passo do fluxo
que mais trava; e, por regra, pelo menos uma hora por mês. Entra antes: um número ruim do
painel ou um cartão parado. Sai depois: **um fato que nenhum relatório contaria**, levado
para a retro, o A3 ou o Quadro Kaizen.

Vive no **Passo 5 — Melhoria Contínua** (M07 A12; v6 aula 08).

## Fonte no método

- Base do método — Passo 5: Melhoria Contínua §2.16, §4.4, §6.4, regras 18, 19 e 21, divergência 18 — M07 A12; v6 aula 08.
- Template oficial: Canvas Editável — Roteiro do Vá e Veja, v6, Passo 5 (referência de origem; modelo público nos assets).
- Regra de verificação adotada pelo laboratório: "pronto só depois de verificar pelo caminho real do usuário".

## O gemba de uma operação de agentes `(acréscimo do laboratório)`

Em uma operação digital, o local de trabalho pode ser um sistema. "Ir ao lugar" é abrir a prova pelo caminho real em vez de ler
o report de quem fez:

| Problema | Onde é o gemba | O que olhar |
|---|---|---|
| timer ou serviço não produz | `journalctl --user -u <serviço> -n 30 --no-pager` | última batida, erro, quem foi pulado e por quê |
| cartão parado | `STATUS.md` do projeto, `git log -5` do repo | data da última linha real, não a data do cabeçalho |
| diretor em silêncio | canal de pedidos e histórico de leitura | carta lida e não respondida × carta nunca aberta |
| report "feito" | o arquivo em registro de relatórios escolhido, a URL, o log citado | a prova existe e bate com o texto? |
| pulso diário | registro diário da área | o que o agente viu hoje, em vez do resumo |
| aluno ou cliente travado | URL de produção logado como aluno; tópico do Telegram | a tela que a pessoa vê |

Só leitura. O Gestor não roda comando de produção (systemd start/stop, deploy, banco) — isso é
do responsável técnico autorizado. Ler log, listar arquivo e abrir URL é observar; mudar é executar.

## Como conduzir

1. **Escolher o lugar.** Pergunta: "Qual passo do fluxo mais trava hoje?" Escreve onde é o
   gemba (serviço, arquivo, caixa, URL). Recusa: gemba escolhido por conveniência.
2. **Escrever a pergunta antes de ir.** Uma só. "O que eu quero entender?" Recusa: pergunta
   que começa com "quem" — vira caça ao culpado.
3. **Com quem.** Quem executa, não quem reporta: o agente dono do cartão, o log do serviço, o
   aluno na tela. Marcar quando e quanto tempo (1–2 h; em operação digital, 15–30 min por gemba de log).
4. **Observar sem corrigir.** Anotar **só o que viu**: linha do log, data do arquivo, texto
   da carta. Recusa: opinião ("parece desorganizado"); corrigir no meio da observação.
5. **O que me surpreendeu.** Uma linha — o fato que o relatório não contaria.
6. **Por que isto acontece.** 5 porquês até a causa no processo, nunca na pessoa.
7. **Contramedida.** Cabe num teste pequeno → Quadro Kaizen; causa incerta ou várias áreas →
   A3; exige código, infra ou timer → pedido ao responsável técnico: o que, por quê, dono, pronto é, prazo e onde trava.
8. **Quem padroniza e prazo.** Sair com uma ação, dono e data. Recusa: gemba que termina em
   "interessante".

## Regras do método que valem aqui

- "Vá ver antes de decidir. Relatório comprime a realidade." (M07 A12)
- "Uma hora por mês no lugar onde o trabalho acontece." (v6 aula 08)
- "Pergunta escrita antes, nunca começando com 'quem'." (v6 aula 08)
- "Observe o processo pessoalmente; converse com quem executa; não culpe nem julgue; planeje
  contramedidas; padronize e replique." (A12 — cinco princípios)
- "Problemas quase sempre têm causa raiz no processo, não nas pessoas. Se o processo permite
  que o erro aconteça, o erro vai acontecer." (M07 A12)
- "O número diz que caiu; só o lugar diz por quê." (canvas v6)
- "Métrica ruim gera pergunta e A3, não cobrança automática." (M07 A06)

## Saída

Os caminhos `.md` abaixo são convenções do fluxo de repositório. Em Word, Docs ou planilhas, use o destino escolhido.

- Arquivo: registro do Gemba com data e nome no destino escolhido (template em `template.md`).
- Depois: o fato vai para a retro da sexta, para um A3 (pasta escolhida para o A3) ou para o
  Quadro Kaizen; a contramedida que é código/infra vira pedido ao responsável técnico autorizado; o cartão do portfólio
  recebe "última prova" com a data do gemba. Pelo menos um gemba por semana num cartão parado.

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
| Documento | `<nome>.html` — documento corrido no design system dos modelos públicos | quando HTML for escolhido | `../assets/modelos/documento.html` (pronto) |
| Canvas | `<nome>-canvas.html` — réplica literal do canvas oficial, campos por cima | **quando pedido**: "gera o canvas", "no formato do curso", "igual ao PDF" | `../assets/modelos/canvas-gemba-v6.html` |

Modelos canvas desta skill (specs `gemba-v6`):

| Modelo | Origem | Pedido que o escolhe | Estado |
|---|---|---|---|
| `../assets/modelos/canvas-gemba-v6.html` **(padrão)** | Canvas Editável — Roteiro do Vá e Veja · família v6 | "no canvas v6" | pronto |

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

- **Leve** (gemba de log, 15 min): onde · pergunta · o que vi · surpresa · ação.
- **Intermediária** (cartão parado, 30–60 min): template completo.
- **Robusta** (problema que atravessa áreas, 1–2 h): com quem executa em mais de uma área,
  5 porquês completo, saída direto para A3.

## O que não fazer

- Transformar em fiscalização — "a equipe mostra a versão apresentável e você gastou a manhã
  para ver o relatório ao vivo".
- Corrigir durante a observação.
- Pergunta com "quem".
- Sair sem ação.
- Ler o report em vez da prova.
- Rodar comando que muda estado (start, restart, deploy, escrita em banco).
