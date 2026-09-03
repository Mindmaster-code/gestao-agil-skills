# Skills do Gestão Ágil 2.0

Este repositório instala 30 skills do Gestão Ágil 2.0 em assistentes de IA.

O pacote funciona com Claude, Codex/GPT, Cursor, OpenCode e ambientes que leem
pastas no formato `SKILL.md`.

## O que uma skill faz

Uma skill ensina o assistente a aplicar uma parte do método. Por exemplo:

- montar um A3;
- encontrar a causa raiz;
- criar um OKR;
- organizar um Kanban;
- conduzir uma revisão ou retrospectiva;
- explicar uma situação com um artefato HTML.

As skills usam português simples. Todo termo técnico aparece com uma explicação curta.

## Instalar no macOS ou Linux

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

## Instalar no Windows

Abra o PowerShell nesta pasta e execute:

```powershell
.\instalar.ps1 -Todos
```

Também existem as opções `-Claude`, `-Codex`, `-Cursor`, `-OpenCode`, `-Agents`
e `-Destino "C:\caminho\skills"`.

## Atualizar

Baixe a versão nova e rode o instalador outra vez. O instalador guarda a versão anterior
em `.ga2-backup` antes de substituir qualquer skill.

## Usar

Depois de instalar, reinicie o assistente. Peça pela tarefa em linguagem comum:

```text
Monta um A3 para este problema.
Me mostra onde este fluxo trava.
Organiza estas ações em um plano com dono e data.
```

O ambiente decide qual skill usar. Você também pode citar o nome, como `$ga2-relatorio-a3`.

## Ambientes com artefato visual

`ga2-me-mostra` sempre gera HTML.

- Claude usa Artifact quando esse recurso estiver disponível.
- Codex e GPT usam o artefato ou a visualização disponível na sessão.
- Cursor usa sua visualização ou prévia disponível.
- Outros ambientes usam o recurso equivalente.
- Sem recurso visual, a skill salva o HTML e mostra um resumo no terminal ou no chat.

O recurso disponível no ambiente prevalece sobre o nome do modelo.

## Conteúdo e privacidade

O pacote não contém credenciais, caminhos de servidores, dados de alunos ou rotinas internas
da MindMaster. Os exemplos usam situações didáticas.

## Versão

A versão atual está em [VERSION](VERSION). A integridade dos arquivos está registrada em
`SHA256SUMS.txt`.

