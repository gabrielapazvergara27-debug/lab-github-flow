import unittest
from app import sumar, restar

class TestCalculadora(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_restar_negativo(self):
        self.assertEqual(restar(2, 5), -3)