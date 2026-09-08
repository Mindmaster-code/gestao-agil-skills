# Diagnóstico — checklist de "bem feito"

## Antes de chamar de pronto

- [ ] Cabeçalho: caso em uma frase, dono único, empresa, data, ciclo, régua.
- [ ] Recorte escrito: o que entra e o que fica de fora deste ciclo.
- [ ] Contexto em 2–3 frases, ligado a receita, cliente, custo ou risco — e diz "por que agora".
- [ ] Contexto **não** contém causa nem solução.
- [ ] Cada linha da situação atual tem número, fonte, data e quem foi ver.
- [ ] "Ir e ver" foi feito no estado (log, painel, banco, arquivo), não no script ou na memória.
- [ ] Número financeiro é do responsável financeiro da empresa ou está marcado "a confirmar".
- [ ] Linha de base escrita: métrica, valor, data, onde mora, frequência, quem lê.
- [ ] Mapa as-is só se o problema é de fluxo; marca onde o trabalho para.
- [ ] Situação desejada tem "de X para Y até dd/mm".
- [ ] Gap calculado e a pergunta "vale um A3?" respondida com motivo.
- [ ] Contexto, atual e desejada usam a **mesma medida**.
- [ ] Histórico do que já foi tentado registrado (ou "nada tentado").
- [ ] Dono leu de volta e assinou.
- [ ] Cabe em uma página (é metade do A3).

## Erros comuns (da aula A06 e v6 aula 03)

| Erro | Como aparece | Correção |
|---|---|---|
| Resolver antes de entender | "o problema é que falta X" na situação atual | mover para contramedida; perguntar "o que acontece hoje, em número?" |
| "Está ruim" | adjetivo no lugar de número | "leva 72h", "12 de 80", "15%" |
| Número sem fonte | "uns 20%" | abrir a fonte; se não existe, `[a medir]` e linha de base |
| Meta como atividade | "fazer reuniões semanais" | "pedidos com erro de 15% para 5% até 30/09" |
| Meta sem prazo | "reduzir retrabalho" | "≤ 5% em 90 dias" |
| Medidas desencontradas | contexto fala de custo, meta fala de prazo | escolher uma medida e reescrever |
| Gap pequeno virando A3 | projeto para mover 1 ponto sem efeito | executar e arquivar sem A3 |
| Linha de base tardia | escrita depois de mudar | voltar ao log/histórico e reconstruir o "antes", com data |
| Contexto enorme | checklist de 10 itens da A05 preenchido em prosa | v6: 2–3 frases; escopo e envolvidos vão para o briefing |

## Formas de saída

- [ ] Formato e destino seguem o pedido ou o documento existente, conforme [Entrega editável](entrega-editavel.md).
- [ ] A entrega foi reaberta e conferida; conteúdo, campos, responsáveis, datas, fontes e edições humanas foram preservados.
- [ ] Se houver Markdown, as âncoras `<!-- c:id -->` estão intactas. Se houver HTML, ele deriva da fonte atual.
- [ ] Se pediram canvas, o modelo correspondente foi usado: IDs intactos, nenhum `{{` residual, sem estouro e uma página quando exigida.
