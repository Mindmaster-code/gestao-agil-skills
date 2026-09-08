# Causa raiz — checklist de "bem feito"

## 5 Porquês

- [ ] O problema observado tem o número do lado esquerdo do A3.
- [ ] Há pelo menos cinco níveis, e cada pergunta é sobre a resposta anterior (sintoma → imediata → processo → rotina → regra → sistema).
- [ ] Cada nível tem evidência nomeada (log, arquivo, número, observação datada) — nenhum "eu acho".
- [ ] A última resposta aponta processo, regra ou estrutura — **nenhum nome de pessoa ou agente**.
- [ ] Teste de retorno respondido: corrigir a causa impede o problema de voltar.
- [ ] Teste de controle respondido: está marcado qual nível o dono controla e o que "depende de" quem.
- [ ] Causa prioritária escolhida e justificada (frequência, impacto ou acionável agora).
- [ ] Escrita final para o campo 5 do A3 cabe em duas frases.

## Ishikawa

- [ ] O problema está na cabeça do peixe com número.
- [ ] Pelo menos três das seis categorias têm causa com evidência; categoria vazia está vazia de propósito, não por pressa.
- [ ] Ramo(s) escolhido(s) por relação causa-efeito e impacto — e o 5 Porquês rodou neles.
- [ ] Se houve contagem, o Pareto ordena e as 2–3 primeiras somam 70–80%.

## Incidente / post-mortem

- [ ] Os cinco níveis estão no post-mortem, não só o fix.
- [ ] A regra que nasce da causa de sistema está escrita e tem destino (repositório de padrões, procedimento ou controle de prevenção).
- [ ] Ninguém foi cobrado pelo número; a métrica que caiu virou A3.

## Erros comuns (cinco armadilhas da v6 aula 04, mais os desta adaptação)

| Erro | Como aparece | Correção |
|---|---|---|
| Parar cedo | 2 porquês e "já sei a solução" | continuar até processo/regra; testar retorno |
| Pular nível | do sintoma direto para "falta de cultura" | preencher processo e rotina; sem eles não há plano acionável |
| Culpar pessoa | "a pessoa esqueceu", "a ferramenta falhou" | "não existe passo ou controle que impeça X" |
| Sem evidência | resposta plausível sem fonte | ir e ver; se não dá para ver, marcar "hipótese" e testar |
| Só uma causa | duas travas independentes numa cadeia só | Ishikawa primeiro; 5 Porquês por ramo |
| Ishikawa decorativo | seis espinhas cheias, nenhum ramo escolhido | escolher e justificar |
| Profundo demais | causa de sistema fora do controle do dono como única ação | atacar a acionável; registrar a profunda como dependência ou regra |

## Formas de saída

- [ ] Formato e destino seguem o pedido ou o documento existente, conforme [Entrega editável](entrega-editavel.md).
- [ ] A entrega foi reaberta e conferida; conteúdo, campos, responsáveis, datas, fontes e edições humanas foram preservados.
- [ ] Se houver Markdown, as âncoras `<!-- c:id -->` estão intactas. Se houver HTML, ele deriva da fonte atual.
- [ ] Se pediram canvas, o modelo correspondente foi usado: IDs intactos, nenhum `{{` residual, sem estouro e uma página quando exigida.
