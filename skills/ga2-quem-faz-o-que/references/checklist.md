# Quem faz o quê — critério de "bem feito" e erros comuns

## Bem feito

Dono
- [ ] Exatamente um nome de pessoa na linha Dono.
- [ ] O dono responde pelo resultado, não pela tarefa.
- [ ] O dono está no cartão do quadro e nas 6 linhas da demanda.
- [ ] Se dois reivindicam, a matriz não foi fechada: há carta ao dirigente responsável com as duas versões.

Aceitante e gate
- [ ] Aceitante nomeado; não é o executor nem o Gestor Ágil.
- [ ] Aceitante consegue conferir a DoD sozinho, pelo caminho real.
- [ ] Toda ação sensível tem decisor de gate com pessoa, proposta escrita e data do pedido.
- [ ] Gate e aceite estão separados; "GO" local não virou aceite.
- [ ] Gates do mesmo decisor listados juntos, não um por vez.

Executores e apoios
- [ ] Executores têm nome e "o que puxa primeiro".
- [ ] Apoio está listado como apoio, sem dividir a responsabilidade.
- [ ] Apoio com DoD/handoff/acesso próprio virou demanda filha com dono.

Processo
- [ ] Dono do processo (Gestor) e dono do rumo (PO/diretor) são pessoas diferentes.
- [ ] Acumulações declaradas por escrito.
- [ ] Quem recebe o resultado está marcado para a review.
- [ ] Transferência de dono, se houve, tem aceite escrito do novo dono.
- [ ] Empresa da frente declarada (Empresa A · Empresa B · Compartilhado).

## Erros comuns (da aula e do laboratório)

| Erro | Sinal | Correção |
|---|---|---|
| Dois donos | "Mariana e Lucas" | um nome; o outro vira Aceitante ou apoio |
| Dono-área | "Operações" | pessoa |
| Cartão de todo mundo | "o time" | "cartão de todo mundo não é de ninguém" (v6 03) |
| SM + PO na mesma pessoa | o gestor prioriza e também conduz a retro | delegar um dos dois (A10) |
| Aceitante = executor | "eu mesmo confiro" | quem recebe o resultado confere |
| Aceitante = Gestor | "o Gestor Ágil aceita" | Gestor cobra, não aceita (organograma l.214) |
| Gate sem pessoa | "depende do Conselho" | nome + proposta + data |
| Gate confundido com aceite | "aprovou a copy, então está entregue" | aceite é DoD global (§8, §11) |
| Apoio co-dono | apoio aparece na coluna Dono | coluna Dono só DRI |
| Filha escondida | apoio publica sem cartão próprio | demanda filha com dono, DoD, Aceitante |
| Transferência por mensagem | "passei pra você" sem resposta | novo dono aceita por escrito; até lá o antigo responde |
| Nome antigo na fonte | "Dono: nome antigo" | atualizar a fonte (pedido ao dono), registrar divergência |

## Formas de saída

- [ ] Entrega no formato pedido, conforme [entrega-editavel.md](entrega-editavel.md), salva e conferida; nas revisões, mesmo documento e edições humanas preservados.
- [ ] Quando houver fonte Markdown para canvas, âncoras `<!-- c:id -->` intactas; HTML não é cópia obrigatória.
- [ ] Se pediram o canvas: IDs intactos, nenhum `{{` sobrando, campos completos, sem estouro e uma página, conferidos no arquivo entregue.
