"""Manifesto dos PDFs oficiais: onde estão no acervo, sha256, página da folha, skill dona."""
import hashlib
import json
import unicodedata
from pathlib import Path

from . import RAIZ, SPECS

ARQ = RAIZ / "oficiais" / "manifesto.json"


def carregar() -> dict:
    return json.loads(ARQ.read_text(encoding="utf-8"))


def salvar(m: dict) -> None:
    ARQ.write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def resolver(base: str, nome: str) -> Path:
    """Acha o arquivo mesmo quando o acento no disco está em NFD e no manifesto em NFC (ou vice-versa)."""
    candidatos = []
    for forma in ("NFC", "NFD"):
        candidatos.append(Path(unicodedata.normalize(forma, str(Path(base) / nome))))
    for c in candidatos:
        if c.exists():
            return c
    # busca pelo nome normalizado dentro da pasta (a pasta pode ter subpastas no nome)
    alvo = unicodedata.normalize("NFC", (Path(base) / nome).name).casefold()
    pai_rel = Path(nome).parent
    for forma in ("NFC", "NFD"):
        pasta = Path(unicodedata.normalize(forma, str(Path(base) / pai_rel)))
        if pasta.is_dir():
            for f in pasta.iterdir():
                if unicodedata.normalize("NFC", f.name).casefold() == alvo:
                    return f
    raise FileNotFoundError(f"{base}/{nome}")


def caminho(m: dict, item: dict) -> Path:
    fam = item["familia"]
    if fam == "laboratorio":
        raise ValueError(f"{item['id']}: família laboratorio não tem PDF")
    base = m["acervo"].get(fam, "")
    return resolver(base, item["arquivo"]) if base else resolver("/", item["arquivo"])


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(Path(p).read_bytes())
    return h.hexdigest()


def por_id(m: dict, id_: str) -> dict:
    for it in m["oficiais"]:
        if it["id"] == id_:
            return it
    raise KeyError(f"oficial '{id_}' não está em {ARQ}")


def ids(m: dict) -> list:
    return [it["id"] for it in m["oficiais"]]


def spec_path(id_: str) -> Path:
    return SPECS / f"{id_}.json"
