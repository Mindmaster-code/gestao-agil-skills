# Fonte canônica e instalação

Este repositório é a fonte das 32 skills GA2, seus métodos, templates, exemplos, modelos e testes.
Edite na `main` do checkout canônico. Instalação, cache e release são cópias de uso; nunca fontes de edição.

## Onde editar

- `skills/<nome>/SKILL.md`: quando aplicar a skill e como conduzir.
- `skills/<nome>/references/`: método completo, templates, checklists, exemplos fictícios e regras de entrega.
- `skills/<nome>/assets/`: recursos usados na entrega.
- `construtor/`: código, especificações e originais dos canvas.

Regras de uma empresa, responsáveis internos, caminhos privados e exemplos reais pertencem ao projeto consumidor.
Esse contexto complementa o método público, sem manter uma segunda versão da mesma skill.

## Alterar e experimentar

1. Edite a fonte neste repositório e revise o diff.
2. Se alterou specs do construtor, gere modelos com `python3 scripts/montar_construtor.py --modelos`.
3. Atualize o manifesto e hashes com `python3 scripts/atualizar_checksums.py`.
4. Execute `python3 scripts/validar.py` e os testes afetados.
5. Instale o pacote em destino de teste e experimente os casos alterados.
6. Faça commit das mudanças concluídas. Publique somente no fluxo autorizado de versão final.

A experiência interna usa a mesma skill distribuível. Melhorias voltam a este repositório antes da próxima instalação.
`skills/procedencia.json` registra o conteúdo por SHA-256. Git registra autoria e histórico.
Um hash comprova os bytes; não comprova qualidade pedagógica ou comportamento do assistente.

## Copiar, instalar e conferir

O instalador requer Python 3.10 ou superior. Não baixa dependências.

```bash
python3 scripts/montar_distribuicao.py --destino /caminho/vazio/skills
bash instalar.sh --destino /caminho/da/instalacao
bash instalar.sh --destino /caminho/da/instalacao --conferir
python3 scripts/empacotar_plugin.py --saida-dir /caminho/temporario
```

Todos os comandos funcionam com este repositório sozinho. Nenhum gerador depende de um projeto privado.
A montagem copia os arquivos exatamente; não reescreve as skills nem importa conteúdo externo.

A instalação registra versão, commit-base quando disponível e hashes em `.gestao-agil-2.json`.
O hash de conteúdo identifica exatamente uma instalação, inclusive durante testes de mudanças ainda sem commit.
Repetir uma instalação idêntica não cria cópias. Atualização com alterações locais é recusada para evitar perda de trabalho.
Pastas antigas sem registro precisam ser preservadas e migradas explicitamente antes da primeira instalação.
Ambientes no mesmo computador podem usar atalhos para uma única instalação registrada.

Escolha a tag ou commit desejado antes de instalar. Uma alteração na fonte não atualiza instalações automaticamente.
Após atualizar, abra uma sessão nova para carregar o catálogo. Plugins de diretório usam a atualização oferecida pelo aplicativo.
Não misture uma versão antiga do plugin com outra instalação das mesmas skills no mesmo ambiente.
