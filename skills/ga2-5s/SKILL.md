---
name: ga2-5s
description: "Aplica o 5S (utilização, organização, limpeza, padronização e disciplina) a qualquer alvo que o usuário nomear: mesa, pasta de arquivos, caixa de e-mail, agenda, backlog, planilha, documentação, processo, repositório de código, estrutura de agentes de IA, campanhas de anúncio, funil comercial. Faz a foto do antes com nota, separa o que não é usado com etiqueta vermelha, dá um lugar a cada coisa, limpa tratando a fonte da sujeira, escreve o padrão de uma página e deixa a rotina que mantém. Use quando pedirem \"5S em/no/na ...\", arrumar, organizar, enxugar, limpar ou padronizar alguma coisa, ou quando procurar algo virou rotina."
---

> Sem canvas oficial no curso. A entrega é o Relatório 5S de `references/template.md`.

# 5S

O 5S nasceu no chão de fábrica da Toyota e vale para mesa física e digital. Os três primeiros S
são de fazer: tirar da frente o que não se usa, dar um lugar a cada coisa e limpar. Os dois
últimos são de comportamento: fazer isso todo dia, do mesmo jeito, até virar hábito. Cada S
elimina desperdício, a começar pelo tempo gasto procurando.

Antes de montar, pergunte o que faltar. Não invente dados.

## O alvo é o parâmetro

O pedido traz o alvo: "5S na pasta do projeto", "5S no repositório", "5S nas campanhas",
"5S na minha agenda", "5S na estrutura de agentes". Sem alvo claro, faça uma pergunta só:
"Em que você quer aplicar o 5S?", com até três sugestões tiradas da conversa.

Consulte `references/alvos.md` para traduzir o alvo: o que é um item, como se prova uso, onde é
o lugar certo, qual é a sujeira típica e de onde vem, que padrão e que rotina mantêm.
Alvo que não está lá: responda essas cinco perguntas antes de começar e mostre a tradução.

## Como conduzir

1. Leia `references/metodo.md` por inteiro antes de começar.
2. **Enquadre** em poucas linhas: alvo e fronteira, para que serve, dono e usuários, risco e
 "pronto quando" (o que fica mais fácil, com uma medida). Alvo grande vira fatias: comece
 pela parte mais usada ou pela que mais dói.
3. **Escolha o modo.** Diagnóstico (só a foto e a nota, não mexe), arrumação (os cinco S com o
 sim do dono), manutenção (refaz a nota e trata o que voltou) ou rotina (padrão, rotina e
 vigia). Sem modo definido: diagnóstico primeiro, depois ofereça a arrumação. O diagnóstico sai
 curto: os achados que mais pesam (de 3 a 10; um achado pode ser um lote) e as decisões do dono.
4. **Foto do antes:** inventário da fatia, três medidas (itens à mão, teste de achar, problemas
 abertos por tipo) e a nota de 0 a 4 em cada S, sempre com o fato que a sustenta. Leia o alvo pelo
 próprio sistema; não altere. Alvo grande: conte e meça amostra; contagem de varredura entra como
 estimada; o que não deu para verificar fica "não verificado", com onde se procurou.
5. **Utilização (Seiri):** destino de cada item pela prova de uso, nunca por opinião: à mão,
 guardado com catálogo, devolvido ao dono, quarentena com etiqueta vermelha e prazo, ou
 descarte com o sim do dono.
6. **Organização (Seiton):** um lugar para cada coisa, nome previsível, o mais usado mais perto,
 poucos níveis. Faça o teste de achar com quem não arrumou.
7. **Limpeza (Seiso):** limpar é inspecionar. Corrija o quebrado e o errado e pergunte de onde a
 sujeira vem. Se já havia uma guarda que devia ter pego, descubra por que falhou. Trate a fonte
 com contramedida à prova de erro; causa difícil vai para `ga2-causa-raiz`.
8. **Padronização (Seiketsu):** padrão em uma página, à vista onde o trabalho acontece; quando
 der, vira guarda automática (modelo, nome sugerido, validação).
9. **Disciplina (Shitsuke):** rotina em doses pequenas, com dono, frequência e a mesma nota na
 auditoria. Em alvo digital, proponha um vigia que só lê e avisa o que é novo.
10. **Leve ao dono numa rodada só** tudo o que depende dele: a tabela item → de onde → para onde
 → por quê, a quarentena, o descarte, o que fica no lugar de propósito, o padrão e a rotina.
11. **Aplique só o aprovado**, refaça a foto no lugar real e entregue o Relatório 5S com antes e
 depois na mesma régua.

## Regras de segurança

- Nada vai embora sem o sim do dono. Quarentena e arquivo vêm antes do descarte; descarte
 definitivo só quando o dono pedir.
- Antes de mover, veja quem aponta para o item: link, atalho, fórmula, código, automação. O que é
 lido por um caminho fixo fica onde está ou muda junto com quem o lê.
- Mover não é copiar. Preserve identidade, link e histórico.
- Em sistema vivo (produção, campanha no ar, dado de cliente, dinheiro): leia o estado atual, faça
 a menor mudança possível, confira depois e tenha como desfazer. Em período crítico, o que mexe
 no que está rodando vai marcado "só depois de <data>".
- O que é de outra pessoa ou área volta para ela; não se reorganiza o que não é seu.
- Arrumar não é reescrever: mude o lugar, não o conteúdo, a menos que peçam.

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
Padrão desta skill, sem formato definido: documento `.docx` com o Relatório 5S; Google Docs quando esse for o destino escolhido. Inventário com mais de umas 50 linhas vai também em planilha.
O formato pedido e o documento existente orientam a entrega. Referências de HTML aplicam-se somente à saída visual. Use ferramentas de arquivos ou integração disponível.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Quando HTML for a entrega escolhida, use `assets/template-artefato.html`.
Apresente o visual no recurso nativo disponível; sem ele, forneça o arquivo HTML autônomo.

Consulte `references/gestao-visual.md` apenas quando precisar escolher ou montar o visual.
Consulte `references/fontes.md` apenas quando precisar conferir a origem ou a força de uma
afirmação do método.

## Critério de pronto

- Alvo, propósito, dono e risco estão escritos.
- Há foto do antes e do depois, com a mesma nota e as mesmas medidas.
- Todo item fora do lugar tem destino, motivo e prova; o duvidoso tem etiqueta vermelha e prazo.
- Cada sujeira que se repete tem fonte nomeada e contramedida.
- O padrão cabe em uma página e está onde o trabalho acontece.
- A rotina tem dono, frequência e data da próxima auditoria.
- Nada foi descartado sem o sim do dono; o que mudou foi conferido no lugar real.
- O arquivo ou documento foi reaberto e conferido; suas exportações refletem a fonte atual.

## Recursos específicos desta habilidade

O método completo está em `references/metodo.md`; ele define a sequência, a nota, a quarentena e
as regras de cada S.
A tradução por alvo está em `references/alvos.md`.
Ao preencher o relatório, leia `references/template.md` por inteiro e preserve seus campos.
Consulte `references/exemplo.md` para entender o preenchimento; é fictício, nunca evidência do caso do usuário.
Antes de entregar, aplique `references/checklist.md` por inteiro.

Combina com: `ga2-causa-raiz` (fonte da sujeira que não é óbvia), `ga2-pop` (padrão que vira
procedimento), `ga2-sistema-de-rotinas` (encaixar a rotina na agenda), `ga2-gemba-walk` (auditoria
no lugar), `ga2-quadro-kaizen` (melhoria que sai da auditoria), `ga2-backlog-2d` (poda mensal da
lista) e `ga2-abrir-projeto` (pasta de projeto que já nasce no padrão).
