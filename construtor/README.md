# Construtor de canvas e documento

Gera, a partir de um arquivo `.md` preenchido, o **canvas oficial** do curso (réplica do PDF, com o
texto por cima) e a **forma documento** (o mesmo conteúdo em documento corrido). Só precisa de
Python 3.10 ou mais novo; não instala nada.

## Como usar

1. Copie o template da skill: `skills/<skill>/assets/modelos/template-<id>.md`.
2. Preencha as células e os blocos. Não apague as marcas `<!-- c:... -->`: elas dizem ao construtor onde
   está cada campo. O que você não souber fica em branco.
3. Gere:

```bash
python3 construtor/construir.py <id> --documento --md meu-caso.md --saida meu-caso.html
python3 construtor/construir.py <id> --canvas    --md meu-caso.md --saida meu-caso-canvas.html
```

`<id>` é o identificador do canvas (tabela abaixo). Abra o HTML no navegador; o botão "imprimir / PDF"
sai em uma página no tamanho do canvas original.

Sem Python: copie `canvas-<id>.html` e escreva dentro das `div[data-campo]`, mantendo os ids.
Os ids e o texto-guia de cada campo estão em `assets/modelos/CAMPOS.md` da skill.

## Canvas disponíveis

| id | canvas | skill | família | padrão |
|---|---|---|---|---|
| `visao-kit-01` | Canvas de Visão | `ga2-canvas-de-visao` | kit | sim |
| `okr-kit-02` | OKR Canvas | Objetivos e Resultados-Chaves | `ga2-okr-canvas` | kit | sim |
| `briefing-projeto-kit-5-1` | Briefing de Projeto | `ga2-briefing-iniciativa` | kit | sim |
| `briefing-processo-kit-5-2` | Briefing de Processo | `ga2-briefing-iniciativa` | kit | sim |
| `briefing-produto-kit-5-3` | Briefing de Produto / Serviço | `ga2-briefing-iniciativa` | kit | sim |
| `backlog-2d-kit-06` | Backlog | 2 Dimensões | `ga2-backlog-2d` | kit | sim |
| `backlog-priorizado-kit-6-1` | Backlog | 2 Dimensões Priorizado | `ga2-backlog-2d` | kit |  |
| `kanban-kit-07` | Kanban | Quadro de Acompanhamento Simples | `ga2-kanban-canvas` | kit | sim |
| `kanban-avancado-kit-7-1` | Kanban | Quadro de Acompanhamento Avançado | `ga2-kanban-canvas` | kit |  |
| `kanban-politicas-kit-7-2` | Políticas do Kanban | "Combinados" da Equipe | `ga2-kanban-canvas` | kit |  |
| `revisao-kit-08` | Revisão de Entregas | Debriefing | `ga2-review-do-ciclo` | kit | sim |
| `retrospectiva-kit-09` | Retrospectiva | Reflexões da Equipe | `ga2-retrospectiva` | kit | sim |
| `a3-kit-10` | Relatório A3 | `ga2-relatorio-a3` | kit | sim |
| `delegacao-kit-11` | Matriz de Delegação | `ga2-delegacao` | kit | sim |
| `feedback-360-kit-12` | Feedback 360 Graus | `ga2-feedback-360` | kit | sim |
| `pop-kit` | POP - Procedimento Operacional Padrão | `ga2-pop` | kit | sim |
| `pdi-kit` | Plano de Desenvolvimento Individual (PDI) | `ga2-pdi` | kit | sim |
| `planejamento-kit` | Canvas de Planejamento | `ga2-canvas-de-planejamento` | kit | sim |
| `planejamento-curso-kit` | Canvas de Planejamento (curso, 9 blocos) | `ga2-canvas-de-planejamento` | kit |  |
| `a3-v6` | Canvas Editável — A3 | `ga2-relatorio-a3` | v6 |  |
| `briefing-projeto-v6` | Canvas Editável — Briefing de Projeto | `ga2-briefing-iniciativa` | v6 |  |
| `briefing-produto-v6` | Canvas Editável — Briefing de Produto | `ga2-briefing-iniciativa` | v6 |  |
| `briefing-processo-v6` | Canvas Editável — Briefing de Processo | `ga2-briefing-iniciativa` | v6 |  |
| `backlog-2d-v6` | Canvas Editável — Backlog 2D | `ga2-backlog-2d` | v6 |  |
| `matriz-v6` | Canvas Editável — Matriz de Priorização | `ga2-matriz-esforco-impacto` | v6 | sim |
| `okr-v6` | Canvas Editável — OKR | `ga2-okr-canvas` | v6 |  |
| `kanban-canvas-v6` | Kanban Canvas (jornada v6) | `ga2-kanban-canvas` | v6 |  |
| `decisao-v6` | Canvas Editável — Decisão: Projeto ou Fluxo | `ga2-decisao-projeto-ou-fluxo` | v6 | sim |
| `plano-ciclo-v6` | Canvas Editável — Plano do Ciclo | `ga2-plano-do-ciclo` | v6 | sim |
| `retrospectiva-v6` | Canvas Editável — Retrospectiva | `ga2-retrospectiva` | v6 |  |
| `revisao-v6` | Canvas Editável — Revisão do Ciclo | `ga2-review-do-ciclo` | v6 |  |
| `gestao-diaria-v6` | Gestão Diária (folha individual) | `ga2-gestao-diaria` | v6 | sim |
| `painel-metricas-v6` | Canvas Editável — Painel de Métricas | `ga2-painel-do-gestor` | v6 | sim |
| `kaizen-v6` | Canvas Editável — Quadro Kaizen do Ciclo | `ga2-quadro-kaizen` | v6 | sim |
| `gemba-v6` | Canvas Editável — Roteiro do Vá e Veja | `ga2-gemba-walk` | v6 | sim |
| `delegacao-v6` | Canvas Editável — Quadro de Delegação | `ga2-delegacao` | v6 |  |
| `pdi-v6` | Canvas PDI (v6) | `ga2-pdi` | v6 |  |
| `cnv-v6` | Canvas de Conversa — CNV | `ga2-canvas-de-conversa-cnv` | v6 | sim |
| `feedback-360-v6` | Feedback 360 e Roteiro (v6) | `ga2-feedback-360` | v6 |  |
| `a3-esquerdo-b-05` | A3 — lado esquerdo (editável) | `ga2-diagnostico` | módulo | sim |
| `cinco-porques-b-06` | Causa raiz — 5 Porquês (editável) | `ga2-causa-raiz` | módulo | sim |
| `ponte-a3-okr-b-01` | Ponte A3 → OKR (editável) | `ga2-okr-canvas` | módulo |  |
| `checkpoint-b-07` | Checkpoint do Plano (editável) | `ga2-okr-canvas` | módulo |  |
| `politicas-quadro-b-05` | Políticas do quadro (editável) | `ga2-politicas-wip-urgencia` | módulo | sim |
| `status-report-b-04` | Status Report — 7 dias (editável) | `ga2-documentos-de-projeto` | módulo | sim |
| `resumo-ciclo-b-04` | Resumo do Ciclo (editável) | `ga2-documentos-de-projeto` | módulo |  |
| `sprint-plano-ciclo-c` | Sprint / Plano do Ciclo (jornada) | `ga2-plano-do-ciclo` | jornada |  |
| `status-report-b-04-p2` | Status Report — 7 dias (editável), página 2 | `ga2-documentos-de-projeto` | módulo |  |
| `resumo-ciclo-b-04-p2` | Resumo do Ciclo (editável), página 2 | `ga2-documentos-de-projeto` | módulo |  |
| `5w2h-lab` | 5W2H — plano de ação (laboratório) | `ga2-5w2h` | laboratório | sim |
| `pdca-lab` | PDCA (laboratório) | `ga2-pdca` | laboratório | sim |
| `ishikawa-lab` | Ishikawa — espinha de peixe (laboratório) | `ga2-causa-raiz` | laboratório |  |
| `dor-dod-lab` | Portões DoR / DoD (laboratório) | `ga2-checklist-producao-entrega` | laboratório | sim |
| `quem-faz-o-que-lab` | Quem faz o quê (laboratório) | `ga2-quem-faz-o-que` | laboratório | sim |
| `folha-experimento-lab` | Folha de experimento (laboratório) | `ga2-folha-de-experimento` | laboratório | sim |

Família: **kit** = canvas do kit do curso (padrão quando existe); **v6** = canvas editável da versão v6;
**módulo** = editável por módulo; **jornada** = folha individual da jornada; **laboratório** = canvas que
não existe no curso, desenhado no mesmo estilo do kit e marcado como acréscimo.

## Como o construtor lê o `.md`

- marca numa célula de tabela → o valor é a última célula da mesma linha;
- marca num título ou rótulo → o texto depois dela na mesma linha ou o bloco seguinte;
- marca sozinha numa linha, antes de uma tabela → a tabela inteira (linha por linha).
