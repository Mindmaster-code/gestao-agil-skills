# Kanban Canvas — Norte-Sul

Exemplo fictício, novo e independente. Pessoas, cartões, datas, números e fontes citadas são simulados, não evidência real.

Régua robusta para ilustrar os três blocos. Em caso menor, use apenas os blocos pedidos pela régua.

## Bloco A — Quadro mínimo

| Campo | Valor |
|---|---|
| Nome do quadro <!-- c:caso --> | Conferência de pedidos — Norte-Sul |
| Coluna 1 <!-- c:coluna_1 --> | A fazer |
| Coluna 2 <!-- c:coluna_2 --> | Fazendo |
| Coluna 3 <!-- c:coluna_3 --> | Feito |
| Coluna 4, opcional <!-- c:coluna_4 --> | Em validação, posicionada entre Fazendo e Feito |
| Como vira feito <!-- c:pronto --> | critério do cartão cumprido, prova registrada e Mariana confirmou que serve |
| Regras do quadro <!-- c:politicas --> | puxar só com vaga; marcar bloqueio sem voltar; registrar prova antes de concluir |
| Limite em andamento <!-- c:limite --> | Fazendo: 2; Em validação: 1; por pessoa: 2 |
| Onde montar <!-- c:onde --> | quadro compartilhado da expedição, escolhido pelo time |
| Ritmo de atualização <!-- c:ritmo --> | dias úteis, 09h, durante a diária de até 15 min |

Cartões essenciais: tarefas NS-11, NS-12 e NS-13 da primeira entrega do Backlog 2D NS-I1. Cada cartão cabe na semana.

### Foto simulada em 16/09/2026

<!-- c:foto -->
| A fazer | Fazendo | Em validação | Feito |
|---|---|---|---|
| NS-13 — revisar checklist | NS-12 — aplicar em cinco pedidos simulados | — | NS-11 — versão inicial |

<!-- c:limites -->
| Coluna | Limite |
|---|---|
| Fazendo | 2 |
| Em validação | 1 |

<!-- c:bloqueios -->
- NS-12 aguarda quantidade do pedido simulado SIM-05; Lucas completa o registro até 16/09 às 14h. Cartão permanece em Fazendo.

Rotina: Lucas atualiza o quadro quando o estado muda; a diária confere prova, próximo passo e bloqueio.

## Bloco B — Quadro da frente

### B1. Cabeçalho

| Campo | Valor |
|---|---|
| Projeto / área | Conferência de pedidos / Expedição |
| Dono do quadro | Lucas, responsável pela atualização |
| Ciclo | 1, de 14 a 18/09/2026 |
| Onde mora | quadro compartilhado da expedição |
| Quem atualiza e quando | Lucas, na mudança de estado e na diária das 09h |

### B2. Colunas do fluxo atual

<!-- c:colunas_fluxo -->
| # | Coluna | Execução? | WIP | Critério para entrar | Quem move |
|---|---|---|---|---|---|
| 1 | A fazer | não | — | tarefa do backlog com dono e pronto é | Lucas |
| 2 | Fazendo | sim | 2 | capacidade confirmada e vaga | Lucas |
| 3 | Em validação | sim | 1 | prova pronta para conferência | Lucas |
| 4 | Feito | não | — | Mariana conferiu o critério completo | Mariana |

Limites iniciais ilustrativos: antes do acordo havia três itens em Fazendo e dois em validação; adotou-se a contagem menos um.

### B3. Raias

| Raia | Tipo | Colunas | Observação |
|---|---|---|---|
| Projeto | preparação do checklist | todas | meta semanal |
| Atendimento | dúvidas de pedidos | todas | fluxo contínuo |
| Urgência | cliente com entrega parada | fila → execução → feito | uma por vez, chamada por Mariana |

### B4. Cartão padrão preenchido

```text
RAIA: Projeto · ORIGEM: OKR NS-O1 / KR1 / entrega NS-I1-E1 · PROJETO: Conferência
O que: aplicar o checklist em cinco pedidos simulados.
Dono: Lucas · Apoio: nenhum · Prazo: 17/09 · Início: 15/09 · Idade: 1 dia.
Pronto é: cinco registros completos; divergências identificadas; Mariana confere os registros.
Bloqueio: SIM-05 sem quantidade; Lucas completa até 16/09 às 14h; marcado em 16/09 às 09h.
Prova: quatro registros simulados concluídos; quinto em aberto. Não entregue.
```

### B5. Políticas no quadro

| Política | Texto |
|---|---|
| Entrada <!-- c:entrada --> | tarefa do backlog, dono único, data e pronto é escritos; só inicia com vaga |
| Pronto <!-- c:pronto_politica --> | prova do critério completo e confirmação de quem recebe |
| Pronto por tipo | checklist: campos completos; aplicação: cinco registros; revisão: mudanças comparadas |
| Prioridade | ordem da fatia fina; atendimento olha o cartão mais velho |
| Limites <!-- c:limites_politica --> | Fazendo 2; Em validação 1; pessoa 2; fila e Feito sem limite |
| Atualização <!-- c:atualizacao --> | Lucas atualiza na mudança de estado e na diária das 09h |
| Bloqueio <!-- c:bloqueio --> | marca, motivo, dono e data; três dias úteis sem prova geram cobrança; dez dias geram escalada |
| Por que existe | terminar trabalho e tornar a espera visível |

### B6. Representação de bloqueio

Opção A: marca no cartão, coluna mantida. Um dia parado entra na diária; três dias úteis geram cobrança ao dono; dez dias escalam a Mariana.

## Bloco C — Portfólio ilustrativo

### C1. Políticas

Uma frente por cartão, com dono nomeado; WIP inicial 3 por dono. Estado vem do registro da frente, não da memória.

Gate exige decisor e data. Entregue exige prova; Aceito exige a confirmação do Aceitante, não do facilitador.

### C2. Raias

Expedição · Atendimento. Números de uma raia não são atribuídos à outra.

### C3. Estados

Sem dono · Sem registro de estado · Em preparação · Em execução · Entregue · Aceito. Em gate, Bloqueado e Parado são condições.

### C4. Quadro

| ID | Frente | Raia | Dono | Coluna | Última prova | Dias parado | Gate / trava | Fonte simulada |
|---|---|---|---|---|---|---|---|---|
| NS-01 | Checklist de conferência | Expedição | Mariana | Em execução | versão inicial, 15/09 | 1 | SIM-05 incompleto; Lucas, 16/09 | registro NS-01 de 16/09 |
| NS-02 | Fila de dúvidas | Atendimento | Lucas | Em execução | resposta registrada, 16/09 | 0 | nenhum | registro NS-02 de 16/09 |

### C5. Leitura da fotografia

Duas frentes, nenhuma sem registro de estado ou dono, nenhuma parada há mais de dez dias. Custo monetário do atraso: não estimado.

Primeira ação: Lucas completar SIM-05 até 14h. Nenhuma cobrança por atraso é necessária nesta fotografia.

### C6. Atualização

Lucas relê as fontes simuladas na quarta e sexta, às 09h. Só muda estado com nova prova e atualiza os dias parados.
