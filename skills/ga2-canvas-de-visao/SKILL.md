---
name: ga2-canvas-de-visao
description: "Define o norte de uma empresa, área ou iniciativa com passado, situação atual, tendências, futuro e frase de visão. Use quando pedirem Canvas de Visão, direção, contexto ou futuro desejado."
---

# Canvas de Visão

## Como conduzir

1. Leia `references/metodo.md` por inteiro antes de montar a resposta.
2. Confirme qual decisão ou resultado o usuário precisa alcançar.
3. Separe fatos, estimativas e pontos ainda sem resposta.
4. Aplique os campos e a sequência descritos na referência.
5. Escolha a forma leve, intermediária ou completa conforme o risco do caso.
6. Feche com consequência, próximo passo, dono e data quando esses dados existirem.

## Linguagem obrigatória

- Escreva em português simples e direto.
- Use a palavra comum antes do termo técnico.
- Explique toda sigla na primeira aparição, na mesma linha.
- Evite inglês quando houver uma palavra comum em português.
- Preserve o nome oficial do artefato e explique sua função.
- Não invente fatos, números, causas, donos, datas ou aprovações.
- Marque cada afirmação como medida, estimada ou em aberto quando houver incerteza.

## Entrega

Leia `references/entrega-editavel.md` ao criar ou revisar um artefato.
Padrão desta skill, sem formato definido: documento Word `.docx`; Google Docs quando esse for o destino escolhido.
O formato pedido e o documento existente orientam a entrega. Referências de HTML aplicam-se somente à saída visual. Use ferramentas de arquivos ou integração disponível.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Quando HTML for a entrega escolhida, use `assets/template-artefato.html`.
Apresente o visual no recurso nativo disponível; sem ele, forneça o arquivo HTML autônomo.

Consulte `references/gestao-visual.md` apenas quando precisar escolher ou montar o visual.
Consulte `references/fontes.md` apenas quando precisar conferir a origem ou a força de uma
afirmação do método.

## Critério de pronto

- O artefato responde à pergunta do usuário.
- Uma pessoa sem conhecimento prévio entende os rótulos.
- Todo número tem fonte ou está marcado como estimativa ou ponto em aberto.
- O próximo passo não fica escondido.
- O arquivo ou documento foi reaberto e conferido; suas exportações refletem a fonte atual.

## Canvas oficial e documento

Quando o usuário pedir o canvas do curso ("gera o canvas", "no formato oficial", "igual ao PDF") ou o documento
HTML, use os modelos de `assets/modelos/`:

- `template-<id>.md` — o arquivo a preencher; as marcas `<!-- c:... -->` dizem onde está cada campo e não podem ser apagadas;
- `canvas-<id>.html` — réplica do canvas oficial, em branco;
- `documento.html` — a forma documento, em branco;
- `CAMPOS.md` — nome e texto-guia de cada campo.

Canvas desta habilidade:

- `visao-kit-01` — Canvas de Visão (canvas do kit do curso) — padrão

Para gerar a partir do `.md` preenchido (Python 3.10 ou mais novo, na pasta do pacote):

```bash
python3 construtor/construir.py visao-kit-01 --documento --md meu-caso.md --saida meu-caso.html
python3 construtor/construir.py visao-kit-01 --canvas --md meu-caso.md --saida meu-caso-canvas.html
```

Sem Python: copie o canvas em branco e escreva dentro das `div[data-campo]`, mantendo os ids.
No construtor HTML, o `.md` é a entrada atual; não use cópia antiga para substituir documento vivo. Canvas marcado como acréscimo do laboratório
não faz parte do curso.
