---
name: agenda-visual
description: "Use para visualizar o planejamento de qualquer projeto como agenda, calendário ou linha do tempo em HTML inline ou imagem. Mostra fases, datas, dependências e responsabilidades; não cria eventos nem aprova o plano."
---

# Agenda visual

Transforme o plano do usuário em uma agenda visual que responda: quando acontece, o que fazer primeiro e quem faz o quê.
Serve para projetos, campanhas, eventos, implantação, estudos e rotinas com horizonte definido.
O planejamento continua sendo a fonte; o visual é uma visão dele.

## Escolha da saída

Respeite a escolha do pedido atual ou da conversa: HTML, imagem ou ambos. Não pergunte novamente quando estiver clara.
Sem escolha, pergunte antes de gerar: "Você prefere HTML interativo aqui na conversa ou uma imagem?"
Use o recurso de perguntas do ambiente quando disponível; caso contrário, pergunte no chat e aguarde a resposta.
Se o usuário delegar a escolha, use HTML, com prévia inline quando disponível.

- **HTML:** leia `references/html-por-ambiente.md`. Use a capacidade real da sessão, não apenas o nome da LLM.
- **Imagem:** siga a seção de imagegen e leia `references/prompt-imagem.md` somente neste modo.
- **Ambos:** produza as duas saídas a partir do mesmo plano, sem alterar os fatos entre elas.

Imagegen é uma opção para pedidos de imagem; não é dependência do HTML.
Uma falha no modo imagem não autoriza trocar a saída por HTML sem combinar com o usuário.

## Entrada e fidelidade

Use o documento, arquivo ou briefing indicado. Se o usuário disser "isso", use o planejamento mais recente da conversa.
Leia a versão atual quando houver documento editável; preserve as edições humanas.
Se não houver um plano identificável, peça que o usuário indique o projeto ou forneça suas etapas.
Não exija um formulário quando a conversa já tiver os dados.

Antes de desenhar, organize os dados numa estrutura de trabalho, sem obrigar a criação de outro arquivo:

- Nome do projeto, objetivo da visualização e fontes consultadas.
- Período, ano, data de referência e fuso quando houver horários ou ações relativas a hoje.
- Fases e marcos: início, fim, ação ou entrega, responsável e dependências conhecidas.
- Situação de cada item: aprovado, proposto, pendente, em andamento ou concluído, conforme a fonte.
- Ações do usuário e decisões que ainda precisam de aprovação.

Não invente prazo, pessoa, orçamento, meta ou aprovação. Use "A definir" quando faltar informação não bloqueante.
Um item pode estar aprovado e ainda não ter começado; preserve essa distinção.
Se o pedido incluir sugestões de planejamento, identifique-as como propostas, separadas dos compromissos existentes.

Confira datas impossíveis, ordem dos marcos, dias da semana e conflitos entre fontes antes de gerar.
Não resolva divergências materiais em silêncio. Pergunte quando a resposta mudar o calendário; caso contrário, marque a pendência.
Uma sobreposição só é conflito se houver restrição ou dependência que a torne incompatível.
Sem ano confirmado, não acrescente dia da semana. Sem data de referência, não afirme "atrasado" ou "começar agora".

## Escolha do visual

Respeite o formato solicitado. Sem escolha explícita:

- Use agenda vertical para explicar fases sucessivas, ações e responsabilidades. Em imagem, retrato 2:3 é um ponto de partida.
- Use calendário mensal ou semanal para localizar poucos marcos em dias concretos. Confira o alinhamento dos dias.
- Use linha do tempo com faixas paralelas quando sobreposições e dependências forem a pergunta principal.

Preserve todas as fases relevantes no panorama. Condense tarefas menores antes de diminuir a letra.
Se o conteúdo não ficar legível, separe panorama e detalhe. Em HTML, use expansão por etapa; em imagem, combine a divisão antes de gerar várias.
Não apresente cartões igualmente espaçados como uma escala proporcional de duração.

Mostre título, período, data de referência, fases, datas, ações e legenda de situação.
Destaque a próxima ação conhecida e as entregas do usuário, quando sua responsabilidade estiver identificada.
Use "Você" apenas para responsabilidades confirmadas; para as demais, mantenha o nome ou "Responsável a definir".
Se o marco já passou, preserve a data e indique "Confirmar andamento" quando não houver registro de conclusão.

Use rótulos e estilos de borda além de cores. Propostas e pendências devem continuar claras em preto e branco.
Separe decisões pendentes de tarefas autorizadas. Dar destaque visual nunca autoriza executar uma ação.

Em campanhas, mostre aquecimento, início dos convites, abertura dos grupos, revelação, vendas e pós-venda quando constarem no plano.
Em outro projeto, use as fases reais dele. Não imponha grupos, Black Friday nem uma cadência de lançamento.

## Identidade visual

Use a identidade visual do projeto. Sem identidade fornecida, adote fundo claro, texto escuro e uma cor de destaque.
Em HTML inline, respeite o tema, a acessibilidade e os componentes exigidos pelo ambiente.
Para MindMaster, use verde-azulado #3D9B9D, grafite #1F2937, fundo #FAFAF8 e Manrope ou equivalente disponível.
Prefira datas em destaque, margens generosas e agrupamentos claros. Evite fotos, logos inventados e enfeites sem função.
Adapte o idioma ao usuário e escreva rótulos curtos, com verbos concretos.
Use apenas os dados necessários ao visual, sem credenciais ou dados pessoais desnecessários.

## Geração com imagegen — somente para imagem

Leia `references/prompt-imagem.md` e monte o prompt com os textos finais e as restrições factuais.
Use a ferramenta imagegen disponível no ambiente; ela pode se chamar `image_gen`, `imagegen` ou equivalente documentado.
Leia a skill de imagegen do ambiente, quando disponível, para respeitar seu contrato de execução e edição.
Não invente nomes de ferramentas, parâmetros ou acesso a arquivos.

Modelo requerido: `gpt-image-2.5-sunburst`. Se houver seletor, informe esse modelo e confira a resposta.
Sem seleção ou confirmação do modelo, informe a limitação e entregue o briefing e o prompt preparados.
Nesse caso, não alegue geração nem uso do modelo. Outro modelo exige autorização explícita.
Não abra uma rota de API paga nem instale dependências como alternativa automática.

Qualquer LLM pode interpretar estas instruções; gerar a imagem exige uma ferramenta de imagem acessível à sessão.
Sem essa capacidade, entregue o prompt reutilizável e diga que a imagem não foi gerada.
Não substitua a imagem pedida por HTML ou SVG sem combinar com o usuário.

Para revisar uma imagem existente, inspecione-a antes e use a operação de edição da ferramenta.
Declare o que muda e o que deve permanecer, sobretudo datas, situação e conteúdo aprovado.

## Conferência e entrega

Compare o visual com o plano e confira a saída conforme o modo:

- Datas, ano, horários, dias da semana e ordem das fases estão corretos.
- Nenhuma fase, dependência crítica ou ação do usuário desapareceu.
- Proposto, aprovado e pendente continuam distintos; o visual não adicionou compromissos.
- Textos estão legíveis, sem cortes, duplicações ou alterações de sentido.
- O usuário encontra a próxima ação e os marcos principais sem ampliar repetidamente a saída.

Em HTML, confira responsividade e as interações existentes pelo procedimento da referência.
Em imagem, inspecione a saída; se houver erro, corrija o trecho afetado com imagegen e confira o que mudou.
Se o ambiente não permitir inspecionar a saída, declare a limitação e não chame o visual de conferido.
Não repita gerações sem uma mudança concreta; pare e relate quando a ferramenta não permitir corrigir o problema.

Mostre a saída inline quando houver suporte, seguindo o contrato do ambiente. Para uso no projeto, salve a versão escolhida na pasta indicada.
Sem destino indicado, use uma pasta de saída do projeto e um nome com projeto, data e versão.
Não sobrescreva um arquivo existente sem pedido de substituição. Envie ao Drive ou outro serviço somente quando estiver no escopo.
Imagens mantêm seu formato de mídia; documentos de apoio seguem as regras do destino.
Na entrega HTML, use o recurso nativo; sem ele, entregue o arquivo ou código HTML e informe a ausência de prévia inline.
Não substitua a prévia inline disponível por um link. Para exportar, siga o procedimento do ambiente.
Identifique fontes do plano e pendências relevantes, sem repetir o panorama no chat.
Na entrega de imagem, informe confirmação ou limitação do modelo; deixe o prompt acessível para revisão.

## Exemplo de pedido

"Use agenda-visual neste plano de implantação. Mostre as fases, quando começamos os testes e o que depende de mim."
