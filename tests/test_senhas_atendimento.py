import unittest

from senhas_atendimento import SistemaSenhas


class SistemaSenhasTest(unittest.TestCase):
    def test_emite_senhas_sequenciais(self) -> None:
        sistema = SistemaSenhas()

        s1 = sistema.emitir_senha()
        s2 = sistema.emitir_senha("P")

        self.assertEqual("A001", s1.codigo)
        self.assertEqual("P002", s2.codigo)

    def test_chama_senhas_em_ordem_fifo(self) -> None:
        sistema = SistemaSenhas()
        sistema.emitir_senha("A")
        sistema.emitir_senha("B")

        primeira = sistema.chamar_proxima()
        segunda = sistema.chamar_proxima()
        terceira = sistema.chamar_proxima()

        self.assertEqual("A001", primeira.codigo)
        self.assertEqual("B002", segunda.codigo)
        self.assertIsNone(terceira)

    def test_painel_mostra_ultima_chamada_e_fila(self) -> None:
        sistema = SistemaSenhas()
        sistema.emitir_senha("A")
        sistema.emitir_senha("C")
        sistema.chamar_proxima()

        painel = sistema.painel()

        self.assertEqual("A001", painel["ultima_chamada"])
        self.assertEqual(["C002"], painel["aguardando"])
        self.assertEqual(1, painel["total_aguardando"])


if __name__ == "__main__":
    unittest.main()
