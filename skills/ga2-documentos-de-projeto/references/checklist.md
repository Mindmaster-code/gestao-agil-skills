# Documentos de projeto — checklist de "bem feito"

## O dossiê (README da frente)

- [ ] Pasta `<pasta-do-projeto>/` existe com `README.md`.
- [ ] README diz dono único, empresa, régua, tipo (3 Ps), fase atual, próxima entrega e cartão ID-do-cartão.
- [ ] Cada documento da tabela tem estado (falta / rascunho / assinado), data e quem assinou.
- [ ] Documento da fase atual existe e tem data dos últimos 10 dias.
- [ ] Documento de fase anterior que falta está em "Dívidas", com data de cobrança.
- [ ] Pack externo (pasta existente) é apontado, não copiado.
- [ ] Régua respeitada: frente leve não é cobrada por OKR de 3 KRs.
- [ ] Estado do portfólio bate com o README (arquivo velho = "parado").

## Status Report

- [ ] Cabe em 2 minutos de leitura.
- [ ] Diz o dia/ciclo e responde "no ritmo?" com adiantado / no prazo / atrasado.
- [ ] Cada entrega tem prova pelo caminho real (URL, arquivo, log, commit).
- [ ] Cada trava nomeia quem destrava e a data do pedido.
- [ ] Tem aprendizado sobre o caso e sobre o próprio sistema de trabalho.
- [ ] Termina com próximo passo: ação, dono, data.
- [ ] Não maquiou: atrasado está escrito "atrasado".

## Resumo do Ciclo

- [ ] Meta combinada copiada do plano, sem maquiagem (ou "não havia", escrito).
- [ ] Entregas com evidência; número de → para quando existe.
- [ ] Aprendizado específico — alguém que não estava no ciclo entende o que mudou.
- [ ] Próximas decisões com verbo (continuar / ajustar / pausar / escalar), dono e data.
- [ ] "Se virar A3" respondido; se sim, A3 novo com dono e data.
- [ ] Uma página.
- [ ] Lido pelo dono; entra no report ao responsável pelo portfólio.

## Erros comuns

| Erro | Como aparece | Correção |
|---|---|---|
| Dossiê de nome | pasta com README e mais nada há 3 semanas | cobrar o documento da fase, com "pronto é" |
| Status = lista de tarefas | 12 bullets de atividade, sem ritmo nem trava | 8 campos do template; cortar ao essencial |
| "No prazo" sem prova | entrega citada sem link | pedir a prova; sem prova = não entregue |
| Trava sem decisor | "depende de aprovação" | nome + data do pedido; entra na fila de gates |
| Resumo genérico | "aprendemos a comunicar melhor" | "tudo que dependia de decisão parou 10 semanas; gate é o gargalo" |
| Decisão sem verbo | "avaliar próximos passos" | "escalar à responsável Mariana até 18/09/2026 — Lucas" |
| Emendar ciclo sem resumo | plano novo sem fechar o anterior | resumo antes do plano; regra 1 da cadência |
| Copiar o pack | dossiê existente copiado para outra pasta | apontar no README |

## Formas de saída

- [ ] Entrega no formato pedido e no destino escolhido, conforme `entrega-editavel.md`; documento reaberto e conferido.
- [ ] Se houver fonte Markdown para o construtor, âncoras `<!-- c:id -->` intactas.
- [ ] Se pediram canvas, confira o HTML renderizado: ids intactos, sem marcadores pendentes, sem cortes e com as páginas esperadas.
