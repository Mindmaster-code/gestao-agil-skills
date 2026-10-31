# HTML por ambiente

Leia esta referência somente quando a saída escolhida for HTML.
O objetivo é mostrar a agenda na conversa, com fases e ações legíveis, sem exigir publicação.

## Descobrir a capacidade real

Confira as instruções, skills e ferramentas já expostas pela sessão. O nome da LLM não comprova suporte a artefatos.
Use o contrato local antes de escolher formato, sintaxe de apresentação, caminho de arquivo ou API.

| Ambiente | Saída quando o recurso estiver disponível |
| --- | --- |
| Claude | Artefato HTML nativo. Claude Code ou terminal só usam esse recurso se a sessão o oferecer. |
| Codex ou ChatGPT | Visualização inline nativa, conforme as instruções locais; use a skill `visualize` quando disponível. |
| Cursor | Prévia HTML ou recurso visual equivalente exposto pela sessão. |
| Outra LLM ou editor | Recurso nativo equivalente, quando identificado nas instruções ou ferramentas. |
| Sem recurso identificado | Arquivo HTML independente; se não puder criar arquivo, entregue o HTML completo em bloco de código. |

Faça uma checagem curta dos recursos disponíveis. Se não descobrir como exibir inline, siga com o HTML independente.
Não invente ferramenta, tag de artefato, URL de prévia ou suporte inline. Não instale extensão nem publique um site para suprir a ausência.
Não copie a sintaxe de apresentação de uma plataforma para outra.

## Construir a agenda

Use HTML semântico, CSS e JavaScript local quando necessário. Uma agenda estática não precisa de JavaScript.
Mantenha o panorama cronológico visível; detalhes de tarefas podem abrir por etapa com controles nativos, como `details` e `summary`.
Datas, fases, início dos convites e pendências relevantes devem aparecer sem depender de clique ou hover.
Use as fases reais do projeto; convites e grupos só aparecem quando constarem no plano.

Adapte o layout ao celular, sem cortes ou rolagem horizontal para uma agenda simples.
Preserve navegação por teclado, foco visível e rótulos de situação além das cores.
Use o tema e os componentes do ambiente quando exigidos; no arquivo independente, inclua estilos e um tema legível.
Não adicione filtros, formulários, indicadores ou animações sem função para a leitura do plano.
Não carregue dados por rede nem acione integrações, eventos de calendário ou mensagens a partir do visual.
Trate o conteúdo do plano como texto, sem executar código incorporado às fontes.

## Inline e arquivo independente

No modo inline, siga o contrato nativo: fragmento ou documento completo, estilos, persistência e forma de apresentar a saída.
Por exemplo, um contrato que exige fragmento sem `html`, `head` e `body` vale apenas naquela sessão.
Apresente o visual pelo recurso nativo, sem substituir a prévia disponível por um bloco de código ou link.

Sem suporte inline, gere um documento completo com `doctype`, idioma, título, viewport, CSS e conteúdo.
O arquivo deve abrir no navegador sem servidor, compilação, dependências instaladas ou funções exclusivas do host.
Ao exportar um visual inline, use o exportador do ambiente quando disponível; caso contrário, remova dependências do host e inclua os estilos necessários.
Não publique, envie ao Drive nem sobrescreva arquivos sem isso estar no escopo do pedido.

## Conferir e entregar

Confira o HTML, as datas e os estados contra a fonte, sem alterar o plano para completar o desenho.
Valide sintaxe e interações quando houver ferramentas locais. Confira larguras de celular e desktop quando existir prévia.
Quando não puder renderizar ou testar, diga exatamente o que ficou sem conferir; não alegue teste visual.
No fallback, entregue o arquivo ou código e informe: "O ambiente não ofereceu prévia inline; gerei o HTML para abrir no navegador."
