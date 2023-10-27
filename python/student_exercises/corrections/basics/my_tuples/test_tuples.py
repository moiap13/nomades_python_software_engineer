import unittest
from my_tuples import *

class TestTupleFunctions(unittest.TestCase):

    def test_create_empty_tuple(self):
        t = create_empty_tuple()
        self.assertIsInstance(t, tuple)
        self.assertEqual(len(t), 0)

    def test_create_tuple_from_list(self):
        lst = [1, 2, 3, 4, 5]
        t = create_tuple_from_list(lst)
        self.assertIsInstance(t, tuple)
        self.assertEqual(len(t), 5)
        self.assertEqual(t, tuple(lst))

    def test_access_element(self):
        t = (1, 2, 3, 4, 5)
        self.assertEqual(access_element(t, 2), 3)
        self.assertEqual(access_element(t, 4), 5)

    def test_slice_tuple(self):
        t = (1, 2, 3, 4, 5)
        self.assertEqual(slice_tuple(t, 1, 4), (2, 3, 4))
        self.assertEqual(slice_tuple(t, 2, 5), (3, 4, 5))

    def test_check_element(self):
        t = (1, 2, 3, 4, 5)
        self.assertTrue(check_element(t, 3))
        self.assertFalse(check_element(t, 6))

    def test_get_tuple_length(self):
        t = (1, 2, 3, 4, 5)
        self.assertEqual(get_tuple_length(t), 5)
        t = ()
        self.assertEqual(get_tuple_length(t), 0)

    def test_concatenate_tuples(self):
        t1 = (1, 2, 3)
        t2 = (4, 5, 6)
        self.assertEqual(concatenate_tuples(t1, t2), (1, 2, 3, 4, 5, 6))

    def test_count_occurrences(self):
        t = (1, 2, 2, 3, 3, 3, 4, 5)
        self.assertEqual(count_occurrences(t, 2), 2)
        self.assertEqual(count_occurrences(t, 3), 3)
        self.assertEqual(count_occurrences(t, 6), 0)

    def test_find_index(self):
        t = (1, 2, 3, 4, 5)
        self.assertEqual(find_index(t, 3), 2)
        self.assertRaises(ValueError, find_index, t, 6)

    def test_check_equal(self):
        t1 = (1, 2, 3)
        t2 = (1, 2, 3)
        t3 = (1, 2, 4)
        self.assertTrue(check_equal(t1, t2))
        self.assertFalse(check_equal(t1, t3))

    def test_find_maximum(self):
        t = (1, 2, 3, 4, 5)
        self.assertEqual(find_maximum(t), 5)

    def test_find_minimum(self):
        t = (1, 2, 3, 4, 5)
        self.assertEqual(find_minimum(t), 1)

    def test_convert_tuple_to_list(self):
        t = (1, 2, 3, 4, 5)
        self.assertEqual(convert_tuple_to_list(t), [1, 2, 3, 4, 5])

    def test_convert_list_to_tuple(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(convert_list_to_tuple(lst), (1, 2, 3, 4, 5))

    def test_sort_tuple(self):
        t = (3, 2, 5, 1, 4)
        self.assertEqual(sort_tuple(t), (1, 2, 3, 4, 5))

if __name__ == '__main__':
    unittest.main()
