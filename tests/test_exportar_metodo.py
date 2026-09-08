"""Contrato de publicação: método preservado, adaptação explícita, deriva bloqueada."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from exportar_metodo import prepare, write_export, verify


class ExportTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.output = self.root / "skills"
        self.slug = "ga2-teste"
        self.skill = self.source / ".claude/skills" / self.slug
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("---\nname: ga2-teste\n---\n# Método\n1. Medir antes de decidir.\n2. Pedir a fonte.\nDestino: pasta-interna\n", encoding="utf-8")
        (self.skill / "template.md").write_text("# Caso\n<!-- c:dono -->\nDono único: ______\n", encoding="utf-8")
        (self.skill / "checklist.md").write_text("- [ ] Meta com prazo e prova.\n", encoding="utf-8")
        (self.skill / "exemplo.md").write_text("DADO REAL QUE NÃO PODE SER PUBLICADO", encoding="utf-8")
        self.adapt = self.source / "laboratorio/publicacao/adaptacoes" / f"{self.slug}.json"
        self.adapt.parent.mkdir(parents=True)
        self.spec = {"skill": self.slug, "files": {
            "SKILL.md": {"replacements": [{"from": "pasta-interna", "to": "pasta escolhida", "reason": "Destino do aluno"}]},
            "template.md": {"replacements": []}, "checklist.md": {"replacements": []}},
            "example": f"exemplos/{self.slug}.md"}
        self.save_spec()
        example = self.source / "laboratorio/publicacao" / self.spec["example"]
        example.parent.mkdir(parents=True)
        example.write_text("# Exemplo fictício\nNorte-Sul; números ilustrativos.\n", encoding="utf-8")

    def save_spec(self):
        self.adapt.write_text(json.dumps(self.spec), encoding="utf-8")

    def export(self):
        files, manifest = prepare(self.source, {self.slug})
        write_export(self.output, files, manifest)
        return files, manifest

    def test_preserva_metodo_template_checklist_e_exemplo_independente(self):
        files, _ = self.export()
        method = files[f"{self.slug}/references/metodo.md"].decode()
        self.assertEqual(method, "# Método\n1. Medir antes de decidir.\n2. Pedir a fonte.\nDestino: pasta escolhida\n")
        self.assertIn(b"<!-- c:dono -->", files[f"{self.slug}/references/template.md"])
        self.assertEqual(files[f"{self.slug}/references/checklist.md"], (self.skill / "checklist.md").read_bytes())
        self.assertNotIn("DADO REAL", "\n".join(value.decode() for value in files.values()))
        verify(self.output, self.source)

    def test_adaptacao_desatualizada_falha_antes_de_gravar(self):
        self.spec["files"]["SKILL.md"]["replacements"][0]["from"] = "trecho que não existe"
        self.save_spec()
        with self.assertRaisesRegex(ValueError, "adaptação desatualizada"):
            self.export()
        self.assertFalse(self.output.exists())

    def test_alteracao_na_fonte_reabre_exportacao(self):
        self.export()
        with (self.skill / "SKILL.md").open("a", encoding="utf-8") as stream:
            stream.write("3. Conferir o dono.\n")
        with self.assertRaisesRegex(ValueError, "fonte divergiu"):
            verify(self.output, self.source)

    def test_alteracao_no_pacote_e_detectada_sem_projeto_local(self):
        self.export()
        (self.output / self.slug / "references/checklist.md").write_text("resumo genérico", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "arquivo divergiu"):
            verify(self.output)

    def test_nao_aceita_substituir_metodo_por_pasta_legada(self):
        with self.assertRaisesRegex(ValueError, "skills canônicas"):
            prepare(self.root, {self.slug})

    def test_recurso_metodologico_exige_adaptacao_explicitada(self):
        self.spec["files"].pop("checklist.md")
        self.save_spec()
        with self.assertRaisesRegex(ValueError, "sem adaptação"):
            self.export()

    def test_referencia_empacotada_nao_pode_apontar_a_modelo_ausente(self):
        with (self.skill / "SKILL.md").open("a", encoding="utf-8") as stream:
            stream.write("Use `../assets/modelos/canvas-ausente.html`.\n")
        self.export()
        with self.assertRaisesRegex(ValueError, "referência ausente"):
            verify(self.output)

    def test_novo_recurso_auxiliar_na_fonte_exige_revisao(self):
        self.export()
        refs = self.skill / "references"
        refs.mkdir()
        (refs / "nova-regra.md").write_text("Uma regra nova.\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "sem adaptação"):
            verify(self.output, self.source)


if __name__ == "__main__":
    unittest.main()
