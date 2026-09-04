# Campos dos modelos canvas — `ga2-kanban-canvas`

Gerado pelo construtor (`construir.py --campos-md`). Não editar à mão.

## `kanban-avancado-kit-7-1` — Kanban | Quadro de Acompanhamento Avançado

| id | rótulo no canvas | texto-guia | âncora no template |
|---|---|---|---|
| `sprint_backlog` | Sprint backlog |  | `<!-- c:foto -->` |
| `etapa_1_nome` | Etapa 1 (nome) |  | `<!-- c:colunas_fluxo -->` (coluna: Coluna) |
| `etapa_1_limite` | Etapa 1 (limite máx.) |  | `<!-- c:colunas_fluxo -->` (coluna: Limite WIP) |
| `etapa_1` | Etapa 1 (cartões) |  | `<!-- c:foto -->` |
| `etapa_2_nome` | Etapa 2 (nome) |  | `<!-- c:colunas_fluxo -->` (coluna: Coluna) |
| `etapa_2_limite` | Etapa 2 (limite máx.) |  | `<!-- c:colunas_fluxo -->` (coluna: Limite WIP) |
| `etapa_2` | Etapa 2 (cartões) |  | `<!-- c:foto -->` |
| `etapa_n_nome` | Etapa N (nome) |  | `<!-- c:colunas_fluxo -->` (coluna: Coluna) |
| `etapa_n_limite` | Etapa N (limite máx.) |  | `<!-- c:colunas_fluxo -->` (coluna: Limite WIP) |
| `etapa_n` | Etapa N (cartões) |  | `<!-- c:foto -->` |
| `feito` | Feito |  | `<!-- c:foto -->` |
| `impedimentos_1` | Impedimentos (etapa 1) |  | `<!-- c:bloqueios -->` |
| `impedimentos_2` | Impedimentos (etapa 2) |  | `<!-- c:bloqueios -->` |
| `impedimentos_n` | Impedimentos (etapa N) |  | `<!-- c:bloqueios -->` |

## `kanban-canvas-v6` — Kanban Canvas (jornada v6)

| id | rótulo no canvas | texto-guia | âncora no template |
|---|---|---|---|
| `caso` | Nome do quadro (o meu caso) |  | `<!-- c:caso -->` |
| `coluna_1` | Coluna 1 |  | `<!-- c:coluna_1 -->` |
| `coluna_2` | Coluna 2 |  | `<!-- c:coluna_2 -->` |
| `coluna_3` | Coluna 3 |  | `<!-- c:coluna_3 -->` |
| `coluna_4` | Coluna 4 (opcional) |  | `<!-- c:coluna_4 -->` |
| `definicao_feito` | Como um item vira 'feito'? |  | `<!-- c:pronto -->` |
| `regras` | Regras do quadro — quando um item anda |  | `<!-- c:politicas -->` |
| `limite_wip` | Limite de itens em andamento |  | `<!-- c:limite -->` |
| `onde` | Onde vou montar o quadro |  | `<!-- c:onde -->` |
| `ritmo` | Meu ritmo de atualização |  | `<!-- c:ritmo -->` |

## `kanban-kit-07` — Kanban | Quadro de Acompanhamento Simples

| id | rótulo no canvas | texto-guia | âncora no template |
|---|---|---|---|
| `limite_fazendo` | Limite máx. (Fazendo) |  | `<!-- c:limites -->` (coluna: Limite) |
| `limite_validacao` | Limite máx. (Em validação) |  | `<!-- c:limites -->` (coluna: Limite) |
| `sprint_backlog` | Sprint backlog (planejado, a fazer) |  | `<!-- c:foto -->` |
| `fazendo` | Fazendo |  | `<!-- c:foto -->` |
| `em_validacao` | Em validação |  | `<!-- c:foto -->` |
| `feito` | Feito |  | `<!-- c:foto -->` |
| `problemas_impedimentos` | Problemas / impedimentos |  | `<!-- c:bloqueios -->` |

## `kanban-politicas-kit-7-2` — Políticas do Kanban | "Combinados" da Equipe

| id | rótulo no canvas | texto-guia | âncora no template |
|---|---|---|---|
| `politica_de_entrada` | Política de entrada | Regras para adicionar novas tarefas ao quadro. | `<!-- c:entrada -->` |
| `politica_de_limites` | Política de limites | Regras para limitar a quantidade de trabalho em paralelo em cada coluna ou no total do quadro. | `<!-- c:limites_politica -->` |
| `politica_de_definicao_de_pronto` | Política de definição de pronto (qualidade) | Critérios que determinam quando uma tarefa pode ser considerada concluída. | `<!-- c:pronto_politica -->` |
| `politica_de_atualizacao` | Política de atualização | Como e quando as atualizações no quadro devem ser feitas. | `<!-- c:atualizacao -->` |
| `politica_de_bloqueios` | Política de bloqueios | Como identificar, sinalizar e gerenciar tarefas bloqueadas. | `<!-- c:bloqueio -->` |
