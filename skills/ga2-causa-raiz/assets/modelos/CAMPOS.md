# Campos dos modelos canvas — `ga2-causa-raiz`

Gerado pelo construtor (`construir.py --campos-md`). Não editar à mão.

## `cinco-porques-b-06` — Causa raiz — 5 Porquês (editável)

| id | rótulo no canvas | texto-guia | âncora no template |
|---|---|---|---|
| `problema_observado` | Problema observado | Problema em uma frase. | `<!-- c:problema -->` |
| `cinco_porques` | 5 Porquês | 1. Por quê? 2. Por quê? 3. Por quê? 4. Por quê? 5. Por quê? | `<!-- c:porques -->` |
| `evidencias` | Evidências | O que confirma ou enfraquece a causa? | `<!-- c:evidencias -->` |
| `causa_prioritaria` | Causa prioritária | Qual causa atacar primeiro? | `<!-- c:causa_prioritaria -->` |

## `ishikawa-lab` — Ishikawa — espinha de peixe (laboratório)

| id | rótulo no canvas | texto-guia | âncora no template |
|---|---|---|---|
| `caso` | Caso / desafio |  | `<!-- c:caso -->` |
| `responsavel` | Responsável |  | `<!-- c:dono -->` |
| `data` | Data |  | `<!-- c:data -->` |
| `problema` | PROBLEMA (efeito) | o problema observado, com número | `<!-- c:problema -->` |
| `metodo` | MÉTODO | como se faz: processo, regra, padrão | `<!-- c:ishikawa -->` (formato: `{Causas levantadas}`) |
| `maquina` | MÁQUINA | sistema, timer, ferramenta, infra | `<!-- c:ishikawa -->` (formato: `{Causas levantadas}`) |
| `material` | MATERIAL | insumo: dado, arquivo, pasta, credencial | `<!-- c:ishikawa -->` (formato: `{Causas levantadas}`) |
| `mao_de_obra` | MÃO DE OBRA | gente e agente: capacidade, carga, papel | `<!-- c:ishikawa -->` (formato: `{Causas levantadas}`) |
| `medida` | MEDIÇÃO | como se mede; o que ninguém olha | `<!-- c:ishikawa -->` (formato: `{Causas levantadas}`) |
| `meio_ambiente` | MEIO AMBIENTE | contexto: prazo, gate, sessão ocupada, regra externa | `<!-- c:ishikawa -->` (formato: `{Causas levantadas}`) |
| `ramos_escolhidos` | RAMO(S) ESCOLHIDO(S) | por relação causa-efeito e impacto → rode os 5 Porquês em cada ramo escolhido | `<!-- c:ramos_escolhidos -->` |
