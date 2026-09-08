# Artefato HTML por ambiente

## Regra-mãe

Detecte a aplicação que executa a sessão e as capacidades realmente expostas. O ambiente
define a superfície; o modelo só produz o conteúdo.

Exemplo: Claude executado dentro do Cursor usa o Canvas do Cursor. Não tente criar um
Claude Artifact dentro de outro ambiente.

Use esta ordem:

1. artefato HTML interativo nativo;
2. prévia ou navegador HTML nativo;
3. arquivo HTML autônomo e resumo visual no terminal.

Não presuma disponibilidade por marca, plano ou versão. Use uma superfície somente quando a
sessão expuser a capacidade ou suas instruções oficiais.

## Adaptadores

| Ambiente ativo | Primeira escolha | Segunda escolha | Alternativa |
|---|---|---|---|
| Claude, Claude Desktop ou Claude Cowork | Claude Artifact de página HTML única | prévia HTML nativa exposta | HTML autônomo + terminal |
| Claude Code | artefato de sessão quando a capacidade estiver exposta | prévia HTML exposta | HTML autônomo + terminal |
| Codex com `visualize` | fragmento `.html` e referência definida pela skill `visualize` ativa | prévia HTML do produto | HTML autônomo + terminal |
| ChatGPT ou GPT | prévia interativa do arquivo `.html` quando exposta | visualização HTML nativa equivalente | HTML autônomo + resumo no chat |
| Codex CLI | visualização nativa somente se estiver explicitamente exposta | visualizador compatível do ambiente | HTML autônomo + terminal |
| Cursor | Canvas com fonte HTML | Browser em painel ou janela para abrir o HTML | HTML autônomo + terminal |
| Outro ambiente | artefato, canvas ou prévia HTML documentada e exposta | navegador nativo exposto | HTML autônomo + terminal |

## Regras por adaptador

### Claude

- Crie um Artifact HTML quando o ambiente oferecer Artifacts.
- No Claude Code, use o artefato de sessão apenas quando a função estiver disponível para a
  conta e a sessão.
- Se o ambiente não expuser Artifacts, não simule comandos. Use a alternativa.

### Codex e ChatGPT

- Se `visualize` estiver disponível, leia a versão ativa da skill e siga seu contrato por
  inteiro. Ela define fragmento, diretório, tema, validação e referência de conteúdo.
- Um fragmento HTML nativo não substitui o HTML autônomo exigido por uma skill dona de
  artefato durável.
- Quando o produto oferecer prévia interativa de `.html`, abra ou anexe o arquivo nessa
  superfície.
- No Codex CLI sem prévia visual, gere o arquivo e reporte o caminho absoluto.

### Cursor

- Prefira Canvas para análise, dashboard, auditoria, relatório e explicação visual.
- Faça o Canvas refletir o mesmo conteúdo do HTML; mantenha pergunta, prova e consequência.
- Sem Canvas, use o Browser nativo para abrir o HTML em painel ou janela.
- Sem Canvas e sem Browser, use a alternativa.

### Outros ambientes

- Inspecione instruções, tools e formatos de resposta disponíveis na sessão.
- Use o equivalente nativo somente se ele renderizar HTML ou aceitar uma fonte HTML.
- Não invente o nome, a sintaxe ou a existência de uma superfície.

## Forma do HTML

O contrato nativo prevalece sobre a casca técnica:

- fragmento quando a superfície exigir fragmento;
- página única quando aceitar documento completo;
- tokens do host quando o host controlar tema e contraste;
- template MindMaster quando o arquivo for autônomo.

A semântica GA 2.0 não muda entre ambientes. Pergunta, foco, exceção, prova, procedência e
próxima decisão precisam sobreviver em todas as versões.

## Alternativa obrigatória

Quando não houver solução nativa:

1. quando HTML for a entrega escolhida, gere um `.html` autônomo; `.md` acompanha apenas se o fluxo precisar;
2. grave no destino da skill dona ou na pasta escolhida pelo usuário;
3. valide que o HTML abre sem rede e sem dependência externa;
4. mostre no terminal uma versão comprimida do mesmo visual;
5. informe o caminho absoluto do HTML e a validação executada.

O resumo terminal repete apenas o essencial do HTML para quem não tem prévia visual.
