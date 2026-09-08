# Molde de resposta — Me mostra

Use este molde como estrutura, não como formulário obrigatório. Corte blocos que não ajudam
a decisão.

## Pergunta

<Uma frase que o visual responde.>

## Leitura

<Resposta direta em uma frase, com a consequência.>

## Visual

**Intenção:** <estado atual | mudança | diagnóstico | decisão>  
**Forma visual:** <fluxo | quadro visual do trabalho (Kanban) | raias | atual×desejado | antes×depois |
esperado×observado | causa | dependência | matriz | árvore | linha do tempo | painel>

```text
<visual principal>
```

## Prova

| Afirmação ou número | Selo | Fonte e data |
|---|---|---|
| | medido / estimado / em aberto | |

## Decisão ou próximo passo

- **O que acontece agora:** <ação ou decisão>.
- **Dono:** <uma pessoa ou “não definido”>.
- **Data:** <data ou “não definida”>.
- **Quem decide:** <pessoa ou “ninguém”>.

Para saída durável, preserve esta estrutura no formato escolhido, conforme `entrega-editavel.md`.
Se o formato for HTML, siga `artefatos-por-harness.md`; mantenha Markdown apenas quando o fluxo precisar.

## Entrega HTML

- **Ambiente detectado:** <Claude | Codex/ChatGPT | Cursor | outro>.
- **Forma usada:** <Artifact | visualização | prévia | Canvas | Browser | arquivo + terminal>.
- **Fonte HTML:** <caminho ou referência exigida pelo ambiente>.
- **Resumo no terminal:** <não, se nativo | sim, se não houver visual nativo>.

Quando a entrega escolhida for visual HTML, gere o HTML mesmo se o pedido nasceu no chat.
Sem superfície nativa, salve o HTML e informe seu caminho. Markdown só acompanha quando necessário.
Um pedido de Word/Docs ou planilha não exige cópias HTML e Markdown.
