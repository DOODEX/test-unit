# tests/test_app.py - v2
import unittest
from app.py import different

class TestDifferentesfontion(unittest.TestCase):

    def trois_egaux(self):
        result = different(1, 1, 1)
        self.assertEqual(result, "trois egaux")

    def tous_differents(self):
        result = different(1, 2, 3)
        self.assertEqual(result, "tous differents")

    def deux_egaux(self):
        result = different(1, 2, 1)
        self.assertEqual(result, "deux egaux")