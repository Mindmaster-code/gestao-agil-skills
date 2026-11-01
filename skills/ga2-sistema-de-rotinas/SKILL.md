---
name: ga2-sistema-de-rotinas
description: "Monta o sistema de rotinas de um gestor: o calendário do dia ao ano, o inventário com o custo por semana de cada rotina e o plano de implantação em 90 dias. Use quando pedirem calendário de rotinas, inventário de reuniões, custo de uma reunião, por onde começar as rotinas, quais rotinas manter ou plano de 90 dias."
---

# Sistema de rotinas

## Como conduzir

1. Leia `references/metodo.md` por inteiro antes de montar a resposta.
2. Confirme qual decisão ou resultado o usuário precisa alcançar.
3. Separe fatos, estimativas e pontos ainda sem resposta.
4. Aplique os campos e a sequência descritos na referência.
5. Siga o nível de detalhe previsto no método para o caso; não force campos de outra variante.
6. Feche com consequência, próximo passo, dono e data quando esses dados existirem.

## Escolha o modo

Líder é qualquer pessoa que coordena trabalho e gente, em qualquer área. Descubra o ramo do usuário e use exemplos do ramo dele.

- **A. Pelo sintoma** (modo principal): o sintoma da área, o número de hoje e a rotina por onde começar.
- **B. Calendário do gestor ágil** (modelo CAL): o que já acontece, do dia ao ano, e a lista dos próximos ciclos.
- **C. Inventário e custo por semana** (modelo T15): minutos vezes pessoas e uma decisão por rotina.
- **D. Utilidade de cada rotina**: o efeito que ela produz, lido em três métricas.
- **E. Plano de implantação em 90 dias** (modelo P90): conjunto inicial, quatro janelas e revisão do dia 90.
- **F. Quem cuida de cada rotina**: dono, versão local em POP e teste do texto.

Sem pedido específico, comece pelo modo A. A diária é de `ga2-gestao-diaria`, o planejamento do ciclo é de `ga2-plano-do-ciclo` e a agenda pessoal do líder é de `ga2-agenda-do-lider`.

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
Padrão desta skill, sem formato definido: planilha `.xlsx`; Google Sheets quando esse for o destino escolhido.
O formato pedido e o documento existente orientam a entrega. Referências de HTML aplicam-se somente à saída visual. Use ferramentas de arquivos ou integração disponível.
Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.
Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.

Quando HTML for a entrega escolhida, use `assets/template-artefato.html`.
Apresente o visual no recurso nativo disponível; sem ele, forneça o arquivo HTML autônomo.

Um pedido só de orientação, como "por onde começo as rotinas?", pode ser respondido no chat, com as tabelas. Gere o arquivo quando o líder pedir ou quando for guardar o sistema.
Na planilha, uma aba para cada peça (calendário, inventário e plano de 90 dias). O custo por semana vai em fórmula (minutos vezes pessoas), e a soma é conferida contra o total escrito.
Se o líder pedir o calendário desenhado, use `agenda-visual` a partir do calendário já preenchido.
Se o ambiente tiver integração de calendário com escrita, proponha as rotinas como eventos e só os crie depois que o líder aprovar, sem convidar ninguém. Sem essa integração, entregue a tabela. Não diga que marcou na agenda sem o retorno da ferramenta.
O inventário e a conta do custo são do líder: não os envie à equipe sem pedido.

Consulte `references/gestao-visual.md` apenas quando precisar escolher ou montar o visual.
Consulte `references/fontes.md` apenas quando precisar conferir a origem ou a força de uma
afirmação do método.

## Critério de pronto

- O artefato responde à pergunta do usuário.
- Uma pessoa sem conhecimento prévio entende os rótulos.
- Todo número tem fonte ou está marcado como estimativa ou ponto em aberto.
- O próximo passo não fica escondido.
- Cada rotina do inventário tem custo por semana (minutos × pessoas) e uma decisão: manter, ajustar, combinar, reduzir ou encerrar. O dono vem com nome, ou fica marcado como não definido.
- O plano de 90 dias tem datas reais nas quatro janelas e o número de hoje, medido antes de mudar qualquer coisa. Sem a medição, o número fica em aberto e a primeira tarefa é medir.
- O arquivo ou documento foi reaberto e conferido; suas exportações refletem a fonte atual.

## Recursos específicos desta habilidade

O método completo está em `references/metodo.md`; ele define a sequência e as regras específicas.
Ao preencher o artefato, leia `references/template.md` por inteiro e preserve seus campos.
Consulte `references/exemplo.md` para entender o preenchimento; é fictício, nunca evidência do caso do usuário.
Antes de entregar, aplique `references/checklist.md` por inteiro.

Esta habilidade não tem canvas oficial do curso. O modelo de entrega é o `references/template.md`:
o calendário, o inventário com o custo por semana e o plano de 90 dias, com os campos dos modelos CAL, T15 e P90 do curso de rotinas.
