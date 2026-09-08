"""Fonte independente, cópia fiel e instalações rastreáveis."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from exportar_metodo import seal_distribution, verify, inventory
from instalar import install, RECEIPT
import montar_distribuicao


class DistributionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.skills = self.root / "skills"
        self.skill = self.skills / "ga2-teste"
        (self.skill / "references").mkdir(parents=True)
        (self.root / "VERSION").write_text("1.0.0\n")
        (self.skill / "SKILL.md").write_text("Leia `references/metodo.md`.\n")
        (self.skill / "references/metodo.md").write_text("Meça antes de decidir. Preserve campos e evidências.\n")
        seal_distribution(self.skills)
        self.destination = Path(self.temp.name) / "installed"

    def test_copia_sem_reescrever_e_sem_fonte_externa(self):
        with patch.object(montar_distribuicao, "ROOT", self.root):
            montar_distribuicao.build(self.destination)
        self.assertEqual(inventory(self.skills), inventory(self.destination))
        verify(self.destination)

    def test_montagem_nao_sobrescreve_destino_ocupado(self):
        self.destination.mkdir()
        file = self.destination / "trabalho.md"
        file.write_text("edição humana")
        with patch.object(montar_distribuicao, "ROOT", self.root):
            with self.assertRaisesRegex(ValueError, "destino vazio"):
                montar_distribuicao.build(self.destination)
        self.assertEqual(file.read_text(), "edição humana")

    def test_metodo_alterado_exige_novo_manifesto(self):
        (self.skill / "references/metodo.md").write_text("conteúdo revisto")
        with self.assertRaisesRegex(ValueError, "divergiu"):
            verify(self.skills)

    def test_recurso_ausente_e_rejeitado_mesmo_com_hash_atualizado(self):
        (self.skill / "references/metodo.md").unlink()
        seal_distribution(self.skills)
        with self.assertRaisesRegex(ValueError, "referência ausente"):
            verify(self.skills)

    def test_links_externos_nao_entram_no_pacote(self):
        (self.skill / "link").symlink_to(self.root / "VERSION")
        with self.assertRaisesRegex(ValueError, "link não distribuível"):
            seal_distribution(self.skills)

    def test_instala_e_repete_sem_copias_novas(self):
        first = install(self.root, self.destination)
        original = (self.destination / RECEIPT).stat().st_mtime_ns
        self.assertEqual(install(self.root, self.destination), first)
        self.assertEqual((self.destination / RECEIPT).stat().st_mtime_ns, original)
        self.assertEqual(install(self.root, self.destination, check=True), first)
        self.assertEqual(first["files"], inventory(self.skills))

    def test_atualiza_versao_preservando_skill_privada(self):
        install(self.root, self.destination)
        private = self.destination / "rotina-privada"
        private.mkdir(); (private / "SKILL.md").write_text("contexto local")
        (self.root / "VERSION").write_text("1.0.1\n")
        (self.skill / "references/metodo.md").write_text("método melhorado")
        seal_distribution(self.skills)
        receipt = install(self.root, self.destination)
        self.assertEqual(receipt["version"], "1.0.1")
        self.assertEqual((private / "SKILL.md").read_text(), "contexto local")
        self.assertEqual(receipt["files"], inventory(self.destination))

    def test_edicao_na_instalacao_nao_e_perdida(self):
        install(self.root, self.destination)
        file = self.destination / "ga2-teste/references/metodo.md"
        file.write_text("edição humana")
        with self.assertRaisesRegex(ValueError, "alterada localmente"):
            install(self.root, self.destination)
        self.assertEqual(file.read_text(), "edição humana")

    def test_pasta_legada_exige_migracao_explicita(self):
        legacy = self.destination / "ga2-teste"
        legacy.mkdir(parents=True)
        with self.assertRaisesRegex(ValueError, "sem registro"):
            install(self.root, self.destination)
        self.assertTrue(legacy.exists())

    def test_nao_instala_sobre_a_fonte(self):
        with self.assertRaisesRegex(ValueError, "sobrepõe"):
            install(self.root, self.skills)


if __name__ == "__main__":
    unittest.main()
