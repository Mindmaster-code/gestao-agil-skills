# Me mostra — Gestão Visual GA 2.0

## Entrega editável

Ao criar ou revisar um artefato, leia [entrega-editavel.md](entrega-editavel.md). O formato pedido e o documento existente orientam a entrega.
Padrão desta skill, sem formato definido: visual HTML; Word `.docx`, Google Docs, Excel `.xlsx` ou Google Sheets quando solicitados.
Use ferramentas de arquivos ou a integração disponível para gerar e conferir a entrega real.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

## Objetivo

Mostre o menor visual que permita entender o caso e decidir sem perguntar de novo.

Sem outro formato solicitado, cada uso termina com um artefato HTML. Apresente esse HTML na forma visual nativa do ambiente.
Se ela não existir ou não estiver exposta, grave o HTML e mostre uma versão visual resumida
no terminal.

Esta skill define a **leitura visual**. A skill do artefato GA 2.0 define o conteúdo e suas
regras. Quando as duas se aplicarem, use primeiro a skill do artefato e depois esta skill
para apresentar o resultado. Não crie um segundo artefato paralelo.

Use para processo, estado, mudança, problema, prioridade, responsabilidade, dependência,
ritmo de trabalho ou ponto de aprovação. Não use para ilustração artística, peça de
marketing ou desenho de interface.

## Linguagem obrigatória

Escreva em PT-BR simples. A pessoa precisa entender o visual sem conhecer Gestão Ágil 2.0.

- Use a palavra comum antes do termo técnico.
- Explique toda sigla na primeira aparição, na mesma linha.
- Evite inglês quando houver uma palavra comum em português.
- Preserve o nome oficial de um artefato quando necessário e explique sua função.
- Use frases curtas, voz ativa e verbos diretos.
- Aplique esta regra no título, nos rótulos, nas legendas, nas dicas, no texto alternativo e
  na resposta final.

| Evite | Escreva |
|---|---|
| `WIP 2/3` | `2 de 3 trabalhos em andamento (WIP)` |
| `gate pendente` | `falta aprovação; pessoa responsável decide` |
| `DRI` | `dono único da entrega` |
| `handoff` | `passagem do trabalho` |
| `baseline` | `número de partida` |
| `as-is` | `como funciona hoje` |

Se o usuário trouxer um jargão, preserve-o apenas quando ajudar a referência. Traduza-o na
mesma frase. Nunca use uma sigla solta como rótulo principal.

Antes de entregar, releia apenas o texto visível. Sigla sem explicação ou jargão com
substituto comum reabre o trabalho.

## Como conduzir

1. **Escreva a pergunta que o visual responde.** Uma frase. Se houver várias perguntas,
   escolha a que libera a próxima decisão e cite o recorte.
2. **Classifique a intenção.** Use uma das quatro:
   - entender o estado atual;
   - entender uma mudança;
   - diagnosticar um problema;
   - tomar uma decisão.
3. **Separe o que é conhecido.** Marque fatos e números como `medido`, `estimado` ou
   `em aberto`. Ponha a fonte junto da afirmação. Não transforme hipótese em fato.
4. **Roteie para o artefato certo.** Leia
   [`roteamento-ga2.md`](roteamento-ga2.md) quando o caso pertencer
   a um artefato ou ritual do método.
5. **Escolha uma forma visual principal.** Processo pede fluxo; trabalho em curso pede
   quadro visual do trabalho (Kanban);
   diferença pede antes/depois; falha pede esperado/observado; causa pede 5 Porquês ou
   Ishikawa; escolha pede matriz ou árvore. Leia
   [`primitivas-visuais.md`](primitivas-visuais.md) quando precisar
   desenhar.
6. **Mostre só o contexto necessário.** Preserve origem, destino e ponto de decisão. Corte
   ramos que não mudam a leitura e marque a continuação com `…`.
7. **Escolha a forma de entrega.** Leia
   [`artefatos-por-harness.md`](artefatos-por-harness.md). Detecte o
   ambiente e as capacidades realmente expostas. Essa referência orienta apenas a saída HTML;
   para Word, Docs ou planilhas solicitados, siga Entrega editável. O ambiente prevalece sobre o modelo.
8. **Gere e apresente o formato escolhido.** Preserve pergunta, visual, prova e consequência.
   Para HTML, use a forma nativa quando disponível. Para documentos, siga a entrega editável.
9. **Feche com consequência.** Diga o que o visual prova, o que segue em aberto e qual
   decisão ou ação vem agora. Se houver ação, nomeie um dono e uma data. Se houver
   aprovação, nomeie quem decide.

## Escolha pela intenção

| Intenção | Visual principal | A leitura precisa responder |
|---|---|---|
| Estado atual | mapa de estado, Kanban ou painel | onde estamos e o que chama atenção? |
| Mudança | antes/depois, linha do tempo ou mapa de transição | o que muda, onde e com qual efeito? |
| Diagnóstico | esperado/observado, fluxo com ruptura, 5 Porquês ou Ishikawa | onde a realidade diverge e por quê? |
| Decisão | matriz, árvore de decisão ou opções comparadas | qual opção vence por qual critério? |

Use **um visual principal por pergunta**. Uma tabela curta pode servir como legenda ou
prova. Dois visuais só entram quando respondem perguntas diferentes e ambas são necessárias
para a mesma decisão.

## Semântica visual fixa

- **Base:** contexto necessário, sem destaque.
- **Foco:** elemento que responde à pergunta.
- **Exceção:** risco, bloqueio ou divergência que pede atenção.
- **Prova:** fonte, data e selo de procedência perto do dado.

Em HTML, use os tokens dos modelos públicos: teal para marca, medido e ok; laranja para risco e
estimativa; cinza para em aberto. Não use cor por decoração. Nunca dependa apenas da cor:
repita o significado em texto, rótulo ou forma.

## Contrato de saída

Quando a entrega escolhida for HTML, siga esta ordem. Para Word, Docs ou planilhas solicitados,
siga a seção Entrega editável e preserve a informação do visual em conteúdo editável:

1. crie a fonte HTML;
2. apresente-a na janela nativa do ambiente, como Artifact, Canvas, visualização ou prévia;
3. se não houver forma nativa, grave o HTML autônomo e mostre o resumo visual no
   terminal;
4. informe o caminho do HTML apenas na alternativa ou quando o ambiente pedir;
5. feche com prova, ponto em aberto e decisão ou próximo passo.

Use a capacidade realmente disponível. Não invente comando, link ou artefato nativo.
Se o recurso nativo falhar e o erro trouxer uma correção objetiva, faça uma correção. Sem
progresso, aplique a alternativa e diga qual capacidade faltou.

### HTML nativo

- Siga o contrato de estrutura, tema, segurança e referência da superfície ativa.
- Preserve a semântica GA 2.0: foco, exceção, prova, medido, estimado e em aberto.
- Um fragmento `.html` é válido quando o ambiente exigir esse formato para mostrar o visual.
- Não duplique no chat os dados que o artefato nativo já mostra.

### HTML autônomo

Use HTML autônomo quando não houver superfície nativa ou quando o artefato precisar circular:

1. leia `primitivas-visuais.md`;
2. parta de `../assets/template-artefato.html`;
3. gere HTML a partir da fonte atual; mantenha `.md` quando o fluxo precisar de versionamento;
4. use o destino definido pela skill dona do artefato;
5. sem destino definido, use a pasta escolhida pelo usuário, com nome curto para o HTML e fonte Markdown somente se necessária;
6. use SVG inline apenas quando mostrar uma relação que a tabela não mostra;
7. não acrescente biblioteca, CDN ou asset externo;
8. valide abertura do arquivo, tema claro, tema escuro e leitura no celular.

O título do HTML é a pergunta. A frase de abertura responde essa pergunta. Todo número tem
selo e fonte. A seção final mostra o que ainda está em aberto.

### Resumo no terminal

Mostre o resumo apenas na alternativa sem visual nativo. Use, nesta ordem:

1. leitura em uma frase;
2. tabela curta ou diagrama de texto monoespaçado;
3. prova e pontos em aberto;
4. decisão ou próximo passo;
5. caminho absoluto do HTML.

Só use Mermaid se o terminal confirmar que renderiza Mermaid. Mesmo assim, o Mermaid não
substitui o HTML.

## Guardrails

- Não invente dado, causa, dono, prazo, aprovação ou vínculo entre itens.
- Não desenhe uma árvore quando a resposta cabe em três linhas.
- Não use um fluxograma para esconder incerteza; mostre o ponto em aberto.
- Não misture estado atual e desejado sem rótulos claros.
- Não destaque tudo. Se tudo chama atenção, nada orienta a decisão.
- Não escolha a forma de entrega pelo nome do modelo. Escolha pelo ambiente e pelas capacidades
  expostas nesta sessão.
- CNV fica no chat por padrão; salve apenas quando solicitado, sem ampliar o compartilhamento.
- Criar o visual não autoriza publicá-lo nem ampliar seu compartilhamento. Respeite o destino e as pessoas autorizados pelo usuário.

## Critério de pronto

- A pergunta aparece antes do visual.
- O visual principal responde à pergunta em até 90 segundos.
- A relação importante é legível sem depender de cor.
- Fato, estimativa e ponto em aberto não se misturam.
- A fonte está ao lado da afirmação que sustenta.
- O fechamento nomeia consequência, decisão ou próximo passo.
- Título, rótulos e fechamento não contêm jargão ou sigla sem explicação.
- Uma pessoa sem vocabulário do método entende a leitura e a próxima decisão.
- A execução entregou o formato solicitado; sem escolha explícita, gerou HTML.
- A alternativa visual contém HTML autônomo e resumo; Markdown acompanha quando necessário ao fluxo.
