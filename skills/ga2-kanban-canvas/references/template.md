<!-- modelos de origem: kanban-kit-07.json, kanban-avancado-kit-7-1.json, kanban-politicas-kit-7-2.json, kanban-canvas-v6.json -->
# Kanban Canvas — template

Três blocos. Preencha só o que a régua do caso pede (leve = bloco A; intermediária = A + B;
robusta = A + B + C). Campo sem fonte na aula vem marcado `(acréscimo do laboratório)`.

---

## Bloco A — Quadro mínimo (v6, artefato 07 "Quadro de Gestão Visual")

| Campo | Preencha |
|---|---|
| Nome do quadro (o meu caso) <!-- c:caso --> | |
| Coluna 1 <!-- c:coluna_1 --> | A fazer |
| Coluna 2 <!-- c:coluna_2 --> | Fazendo |
| Coluna 3 <!-- c:coluna_3 --> | Feito |
| Coluna 4 (opcional) <!-- c:coluna_4 --> | |
| Como um item vira "feito" <!-- c:pronto --> | |
| Regras do quadro — quando um item anda <!-- c:politicas --> | |
| Limite de itens em andamento <!-- c:limite --> | |
| Onde vou montar o quadro <!-- c:onde --> | |
| Meu ritmo de atualização (dia, hora, duração) <!-- c:ritmo --> | |

Kanban Mínimo (artefato 03) pede ainda: **Cartões essenciais** (quais itens viram cartão) e
**Foto do quadro** (um cartão por linha; os canvas 7 e 7.1 do kit leem daqui):
<!-- c:foto -->
| Sprint backlog (a fazer) | Fazendo | Em validação | Feito |
|---|---|---|---|
| | | | |

**Limites por coluna** `(kit 7 / 7.1)`:
<!-- c:limites -->
| Coluna | Limite máx. |
|---|---|
| Fazendo | |
| Em validação | |

**Impedimentos abertos** <!-- c:bloqueios -->
- 

**Rotina de uso** (quando olhar e atualizar).

```
| A FAZER            | FAZENDO (limite: __) | FEITO              |
|--------------------|----------------------|--------------------|
|                    |                      |                    |
```

---

## Bloco B — Kanban completo de uma área ou frente

### B1. Cabeçalho (A08, professor)

| Campo | Preencha |
|---|---|
| Nome do projeto / área | |
| Líder / dono do quadro | |
| Ciclo atual (nº e datas) | |
| Onde o quadro mora | |
| Quem atualiza e quando | |

### B2. Colunas do fluxo real (A09–A12)

Desenhe da entrada da demanda até a entrega. Limite só nas colunas de execução.

<!-- c:colunas_fluxo -->
| # | Coluna | É etapa de execução? | Limite WIP | Critério para entrar | Quem move |
|---|---|---|---|---|---|
| 1 | | não (fila) | — | | |
| 2 | | sim | | | |
| 3 | | sim | | | |
| 4 | | não (pronto) | — | | |

### B3. Raias — tipos de demanda (A14)

| Raia | Tipo de demanda | Colunas que usa | Observação |
|---|---|---|---|
| | | | |
| Urgência | emergencial | fila → execução → feito | ver `ga2-politicas-wip-urgencia` |

### B4. Cartão padrão (A17 + v6 aula 03)

```
[RAIA] ______ | [ORIGEM] OKR ___ · KR __ · entrega ___ | [PROJETO] ______
O que (uma frase, resultado): ______________________________
Dono (nome de pessoa): ______   Apoio (não é co-dono): ______
Prazo: __/__   Início: __/__   Idade: __ dias
Pronto é (checklist): [ ] ____ [ ] ____ [ ] prova pelo caminho real
Bloqueio: [ ] nenhum  [ ] gate: quem decide ______ pedido em __/__  [ ] trava: ______
Prova: (link / arquivo / log / mensagem)
```

### B5. Políticas escritas no quadro (artefato 05 + Canvas 7.2)

| Política | Texto (curto, no topo do quadro) |
|---|---|
| Entrada — quando um item entra <!-- c:entrada --> | |
| Pronto — quando termina (checklist genérico) <!-- c:pronto_politica --> | |
| Pronto por tipo de tarefa | |
| Prioridade — como escolher o próximo | |
| Limites — por coluna e por pessoa <!-- c:limites_politica --> | |
| Atualização — quem, quando <!-- c:atualizacao --> | |
| Bloqueio — o que fazer quando trava; parado N dias sobe para <!-- c:bloqueio --> | |
| Por que isso existe (Kit Implementação) | |

### B6. Bloqueio — representação escolhida

- [ ] A. marca no cartão, coluna mantida (**padrão do laboratório**)
- [ ] B. coluna "Bloqueados"
- [ ] C. área "Impedimentos" separada

Escalada: parado __ dias → pergunta na diária; __ dias → carta de cobrança; __ dias → sobe para ______.

---

## Bloco C — Kanban de portfólio (formato de registro do portfólio na pasta do caso)

### C1. Políticas do quadro

- Entra só frente com dono único nomeado.
- WIP por dono em execução: __.
- Parado ≥ __ dias úteis → carta; ≥ __ dias → escala.
- "Em gate" exige decisor nomeado e data do pedido.
- "Entregue" só com prova pelo caminho real.
- "Aceito" é do Aceitante, nunca do Gestor.
- Estado vem de arquivo, não de memória.

### C2. Raias

`Empresa A` · `Empresa B` · `Compartilhado` · `Processo interno`

### C3. Colunas (estados comuns do modelo operacional §7, reduzidos para o portfólio)

`Sem dono` · `Sem STATUS` · `Em preparação` · `Em execução` · `Em gate` (condição) · `Bloqueado` (condição) · `Parado` (condição) · `Entregue` · `Aceito`

### C4. Quadro

| ID | Frente | Raia | Dono | Coluna | Última prova | Dias parado | Gate / trava | Fonte |
|---|---|---|---|---|---|---|---|---|
| P-__ | | | | | | | | |

### C5. Leitura da fotografia (acréscimo do laboratório)

- Total de frentes: __ · sem STATUS: __ · sem dono: __
- Cartões parados > 10 dias: __
- Maior custo de atraso declarado: __
- Primeira cobrança que sai: __

### C6. Como atualizar

Dias fixos: ______. Reler a fonte de cada cartão; atualizar "Última prova" e "Dias parado";
mover coluna só com prova.
