# Como atualizar sem perder o método

## Fonte e adaptação

A fonte das 31 skills de método é `.claude/skills/ga2-*/` no projeto canônico.
O gerador não usa a antiga suíte de GPTs. Ela pode ser material complementar, não a fonte deste pacote.

Cada exportação lê:

- `SKILL.md` completo, sem o cabeçalho técnico, para `references/metodo.md`;
- `template.md` e `checklist.md`, quando existente, para `references/`;
- referências auxiliares da skill, com caminhos adaptados;
- um exemplo fictício independente, nunca o exemplo operacional interno.

O projeto mantém `laboratorio/publicacao/adaptacoes/<skill>.json` com substituições exatas e seus motivos.
O que não está nessas substituições permanece igual à fonte. Uma substituição desatualizada interrompe a geração.
Os exemplos didáticos ficam em `laboratorio/publicacao/exemplos/` no projeto canônico.
As adaptações contêm trechos internos e **não são distribuídas**; o pacote contém apenas seus hashes e resultados públicos.

Modelos oficiais em branco, construtor e regras de entrega editável continuam empacotados.
As referências distinguem artefatos do curso, variantes e acréscimos do laboratório.

## Exceções explícitas

`ga2-abrir-projeto` nasce no pacote público. Não possui contraparte interna com o mesmo nome.
Seu conteúdo entra na verificação de integridade, sem alegação de origem em uma skill interna.

`ga2-me-mostra` não tem checklist separado na fonte. Seus critérios de pronto vivem no método;
as três referências de roteamento, primitivas visuais e entrega por ambiente também são exportadas.

## Gerar e conferir

Na raiz deste pacote, substitua o caminho do exemplo pelo checkout canônico real:

```bash
python3 scripts/montar_distribuicao.py --fonte /caminho/do/projeto-canonico --destino skills
python3 scripts/validar.py --fonte /caminho/do/projeto-canonico
python3 -m unittest discover -s tests -p test_exportar_metodo.py
python3 scripts/atualizar_checksums.py
```

Revise o diff antes de incorporar uma adaptação. Não edite uma release nem o cache instalado.
Se alterar modelos ou roteadores depois da geração, regenere o manifesto antes de conferir.

`validar.py` sem fonte confere a integridade do pacote disponível.
Com `--fonte`, compara também o catálogo, os arquivos canônicos, as adaptações e os exemplos atuais.
O empacotador exige `--fonte` e executa essa conferência antes de criar qualquer ZIP:

```bash
python3 scripts/empacotar_plugin.py --fonte /caminho/do/projeto-canonico --saida-dir /caminho/temporario
```

Hash detecta mudança de arquivo; não comprova qualidade pedagógica nem comportamento de um assistente.
Teste casos representativos no ambiente de destino antes de publicar. Geração local não é publicação nem atualização da instalação.
