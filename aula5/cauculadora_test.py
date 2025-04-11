import unittest
from cauculadora import dividir, somar
from funcoes import *

class TesteCauculadora(unittest.TestCase):
    def testarSoma(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)
        
    def testarDivi_Por_Zero(self):
        with self.assertRaises(ValueError):
            dividir(10,0)    

    def test_eh_Par(self):
        with self.assertRaises(ValueError):
            eh_Par(5)