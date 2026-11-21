<!-- modelos de origem: quem-faz-o-que-lab.json -->
# Quem faz o quê — template

Não existe template oficial no curso. Campos da aula M06 A10 (SM, PO, membros, gerente ágil),
da material de referência (dono do ciclo, quem faz, quem recebe) e do modelo operacional do método (Dono,
Aceitante, gate, apoio). Tudo que não está em aula vem marcado .

---

## Cabeçalho

| Campo | Preencha |
|---|---|
| Frente / demanda <!-- c:frente --> | |
| Entrega (resultado, não tarefa) <!-- c:entrega --> | |
| Área (Área A · Área B · Compartilhado) <!-- c:empresa --> | |
| Cartão no quadro <!-- c:cartao --> | P-__ |
| Data desta matriz <!-- c:data --> | |

## Matriz de papéis

<!-- c:matriz -->
| Papel | Nome (pessoa) | O que faz nesta frente | O que não faz |
|---|---|---|---|
| **Dono** (PO da aula) | | responde pelo resultado; prioriza dentro da frente; apresenta a prova; marca Entregue | não promete capacidade sozinho; não autoriza ação sensível |
| **Aceitante** (quem recebe o resultado) | | confere a DoD e marca Aceita; está na review | não executa; nunca é o dono do processo |
| **Executor(es)** (membros do time) | | faz o trabalho; decide o como | não decide o quê |
| **Apoio(s)** | | contribui sem responder | não vira co-dono |
| **Decisor de gate** | | autoriza a ação sensível: ______ | não é aceite |
| **Dono do processo** (SM da aula) | quem conduz o método | ritual, quadro, cobrança, métrica de fluxo | não aceita entrega; não prioriza entre áreas |
| **Quem decide prioridade entre áreas** (gerente ágil) | nome a definir | ordem entre frentes; fronteira entre donos | não opera |

## Papéis do ritmo (material de referência)

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

## Revisão de responsabilidades: papel previsto contra papel assumido (ficha E11)

Registro reservado. Remuneração, contrato e obrigação legal ficam com quem decide e com as áreas responsáveis. Esta folha organiza a comparação e a evidência.

| Responsabilidade ou entrega | Papel previsto | Papel assumido | Desde quando | Evidência de contribuição |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

| Campo | Resposta |
|---|---|
| Pessoa e período revisado | |
| Critérios da organização para reconhecimento, progressão e remuneração | |
| Casos comparáveis consultados (para o tratamento ser coerente) | |
| Proposta levada a quem decide, com impacto e justificativa (data e nome) | |
| Decisão e data em que a pessoa foi informada, individualmente | |
| Discrepâncias e decisões pendentes para o semestre seguinte | |

## Transferência de responsabilidades quando alguém muda de função ou sai (ficha E12, roteiro de comunicação, cobertura e transição página 3)

Plano restrito. A parte formal (desligamento, acessos, devoluções, obrigações) segue com as áreas responsáveis, nos momentos autorizados.

| Campo | Resposta |
|---|---|
| Quem sai ou muda de função, e a data | |
| Áreas responsáveis alinhadas (nome e data) | |
| Conhecimento e documentos que precisam ser transferidos | |
| Acessos e recursos que exigem coordenação autorizada | |
| Contatos, pendências e comunicação às partes afetadas (quando e por quem) | |
| Confirmação final e responsável pelo acompanhamento | |

| Entrega | POP escrito (código e versão) | Novo dono | Aceitou por escrito em | Trabalho feito uma vez com quem sai ao lado (data) |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

## Teste de fronteira

- [ ] Só um nome na linha Dono.
- [ ] Dois acham que é deles? → mensagem escrita ao responsável pela área com as duas versões; não resolver o caso.
- [ ] O Aceitante consegue conferir a DoD sem perguntar ao dono?
- [ ] Cada gate tem pessoa e data.

## Linha para o cartão e para as 6 linhas da demanda

`
Dono: <nome> · Aceitante: <nome> · Gate: <decisor> (pedido __/__) · Apoio: <nomes> (não é co-dono)
`
