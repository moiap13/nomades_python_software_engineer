import unittest

from my_array import (
    tri_croissant,
    tri_decroissant,
    somme,
    moyenne,
    min,
    max,
    min_max,
    mediane,
    mode,
    ecart_type,
    existe,
    position,
    similaires,
    est_tableau,
    est_tableau_de_nombres,
)


class TestArrayFunctions(unittest.TestCase):
    def test_triCroissant(self):
        self.assertEqual(tri_croissant([1, 3, 2, 5, 4]), [1, 2, 3, 4, 5])

    def test_triDecroissant(self):
        self.assertEqual(tri_decroissant([1, 3, 2, 5, 4]), [5, 4, 3, 2, 1])

    def test_somme(self):
        self.assertEqual(somme([1, 2, 3, 4, 5]), 15)

    def test_moyenne(self):
        self.assertEqual(moyenne([1, 2, 3, 4, 5]), 3)
        self.assertEqual(moyenne([1, 2, 3, 4, 5, 6]), 3.5)

    def test_min(self):
        self.assertEqual(min([1, 2, 3, 4, 5]), 1)

    def test_max(self):
        self.assertEqual(max([1, 2, 3, 4, 5]), 5)

    def test_minMax(self):
        self.assertEqual(min_max([1, 2, 3, 4, 5]), [1, 5])

    def test_mediane(self):
        self.assertEqual(mediane([1, 2, 3, 4, 5]), 3)
        self.assertEqual(mediane([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(mediane([1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(mediane([1, 1, 1, 10, 10]), 1)
        self.assertEqual(mediane([3, 5, 1, 4, 2]), 3)

    def test_mode(self):
        self.assertEqual(mode([1, 2, 3, 4, 5]), 1)
        self.assertEqual(mode([1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(mode([1, 1, 1, 10, 10]), 1)
        self.assertEqual(mode([4, 2, 4, 3, 2, 2]), 2)

    def test_ecartType(self):
        self.assertAlmostEqual(ecart_type([1, 2, 3, 4, 5]), 1.4142135623730951)
        self.assertAlmostEqual(ecart_type([1, 1, 1, 1, 1, 1]), 0)
        self.assertAlmostEqual(ecart_type([1, 1, 1, 10, 10]), 4.409081537009721)
        self.assertAlmostEqual(ecart_type([4, 2, 4, 3, 2, 2]), 0.8975274678557507)

    def test_existe(self):
        self.assertTrue(existe([1, 2, 3], 2))
        self.assertFalse(existe([1, 2, 3], 4))

    def test_position(self):
        self.assertEqual(position([1, 2, 3], 1), 0)
        self.assertEqual(position([1, 2, 3], 2), 1)
        self.assertEqual(position([1, 2, 3], 4), -1)

    def test_similaires(self):
        self.assertTrue(similaires([1, 2, 3], [1, 2, 3]))
        self.assertFalse(similaires([1, 2, 3], [1, 2, 4]))
        self.assertFalse(similaires([1, 2, 3], [1, 2]))

    def test_estTableau(self):
        self.assertTrue(est_tableau([]))
        self.assertTrue(est_tableau([1, 2, 3]))
        self.assertFalse(est_tableau(1))

    def test_estTableauDeNombres(self):
        self.assertTrue(est_tableau_de_nombres([]))
        self.assertTrue(est_tableau_de_nombres([1, 2, 3]))
        self.assertFalse(est_tableau_de_nombres([1, 2, "3"]))
        self.assertFalse(est_tableau_de_nombres(1))


if __name__ == "__main__":
    unittest.main()
