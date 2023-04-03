import unittest
from main import soma_lista


class TesteSomaLista(unittest.TestCase):
    def test_soma_lista_01(self):
        self.assertEqual(soma_lista(lista_de_elemento=[[2, 5], 1, [1], [1, 1, 1]]), 12)

    def test_soma_lista_02(self):
        self.assertEqual(soma_lista(lista_de_elemento=[[1, 2], [0], [1, 2, 3]]), 9)

    def test_soma_lista_03(self):
        self.assertEqual(soma_lista(lista_de_elemento=[[2], [1, 2], [6, 7, 8]]), 26)

    def test_soma_lista_04(self):
        self.assertEqual(soma_lista(lista_de_elemento=[1, 5, 3, [3, 6, 1, 10, 9, 11]]), 49)

