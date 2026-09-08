# Checklist de produção e entrega — critério de "bem feito" e erros comuns

## Bem feito

O próprio DoR / DoD (o artefato)
- [ ] "Pronto" está escrito por extenso e colado ao lado da coluna Pronto do quadro.
- [ ] Foi definido uma vez, com quem faz o trabalho, não imposto.
- [ ] Há DoD genérico e DoD por tipo para as tarefas mais comuns da área.
- [ ] DoR e DoD cabem numa tela; ninguém precisa abrir outro documento.
- [ ] Nenhum item aceita "mais ou menos" (v6 aula 09).

Ao aplicar o DoR a um cartão
- [ ] Origem no A3 / OKR / Backlog 2D escrita.
- [ ] Um dono, um Aceitante.
- [ ] "Pronto é" verificável pelo caminho real.
- [ ] Cabe em uma semana; tarefas de um dia.
- [ ] Comprometida, com classe e data.
- [ ] Gates listados de uma vez, com decisor e data do pedido.
- [ ] Risco com resposta; contexto suficiente; dono abaixo do WIP; empresa rotulada.
- [ ] Falhou em algo → cartão volta a Em preparação com o que falta escrito, não entra "por enquanto".

Ao aplicar o DoD a um cartão
- [ ] Prova citada com o quê, onde e quando (HH:MM).
- [ ] Caminho do usuário real: URL de produção, login real, curl autenticado, log — não build local.
- [ ] Registro durável (acompanhamento, diário, versão; commit quando houver repositório) e carta de volta.
- [ ] Número de negócio lido e rotulado por empresa; demanda cumprida ≠ objetivo atingido, os dois registrados.
- [ ] Nenhum gate exigido pendente.
- [ ] Verbo exato no report.
- [ ] Dono marcou Entregue; Aceitante (não o executor, não o Gestor) marcou Aceita.
- [ ] Falhou na prova → fica em "Em prova" com marca; não dá ré.

Checklist de 9 etapas (trimestre / frente nova)
- [ ] Aplicado no fechamento de trimestre e na abertura de frente, com data, responsável e "onde voltar".
- [ ] Não aplicado cartão a cartão.

## Erros comuns (da aula e do laboratório)

| Erro | Sinal | Correção |
|---|---|---|
| "Pronto" na cabeça | cada um entrega uma coisa diferente | escrever e colar na coluna (v6 07) |
| Cartão puxado cru | sem dono / sem "pronto é" / sem origem | DoR antes de puxar; volta a Em preparação |
| Gate descoberto na entrega | "ah, precisa do dirigente responsável" na sexta | item 8 do DoR: todos os gates de uma vez |
| Prova de laboratório | "buildei local", "deveria funcionar" | conferir pelo caminho real de quem usa |
| Prova sem hora | "testei e funciona" | "validado em produção às HH:MM, URL X" |
| Tarefa sim, meta não | 100% das tarefas, KR parado | ler a métrica do negócio (etapa 6; A07) |
| Entrega com gate pendente | "publiquei, depois ele aprova" | §11: nunca |
| Aceite do executor | "eu confiro o meu" | Aceitante separado |
| "GO" local = aceite | copy aprovada → "entregue" | aceite é a DoD global (§8) |
| Só na memória | sem arquivo, sem versão, sem resposta | registro durável é item do DoD |
| Número sem empresa | "faturamento" sem origem | nome da empresa ou unidade, sempre |
| Checklist de 9 etapas por cartão | 9 etapas para uma carta | DoR/DoD por cartão; 9 etapas por trimestre |
| Urgência sem DoD | "era urgente, não deu pra provar" | urgência não elimina DoD (§11) |

## Formas de saída

- [ ] Entrega no formato pedido, conforme [entrega-editavel.md](entrega-editavel.md), salva e conferida; nas revisões, mesmo documento e edições humanas preservados.
- [ ] Quando houver fonte Markdown para canvas, âncoras `<!-- c:id -->` intactas; HTML não é cópia obrigatória.
- [ ] Se pediram o canvas: IDs intactos, nenhum `{{` sobrando, campos completos, sem estouro e uma página, conferidos no arquivo entregue.
