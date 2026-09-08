---
name: ga2-abrir-projeto
description: "Abre ou organiza a pasta durável de um projeto com responsável, acordo inicial, status, fases e evidências, localmente ou no Google Drive. Use para iniciar ou arrumar um projeto; não use para uma dúvida pontual."
---

# Abrir projeto

Use esta habilidade quando uma iniciativa precisa de um lugar durável para decisões, trabalho, evidências e acompanhamento. Ela serve tanto para abrir um projeto quanto para organizar uma pasta existente. Não imponha a abertura de projeto para uma pergunta, uma tarefa isolada ou uma decisão que se resolve no chat.

O resultado é uma pasta que outra pessoa consegue entender sem recuperar o histórico da conversa: há um responsável único, objetivo, limites, estado atual, próxima decisão e provas preservadas.

## Antes de criar ou alterar

1. Descubra se há uma pasta existente para o mesmo esforço. Se houver, mantenha-a; não crie uma segunda versão em paralelo.
2. Confirme nome, local e um responsável pelo resultado. Quando ainda não houver pessoa definida, registre isso como ponto em aberto em vez de inventar um nome.
3. Defina a necessidade de aprovação pelo risco da próxima ação. Peça aprovação somente para uma decisão, gasto, compromisso externo ou mudança irreversível que realmente a exija.
4. Se o ambiente não permitir criar arquivos, entregue abaixo a estrutura e os documentos em formato copiável. Diga que a estrutura foi preparada para copiar; não diga que criou uma pasta.

Leia [references/metodo.md](references/metodo.md) antes de estruturar o projeto. Leia [references/fontes.md](references/fontes.md) se precisar explicar a procedência do método.

## Estrutura padrão

Use o nome do projeto escolhido pelo usuário. Para projetos novos, adote estas seis pastas, com nomes em português:

```text
<projeto>/
  Guia do projeto.docx
  Status do projeto.docx
  01 - Contexto e abertura/
    Abertura do projeto.docx
  02 - Planejamento/
  03 - Execução e acompanhamento/
  04 - Revisão e aprendizados/
  05 - Encerramento/
  06 - Referências e anexos/
```

O exemplo usa Word. No Google Drive, crie documentos Google Docs nativos, sem extensão no título.
Se o usuário escolher um fluxo de repositório, use Markdown: `README.md`, `STATUS.md` e `01 - Contexto e abertura/ABERTURA.md`.
Não gere versões Markdown e HTML extras por padrão.

Use os modelos de conteúdo em [assets/templates/](assets/templates/): `README.md` para o guia, `STATUS.md` para o status e `PROJECT-CHARTER.md` para a abertura.
Adapte títulos, formato e links ao destino real; os modelos Markdown não determinam o formato da entrega.
Não deixe texto de exemplo como se fosse fato. Se o pedido for somente pelas pastas, respeite esse limite e não crie documentos.

## Como conduzir

- Preencha a abertura em `01 - Contexto e abertura` com problema, objetivo, limites, métricas, papéis, dependências e riscos conhecidos.
- Se já houver briefing que cumpra esse papel, use-o como acordo inicial. Não crie um segundo documento com as mesmas decisões.
- Mantenha o status na raiz como visão viva: fase, atualização, itens abertos com responsável, itens fechados com prova e próximo passo ou decisão.
- Crie um registro de aprovação somente enquanto houver decisão pendente que o exija. Use `REVIEW-GATE.md` como modelo de conteúdo.
- Mantenha as evidências junto da fase que comprovam. `06 - Referências e anexos` guarda fontes e anexos compartilhados; os documentos apontam para eles.
- Preserve a estrutura de projetos existentes. Mapeie as funções das pastas antes de propor migração; não renomeie ou mova conteúdo só para impor o padrão novo.

As seis pastas organizam o ciclo de vida; não obrigam a produzir todos os documentos na abertura.
Escolha a forma leve, intermediária ou robusta conforme risco, duração e necessidade de acompanhamento, usando a referência do método.
Sem esses dados, comece leve e registre a escolha como provisória. Crie os documentos das próximas fases quando forem necessários.
Para detalhar o dossiê ou um briefing, use `ga2-documentos-de-projeto` e `ga2-briefing-iniciativa`, quando disponíveis.

## Criação e conferência por destino

Crie a estrutura somente nos destinos pedidos. Se o usuário pedir local e Google Drive, crie a raiz e as seis subpastas em ambos.
No Drive, confira os IDs das pastas e seus pais; uma raiz criada não comprova que as subpastas existem.
Depois de criar, liste o conteúdo em cada destino e reabra os documentos produzidos para conferir conteúdo e links.
Informe separadamente o que foi criado e o que ficou pendente em cada local. Nunca use a conferência local como prova do Drive.
Duas cópias não ficam sincronizadas automaticamente. Quando houver ambas, identifique qual será atualizada como fonte principal e registre essa escolha no guia.

## Entrega

Informe o caminho da pasta, o responsável, a fase atual, a próxima decisão e o que está pronto ou bloqueado. Se faltarem fatos essenciais, entregue o esqueleto com os campos marcados como “em aberto”.

## Entrega editável

Ao criar ou revisar um artefato, leia [references/entrega-editavel.md](references/entrega-editavel.md). O formato pedido e o documento existente orientam a entrega.
Padrão desta skill, sem formato definido: documento Word `.docx`; Google Docs quando esse for o destino escolhido.
Use ferramentas de arquivos ou a integração disponível para gerar e conferir a entrega real.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Em cada destino, use links reais para as pastas e documentos conferidos.
