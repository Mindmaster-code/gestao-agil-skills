---
name: ga2-diagnostico
description: "Compara a situação atual com a desejada, mede a distância e registra a linha de partida. Use quando pedirem diagnóstico, estado atual, meta, distância para a meta ou lado esquerdo do A3."
---

# Diagnóstico atual e desejado

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

Quando o pedido criar um artefato, gere uma fonte Markdown e um HTML com o mesmo nome.
Use `assets/template-artefato.html` como ponto de partida para o HTML.

Use o recurso visual do ambiente quando ele estiver disponível: Artifact no Claude,
artefato ou visualização no Codex/GPT, prévia no Cursor e o equivalente em outro ambiente.
O ambiente prevalece sobre o nome do modelo.

Sem recurso visual nativo, salve o HTML e apresente um resumo visual curto no terminal ou
no chat. Informe o caminho do arquivo. O HTML precisa funcionar sem rede e no celular.

Consulte `references/gestao-visual.md` apenas quando precisar escolher ou montar o visual.
Consulte `references/fontes.md` apenas quando precisar conferir a origem ou a força de uma
afirmação do método.

## Critério de pronto

- O artefato responde à pergunta do usuário.
- Uma pessoa sem conhecimento prévio entende os rótulos.
- Todo número tem fonte ou está marcado como estimativa ou ponto em aberto.
- O próximo passo não fica escondido.
- O Markdown e o HTML dizem a mesma coisa.

## Canvas oficial e documento

Quando o usuário pedir o canvas do curso ("gera o canvas", "no formato oficial", "igual ao PDF") ou o documento
padrão, use os modelos de `assets/modelos/`:

- `template-<id>.md` — o arquivo a preencher; as marcas `<!-- c:... -->` dizem onde está cada campo e não podem ser apagadas;
- `canvas-<id>.html` — réplica do canvas oficial, em branco;
- `documento.html` — a forma documento, em branco;
- `CAMPOS.md` — nome e texto-guia de cada campo.

Canvas desta habilidade:

- `a3-esquerdo-b-05` — A3 — lado esquerdo (editável) (editável por módulo) — padrão

Para gerar a partir do `.md` preenchido (Python 3.10 ou mais novo, na pasta do pacote):

```bash
python3 construtor/construir.py a3-esquerdo-b-05 --documento --md meu-caso.md --saida meu-caso.html
python3 construtor/construir.py a3-esquerdo-b-05 --canvas --md meu-caso.md --saida meu-caso-canvas.html
```

Sem Python: copie o canvas em branco e escreva dentro das `div[data-campo]`, mantendo os ids.
O `.md` é a fonte; o que não estiver nele não entra no canvas. Canvas marcado como acréscimo do laboratório
não faz parte do curso.
