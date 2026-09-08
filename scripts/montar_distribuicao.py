#!/usr/bin/env python3
"""Monta as skills públicas a partir das skills canônicas e adaptações revisadas."""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

from exportar_metodo import prepare, write_export, seal_distribution


@dataclass(frozen=True)
class Skill:
    title: str
    description: str


SKILLS: dict[str, Skill] = {
    "ga2-5w2h": Skill(
        "5W2H — plano de ação",
        "Cria um plano de ação 5W2H com ação, motivo, dono único, data, local, modo de execução, custo e prova. Use quando pedirem plano de ação, 5W2H, contramedidas ou responsáveis e prazos.",
    ),
    "ga2-backlog-2d": Skill(
        "Backlog 2D — mapa de entregas e tarefas",
        "Monta um Backlog 2D com etapas ou iniciativas, entregas, tarefas, prioridades e o menor primeiro ciclo. Use quando pedirem backlog, quebra de projeto, mapa de trabalho ou recorte do primeiro ciclo.",
    ),
    "ga2-briefing-iniciativa": Skill(
        "Briefing da iniciativa",
        "Cria o acordo inicial de uma iniciativa e escolhe entre projeto, produto e processo. Use quando pedirem briefing, definição de escopo, alinhamento da entrega ou classificação pelos 3 Ps.",
    ),
    "ga2-canvas-de-conversa-cnv": Skill(
        "Canvas de conversa",
        "Prepara uma conversa difícil com fato, sentimento, necessidade e pedido. Use quando pedirem conversa difícil, comunicação não violenta, cobrança sem acusação ou Canvas de Conversa.",
    ),
    "ga2-canvas-de-planejamento": Skill(
        "Canvas de Planejamento — a folha do curso",
        "Resume numa folha os nove blocos do planejamento: contexto, situação atual, ideal, gap, causa raiz, lista de objetivos, matriz de priorização, objetivos selecionados e resultados-chave com iniciativas. Use quando pedirem o canvas de planejamento, o canvas do curso numa página ou um resumo do diagnóstico e dos objetivos.",
    ),
    "ga2-canvas-de-visao": Skill(
        "Canvas de Visão",
        "Define o norte de uma empresa, área ou iniciativa com passado, situação atual, tendências, futuro e frase de visão. Use quando pedirem Canvas de Visão, direção, contexto ou futuro desejado.",
    ),
    "ga2-causa-raiz": Skill(
        "Causa raiz",
        "Investiga causas com 5 Porquês ou Ishikawa e exige evidência em cada ligação. Use quando pedirem causa raiz, 5 Porquês, espinha de peixe, post-mortem ou separação entre sintoma e causa.",
    ),
    "ga2-checklist-producao-entrega": Skill(
        "Checklist para começar e entregar",
        "Define o que um trabalho precisa para começar e para ser entregue com prova. Use quando perguntarem se algo pode começar, se está pronto, ou citarem DoR, DoD e critério de pronto.",
    ),
    "ga2-decisao-projeto-ou-fluxo": Skill(
        "Decisão: projeto ou fluxo",
        "Escolhe entre projeto em ciclos, fluxo contínuo ou modelo híbrido e define como acompanhar. Use quando perguntarem se o trabalho é projeto ou fluxo, ou quando ciclos não parecem funcionar.",
    ),
    "ga2-delegacao": Skill(
        "Quadro de Delegação",
        "Monta um quadro com assuntos, pessoas e sete níveis claros de decisão. Use quando pedirem matriz de delegação, autonomia, responsáveis por decisões ou Delegation Poker.",
    ),
    "ga2-diagnostico": Skill(
        "Diagnóstico atual e desejado",
        "Compara a situação atual com a desejada, mede a distância e registra a linha de partida. Use quando pedirem diagnóstico, estado atual, meta, distância para a meta ou lado esquerdo do A3.",
    ),
    "ga2-documentos-de-projeto": Skill(
        "Documentos do projeto",
        "Organiza os documentos necessários em cada fase de um projeto, do contexto ao encerramento. Use quando pedirem dossiê, documentos do projeto, relatório de andamento ou resumo do ciclo.",
    ),
    "ga2-feedback-360": Skill(
        "Feedback 360",
        "Conduz um Feedback 360 com diferentes pontos de vista, padrões e até dois focos com prazo. Use quando pedirem avaliação 360, feedback de líder, pares e equipe ou plano após feedback.",
    ),
    "ga2-folha-de-experimento": Skill(
        "Folha de experimento",
        "Registra dor, problema, ideia, protótipo, teste e decisão em uma experiência pequena. Use quando pedirem experimento, hipótese, protótipo, teste barato ou portfólio de inovação.",
    ),
    "ga2-gemba-walk": Skill(
        "Vá e Veja — Gemba Walk",
        "Conduz uma observação no lugar onde o trabalho acontece, com pergunta, fatos e uma ação. Use quando pedirem Gemba, observação direta, investigação no local ou entendimento de uma queda.",
    ),
    "ga2-gestao-diaria": Skill(
        "Gestão diária",
        "Conduz uma reunião diária curta diante do quadro, destacando avanço, próximo passo e bloqueio. Use quando pedirem diária, daily, trabalhos parados, registro do dia ou remoção de bloqueios.",
    ),
    "ga2-kanban-canvas": Skill(
        "Kanban Canvas",
        "Desenha um quadro Kanban com estados, raias, cartões, limites e regras visíveis. Use quando pedirem Kanban, quadro de trabalho, fluxo, cartões, bloqueios ou políticas do quadro.",
    ),
    "ga2-matriz-esforco-impacto": Skill(
        "Matriz Impacto e Esforço",
        "Compara iniciativas pelo impacto e esforço e devolve uma fila com critérios claros. Use quando pedirem prioridade, matriz, ordem das iniciativas ou escolha do próximo trabalho.",
    ),
    "ga2-me-mostra": Skill(
        "Me Mostra",
        "Use quando o usuário pedir para ver, desenhar ou explicar visualmente um caso, fluxo, problema, mudança ou decisão de gestão descrito no pedido ou na conversa atual; não use para assuntos sem um caso de gestão.",
    ),
    "ga2-okr-canvas": Skill(
        "OKR Canvas",
        "Monta e acompanha um OKR Canvas com objetivo, resultados-chave de partida e chegada, iniciativas e revisão periódica. Use quando pedirem OKR, resultado-chave, iniciativa ou acompanhamento de meta.",
    ),
    "ga2-painel-do-gestor": Skill(
        "Painel do Gestor",
        "Monta uma visão curta de um ciclo com poucos números úteis para decidir. Use quando pedirem painel, números do ciclo, indicador principal, leitura da meta ou resumo para o gestor.",
    ),
    "ga2-pdca": Skill(
        "PDCA — ciclo de melhoria",
        "Registra uma melhoria em quatro etapas: planejar, executar, verificar e agir. Use quando pedirem PDCA, melhoria de processo, acompanhamento de contramedida ou decisão de padronizar e ajustar.",
    ),
    "ga2-pdi": Skill(
        "Plano de Desenvolvimento Individual",
        "Monta um plano de desenvolvimento com objetivo de trabalho, forças, lacuna, ações 70-20-10, marco e acompanhamento. Use quando pedirem PDI, desenvolvimento de pessoa ou evolução profissional.",
    ),
    "ga2-plano-do-ciclo": Skill(
        "Plano do ciclo",
        "Planeja um ciclo com uma meta, capacidade segura, trabalhos com dono e data, e critério de pronto. Use quando pedirem plano da semana, sprint, meta do ciclo ou escolha do que entra.",
    ),
    "ga2-politicas-wip-urgencia": Skill(
        "Limite de trabalho e urgência",
        "Define limites de trabalho em andamento, bloqueios e critérios de urgência de um quadro. Use quando pedirem limite do quadro, WIP, gargalo, raia urgente ou política de urgência.",
    ),
    "ga2-pop": Skill(
        "Procedimento Operacional Padrão",
        "Escreve um procedimento recorrente com dono, gatilho, passos, saída, sistema, indicador, exceção e aprovação. Use quando pedirem POP, procedimento, rotina ou padronização de processo.",
    ),
    "ga2-quadro-kaizen": Skill(
        "Quadro Kaizen",
        "Registra uma melhoria pequena com sinal, aposta, dono, prazo, aprendizado e decisão. Use quando pedirem Kaizen, fila de melhorias, pequeno ajuste ou resposta a indicador parado.",
    ),
    "ga2-quem-faz-o-que": Skill(
        "Quem faz o quê",
        "Define dono único, quem aceita, quem apoia, quem executa e quem aprova. Use quando pedirem responsáveis, papéis, dono da entrega, matriz de responsabilidade ou decisão de aprovação.",
    ),
    "ga2-relatorio-a3": Skill(
        "Relatório A3",
        "Monta um Relatório A3 completo, do contexto e causa raiz ao plano, acompanhamento e aprendizado. Use quando pedirem A3, solução estruturada de problema, queda de indicador ou plano para diretoria.",
    ),
    "ga2-retrospectiva": Skill(
        "Retrospectiva",
        "Conduz uma retrospectiva sobre o modo de trabalhar e escolhe uma melhoria com dono e data. Use quando pedirem retro, manter, melhorar e parar, ou mudança de processo após um ciclo.",
    ),
    "ga2-review-do-ciclo": Skill(
        "Revisão do ciclo",
        "Compara o combinado com o entregue, exige prova e registra a decisão seguinte. Use quando pedirem review, revisão do ciclo, demonstração da entrega ou fechamento da semana.",
    ),
}


HTML_TEMPLATE = """<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{TITULO}}</title>
  <style>
    :root { color-scheme: light dark; --paper:#fafaf8; --panel:#fff; --ink:#1f2937;
      --muted:#576270; --line:#dfe3e8; --brand:#3d9b9d; --risk:#c2560a; --open:#6b7280; }
    @media (prefers-color-scheme:dark) { :root { --paper:#111827; --panel:#1f2937;
      --ink:#f3f4f6; --muted:#c7ceda; --line:#3b4757; --brand:#52c7cb;
      --risk:#fb923c; --open:#a6aebb; } }
    * { box-sizing:border-box; } body { margin:0; background:var(--paper); color:var(--ink);
      font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif; }
    main { width:min(1040px,calc(100% - 32px)); margin:auto; padding:56px 0 80px; }
    header,section { padding:28px 0; border-bottom:1px solid var(--line); }
    h1 { max-width:19ch; font-size:clamp(2rem,6vw,3.4rem); line-height:1.05; }
    h2 { font-size:1.35rem; } p,li { max-width:68ch; } .lead { color:var(--muted);
      font-size:1.18rem; } .visual { margin-top:20px; padding:20px; background:var(--panel);
      border:1px solid var(--line); border-radius:12px; overflow:auto; }
    table { width:100%; border-collapse:collapse; } th,td { padding:10px 12px;
      text-align:left; border-bottom:1px solid var(--line); vertical-align:top; }
    .seal { display:inline-block; padding:2px 7px; border:1px solid currentColor;
      border-radius:99px; font-size:.75rem; } .measured { color:var(--brand); }
    .estimated { color:var(--risk); } .open { color:var(--open); }
    code,pre { white-space:pre-wrap; overflow-wrap:anywhere; }
  </style>
</head>
<body>
<main>
  <header><h1>{{PERGUNTA}}</h1><p class="lead">{{LEITURA_DIRETA}}</p></header>
  <section><h2>Visual</h2><div class="visual">{{VISUAL_PRINCIPAL}}</div></section>
  <section><h2>Prova</h2>{{PROVAS_E_FONTES}}</section>
  <section><h2>Decisão ou próximo passo</h2>{{PROXIMO_PASSO}}</section>
</main>
</body>
</html>
"""


COMMON_BODY = """# {title}

## Como conduzir

1. Leia `references/metodo.md` por inteiro antes de montar a resposta.
2. Confirme qual decisão ou resultado o usuário precisa alcançar.
3. Separe fatos, estimativas e pontos ainda sem resposta.
4. Aplique os campos e a sequência descritos na referência.
5. Siga o nível de detalhe previsto no método para o caso; não force campos de outra variante.
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

{delivery}
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
"""


ME_MOSTRA_BODY = """# Me Mostra — Gestão Visual GA 2.0

## Regra principal

Quando houver um caso de gestão identificável, gere HTML por padrão e respeite outro formato solicitado. Leia
`references/metodo.md` por inteiro antes de criar o visual. Mostre o menor visual que permita
entender o caso e decidir.

## Objeto do visual

Determine o objeto antes de escolher o formato:

1. Se o pedido atual nomeia um caso, processo, artefato ou decisão, esse é o objeto.
2. Se usa “isso”, “aqui”, “o que falamos”, “este caso” ou apenas “me mostra”, use o caso ou
   artefato de gestão mais recente da conversa atual.
3. O nome do plug-in ou da habilidade serve apenas para invocá-la. Nunca o use como objeto por
   padrão. Mostre o método Gestão Ágil 2.0 somente quando o usuário pedir isso explicitamente.

Prenda a resposta aos elementos concretos disponíveis no caso, como números, etapas, pessoas,
bloqueios ou decisões. Quando a conversa contiver dois ou mais desses elementos, use pelo menos
dois deles no título, na leitura ou na prova.

Se não houver um caso de gestão identificável, não gere HTML nem substitua o assunto pelo método.
Faça somente uma pergunta curta para o usuário indicar qual situação de gestão deseja visualizar.

## Linguagem obrigatória

- Escreva em português simples e direto.
- Use a palavra comum antes do termo técnico.
- Explique toda sigla na primeira aparição, na mesma linha.
- Evite inglês quando houver uma palavra comum em português.
- Aplique a regra no título, rótulos, legendas, dicas, texto alternativo e resposta final.
- Releia apenas o texto visível antes de entregar. Jargão solto reabre o trabalho.

## Como conduzir

1. Confirme o objeto usando o pedido atual e o histórico da conversa.
2. Escreva a pergunta que o visual responde.
3. Escolha a pergunta que libera a próxima decisão.
4. Separe o que é medido, estimado e ainda está em aberto.
5. Escolha um visual principal: fluxo, quadro, antes e depois, causa, matriz ou linha do tempo.
6. Gere a entrega escolhida com pergunta, leitura direta, visual, prova e consequência.
7. Feche com o que ficou claro, o que segue em aberto e o próximo passo.

Para HTML, use `assets/template-artefato.html` como ponto de partida. Ele deve funcionar sem rede,
biblioteca externa ou imagem remota.

## Entrega por ambiente

- No Claude, use Artifact quando esse recurso estiver disponível.
- No Codex ou GPT, use o artefato ou a visualização exposta na sessão.
- No Cursor, use sua prévia ou visualização disponível.
- Em outro ambiente, use o recurso equivalente.
- Não escolha pela marca do modelo. Verifique o que o ambiente oferece.
- Quando a saída escolhida for HTML e não houver recurso nativo, salve `.html` e mostre um resumo.
  Markdown acompanha somente quando necessário ao fluxo. Informe o caminho do HTML.

Para entrega visual sem outro formato pedido, gere HTML. Para Word, Docs ou planilhas solicitados, siga a entrega editável.

## Critério de pronto

- O visual principal responde à pergunta em até 90 segundos.
- O significado continua claro sem cor.
- Fato, estimativa e ponto em aberto não se misturam.
- Título e rótulos não contêm sigla ou jargão sem explicação.
- O objeto é o caso de gestão ativo, nunca o nome do plug-in por padrão.
- A entrega usou o formato solicitado; sem escolha explícita, gerou HTML.
"""


CNV_NOTE = """
## Privacidade

Esta exceção prevalece sobre o padrão de documento da seção Entrega.
Não grave uma conversa privada por padrão. Entregue o texto no chat. Gere arquivo ou HTML
somente quando o usuário pedir para salvar. O pedido já autoriza a gravação no destino indicado; não amplie o compartilhamento.
"""


FAMILIA = {"kit": "canvas do kit do curso", "v6": "canvas editável v6", "b": "editável por módulo", "c": "folha da jornada", "laboratorio": "desenhado no estilo do kit; não está no curso"}


def secao_construtor(name: str, construtor: Path | None) -> str:
    """Seção 'Canvas oficial e documento' quando a habilidade tem canvas no construtor exportado."""
    if not construtor or not (construtor / "oficiais" / "manifesto.json").is_file():
        return ""
    manifesto = json.loads((construtor / "oficiais" / "manifesto.json").read_text(encoding="utf-8"))
    itens = [it for it in manifesto["oficiais"] if it.get("skill") == name]
    if not itens:
        return ""
    itens.sort(key=lambda i: (not i.get("padrao"), i["id"]))
    if name == "ga2-canvas-de-conversa-cnv":
        return ("\n## Canvas oficial\n\nO canvas preenchido fica no chat por padrão; salve no formato pedido quando solicitado. Existe o modelo em branco "
                f"`assets/modelos/canvas-{itens[0]['id']}.html`, para imprimir ou preencher à mão.\n")
    tem_doc = False
    linhas = []
    for it in itens:
        sp = json.loads((construtor / "specs" / f"{it['id']}.json").read_text(encoding="utf-8"))
        le = sp.get("leitura") or {}
        doc = bool(le.get("capitulos")) and not le.get("sem_documento")
        tem_doc = tem_doc or doc
        linhas.append(f"- `{it['id']}` — {it['titulo']} ({FAMILIA.get(it['familia'], it['familia'])}){' — padrão' if it.get('padrao') else ''}")
    padrao = itens[0]["id"]
    partes = ["", "## Canvas oficial e documento", "",
              "Quando o usuário pedir o canvas do curso (\"gera o canvas\", \"no formato oficial\", \"igual ao PDF\") ou o documento",
              "HTML, use os modelos de `assets/modelos/`:", "",
              "- `template-<id>.md` — o arquivo a preencher; as marcas `<!-- c:... -->` dizem onde está cada campo e não podem ser apagadas;",
              "- `canvas-<id>.html` — réplica do canvas oficial, em branco;",
              *(["- `documento.html` — a forma documento, em branco;"] if tem_doc else []),
              "- `CAMPOS.md` — nome e texto-guia de cada campo.", "",
              "Canvas desta habilidade:", "", *linhas, "",
              "Para gerar a partir do `.md` preenchido (Python 3.10 ou mais novo, na pasta do pacote):", "",
              "```bash",
              *([f"python3 construtor/construir.py {padrao} --documento --md meu-caso.md --saida meu-caso.html"] if tem_doc else []),
              f"python3 construtor/construir.py {padrao} --canvas --md meu-caso.md --saida meu-caso-canvas.html",
              "```", "",
              "Sem Python: copie o canvas em branco e escreva dentro das `div[data-campo]`, mantendo os ids.",
              "No construtor HTML, o `.md` é a entrada atual; não use cópia antiga para substituir documento vivo. Canvas marcado como acréscimo do laboratório",
              "não faz parte do curso.", ""]
    return "\n".join(partes)



SHEET_SKILLS = {'ga2-delegacao', 'ga2-quadro-kaizen', 'ga2-plano-do-ciclo', 'ga2-backlog-2d', 'ga2-matriz-esforco-impacto', 'ga2-5w2h', 'ga2-okr-canvas', 'ga2-quem-faz-o-que'}
VISUAL_SKILLS = {'ga2-painel-do-gestor', 'ga2-canvas-de-planejamento', 'ga2-kanban-canvas', 'ga2-me-mostra'}


def entrega_editavel(name: str) -> str:
    if name in SHEET_SKILLS:
        formato = "planilha `.xlsx`; Google Sheets quando esse for o destino escolhido"
    elif name in VISUAL_SKILLS:
        formato = "visual HTML; Word `.docx`, Google Docs, Excel `.xlsx` ou Google Sheets quando solicitados"
    else:
        formato = "documento Word `.docx`; Google Docs quando esse for o destino escolhido"
    return (
        "Leia `references/entrega-editavel.md` ao criar ou revisar um artefato.\n"
        f"Padrão desta skill, sem formato definido: {formato}.\n"
        "O formato pedido e o documento existente orientam a entrega. Referências de HTML aplicam-se somente à saída visual. Use ferramentas de arquivos ou integração disponível.\n"
        "Nas revisões, leia e atualize o mesmo documento, preservando edições humanas, IDs e evidências.\n"
        "Markdown serve ao versionamento quando necessário; HTML sai para visualização ou quando pedido, sem cópias obrigatórias.\n"
    )


def skill_markdown(name: str, skill: Skill, construtor: Path | None = None) -> str:
    body = ME_MOSTRA_BODY if name == "ga2-me-mostra" else COMMON_BODY.format(title=skill.title, delivery=entrega_editavel(name))
    if name == "ga2-me-mostra":
        body += "\n## Entrega editável\n\n" + entrega_editavel(name)
    if name == "ga2-canvas-de-conversa-cnv":
        body += CNV_NOTE
    body += (
        "\n## Recursos específicos desta habilidade\n\n"
        "O método completo está em `references/metodo.md`; ele define a sequência e as regras específicas.\n"
        "Ao preencher o artefato, leia `references/template.md` por inteiro e preserve seus campos.\n"
        "Consulte `references/exemplo.md` para entender o preenchimento; é fictício, nunca evidência do caso do usuário.\n"
        + ("Antes de entregar, confira os critérios de pronto de `references/metodo.md`.\n" if name == "ga2-me-mostra" else
           "Antes de entregar, aplique `references/checklist.md` por inteiro.\n")
    )
    body += secao_construtor(name, construtor)
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {json.dumps(skill.description, ensure_ascii=False)}\n"
        "---\n\n"
        f"{body.rstrip()}\n"
    )


def openai_yaml(name: str, skill: Skill) -> str:
    if name == "ga2-me-mostra":
        short = "Visualiza o caso de gestão desta conversa"
        prompt = (
            "Use $ga2-me-mostra para visualizar o caso de gestão desta conversa; "
            "se não houver um caso identificável, peça que eu o indique."
        )
    else:
        short = skill.description.split(". Use", 1)[0]
        if len(short) > 64:
            short = short[:61].rstrip() + "..."
        prompt = f"Aplique {skill.title} ao meu caso, em português simples."
    return (
        "interface:\n"
        f"  display_name: {json.dumps(skill.title, ensure_ascii=False)}\n"
        f"  short_description: {json.dumps(short, ensure_ascii=False)}\n"
        f"  default_prompt: {json.dumps(prompt, ensure_ascii=False)}\n"
    )



def build(source_root: Path, output_root: Path, construtor: Path | None = None) -> None:
    # Valide TODAS as adaptações antes da primeira gravação. Não há fallback para GPTs.
    catalog = {path.name for path in (source_root / ".claude/skills").glob("ga2-*") if path.is_dir()}
    if catalog and catalog != set(SKILLS):
        raise ValueError(f"catálogo canônico mudou; revise metadados e adaptações: {sorted(catalog ^ set(SKILLS))}")
    files, manifest = prepare(source_root, set(SKILLS))
    package_root = Path(__file__).resolve().parents[1]
    # Esta habilidade é mantida no pacote; não deriva da suíte de GPTs.
    opening_source = Path(__file__).resolve().parents[1] / "skills" / "ga2-abrir-projeto"
    opening_target = output_root / "ga2-abrir-projeto"
    if opening_source.resolve() != opening_target.resolve():
        shutil.copytree(opening_source, opening_target, dirs_exist_ok=True)

    for name, skill in SKILLS.items():
        directory = output_root / name
        existing = package_root / "skills" / name
        if existing.resolve() != directory.resolve():
            shutil.copytree(existing, directory, dirs_exist_ok=True)
        references = directory / "references"
        assets = directory / "assets"
        agents = directory / "agents"
        references.mkdir(parents=True, exist_ok=True)
        assets.mkdir(parents=True, exist_ok=True)
        agents.mkdir(parents=True, exist_ok=True)

        shutil.copyfile(Path(__file__).resolve().parents[1] / "docs/SAIDA-EDITAVEL.md", references / "entrega-editavel.md")
        (directory / "SKILL.md").write_text(skill_markdown(name, skill, construtor), encoding="utf-8")
        method = files[f"{name}/references/metodo.md"].decode("utf-8")
        if name != "ga2-me-mostra":
            (references / "gestao-visual.md").write_text(
                "# Escolha visual\n\nSiga primeiro o método desta habilidade e o formato escolhido em `entrega-editavel.md`.\n"
                "Um fluxo mostra sequência; um quadro mostra estados; uma matriz compara alternativas.\n"
                "Use pergunta, leitura direta, visual, prova e próximo passo. Separe medido, estimado e em aberto.\n"
                "Quando disponível, `ga2-me-mostra` explica o mesmo caso visualmente. Não substitua o artefato por um resumo genérico.\n",
                encoding="utf-8")
        origin = method.split("## Fonte no método", 1)
        source_notes = origin[1].split("\n## ", 1)[0].strip() if len(origin) == 2 else "Consulte a procedência indicada no método desta habilidade."
        (references / "fontes.md").write_text(
            "# Fontes e procedência\n\n" + source_notes + "\n\n"
            "As citações identificam aulas e artefatos; não prometem acesso a arquivos externos.\n"
            "O método, template e critérios aplicáveis estão nos arquivos vizinhos.\n"
            "A origem e os hashes desta exportação constam em `skills/procedencia.json` na raiz do pacote.\n"
            "Exemplos são fictícios e independentes; não comprovam resultados do usuário.\n", encoding="utf-8")
        (assets / "template-artefato.html").write_text(HTML_TEMPLATE, encoding="utf-8")
        (agents / "openai.yaml").write_text(openai_yaml(name, skill), encoding="utf-8")
    write_export(output_root, files, manifest)
    seal_distribution(output_root, manifest)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fonte", required=True, type=Path, help="projeto canônico com .claude/skills e laboratorio/publicacao; não a suíte de GPTs")
    parser.add_argument("--destino", default=Path("skills"), type=Path)
    parser.add_argument("--construtor", default=Path("construtor"), type=Path, help="pasta do construtor exportado (montar_construtor.py --exportar)")
    args = parser.parse_args()
    construtor = args.construtor.resolve() if args.construtor and args.construtor.exists() else None
    build(args.fonte.resolve(), args.destino.resolve(), construtor)


if __name__ == "__main__":
    main()
