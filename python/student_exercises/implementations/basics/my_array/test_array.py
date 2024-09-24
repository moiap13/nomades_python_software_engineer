import unittest

from my_array import (
    sort_ascending,
    sort_descending,
    sum,
    average,
    min,
    max,
    min_max,
    median,
    mode,
    variance,
    standard_deviation,
    exist,
    position,
    similars,
    is_list,
    is_list_of_numbers,
)


class TestArrayFunctions(unittest.TestCase):
    def test_sort_ascending(self):
        self.assertEqual(sort_ascending([1, 3, 2, 5, 4]), [1, 2, 3, 4, 5])

    def test_sort_descending(self):
        self.assertEqual(sort_descending([1, 3, 2, 5, 4]), [5, 4, 3, 2, 1])

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3, 4, 5]), 15)

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(average([1, 2, 3, 4, 5, 6]), 3.5)

    def test_min(self):
        self.assertEqual(min([1, 2, 3, 4, 5]), 1)

    def test_max(self):
        self.assertEqual(max([1, 2, 3, 4, 5]), 5)

    def test_min_max(self):
        self.assertEqual(min_max([1, 2, 3, 4, 5]), (1, 5))

    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(median([1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(median([1, 1, 1, 10, 10]), 1)
        self.assertEqual(median([3, 5, 1, 4, 2]), 3)

    def test_mode(self):
        self.assertEqual(mode([1, 2, 3, 4, 5]), 1)
        self.assertEqual(mode([1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(mode([1, 1, 1, 10, 10]), 1)
        self.assertEqual(mode([4, 2, 4, 3, 2, 2]), 2)

    def test_variance(self):
        self.assertEqual(variance([1, 2, 3, 4, 5]), 2)
        self.assertEqual(variance([1, 1, 1, 1, 1, 1]), 0)
        self.assertEqual(variance([1, 1, 1, 10, 10]), 19.44)
        self.assertEqual(variance([4, 2, 4, 3, 2, 2]), 0.8055555555555556)

    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4, 5]), 1.4142135623730951)
        self.assertAlmostEqual(standard_deviation([1, 1, 1, 1, 1, 1]), 0)
        self.assertAlmostEqual(standard_deviation([1, 1, 1, 10, 10]), 4.409081537009721)
        self.assertAlmostEqual(standard_deviation([4, 2, 4, 3, 2, 2]), 0.8975274678557507)

    def test_exist(self):
        self.assertTrue(exist([1, 2, 3], 2))
        self.assertFalse(exist([1, 2, 3], 4))

    def test_position(self):
        self.assertEqual(position([1, 2, 3], 1), 0)
        self.assertEqual(position([1, 2, 3], 2), 1)
        self.assertEqual(position([1, 2, 3], 4), -1)

    def test_similar(self):
        self.assertTrue(similars([1, 2, 3], [1, 2, 3]))
        self.assertFalse(similars([1, 2, 3], [1, 2, 4]))
        self.assertFalse(similars([1, 2, 3], [1, 2]))

    def test_is_list(self):
        self.assertTrue(is_list([]))
        self.assertTrue(is_list([1, 2, 3]))
        self.assertFalse(is_list(1))

    def test_is_list_of_numbers(self):
        self.assertFalse(is_list_of_numbers([]))
        self.assertTrue(is_list_of_numbers([1, 2, 3]))
        self.assertFalse(is_list_of_numbers([1, 2, "3"]))
        self.assertFalse(is_list_of_numbers(1))


if __name__ == "__main__":
    unittest.main()
