from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ABERTURA = "Antes de montar, pergunte o que faltar. Não invente dados."
MARCAS_INTERNAS = (
    r"\bv6\s*(?:aula|a)\s*\d+",
    r"\bv6[\s,/]{0,3}(?:aulas?|a)\s*\d+",
    r"\bM\d{2}\s*A\d{2}",
    r"\(\s*§\s?\d",
    r"\bL-\d{2}\b",
    r"\bregras?\s+\d+(?:\s*[–-]\s*\d+)?\s+do\s+Passo",
    r"§\s?\d",
    r"\bapostila\b",
    r"\bmodelo operacional\b",
    r"\bBase do método\b",
    r"\bMod\.?\s?0?\d\b",
    r"--help",
    r"\bfichas?\s+[A-G]\d{2}\b",
    r"Guia completo de rotinas",
    r"\b(?:legado|ao vivo)\s+A\d{2}\b|\bA\d{2}\s+ao vivo\b",
    r"\b(?:des)?trav(?:a|as|o|ar|am|ou|ava|ado|ada|ados|adas|ando|amento|e|em)\b",
    r"\((?:adaptação|acréscimo)",
    r"\b(?:adaptação|acréscimo)\s+do\s+(?:método|laboratório)",
    r"\bmodelo\s+T\d*",
    r"\[v6",
    r"\b(?:aulas?|slides?)\s+\d{1,2}\b",
    r"Onde a aula fala",
    r"\(ficha[;)]",
    r"Procedência que saiu",
)
RESIDUOS_VAZIOS = (r"(?<!`)``(?!`)", r"\(\)", r"\*{4}")
SUFIXOS_TEXTO = {".md", ".yaml", ".yml", ".json", ".html", ".txt", ".css", ".js", ".csv", ".svg"}


def arquivos_entregues() -> list[Path]:
    """Tudo o que a montagem do pacote leva ao comprador: skills, kit e manifestos."""
    arquivos = [p for p in SKILLS.rglob("*") if p.is_file()]
    kit = ROOT / "modelos" / "kit"
    arquivos += [p for p in kit.rglob("*") if p.is_file()
                 and not ({"_build", "previa", "__pycache__"} & set(p.relative_to(kit).parts))
                 and p.name != "migracao.json"]
    for pasta in (".claude-plugin", ".codex-plugin"):
        arquivos += [p for p in (ROOT / pasta).rglob("*") if p.is_file()]
    return sorted(p for p in arquivos if p.suffix.lower() in SUFIXOS_TEXTO)


def arquivos_carregados(skill: Path) -> list[Path]:
    candidatos = [skill / "SKILL.md"]
    for nome in ("metodo.md", "template.md", "checklist.md", "exemplo.md"):
        candidatos.append(skill / "references" / nome)
    candidatos.extend((skill / "assets" / "modelos").glob("template-*.md"))
    return [arquivo for arquivo in candidatos if arquivo.is_file()]


def test_skills_de_venda_perguntam_e_nao_expoem_marcas_internas() -> None:
    skills = sorted(list(SKILLS.glob("ga2-*")) + [SKILLS / "agenda-visual"])
    assert len(skills) == 41

    for skill in skills:
        conteudo = (skill / "SKILL.md").read_text(encoding="utf-8")
        assert ABERTURA in conteudo, skill.name
        for arquivo in arquivos_carregados(skill):
            texto = arquivo.read_text(encoding="utf-8")
            assert not any(re.search(marca, texto, flags=re.I) for marca in MARCAS_INTERNAS), arquivo
            assert "Entrada:" not in texto, arquivo
            assert not any(re.search(marca, texto) for marca in RESIDUOS_VAZIOS), arquivo


def test_arvore_entregue_sem_marcas_internas() -> None:
    """Inclui references/fontes.md, modelos, canvas e kit, que também chegam ao comprador."""
    arquivos = arquivos_entregues()
    assert len(arquivos) > 500
    assert len(list(SKILLS.glob("*/references/fontes.md"))) == 40
    achados = []
    for arquivo in arquivos:
        texto = arquivo.read_text(encoding="utf-8")
        for marca in MARCAS_INTERNAS:
            for m in re.finditer(marca, texto, flags=re.I):
                achados.append(f"{arquivo.relative_to(ROOT)}: {texto[max(0, m.start() - 30):m.end() + 20]!r}")
    assert not achados, "\n".join(achados[:20])
