# Kanban Canvas — critério de "bem feito" e erros comuns

## Bem feito (marque tudo antes de declarar o quadro pronto)

Desenho
- [ ] O quadro tem nome, dono de atualização e lugar onde mora.
- [ ] As colunas foram desenhadas a partir do fluxo **atual**, com quem faz o trabalho.
- [ ] Há pelo menos fila, execução e pronto; não é o "melancia" genérico.
- [ ] Mais de um tipo de demanda virou raia, não quadro solto.
- [ ] Quadros de níveis diferentes se conversam: um cartão na carteira de iniciativas = um quadro na área.

Cartão
- [ ] Todo cartão tem origem (OKR/entrega), o que é numa frase, dono com nome de pessoa, prazo, idade.
- [ ] Todo cartão cabe em uma semana; dá para dizer o momento em que fica pronto.
- [ ] Cartão veio do Backlog 2D, não foi inventado no quadro.
- [ ] Cartão tem campo de prova.

Políticas
- [ ] "Feito" está escrito por extenso ao lado da coluna Feito.
- [ ] Limite de WIP está no topo de cada coluna de execução, como número.
- [ ] Ritmo de atualização tem dia, hora e duração.
- [ ] Entrada, prioridade, bloqueio e atualização estão escritas **no quadro**, não em documento à parte.
- [ ] A representação de bloqueio está escolhida (opção A do método: marca no cartão) e a escalada tem dias e nome.

Uso
- [ ] Alguém decide sem perguntar olhando o quadro (teste material de referência).
- [ ] Cartão nunca volta de coluna.
- [ ] O quadro é usado na diária, na review e na retro.
- [ ] Estado vem de arquivo, não de memória.

Carteira de iniciativas
- [ ] Cada cartão tem fonte (caminho do STATUS, backlog ou demanda).
- [ ] Dias parado e gate (decisor + data) estão preenchidos ou marcados "?".
- [ ] Número nunca cruza raia (uma área ≠ outra área).
- [ ] A "leitura da fotografia" diz qual é a primeira cobrança que sai.

Dependência entre áreas (ficha B06)
- [ ] O cartão tem "depende de" e "entrega para", com a pessoa e a data de passagem.
- [ ] Existe a coluna "Aguardando outra área", com limite próprio, e o cartão que espera nela não volta para trás.
- [ ] As duas áreas veem o mesmo cartão.
- [ ] O encontro entre áreas tem quem possa assumir compromisso, pauta curta e custo calculado.
- [ ] Cada dependência crítica fechou com dono, aceite e próxima verificação.
- [ ] O conflito sem alçada subiu a quem responde pelo resultado das duas áreas.

## Erros comuns (da aula)

| Erro | Como reconhecer | Antídoto |
|---|---|---|
| Kanban melancia | colunas iguais às de qualquer tutorial | desenhar o próprio fluxo (material de referência) |
| Kanban no limbo | última atualização há semanas | combinar quem atualiza e quando |
| Kanban congestionado | coluna Fazendo com 12 cartões | escrever limite por etapa |
| Cartão de área | "Marketing" no campo dono | nome de pessoa (material de referência) |
| Cartão-iniciativa | seis semanas em "fazendo" | quebrar no Backlog 2D até caber numa semana |
| Dar ré | cartão volta para A fazer quando trava | marca no cartão; fica parado e sinalizado |
| Política na gaveta | regra num PDF que ninguém abre | três regras mínimas no topo do quadro |
| Quadro decorativo | "está lá só para tirar foto" | "um quadro que mente é pior que quadro nenhum" |
| Coluna invisível | cartões somem por dias numa validação externa | criar a coluna com WIP próprio (M06 A20) |
| Dependência só na conversa | a outra área descobre o atraso na hora de precisar | escrever "depende de" e "entrega para" no cartão |
| Encontro entre áreas sem poder de decisão | sai sem dono nem próxima verificação | chamar quem pode assumir compromisso pela área |

## Formas de saída

- [ ] Entrega no formato pedido, conforme [entrega-editavel.md](entrega-editavel.md), salva e conferida; nas revisões, mesmo documento e edições humanas preservados.
- [ ] Quando houver fonte Markdown para canvas, âncoras `<!-- c:id -->` intactas; HTML não é cópia obrigatória.
- [ ] Se pediram o canvas: IDs intactos, nenhum `{{` sobrando, campos completos, sem estouro e uma página, conferidos no arquivo entregue.
