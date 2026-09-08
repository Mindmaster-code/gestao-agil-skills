<!-- modelos de origem: dor-dod-lab.json -->
# Checklist de produção e entrega — template (DoR / DoD)

Três partes: (A) o checklist original de 9 etapas da aula M06 A09, como está no PDF; (B) o DoR
do laboratório, derivado das etapas 1–4 e do contrato mínimo do modelo operacional (§5); (C) o DoD da
laboratório, derivado das etapas 5–8, do Canvas 7.2 e da regra "prova pelo caminho real". Campo que a
aula não cita vem marcado `(acréscimo do laboratório)`.

---

| Campo | Preencha |
|---|---|
| Cartão / frente <!-- c:cartao --> | |
| Dono (um nome) <!-- c:dono --> | |
| Data <!-- c:data --> | |

## A. Checklist de Planejamento e Execução — 9 etapas (M06 A09, texto do PDF)

Use no fechamento de trimestre e na abertura de frente nova; não cartão a cartão.

| Etapa | Itens (como no PDF) | Artefato | OK |
|---|---|---|---|
| 1 Planejamento e preparação | Canvas de Planejamento: contexto, situação atual, ideal, gap, causa raiz | Canvas de Planejamento / A3 | [ ] |
| 2 Objetivos (OKR) e preparação | OKRs do trimestre; iniciativas por KR; Briefing do Projeto | OKR Canvas, Briefing | [ ] [ ] [ ] |
| 3 Backlog | backlog detalhado com tarefas e atividades | Backlog 2D | [ ] |
| 4 Planejamento do sprint | reunião de alinhamento com briefing; metas e métricas do sprint; meta, início e fim; equipe com nome e função; sprint backlog; ações para riscos | Canvas Sprint Plan, Briefing | [ ] [ ] [ ] [ ] [ ] [ ] |
| 5 Ritmo de execução | daily scrum; implementar o sprint backlog priorizado; atualizar o Kanban diariamente | Kanban Canvas | [ ] [ ] [ ] |
| 6 Monitoramento e controle | acompanhar indicadores diariamente | — | [ ] |
| 7 Avaliação e aprendizado | resultados × metas; Sprint Review; Retrospectiva | Canvas Review, Retro | [ ] [ ] [ ] |
| 8 Encerramento do sprint | status dos objetivos e KRs (perto, alcançado, superado, replanejar) | OKR Canvas | [ ] |
| 9 Próximo planejamento | OKRs do próximo trimestre; atualizar backlog com lições | OKR Canvas, Backlog 2D | [ ] [ ] |

Campos que o agente acrescenta ao usar `(acréscimo do laboratório)`: data da checagem ·
responsável · item marcado/falhou · onde voltar.

### Checklist do ritmo — 6 perguntas (v6 aula 09; nenhuma aceita "mais ou menos")

| Pergunta | sim/não | Se não, volta para |
|---|---|---|
| Duração do ciclo escolhida e fixa? | | Decisão projeto ou fluxo |
| Toda semana abre com meta escrita? | | Plano do Ciclo |
| Diária no mesmo horário, em frente ao quadro, 15 min? | | Gestão diária |
| Quadro com limite e fila olhada? | | Políticas de WIP |
| Política escrita para urgência? | | Política de urgência |
| Revisão e retrospectiva toda vez, com uma ação de cada? | | Ciclo semanal |

---

## B. Definition of Ready — o cartão pode entrar em execução?

Cartão: P-__ · Dono: ______ · Checado por: ______ em __/__/____

<!-- c:dor -->
| # | Item | Origem | OK | Se falta, o que escrever |
|---|---|---|---|---|
| 1 | Origem: contramedida do A3 / iniciativa do OKR / entrega do Backlog 2D | etapas 1–3 | [ ] | |
| 2 | Dono único (nome de pessoa) | etapa 4 "equipe com nome e função"; §5 | [ ] | |
| 3 | Aceitante nomeado (ou verificação objetiva) | §5 | [ ] | |
| 4 | "Pronto é" escrito — prova pelo caminho real | etapa 4 "metas e métricas"; 6 linhas | [ ] | |
| 5 | Cabe em uma semana; quebrado em tarefas ≤ 1 dia | etapa 4 "sprint backlog"; v6 04 | [ ] | |
| 6 | Compromisso: Comprometida (capacidade confirmada pelo diretor) | §9 | [ ] | |
| 7 | Classe: Crítica / Com prazo / Normal; Data comprometida | §9 | [ ] | |
| 8 | Gates mapeados de uma vez: ação sensível → decisor → proposta → data do pedido | §11; regra de ouro | [ ] | |
| 9 | Riscos com plano de resposta | etapa 4 "ações para riscos" | [ ] | |
| 10 | Pacote de contexto: quem executa acha tudo sem perguntar | §5 | [ ] | |
| 11 | Dono abaixo do WIP (laboratório: 3) | política do quadro | [ ] | |
| 12 | Empresa rotulada (Empresa A · Empresa B · Compartilhado) | (acréscimo do laboratório) | [ ] | |

Resultado: [ ] entra em execução · [ ] volta a Em preparação — falta: ______

---

## C. Definition of Done — o cartão pode ser entregue e aceito?

Cartão: P-__ · Dono: ______ · Aceitante: ______ · Checado em __/__/____ às __:__

### C1. DoD genérico (Canvas 7.2 + etapas 5–8 + laboratório)

<!-- c:dod -->
| # | Item | Origem | OK | Prova (o quê, onde, quando) |
|---|---|---|---|---|
| 1 | Esteve no quadro e passou pela diária; cartão atualizado | etapa 5 | [ ] | |
| 2 | Prova pelo caminho real citada: URL de produção / login real / curl / log / arquivo | etapa 7; regra de entrega verificada (acréscimo do laboratório) | [ ] | |
| 3 | Revisão por par ou revisor nomeado (quando o tipo exige) | 7.2 "revisão e aprovação" | [ ] | |
| 4 | Documentação / registro durável atualizado (acompanhamento, diário, versão; commit quando houver repositório) | 7.2 "documentação" | [ ] | |
| 5 | Comunicação: carta de volta na caixa de quem pediu | 7.2 "comunicação" | [ ] | |
| 6 | Métrica de negócio lida, com empresa rotulada; demanda cumprida ≠ objetivo atingido | etapa 6; §12 | [ ] | |
| 7 | Nenhum gate exigido pela DoD pendente | §11 | [ ] | |
| 8 | Verbo honesto no report ("validado em produção às HH:MM" / "não validado em runtime") | regra de entrega verificada (acréscimo do laboratório) | [ ] | |
| 9 | Dono marcou Entregue; Aceitante conferiu e marcou Aceita | §11; etapa 8 | [ ] | |

### C2. DoD por tipo de tarefa (Canvas 7.2 pede "checklist por tipo"; tipos são do laboratório — acréscimo do laboratório)

| Tipo | Pronto é | Prova mínima |
|---|---|---|
| Código / deploy / timer | roda em produção pelo caminho do usuário; SHA em `origin/main`; rollback conhecido | URL ou curl autenticado + `journalctl` sem erro + commit hash |
| Conteúdo de aula / material | aula visível no curso com login de aluno; material baixa | print ou log do LMS com data; id do curso |
| Campanha / peça | peça ativa na conta, métrica inicial lida | id do anúncio + print do painel + número com data |
| Relatório / número | fonte canônica declarada (responsável pelo número nomeado); divergência sinalizada; empresa rotulada | caminho do arquivo + fonte + data de apuração |
| Carta / cobrança | carta na caixa do destinatário com as 6 linhas; resposta ou handoff registrado | mensagem ou arquivo no canal combinado |
| Decisão / gate | proposta escrita (estado, mudança, risco, reversão, decisor); "sim" com fonte (arquivo, linha, hora) | caminho + citação |
| Ritual (plano, review, retro) | arquivo existe em pasta do ciclo escolhido com os campos do canvas | caminho + versão; commit quando houver repositório |

Resultado: [ ] Entregue (dono) · [ ] Aceito (Aceitante) · [ ] fica em "Em prova" com marca — falta: ______


## D. Vereditos (o canvas dos portões lê daqui)

| Portão | Veredito |
|---|---|
| Veredito do portão 1 — pode entrar? o que falta, quem resolve, até quando <!-- c:veredito_entrada --> | |
| Veredito do portão 2 — pode entregar? prova pelo caminho real, aceitante <!-- c:veredito_saida --> | |