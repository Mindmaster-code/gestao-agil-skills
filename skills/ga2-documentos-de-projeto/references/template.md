<!-- spec: construtor/specs/status-report-b-04.json, construtor/specs/resumo-ciclo-b-04.json, construtor/specs/status-report-b-04-p2.json, construtor/specs/resumo-ciclo-b-04-p2.json -->
# Documentos de projeto — templates (README da frente · Status Report · Resumo do Ciclo)

## 1. `<pasta-do-projeto>/README.md` — índice do dossiê

```markdown
# Frente: <nome> (<ID-do-cartão>)

| Campo | Resposta |
|---|---|
| Dono <!-- c:dono --> | ______ |
| Empresa <!-- c:empresa --> | <empresa / área / processo> |
| Régua <!-- c:regua --> | leve / intermediária / robusta |
| Aberta em <!-- c:aberta_em --> | ____/____/______ |
| Tipo (3 Ps) | projeto / produto / processo |
**Fase atual:** ___ · **Próxima entrega (Mapa da Jornada):** ______ · **Cartão:** <quadro escolhido> ID-do-cartão

| # | Documento | Arquivo | Estado | Data | Assinado por |
|---|---|---|---|---|---|
| 0 | Canvas de Visão curto | `00-canvas-de-visao.md` | falta / rascunho / assinado | | |
| 1 | A3 | `01-a3.md` | | | |
| 2 | Briefing | `02-briefing.md` | | | |
| 3 | OKR | `03-okr.md` | | | |
| 4 | Backlog 2D | `04-backlog-2d.md` | | | |
| 5 | Kanban | `05-kanban.md` | | | |
| 6 | Plano do ciclo | `ciclos/AAAA-Www/plano.md` (linha) | | | |
| 7 | Status Report | `status/AAAA-MM-DD.md` (último) | | | |
| 8 | Review / Retro | `ciclos/AAAA-Www/{review,retro}.md` | | | |
| 9 | Resumo do Ciclo | `90-resumo-ciclo-<n>.md` | | | |

**Pack externo (se houver):** <pasta existente escolhida> — charter = briefing; STATUS.md = status.
**Dívidas do dossiê:** (documento de fase anterior que falta, com data de cobrança)
**Encerramento:** entregue em ____/____ · aceito por ______ (dono do resultado) · prova: ______
```

---

## 2. Status Report — `<pasta-do-projeto>/status/AAAA-MM-DD.md`

Template oficial: `desafio-7-dias-status-report-ga2.pdf` (8 campos). Campos marcados `(legado)` vêm do `04-status-report-7-dias-ga2-editavel.pdf`; `(lab)` = acréscimo do laboratório.

```markdown
# Status — <frente> · <dd/mm/aaaa>

**Participante e caso:** <!-- c:participante --> <dono> · <frente / ID-do-cartão>
**Objetivo do desafio** <!-- c:compromisso --> (o que quero ter feito no dia 7 / no fim do ciclo): ______
**Em que dia estou** <!-- c:periodo --> (1 a 7) / **ciclo e semana**: ___
**No ritmo?** adiantado / no prazo / atrasado — sem maquiar
**Semáforo** <!-- c:status --> `(legado)`: verde / amarelo / vermelho

## O que já entreguei <!-- c:feito -->
- <entrega> — prova: <URL / arquivo / log / commit> `(lab: prova obrigatória)`

## Que resultado apareceu `(legado)` <!-- c:resultado -->
- <sinal simples: prazo, qualidade, fila, bloqueio removido, feedback observado ou aprendizado>

## O que travou (bloqueios) <!-- c:travou -->
- <trava> — quem destrava: <nome> — pedido em <dd/mm> `(lab: decisor e data)`

## O que aprendi até aqui <!-- c:aprendi -->
- (sobre o caso e sobre o meu sistema de trabalho `(legado)`)

## Qual ajuste no próximo ciclo `(legado)` <!-- c:ajuste -->
- 

## Meu próximo passo <!-- c:proxima_acao -->
- <ação> — dono: <nome> — até <dd/mm> `(legado: ação, dono, prazo)`
```

Regra de leitura: "um retrato honesto vale mais que um relatório bonito". Dois minutos.

---

## 3. Resumo do Ciclo — `<pasta-do-projeto>/90-resumo-ciclo-<n>.md`

Template oficial: `04-resumo-do-ciclo-ga2-editavel.pdf` (Artefato 17, 5 campos).

```markdown
# Resumo do Ciclo <n> — <frente> · <período>

**Dono:** ______ · **Ciclo:** AAAA-Www a AAAA-Www · **Meta combinada (copiada do plano, sem maquiagem):** ______

## 1. Contexto do ciclo <!-- c:contexto_ciclo -->
Qual era o problema ou objetivo?

## 2. Entregas e evidências <!-- c:entregas_evidencias -->
O que foi produzido ou melhorou? (cada linha com prova; número de → para quando houver)
| Entrega | Evidência (URL, arquivo, log, número) |
|---|---|
| | |

## 3. Aprendizados <!-- c:aprendizados -->
O que ficou claro depois de executar? (específico, não "comunicar melhor")

## 4. Próximas decisões <!-- c:proximas_decisoes -->
Continuar / ajustar / pausar / escalar — com verbo, dono e data.
- 

## 5. Se virar A3 de melhoria <!-- c:vira_a3 -->
Qual problema merece voltar para o template A3? (um caso, um A3 → `01-a3.md` novo)
- nenhum / <problema> → abrir A3 até <dd/mm>, dono <nome>

**Lido por:** <dono> em <dd/mm> · <Gestor Ágil> · vai para o report ao responsável pelo portfólio de <dd/mm>
```

"Feche o ciclo em uma página. Depois disso, se precisar, reutilize o A3."
