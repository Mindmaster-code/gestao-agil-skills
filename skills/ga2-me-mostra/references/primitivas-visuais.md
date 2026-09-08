# Primitivas visuais

Escolha pela relação que precisa ficar visível. Preserve a mesma semântica no texto e no
HTML: base, foco, exceção e prova.

## 1. Fluxo

Use para ordem, passagem do trabalho e ponto de espera.

```text
Entrada → Triagem → Execução → Aprovação → Entrega
                     │          ▲
                     └─ trava: prova ausente
```

Rótulo em cada seta só quando a condição importa. Em HTML, use SVG inline ou blocos com
setas CSS. Não desenhe fluxo para uma lista sem dependência.

## 2. Fotografia Kanban

Use para distribuição do trabalho, limite, idade e bloqueio.

```text
FILA (3)        FAZENDO (2/2)       FEITO
NS-01           NS-02 · 4 dias      NS-03 · prova
NS-04           NS-05 · BLOQUEADO
NS-06
```

Mostre o limite junto da coluna. Bloqueio fica no cartão e não depende só da cor.

## 3. Raias de responsabilidade

Use para papéis, passagens e esperas entre pessoas ou agentes.

```text
Dono       define pronto ─────────────── aceita
Agente                    executa ── prova
Decisor                              aprova
```

Pessoa e agente ficam em linhas diferentes. Não use raia para atribuir dono inexistente.

## 4. Atual × desejado

Use para meta, gap ou transformação.

```text
ATUAL                  GAP                 DESEJADO
2 dias ─────────────── 3 dias ─────────── 5 dias
[medido · fonte]                           [meta · prazo]
```

Compare a mesma medida dos dois lados. Se a unidade mudar, o visual é inválido.

## 5. Antes × depois

Use para mudança de regra, processo ou estrutura.

```text
ANTES                              DEPOIS
pedido → três caixas → espera      pedido → dono único → resposta
          ^ sem aprovação                    ^ quem aprova está nomeado
```

Marque o ponto alterado. Não redesenhe o que permaneceu igual.

## 6. Esperado × observado

Use para diagnóstico de falha.

```text
ESPERADO   agendador → tarefa → 6 arquivos → leitura
OBSERVADO  agendador → ERRO ─────────────→ 0 arquivos
                    ^ primeira divergência
```

Comece no último ponto conhecido como correto. Destaque a primeira divergência, não o último
sintoma.

## 7. Causa

Use 5 Porquês quando houver uma cadeia dominante.

```text
Sintoma → por quê 1 → por quê 2 → causa de processo → contramedida
```

Use Ishikawa quando categorias paralelas explicarem o efeito. Em HTML, o SVG mostra a
espinha; uma tabela curta guarda evidência e fonte de cada ramo.

## 8. Dependência e linhagem

Use para mostrar de onde um item veio e o que ele alimenta.

```text
Causa → Contramedida → Iniciativa → Entrega → Cartão → Prova
```

O foco ganha rótulo; os demais nós ficam como contexto. Corte a cadeia em `…` quando a parte
omitida não muda a decisão.

## 9. Matriz de decisão

Use quando duas dimensões separam opções.

```text
IMPACTO ↑
        planeje        faça já
        evite          encaixe
                       → ESFORÇO
```

Escreva os critérios e a fonte da posição. Sem critério medido, marque a posição como
estimada.

## 10. Árvore de decisão

Use quando respostas sucessivas mudam o caminho.

```text
Tem fim e entrega única?
├─ sim → Projeto em ciclos
└─ não → A demanda se repete?
          ├─ sim → Fluxo contínuo
          └─ misto → Híbrido, com regra de quem cede
```

Cada folha precisa terminar em decisão, ação ou ponto em aberto.

## 11. Linha do tempo

Use para cadência, marcos e mudança ao longo do tempo.

```text
SEG plano ─ QUA pulso ─ SEX review ─ SEX retro ─ PRÓXIMO ciclo
```

Mostre datas exatas quando houver compromisso. Não use linha do tempo para itens sem ordem.

## 12. Painel e tabela

Use painel para 3–5 números-âncora. Use tabela quando valores exatos ou muitos atributos
importarem mais que a forma.

```text
[12 em curso] [3 bloqueados] [8 dias: mais antigo] [2 gates]
```

Barra é proporcional ao maior valor comparado. Número sem fonte não vira gráfico.

## Regras por meio

| Meio | Preferência | Evite |
|---|---|---|
| Artefato nativo | HTML no formato exigido pelo ambiente | simular recurso indisponível |
| Prévia ou navegador nativo | HTML autônomo aberto no ambiente | captura de tela como entrega principal |
| Terminal sem prévia | HTML autônomo + texto monoespaçado resumido | resposta apenas em texto |
| HTML para circular | template público e SVG inline | biblioteca, CDN e imagem externa |
| Celular | uma coluna, rótulo curto, rolagem só em tabela | mapa largo sem recorte |

Leia [`artefatos-por-harness.md`](artefatos-por-harness.md) para escolher a superfície. O
HTML é o padrão para pedidos de explicação visual sem outro formato escolhido. Para Word/Docs
ou planilhas solicitados, preserve a informação visual em conteúdo editável, sem cópia HTML obrigatória.
No fluxo HTML, Mermaid ou texto monoespaçado são apenas o resumo sem renderização nativa.

## Teste de compressão

1. Remova um nó. A decisão muda? Se não, mantenha removido.
2. Tire as cores. O significado continua legível? Se não, acrescente rótulo.
3. Leia só título, foco e fechamento. A resposta aparece? Se não, refaça o recorte.
