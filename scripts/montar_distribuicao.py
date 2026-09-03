#!/usr/bin/env python3
"""Monta as skills públicas a partir do conteúdo limpo da suíte de GPTs."""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Skill:
    title: str
    description: str
    sources: tuple[str, ...]


SKILLS: dict[str, Skill] = {
    "ga2-5w2h": Skill(
        "5W2H — plano de ação",
        "Cria um plano de ação 5W2H com ação, motivo, dono único, data, local, modo de execução, custo e prova. Use quando pedirem plano de ação, 5W2H, contramedidas ou responsáveis e prazos.",
        ("diagnostico-a3/conhecimento/04-contramedidas-5w2h.md",),
    ),
    "ga2-backlog-2d": Skill(
        "Backlog 2D — mapa de entregas e tarefas",
        "Monta um Backlog 2D com etapas ou iniciativas, entregas, tarefas, prioridades e o menor primeiro ciclo. Use quando pedirem backlog, quebra de projeto, mapa de trabalho ou recorte do primeiro ciclo.",
        ("iniciativas-e-ciclos/conhecimento/05-backlog-2d.md",),
    ),
    "ga2-briefing-iniciativa": Skill(
        "Briefing da iniciativa",
        "Cria o acordo inicial de uma iniciativa e escolhe entre projeto, produto e processo. Use quando pedirem briefing, definição de escopo, alinhamento da entrega ou classificação pelos 3 Ps.",
        ("iniciativas-e-ciclos/conhecimento/03-briefing-da-iniciativa.md",),
    ),
    "ga2-canvas-de-conversa-cnv": Skill(
        "Canvas de conversa",
        "Prepara uma conversa difícil com fato, sentimento, necessidade e pedido. Use quando pedirem conversa difícil, comunicação não violenta, cobrança sem acusação ou Canvas de Conversa.",
        ("lideranca-e-times/conhecimento/04-canvas-de-conversa-cnv.md",),
    ),
    "ga2-canvas-de-visao": Skill(
        "Canvas de Visão",
        "Define o norte de uma empresa, área ou iniciativa com passado, situação atual, tendências, futuro e frase de visão. Use quando pedirem Canvas de Visão, direção, contexto ou futuro desejado.",
        ("estrategia-e-okr/conhecimento/02-canvas-de-visao.md",),
    ),
    "ga2-causa-raiz": Skill(
        "Causa raiz",
        "Investiga causas com 5 Porquês ou Ishikawa e exige evidência em cada ligação. Use quando pedirem causa raiz, 5 Porquês, espinha de peixe, post-mortem ou separação entre sintoma e causa.",
        ("diagnostico-a3/conhecimento/03-causa-raiz.md",),
    ),
    "ga2-checklist-producao-entrega": Skill(
        "Checklist para começar e entregar",
        "Define o que um trabalho precisa para começar e para ser entregue com prova. Use quando perguntarem se algo pode começar, se está pronto, ou citarem DoR, DoD e critério de pronto.",
        ("operacao-e-fluxo/conhecimento/05-dor-e-dod.md",),
    ),
    "ga2-decisao-projeto-ou-fluxo": Skill(
        "Decisão: projeto ou fluxo",
        "Escolhe entre projeto em ciclos, fluxo contínuo ou modelo híbrido e define como acompanhar. Use quando perguntarem se o trabalho é projeto ou fluxo, ou quando ciclos não parecem funcionar.",
        ("iniciativas-e-ciclos/conhecimento/02-projeto-fluxo-hibrido.md",),
    ),
    "ga2-delegacao": Skill(
        "Quadro de Delegação",
        "Monta um quadro com assuntos, pessoas e sete níveis claros de decisão. Use quando pedirem matriz de delegação, autonomia, responsáveis por decisões ou Delegation Poker.",
        ("lideranca-e-times/conhecimento/03-quadro-de-delegacao.md",),
    ),
    "ga2-diagnostico": Skill(
        "Diagnóstico atual e desejado",
        "Compara a situação atual com a desejada, mede a distância e registra a linha de partida. Use quando pedirem diagnóstico, estado atual, meta, distância para a meta ou lado esquerdo do A3.",
        ("diagnostico-a3/conhecimento/02-diagnostico.md",),
    ),
    "ga2-documentos-de-projeto": Skill(
        "Documentos do projeto",
        "Organiza os documentos necessários em cada fase de um projeto, do contexto ao encerramento. Use quando pedirem dossiê, documentos do projeto, relatório de andamento ou resumo do ciclo.",
        ("iniciativas-e-ciclos/conhecimento/04-dossie-de-projeto.md",),
    ),
    "ga2-feedback-360": Skill(
        "Feedback 360",
        "Conduz um Feedback 360 com diferentes pontos de vista, padrões e até dois focos com prazo. Use quando pedirem avaliação 360, feedback de líder, pares e equipe ou plano após feedback.",
        ("lideranca-e-times/conhecimento/05-feedback-360.md",),
    ),
    "ga2-folha-de-experimento": Skill(
        "Folha de experimento",
        "Registra dor, problema, ideia, protótipo, teste e decisão em uma experiência pequena. Use quando pedirem experimento, hipótese, protótipo, teste barato ou portfólio de inovação.",
        ("melhoria-e-inovacao/conhecimento/05-folha-de-experimento.md",),
    ),
    "ga2-gemba-walk": Skill(
        "Vá e Veja — Gemba Walk",
        "Conduz uma observação no lugar onde o trabalho acontece, com pergunta, fatos e uma ação. Use quando pedirem Gemba, observação direta, investigação no local ou entendimento de uma queda.",
        ("melhoria-e-inovacao/conhecimento/06-gemba-walk.md",),
    ),
    "ga2-gestao-diaria": Skill(
        "Gestão diária",
        "Conduz uma reunião diária curta diante do quadro, destacando avanço, próximo passo e bloqueio. Use quando pedirem diária, daily, trabalhos parados, registro do dia ou remoção de bloqueios.",
        ("operacao-e-fluxo/conhecimento/04-gestao-diaria.md",),
    ),
    "ga2-kanban-canvas": Skill(
        "Kanban Canvas",
        "Desenha um quadro Kanban com estados, raias, cartões, limites e regras visíveis. Use quando pedirem Kanban, quadro de trabalho, fluxo, cartões, bloqueios ou políticas do quadro.",
        ("operacao-e-fluxo/conhecimento/02-kanban-canvas.md",),
    ),
    "ga2-matriz-esforco-impacto": Skill(
        "Matriz Impacto e Esforço",
        "Compara iniciativas pelo impacto e esforço e devolve uma fila com critérios claros. Use quando pedirem prioridade, matriz, ordem das iniciativas ou escolha do próximo trabalho.",
        ("estrategia-e-okr/conhecimento/03-matriz-impacto-esforco.md",),
    ),
    "ga2-me-mostra": Skill(
        "Me Mostra",
        "Use quando o usuário pedir para ver, desenhar ou explicar visualmente um caso, fluxo, problema, mudança ou decisão de gestão descrito no pedido ou na conversa atual; não use para assuntos sem um caso de gestão.",
        ("diagnostico-a3/conhecimento/11-gestao-visual-html.md",),
    ),
    "ga2-okr-canvas": Skill(
        "OKR Canvas",
        "Monta e acompanha um OKR Canvas com objetivo, resultados-chave de partida e chegada, iniciativas e revisão periódica. Use quando pedirem OKR, resultado-chave, iniciativa ou acompanhamento de meta.",
        ("estrategia-e-okr/conhecimento/04-okr-canvas.md",),
    ),
    "ga2-painel-do-gestor": Skill(
        "Painel do Gestor",
        "Monta uma visão curta de um ciclo com poucos números úteis para decidir. Use quando pedirem painel, números do ciclo, indicador principal, leitura da meta ou resumo para o gestor.",
        ("estrategia-e-okr/conhecimento/05-painel-do-gestor.md",),
    ),
    "ga2-pdca": Skill(
        "PDCA — ciclo de melhoria",
        "Registra uma melhoria em quatro etapas: planejar, executar, verificar e agir. Use quando pedirem PDCA, melhoria de processo, acompanhamento de contramedida ou decisão de padronizar e ajustar.",
        ("diagnostico-a3/conhecimento/05-pdca-e-acompanhamento.md",),
    ),
    "ga2-pdi": Skill(
        "Plano de Desenvolvimento Individual",
        "Monta um plano de desenvolvimento com objetivo de trabalho, forças, lacuna, ações 70-20-10, marco e acompanhamento. Use quando pedirem PDI, desenvolvimento de pessoa ou evolução profissional.",
        ("lideranca-e-times/conhecimento/06-pdi.md",),
    ),
    "ga2-plano-do-ciclo": Skill(
        "Plano do ciclo",
        "Planeja um ciclo com uma meta, capacidade segura, trabalhos com dono e data, e critério de pronto. Use quando pedirem plano da semana, sprint, meta do ciclo ou escolha do que entra.",
        ("iniciativas-e-ciclos/conhecimento/06-plano-do-ciclo.md",),
    ),
    "ga2-politicas-wip-urgencia": Skill(
        "Limite de trabalho e urgência",
        "Define limites de trabalho em andamento, bloqueios e critérios de urgência de um quadro. Use quando pedirem limite do quadro, WIP, gargalo, raia urgente ou política de urgência.",
        ("operacao-e-fluxo/conhecimento/03-wip-e-urgencia.md",),
    ),
    "ga2-pop": Skill(
        "Procedimento Operacional Padrão",
        "Escreve um procedimento recorrente com dono, gatilho, passos, saída, sistema, indicador, exceção e aprovação. Use quando pedirem POP, procedimento, rotina ou padronização de processo.",
        ("operacao-e-fluxo/conhecimento/06-pop.md",),
    ),
    "ga2-quadro-kaizen": Skill(
        "Quadro Kaizen",
        "Registra uma melhoria pequena com sinal, aposta, dono, prazo, aprendizado e decisão. Use quando pedirem Kaizen, fila de melhorias, pequeno ajuste ou resposta a indicador parado.",
        ("melhoria-e-inovacao/conhecimento/04-quadro-kaizen.md",),
    ),
    "ga2-quem-faz-o-que": Skill(
        "Quem faz o quê",
        "Define dono único, quem aceita, quem apoia, quem executa e quem aprova. Use quando pedirem responsáveis, papéis, dono da entrega, matriz de responsabilidade ou decisão de aprovação.",
        ("lideranca-e-times/conhecimento/02-quem-faz-o-que.md",),
    ),
    "ga2-relatorio-a3": Skill(
        "Relatório A3",
        "Monta um Relatório A3 completo, do contexto e causa raiz ao plano, acompanhamento e aprendizado. Use quando pedirem A3, solução estruturada de problema, queda de indicador ou plano para diretoria.",
        (
            "diagnostico-a3/conhecimento/01-fundamentos-a3.md",
            "diagnostico-a3/conhecimento/06-template-a3.md",
        ),
    ),
    "ga2-retrospectiva": Skill(
        "Retrospectiva",
        "Conduz uma retrospectiva sobre o modo de trabalhar e escolhe uma melhoria com dono e data. Use quando pedirem retro, manter, melhorar e parar, ou mudança de processo após um ciclo.",
        ("melhoria-e-inovacao/conhecimento/03-retrospectiva.md",),
    ),
    "ga2-review-do-ciclo": Skill(
        "Revisão do ciclo",
        "Compara o combinado com o entregue, exige prova e registra a decisão seguinte. Use quando pedirem review, revisão do ciclo, demonstração da entrega ou fechamento da semana.",
        ("melhoria-e-inovacao/conhecimento/02-review-do-ciclo.md",),
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
"""


ME_MOSTRA_BODY = """# Me Mostra — Gestão Visual GA 2.0

## Regra principal

Quando houver um caso de gestão identificável, sempre termine com um artefato HTML. Leia
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
6. Gere o HTML com pergunta, leitura direta, visual, prova e consequência.
7. Feche com o que ficou claro, o que segue em aberto e o próximo passo.

Use `assets/template-artefato.html` como ponto de partida. O HTML deve funcionar sem rede,
biblioteca externa ou imagem remota.

## Entrega por ambiente

- No Claude, use Artifact quando esse recurso estiver disponível.
- No Codex ou GPT, use o artefato ou a visualização exposta na sessão.
- No Cursor, use sua prévia ou visualização disponível.
- Em outro ambiente, use o recurso equivalente.
- Não escolha pela marca do modelo. Verifique o que o ambiente oferece.
- Sem recurso nativo, salve `.md` e `.html`, mostre um resumo visual no terminal ou no chat e
  informe o caminho do HTML.

Nunca entregue apenas Markdown, Mermaid, imagem ou diagrama de terminal. O HTML é obrigatório.

## Critério de pronto

- O visual principal responde à pergunta em até 90 segundos.
- O significado continua claro sem cor.
- Fato, estimativa e ponto em aberto não se misturam.
- Título e rótulos não contêm sigla ou jargão sem explicação.
- O objeto é o caso de gestão ativo, nunca o nome do plug-in por padrão.
- A entrega gerou HTML e usou a melhor forma disponível no ambiente.
"""


CNV_NOTE = """
## Privacidade

Não grave uma conversa privada por padrão. Entregue o texto no chat. Gere arquivo ou HTML
somente quando o usuário pedir de forma explícita e confirmar que pode salvar esse conteúdo.
"""


def skill_markdown(name: str, skill: Skill) -> str:
    body = ME_MOSTRA_BODY if name == "ga2-me-mostra" else COMMON_BODY.format(title=skill.title)
    if name == "ga2-canvas-de-conversa-cnv":
        body += CNV_NOTE
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


def combine_sources(source_root: Path, relative_sources: tuple[str, ...]) -> str:
    chunks: list[str] = []
    for relative in relative_sources:
        path = source_root / relative
        if not path.is_file():
            raise FileNotFoundError(f"Fonte não encontrada: {path}")
        chunks.append(path.read_text(encoding="utf-8").rstrip())
    return "\n\n---\n\n".join(chunks) + "\n"


def build(source_root: Path, output_root: Path) -> None:
    visual_source = source_root / "diagnostico-a3/conhecimento/11-gestao-visual-html.md"

    for name, skill in SKILLS.items():
        directory = output_root / name
        references = directory / "references"
        assets = directory / "assets"
        agents = directory / "agents"
        references.mkdir(parents=True, exist_ok=True)
        assets.mkdir(parents=True, exist_ok=True)
        agents.mkdir(parents=True, exist_ok=True)

        (directory / "SKILL.md").write_text(skill_markdown(name, skill), encoding="utf-8")
        (references / "metodo.md").write_text(
            combine_sources(source_root, skill.sources), encoding="utf-8"
        )
        if name != "ga2-me-mostra":
            shutil.copyfile(visual_source, references / "gestao-visual.md")

        group = skill.sources[0].split("/", 1)[0]
        shutil.copyfile(
            source_root / group / "conhecimento/10-fontes-e-procedencia.md",
            references / "fontes.md",
        )
        (assets / "template-artefato.html").write_text(HTML_TEMPLATE, encoding="utf-8")
        (agents / "openai.yaml").write_text(openai_yaml(name, skill), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fonte", required=True, type=Path)
    parser.add_argument("--destino", default=Path("skills"), type=Path)
    args = parser.parse_args()
    build(args.fonte.resolve(), args.destino.resolve())


if __name__ == "__main__":
    main()
