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
)
RESIDUOS_VAZIOS = (r"(?<!`)``(?!`)", r"\(\)", r"\*{4}")


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
