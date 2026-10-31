# Prompt para gerar a agenda

Preencha este modelo com os dados do plano. Retire instruções e campos que não se aplicarem antes de chamar imagegen.
Este arquivo organiza o prompt; seus campos não são parâmetros da ferramenta.

```text
Use case: infographic-diagram
Entrega: imagem de agenda, calendário ou linha do tempo para consulta do projeto.
Objetivo: permitir enxergar a sequência, os marcos e o que cada pessoa precisa fazer.
Formato escolhido: {formato e proporção, com o motivo ligado à pergunta do usuário}.
Projeto: {nome real}.
Período: {intervalo e ano conhecidos}.
Data de referência: {data e fuso pertinentes; ou omitir se desconhecidos}.
Identidade visual: {cores, tipografia e referências autorizadas do projeto}.

Composição:
Título e período no topo. Organizar as fases em ordem cronológica.
Datas grandes; ações curtas; responsáveis próximos às ações.
Destacar a próxima ação confirmada e as entregas do usuário, quando identificadas.
Separar propostas e pendências com rótulos e bordas diferentes; não depender apenas da cor.
Se usar grade de calendário, alinhar cada data ao dia correto da semana.
Se usar escala temporal proporcional, representar durações e sobreposições fielmente.
Se usar agenda de cartões, não sugerir que o tamanho do cartão representa duração.

Texto visível, por bloco, a reproduzir fielmente:
{título, subtítulo, fases, datas, ações, responsáveis, situação, legenda e rodapé finais}.

Relações que precisam aparecer:
{dependências e sobreposições presentes no plano; omitir se não existirem}.

Pendências que precisam continuar explícitas:
{itens propostos, decisões em aberto e informações a definir; omitir se não existirem}.

Restrições:
Não inventar nem alterar datas, nomes, responsáveis, compromissos ou aprovação.
Não promover uma proposta a tarefa autorizada. Não acrescentar fases para completar o desenho.
Não criar promessas, métricas, orçamento ou urgência.
Priorizar legibilidade. Não cortar texto nem reduzir tudo a letras pequenas.
Sem logos inventados, fotos decorativas, emojis ou moldura de aparelho.
```

Antes da chamada, confira os textos visíveis contra a fonte. Modelos e dimensões devem usar apenas opções reais da ferramenta.
O nome do modelo no texto do prompt não seleciona o modelo. Faça essa escolha na ferramenta e confira quando disponível.

Em revisão, acrescente:

```text
Alterar somente: {mudança solicitada}.
Preservar: {conteúdo, datas, situações, identidade e composição que devem permanecer}.
```
