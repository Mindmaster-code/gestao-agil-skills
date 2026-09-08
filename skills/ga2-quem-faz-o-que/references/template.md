<!-- modelos de origem: quem-faz-o-que-lab.json -->
# Quem faz o quê — template

Não existe template oficial no curso. Campos da aula M06 A10 (SM, PO, membros, gerente ágil),
da v6 aula 03 (dono do ciclo, quem faz, quem recebe) e do modelo operacional do laboratório (Dono,
Aceitante, gate, apoio). Tudo que não está em aula vem marcado `(acréscimo do laboratório)`.

---

## Cabeçalho

| Campo | Preencha |
|---|---|
| Frente / demanda <!-- c:frente --> | |
| Entrega (resultado, não tarefa) <!-- c:entrega --> | |
| Empresa (Empresa A · Empresa B · Compartilhado) <!-- c:empresa --> | (acréscimo do laboratório) |
| Cartão no portfólio <!-- c:cartao --> | P-__ |
| Data desta matriz <!-- c:data --> | |

## Matriz de papéis

<!-- c:matriz -->
| Papel | Nome (pessoa) | O que faz nesta frente | O que não faz |
|---|---|---|---|
| **Dono / DRI** (PO da aula) | | responde pelo resultado; prioriza dentro da frente; apresenta a prova; marca Entregue | não promete capacidade sozinho; não autoriza ação sensível |
| **Aceitante** (quem recebe o resultado) | | confere a DoD e marca Aceita; está na review | não executa; nunca é o Gestor |
| **Executor(es)** (membros do time) | | faz o trabalho; decide o como | não decide o quê |
| **Apoio(s)** | | contribui sem responder | não vira co-dono |
| **Decisor de gate** (acréscimo do laboratório) | | autoriza a ação sensível: ______ | não é aceite |
| **Dono do processo** (SM da aula) | Gestor Ágil | ritual, quadro, cobrança, métrica de fluxo | não aceita entrega; não prioriza entre áreas |
| **Quem decide prioridade entre áreas** (gerente ágil) | nome a definir | ordem entre frentes; fronteira entre donos | não opera |

## Papéis do ritmo (v6 aula 03)

| | Nome |
|---|---|
| Dono do ciclo (responde pela meta) <!-- c:dono_ciclo --> | |
| Quem faz <!-- c:quem_faz --> | |
| Quem recebe o resultado (aparece na review) <!-- c:quem_recebe --> | |

## Acumulações declaradas (A10)

| Pessoa | Acumula | Permitido? |
|---|---|---|
| | dono + executor | sim |
| | dono do processo + dono do rumo (SM + PO) | **não** |
| | Aceitante + decisor de gate | sim, se o organograma der as duas autoridades |

## Gates desta frente (modelo operacional §11)

| Ação sensível | Decisor | Proposta escrita? (estado atual, mudança exata, risco, reversão) | Pedido em | Decidido em |
|---|---|---|---|---|
| | | | | |

## Demandas filhas (apoio com responsabilidade própria — §6)

| Filha | Dono | DoD | Aceitante | Por que é filha e não apoio |
|---|---|---|---|---|
| | | | | tem dono/DoD/Aceitante/handoff ou gate próprios |

## Transferência de dono (§6)

| De | Para | Aceitou por escrito em | Contexto entregue (arquivo) |
|---|---|---|---|
| | | | |

## Teste de fronteira (acréscimo do laboratório)

- [ ] Só um nome na linha Dono.
- [ ] Dois acham que é deles? → carta ao dirigente responsável com as duas versões; não resolver o caso.
- [ ] O Aceitante consegue conferir a DoD sem perguntar ao dono?
- [ ] Cada gate tem pessoa e data.

## Linha para o cartão e para as 6 linhas da demanda

```
Dono: <nome>  ·  Aceitante: <nome>  ·  Gate: <decisor> (pedido __/__)  ·  Apoio: <nomes> (não é co-dono)
```
