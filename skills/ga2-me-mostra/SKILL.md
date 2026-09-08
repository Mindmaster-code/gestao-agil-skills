---
name: ga2-me-mostra
description: "Use quando o usuário pedir para ver, desenhar ou explicar visualmente um caso, fluxo, problema, mudança ou decisão de gestão descrito no pedido ou na conversa atual; não use para assuntos sem um caso de gestão."
---

# Me Mostra — Gestão Visual GA 2.0

## Regra principal

Quando houver um caso de gestão identificável, gere HTML por padrão e respeite outro formato solicitado. Leia
`references/metodo.md` por inteiro antes de criar o visual. Mostre o menor visual que permita
entender o caso e decidir.

## Objeto do visual

Determine o objeto antes de escolher o formato:

1. Se o pedido atual nomeia um caso, processo, artefato ou decisão, esse é o objeto.
2. Se usa “isso”, “aqui”, “o que falamos”, “este caso” ou apenas “me mostra”, use o caso ou
   artefato de gestão mais recente da conversa atual.
3. O nome do plug-in ou da habilidade serve apenas para invocá-la. Nunca o use como objeto por
   padrão. Mostre o método Gestão Ágil 2.0 somente quando o usuário pedir isso explicitamente.

Prenda a resposta aos elementos concretos disponíveis no caso, como números, etapas, pessoas,
bloqueios ou decisões. Quando a conversa contiver dois ou mais desses elementos, use pelo menos
dois deles no título, na leitura ou na prova.

Se não houver um caso de gestão identificável, não gere HTML nem substitua o assunto pelo método.
Faça somente uma pergunta curta para o usuário indicar qual situação de gestão deseja visualizar.

## Linguagem obrigatória

- Escreva em português simples e direto.
- Use a palavra comum antes do termo técnico.
- Explique toda sigla na primeira aparição, na mesma linha.
- Evite inglês quando houver uma palavra comum em português.
- Aplique a regra no título, rótulos, legendas, dicas, texto alternativo e resposta final.
- Releia apenas o texto visível antes de entregar. Jargão solto reabre o trabalho.

## Como conduzir

1. Confirme o objeto usando o pedido atual e o histórico da conversa.
2. Escreva a pergunta que o visual responde.
3. Escolha a pergunta que libera a próxima decisão.
4. Separe o que é medido, estimado e ainda está em aberto.
5. Escolha um visual principal: fluxo, quadro, antes e depois, causa, matriz ou linha do tempo.
6. Gere a entrega escolhida com pergunta, leitura direta, visual, prova e consequência.
7. Feche com o que ficou claro, o que segue em aberto e o próximo passo.

Para HTML, use `assets/template-artefato.html` como ponto de partida. Ele deve funcionar sem rede,
biblioteca externa ou imagem remota.

## Entrega por ambiente

- No Claude, use Artifact quando esse recurso estiver disponível.
- No Codex ou GPT, use o artefato ou a visualização exposta na sessão.
- No Cursor, use sua prévia ou visualização disponível.
- Em outro ambiente, use o recurso equivalente.
- Não escolha pela marca do modelo. Verifique o que o ambiente oferece.
- Quando a saída escolhida for HTML e não houver recurso nativo, salve `.html` e mostre um resumo.
  Markdown acompanha somente quando necessário ao fluxo. Informe o caminho do HTML.

Para entrega visual sem outro formato pedido, gere HTML. Para Word, Docs ou planilhas solicitados, siga a entrega editável.

## Critério de pronto

- O visual principal responde à pergunta em até 90 segundos.
- O significado continua claro sem cor.
- Fato, estimativa e ponto em aberto não se misturam.
- Título e rótulos não contêm sigla ou jargão sem explicação.
- O objeto é o caso de gestão ativo, nunca o nome do plug-in por padrão.
- A entrega usou o formato solicitado; sem escolha explícita, gerou HTML.

## Entrega editável

Leia `references/entrega-editavel.md` ao criar ou revisar um artefato.
Padrão desta skill, sem formato definido: visual HTML; Word `.docx`, Google Docs, Excel `.xlsx` ou Google Sheets quando solicitados.
O formato pedido e o documento existente orientam a entrega. Referências de HTML aplicam-se somente à saída visual. Use ferramentas de arquivos ou integração disponível.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

## Recursos específicos desta habilidade

O método completo está em `references/metodo.md`; ele define a sequência e as regras específicas.
Ao preencher o artefato, leia `references/template.md` por inteiro e preserve seus campos.
Consulte `references/exemplo.md` para entender o preenchimento; é fictício, nunca evidência do caso do usuário.
Antes de entregar, confira os critérios de pronto de `references/metodo.md`.
