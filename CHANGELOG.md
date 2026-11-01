# Histórico de versões

## 0.5.0 - 01/11/2026

- 40 habilidades: entram sete habilidades de rotinas do gestor, reunidas na nova trilha 7, "Rotinas do gestor".
  - `ga2-sistema-de-rotinas`: calendário do dia ao ano, inventário com o custo por semana de cada rotina e plano de implantação em 90 dias.
  - `ga2-agenda-do-lider`: a semana de quem coordena trabalho e gente, com a pedra grande primeiro, blocos de concentração e a revisão pessoal do líder.
  - `ga2-conversa-individual`: acompanhamento de pauta aberta, conversa de motivação, acompanhamento do PDI e conversa de permanência.
  - `ga2-contratar-e-integrar`: teste do gargalo antes da vaga, seleção com critérios escritos antes e integração em degraus.
  - `ga2-reunioes-e-comunicados`: reunião que termina em decisão escrita, com teto e custo, revisão mensal e comunicado de mudança em três grupos.
  - `ga2-registro-de-decisoes-e-riscos`: decisão com motivo, dono e data de rever, lista de riscos com sinal e resposta, e revisão da decisão.
  - `ga2-estagio-do-time`: estágios de Tuckman, Termômetro da Confiança e plano de transição de uma mudança.
- 14 habilidades ganham modos novos: `ga2-gestao-diaria` (preparar o dia e fechar o expediente), `ga2-delegacao` (levantamento das aprovações), `ga2-pdi` (PDI do próprio líder e conversa de carreira), `ga2-politicas-wip-urgencia` (antes de abrir vaga e canal oficial por tipo de pedido), `ga2-abrir-projeto` (pasta de área ou de rotina), `ga2-backlog-2d` (poda mensal), `ga2-pop` (cobertura e substituto), `ga2-quem-faz-o-que` (papel previsto contra papel assumido e transição), `ga2-plano-do-ciclo` (capacidade e carga por pessoa), `ga2-5w2h` (orçado, contratado e realizado), `ga2-kanban-canvas` (dependência entre áreas), `ga2-review-do-ciclo` (voz do cliente do mês), `ga2-folha-de-experimento` (testar ferramenta) e `ga2-feedback-360` (revisão de desempenho, feedback na hora e reconhecimento).
- `ga2-me-mostra` roteia os pedidos visuais para as sete habilidades novas, e `docs/TRILHAS.md` ganha a trilha 7.
- `scripts/validar.py` passa a derivar da pasta `skills/` e de `docs/TRILHAS.md` a contagem de habilidades e de trilhas, em vez de exigir um número fixo.

## 0.4.2 — 31/10/2026

- 33 habilidades: entra `agenda-visual`, que transforma o planejamento de qualquer projeto em agenda, calendário ou linha do tempo, com fases, datas, responsabilidades e pendências.
- Pergunta entre HTML e imagem quando o formato não estiver definido. HTML usa o recurso inline do ambiente ou um arquivo independente; imagem só quando o usuário escolhe, com o modelo requerido, e sem ele entrega o briefing e o prompt.
- Instalador, exportação do método e validação passam a aceitar a habilidade sem o prefixo `ga2-`; testes de exportação ampliados.
- Versão própria, fechada antes do lote de rotinas (0.5.0).

## 0.4.1 — 10/09/2026

- `ga2-briefing-iniciativa`: quando o gestor não traz as entregas do projeto, a habilidade propõe de 4 a 7 a partir do "entra" do escopo, puxa o marco do prazo e pede aceite item a item. Antes, o campo ficava em branco ou parava a conversa.

## 0.4.0 — 06/09/2026

- 32 habilidades: entra `ga2-abrir-projeto`, adaptação pública da `project-scaffold`.
- Abertura de projeto passa a ser o primeiro passo do catálogo e da jornada integrada.
- A nova habilidade organiza responsável, definição do projeto, andamento, aprovações e evidências; também mantém projetos existentes.

## 0.3.0 — 04/09/2026

- 31 habilidades: entra `ga2-canvas-de-planejamento` (a folha de nove blocos da versão ao vivo do curso).
- Cada habilidade de artefato ganha modelos em `assets/modelos/`: canvas oficial em branco (réplica do PDF do curso), forma documento em branco, `template-<id>.md` com as marcas de campo e `CAMPOS.md`.
- Construtor em `construtor/`: gera o canvas e o documento a partir do `.md` preenchido, só com Python.
- Seis canvas desenhados no estilo do kit para artefatos sem canvas oficial (5W2H, PDCA, Ishikawa, DoR/DoD, Quem faz o quê, Folha de experimento), com selo de acréscimo.
- Seção "Canvas oficial e documento" em cada `SKILL.md` que tem canvas.

## 0.2.1 — 03/09/2026

- Corrigido o `ga2-me-mostra` para usar o caso de gestão ativo da conversa como objeto visual.
- Impedido o uso do nome do plug-in ou do método como assunto substituto.
- Adicionada uma pergunta curta de esclarecimento quando não houver caso de gestão identificável.
- Atualizado o prompt de invocação da habilidade para preservar o contexto da conversa.
- Adicionados dois testes de regressão: contexto gerencial ativo e conversa fora do escopo.

## 0.2.0 — 03/09/2026

- Adicionado o manifesto do plug-in Gestão Ágil 2.0 com as 30 habilidades.
- Adicionada identidade visual do plug-in com a paleta MindMaster.
- Organizadas as 29 habilidades do método em seis trilhas pedagógicas.
- Mantido `ga2-me-mostra` como camada visual compartilhada.
- Preparados cinco testes positivos e três negativos para revisão pública.
- Adicionados materiais de privacidade, termos, suporte e publicação.
- Removida a dependência de uma sintaxe específica nos prompts iniciais das habilidades.

## 0.1.0 — 03/09/2026

- Primeira versão técnica das 30 skills.
- Instalação para Claude, Codex/GPT, Cursor, OpenCode e pasta compatível.
- Conteúdo público separado das regras e dos exemplos internos.
- `ga2-me-mostra` gera HTML e usa o recurso visual disponível no ambiente.
- Linguagem simples obrigatória em todas as skills.
