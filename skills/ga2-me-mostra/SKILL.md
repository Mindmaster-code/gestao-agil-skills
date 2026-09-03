---
name: ga2-me-mostra
description: "Transforma uma situação de gestão em um visual curto, acionável e sem jargão. Sempre gera HTML e usa o recurso visual disponível. Use para me mostra, desenha, explica visualmente, onde trava, antes e depois ou qual decisão o quadro pede."
---

# Me Mostra — Gestão Visual GA 2.0

## Regra principal

Sempre termine com um artefato HTML. Leia `references/metodo.md` por inteiro antes de criar
o visual. Mostre o menor visual que permita entender o caso e decidir.

## Linguagem obrigatória

- Escreva em português simples e direto.
- Use a palavra comum antes do termo técnico.
- Explique toda sigla na primeira aparição, na mesma linha.
- Evite inglês quando houver uma palavra comum em português.
- Aplique a regra no título, rótulos, legendas, dicas, texto alternativo e resposta final.
- Releia apenas o texto visível antes de entregar. Jargão solto reabre o trabalho.

## Como conduzir

1. Escreva a pergunta que o visual responde.
2. Escolha a pergunta que libera a próxima decisão.
3. Separe o que é medido, estimado e ainda está em aberto.
4. Escolha um visual principal: fluxo, quadro, antes e depois, causa, matriz ou linha do tempo.
5. Gere o HTML com pergunta, leitura direta, visual, prova e consequência.
6. Feche com o que ficou claro, o que segue em aberto e o próximo passo.

Use `assets/template-artefato.html` como ponto de partida. O HTML deve funcionar sem rede,
biblioteca externa ou imagem remota.

## Entrega por ambiente

- No Claude, use Artifact quando esse recurso estiver disponível.
- No Codex ou GPT, use o artefato ou a visualização exposta na sessão.
- No Cursor, use sua prévia ou visualização disponível.
- Em outro ambiente, use o recurso equivalente.
- Não escolha pela marca do modelo. Verifique o que o ambiente oferece.
- Sem recurso nativo, salve `.md` e `.html`, mostre um resumo visual no terminal ou no chat e
  informe o caminho do HTML.

Nunca entregue apenas Markdown, Mermaid, imagem ou diagrama de terminal. O HTML é obrigatório.

## Critério de pronto

- O visual principal responde à pergunta em até 90 segundos.
- O significado continua claro sem cor.
- Fato, estimativa e ponto em aberto não se misturam.
- Título e rótulos não contêm sigla ou jargão sem explicação.
- A entrega gerou HTML e usou a melhor forma disponível no ambiente.
