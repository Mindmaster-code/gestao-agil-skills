# Roteamento para os artefatos GA 2.0

Use esta referência quando o pedido visual pertencer ao método. A skill indicada determina
campos, regras e destino. `ga2-me-mostra` determina o recorte e a apresentação.

| Sinal no pedido | Skill dona do conteúdo | Visual que costuma ajudar |
|---|---|---|
| norte, futuro, contexto estratégico | `ga2-canvas-de-visao` | passado → hoje → tendência → visão |
| atual, desejado, meta, diferença | `ga2-diagnostico` | atual × desejado com diferença medida |
| problema completo, causa e plano | `ga2-relatorio-a3` | A3 esquerdo → A3 direito |
| por que acontece, causa raiz | `ga2-causa-raiz` | 5 Porquês; Ishikawa para causas paralelas |
| ação, dono, prazo | `ga2-5w2h` | plano por linha ou linha do tempo |
| projeto, produto ou processo | `ga2-briefing-iniciativa` | mapa dos 3 Ps e fronteiras |
| projeto ou fluxo contínuo | `ga2-decisao-projeto-ou-fluxo` | árvore de decisão |
| objetivo, KR, iniciativa | `ga2-okr-canvas` | objetivo → resultado-chave → iniciativa |
| prioridade | `ga2-matriz-esforco-impacto` | matriz 2 × 2 com fila resultante |
| jornada, entregas e fatia fina | `ga2-backlog-2d` | mapa 2D com corte do primeiro ciclo |
| colunas, trabalho em curso, bloqueio | `ga2-kanban-canvas` | quadro Kanban com limite e idade |
| limite, urgência, congestionamento | `ga2-politicas-wip-urgencia` | fluxo com limite e classe crítica |
| passo a passo recorrente | `ga2-pop` | fluxo com gatilho, exceção e saída |
| papéis e responsabilidade | `ga2-quem-faz-o-que` | raias por papel ou matriz curta |
| autonomia para decidir | `ga2-delegacao` | assuntos × níveis de delegação |
| meta e capacidade da semana | `ga2-plano-do-ciclo` | linha do ciclo e carga a 70% |
| andamento diário | `ga2-gestao-diaria` | fotografia do quadro e bloqueios |
| prometido contra entregue | `ga2-review-do-ciclo` | antes/depois com prova |
| manter, melhorar, parar | `ga2-retrospectiva` | três colunas e uma ação escolhida |
| melhoria em ciclos | `ga2-pdca` | roda ou fluxo Plan → Do → Check → Act |
| melhoria pequena | `ga2-quadro-kaizen` | sinal → aposta → aprendizado → decisão |
| hipótese e teste | `ga2-folha-de-experimento` | hipótese → protótipo → teste → critério |
| números para quem decide | `ga2-painel-do-gestor` | painel com 3–5 números-âncora |
| conversa difícil | `ga2-canvas-de-conversa-cnv` | fato → sentimento → necessidade → pedido |

## Regra de desempate

1. Pedido nomeia um artefato: use a skill desse artefato.
2. Pedido nomeia uma decisão: use a skill que possui essa decisão.
3. Pedido só pede para entender: escolha a skill que já contém a fonte do estado.
4. Nenhuma skill contém o caso: use `ga2-me-mostra` e gere o HTML no destino padrão; não
   invente um artefato do método.

## Encadeamentos úteis

```text
Canvas de Visão → A3 → Briefing → OKR → Backlog 2D → Kanban
                                        ↓
                         Plano → Diária → Review → Retro → PDCA
```

Mostre a cadeia inteira só quando a pergunta for sobre dependência. Para um problema local,
recorte o predecessor, o ponto em foco e o sucessor.
