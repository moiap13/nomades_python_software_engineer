import unittest

from my_maths import *


class TestFunctions(unittest.TestCase):
    def test_estPair(self):
        self.assertEqual(estPair(2), "Le nombre est pair")
        self.assertEqual(estPair(3), "Le nombre est impair")

    def test_factorielle(self):
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(1), 1)
        self.assertEqual(factorielle(2), 2)
        self.assertEqual(factorielle(3), 6)
        self.assertEqual(factorielle(4), 24)
        self.assertEqual(factorielle(5), 120)
        self.assertEqual(factorielle(6), 720)
        self.assertEqual(factorielle(7), 5040)
        self.assertEqual(
            factorielle(25),
            15511210043330985984000000
        )

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(25), 75025)

    def test_somme(self):
        self.assertEqual(somme(0), 0)
        self.assertEqual(somme(1), 1)
        self.assertEqual(somme(2), 3)
        self.assertEqual(somme(3), 6)
        self.assertEqual(somme(4), 10)
        self.assertEqual(somme(5), 15)
        self.assertEqual(somme(10), 55)
        self.assertEqual(somme(50), 1275)

    def test_auCarre(self):
        self.assertEqual(auCarre(0), 0)
        self.assertEqual(auCarre(1), 1)
        self.assertEqual(auCarre(2), 4)
        self.assertEqual(auCarre(3), 9)
        self.assertEqual(auCarre(4), 16)
        self.assertEqual(auCarre(5), 25)
        self.assertEqual(auCarre(10), 100)
        self.assertEqual(auCarre(50), 2500)

    def test_est_premier(self):
        self.assertEqual(est_premier(0), False)
        self.assertEqual(est_premier(1), False)
        self.assertEqual(est_premier(2), True)
        self.assertEqual(est_premier(3), True)
        self.assertEqual(est_premier(4), False)
        self.assertEqual(est_premier(5), True)


if __name__ == "__main__":
    unittest.main()
