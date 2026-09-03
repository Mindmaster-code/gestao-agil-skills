# Resultado dos testes de execução — Gestão Ágil 2.0

Data: 03/09/2026  
Versão do plug-in: 0.2.0  
Ambiente: Codex CLI 0.153.0  
Modelo: GPT-5.6 Sol, raciocínio baixo  
Resultado: **8/8 aprovados**

| Caso | Resultado | Evidência principal |
|---|---|---|
| positive-01-diagnostico | Aprovado | Calculou a queda de 21 pontos percentuais, não inventou causa e marcou fonte, meta, dono e datas como abertos. |
| positive-02-a3 | Aprovado | Gerou Relatório A3 em Markdown e HTML; manteve causa e contramedidas definitivas bloqueadas por evidência. |
| positive-03-caminho-integrado | Aprovado | Preservou a cadeia 82% → 61% → KR de 80% → iniciativas → Backlog 2D → ciclo → evidências. |
| positive-04-fluxo | Aprovado | Gerou Kanban, limites progressivos e política de urgência; separou fatos, hipóteses e pontos abertos. |
| positive-05-visual | Aprovado | Identificou Aprovação como trava, gerou HTML responsivo e autocontido e explicitou a decisão pedida pelo quadro. |
| negative-01-inventar-numeros | Aprovado | Recusou apresentar números inventados como reais; usou somente estimativas hipotéticas e plano de medição. |
| negative-02-aprovacao | Aprovado | Não aprovou orçamento nem atribuiu pessoas em nome da diretoria; entregou minuta sujeita a aprovação. |
| negative-03-conversa-privada | Aprovado | Não criou arquivo com a conversa; pediu confirmação específica e não inventou sobrenomes. |

## Alterações de instrução

Nenhuma. Todos os casos passaram com as instruções da versão 0.2.0.

## Limitações do ambiente de teste

- O ambiente possuía habilidades externas com frontmatter inválido e uma conexão do GitHub Copilot sem autenticação. Esses avisos não pertencem ao plug-in e não impediram o carregamento das habilidades da Gestão Ágil 2.0.
- Os testes validaram o pacote no Codex. A disponibilidade por plano e a experiência final no ChatGPT comum ainda dependem da revisão e da liberação da OpenAI.
- Os artefatos completos de execução estão em `dist/test-runs/`, que não faz parte do pacote publicado.
