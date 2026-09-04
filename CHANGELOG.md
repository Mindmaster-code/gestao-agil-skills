# Histórico de versões

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
