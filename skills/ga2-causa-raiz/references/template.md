<!-- modelos: cinco-porques-b-06.json, ishikawa-lab.json -->
# Causa raiz — template (5 Porquês e Ishikawa)

| Campo | Resposta |
|---|---|
| Caso / desafio <!-- c:caso --> | ______ |
| Responsável <!-- c:dono --> | ______ |
| Data <!-- c:data --> | ____/____/______ |
| Ferramenta <!-- c:ferramenta --> | 5 Porquês / Ishikawa + 5 Porquês / + Pareto |

## A. 5 Porquês (Artefato 06)

**Problema observado** <!-- c:problema --> (uma frase, com o número do lado esquerdo do A3):

>

<!-- c:porques -->
| Nível | Pergunta | Resposta | Evidência — como sei que é verdade? (log, arquivo, número, observação) |
|---|---|---|---|
| Sintoma | o que grita | | (número do lado esquerdo) |
| 1 · causa imediata | Por que isso acontece? | | |
| 2 · causa do processo | Por que (a resposta 1)? | | |
| 3 · causa da rotina | Por que (a resposta 2)? | | |
| 4 · causa da regra | Por que (a resposta 3)? | | |
| 5 · causa do sistema | Por que (a resposta 4)? | | |

**Testes antes de fechar**

| Teste | Pergunta | Resposta |
|---|---|---|
| Pessoa | A causa é processo/regra, ou nome de alguém? | processo / regra / **pessoa → reescrever** |
| Retorno | Se corrigir só isso, o problema volta? | não / **sim → continuar** |
| Controle | O dono controla essa causa? | sim / não → nível ____ é o acionável; o acima vira "depende de ____" |

**Evidências** <!-- c:evidencias --> — o que confirma ou enfraquece a causa:

>

**Causa prioritária** <!-- c:causa_prioritaria --> — qual atacar primeiro e por quê (mais frequente / maior impacto / acionável agora):

>

**Depende de** (causa acima do controle do dono — vira aprovação, decisão ou comunicação ao responsável):

>

## B. Ishikawa — espinha de peixe `(adaptação metodológica: sem template oficial)`

Use quando há várias causas ao mesmo tempo. Cabeça do peixe = o problema observado acima.

<!-- c:ishikawa -->
| Categoria (6M) | Causas levantadas (brainstorm) | Subcausas | Evidência | Frequência / impacto |
|---|---|---|---|---|
| **Método** (como se faz; processo, regra, padrão) | | | | |
| **Mão de obra** (pessoas: capacidade, carga, papel) | | | | |
| **Máquina** (sistema, equipamento, ferramenta, infraestrutura) | | | | |
| **Material** (insumo: dado, documento, material, acesso autorizado) | | | | |
| **Medição** (como se mede; o que ninguém olha) | | | | |
| **Meio ambiente** (contexto: prazo, aprovação, espaço de trabalho, regra externa) | | | | |

**Ramo(s) escolhido(s)** <!-- c:ramos_escolhidos --> por relação causa-efeito e impacto: ______
→ rode o bloco A (5 Porquês) em cada ramo escolhido.

## C. Pareto `(adaptação metodológica: sem template oficial)` — só com contagem

| Causa | Ocorrências no período ____ | % | % acumulado |
|---|---|---|---|
| | | | |
| | | | |

As duas ou três primeiras respondem por 70–80%? Ataque essas primeiro.

## Para o campo 5 do A3

Escreva em uma ou duas frases, como processo ou regra:

> Causa raiz: ______

Próximo: `ga2-relatorio-a3` — uma contramedida por causa.
