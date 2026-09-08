# Gestão Ágil 2.0 — habilidades e plug-in

Este repositório distribui 31 habilidades do Gestão Ágil 2.0 em um único plug-in e
mantém os instaladores por pasta para ambientes compatíveis.

O plug-in é somente de habilidades: não inclui MCP, Apps, Actions, conectores nem
autenticação externa.

## Plug-in Gestão Ágil 2.0

O aluno instala o plug-in uma vez e usa as habilidades dentro do Projeto do seu
caso real. O conteúdo está organizado pedagogicamente em seis trilhas:

1. Diagnóstico e A3;
2. Estratégia e objetivos;
3. Iniciativas e ciclos;
4. Operação e fluxo;
5. Melhoria e inovação;
6. Liderança e times.

A relação completa entre trilhas e habilidades está em [docs/TRILHAS.md](docs/TRILHAS.md).

No ChatGPT, digite `@` e escolha o plug-in ou uma habilidade. No Codex, cite uma
habilidade com `$`, como `$ga2-relatorio-a3`. Também é possível pedir o resultado
em linguagem comum e deixar o ambiente selecionar a habilidade adequada.

> A versão deste checkout está em [VERSION](VERSION). Alterar este repositório não
> atualiza o diretório nem o plugin instalado. Esta revisão local ainda não foi publicada.

Para gerar o arquivo de distribuição:

```bash
python3 scripts/empacotar_plugin.py
```

Os dez casos de validação e regressão estão em
[tests/plugin-submission-cases.json](tests/plugin-submission-cases.json). O roteiro
de piloto e publicação está em [docs/PUBLICACAO.md](docs/PUBLICACAO.md).

## Uma fonte para o método

Este repositório é a fonte canônica das 32 skills, incluindo método, templates, exemplos, modelos e testes.
A operação interna e os alunos usam instalações deste pacote. Regras privadas ficam no projeto consumidor.
Edite aqui, valide e instale uma versão identificada. Não edite instalações, caches ou releases.

Leia [Fonte canônica e instalação](docs/FONTE-DO-METODO.md) para atualizar sem criar versões paralelas.
O manifesto `skills/procedencia.json` registra os hashes dos arquivos distribuídos.

## Instalação das habilidades por pasta

Os instaladores requerem Python 3.10 ou superior e registram versão e hashes.
Use `--conferir` (PowerShell: `-Conferir`) para comparar a instalação com o pacote.

O pacote também funciona com Claude, Codex, Cursor, OpenCode e ambientes que leem
pastas no formato `SKILL.md`.

## O que uma habilidade faz

Uma habilidade ensina o assistente a aplicar uma parte do método. Por exemplo:

- montar um A3;
- encontrar a causa raiz;
- criar um OKR;
- organizar um Kanban;
- conduzir uma revisão ou retrospectiva;
- explicar uma situação com um artefato HTML.

As habilidades usam português simples. Todo termo técnico aparece com uma explicação curta.

### macOS ou Linux

Instalar em todos os ambientes conhecidos:

```bash
./instalar.sh --todos
```

Instalar em um ambiente específico:

```bash
./instalar.sh --claude
./instalar.sh --codex
./instalar.sh --cursor
./instalar.sh --opencode
./instalar.sh --agents
```

Instalar em uma pasta escolhida:

```bash
./instalar.sh --destino /caminho/para/skills
```

### Windows

Abra o PowerShell nesta pasta e execute:

```powershell
.\instalar.ps1 -Todos
```

Também existem as opções `-Claude`, `-Codex`, `-Cursor`, `-OpenCode`, `-Agents`
e `-Destino "C:\caminho\skills"`.

### Atualizar

Baixe a versão nova e rode o instalador outra vez. O instalador guarda a versão anterior
em `.ga2-backup` antes de substituir qualquer skill.

## Usar as habilidades

Depois de instalar, reinicie o assistente. Peça pela tarefa em linguagem comum:

```text
Monta um A3 para este problema.
Me mostra onde este fluxo trava.
Organiza estas ações em um plano com dono e data.
```

O ambiente decide qual skill usar. Você também pode citar o nome, como `$ga2-relatorio-a3`.

## Documentos e planilhas editáveis

As skills entregam Word `.docx` ou Google Docs para documentos, Excel `.xlsx` ou Google Sheets
para planilhas e HTML para visuais. O formato pedido e o documento existente orientam a entrega.
Nas revisões, atualizam o mesmo documento e preservam edições humanas e evidências.
Google Docs e Sheets exigem integração com escrita; sem ela, a alternativa é um arquivo editável.
O pacote contém as instruções do método; o ambiente precisa oferecer a criação de arquivos ou a integração.
Não é necessário gerar Markdown e HTML junto de cada documento. Veja [o contrato de entrega](docs/SAIDA-EDITAVEL.md).

## Ambientes com artefato visual

`ga2-me-mostra` gera HTML por padrão e respeita outro formato solicitado.

- Claude usa Artifact quando esse recurso estiver disponível.
- Codex e GPT usam o artefato ou a visualização disponível na sessão.
- Cursor usa sua visualização ou prévia disponível.
- Outros ambientes usam o recurso equivalente.
- Sem recurso visual, a skill salva o HTML e mostra um resumo no terminal ou no chat.

O recurso disponível no ambiente prevalece sobre o nome do modelo.

## Gerar o canvas oficial e o documento

Cada habilidade de artefato traz, em `assets/modelos/`:

- `template-<id>.md` — o arquivo que você preenche; as marcas `<!-- c:... -->` dizem ao construtor onde está cada campo;
- `canvas-<id>.html` — a réplica do canvas oficial do curso, em branco;
- `documento.html` — a forma documento, em branco;
- `CAMPOS.md` — o nome e o texto-guia de cada campo.

Com Python 3.10 ou mais novo (sem instalar pacotes), na pasta deste repositório:

```bash
python3 construtor/construir.py okr-kit-02 --documento --md meu-okr.md --saida meu-okr.html
python3 construtor/construir.py okr-kit-02 --canvas --md meu-okr.md --saida meu-okr-canvas.html
```

Nesse construtor HTML, o `.md` é a entrada. Prepare-a da versão atual do documento; `--documento` gera HTML, não Word. A lista dos canvas e o modo de leitura estão em
[construtor/README.md](construtor/README.md). Seis canvas (5W2H, PDCA, Ishikawa, portões DoR/DoD,
Quem faz o quê e Folha de experimento) não existem no curso: foram desenhados no mesmo estilo do kit e
trazem o selo "acréscimo do laboratório".

## Conteúdo e privacidade

O pacote não contém credenciais, caminhos de servidores, dados de alunos ou rotinas internas
da MindMaster. Os exemplos usam situações didáticas.

## Versão

A versão atual está em [VERSION](VERSION). A integridade dos arquivos está registrada em
`SHA256SUMS.txt`.
