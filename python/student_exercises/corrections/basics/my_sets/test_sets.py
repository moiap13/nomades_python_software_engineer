import unittest
from my_sets import *

class TestSetFunctions(unittest.TestCase):

    def test_create_empty_set(self):
        s = create_empty_set()
        self.assertIsInstance(s, set)
        self.assertEqual(len(s), 0)

    def test_create_set_from_list(self):
        lst = [1, 2, 3, 4, 5]
        s = create_set_from_list(lst)
        self.assertIsInstance(s, set)
        self.assertEqual(len(s), 5)
        self.assertEqual(s, set(lst))

    def test_add_element(self):
        s = set()
        add_element(s, 1)
        self.assertEqual(len(s), 1)
        self.assertIn(1, s)
        add_element(s, 2)
        self.assertEqual(len(s), 2)
        self.assertIn(2, s)

    def test_remove_element(self):
        s = {1, 2, 3}
        remove_element(s, 2)
        self.assertEqual(len(s), 2)
        self.assertNotIn(2, s)
        self.assertRaises(KeyError, remove_element, s, 4)

    def test_check_element(self):
        s = {1, 2, 3}
        self.assertTrue(check_element(s, 1))
        self.assertFalse(check_element(s, 4))

    def test_count_elements(self):
        s = {1, 2, 3, 4, 5}
        self.assertEqual(count_elements(s), 5)
        s = set()
        self.assertEqual(count_elements(s), 0)

    def test_union_sets(self):
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        self.assertEqual(union_sets(s1, s2), {1, 2, 3, 4, 5})

    def test_intersect_sets(self):
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        self.assertEqual(intersect_sets(s1, s2), {3})

    def test_difference_sets(self):
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        self.assertEqual(difference_sets(s1, s2), {1, 2})

    def test_check_subset(self):
        s1 = {1, 2, 3}
        s2 = {1, 2, 3, 4, 5}
        self.assertTrue(check_subset(s1, s2))
        self.assertFalse(check_subset(s2, s1))

    def test_check_disjoint(self):
        s1 = {1, 2, 3}
        s2 = {4, 5, 6}
        self.assertTrue(check_disjoint(s1, s2))
        self.assertFalse(check_disjoint(s1, {3, 4}))

    def test_clear_set(self):
        s = {1, 2, 3}
        clear_set(s)
        self.assertEqual(len(s), 0)

    def test_copy_set(self):
        s = {1, 2, 3}
        s_copy = copy_set(s)
        self.assertEqual(s_copy, s)
        self.assertIsNot(s_copy, s)

    def test_find_maximum(self):
        s = {1, 2, 3, 4, 5}
        self.assertEqual(find_maximum(s), 5)

    def test_check_equal(self):
        s1 = {1, 2, 3}
        s2 = {3, 2, 1}
        s3 = {1, 2, 4}
        self.assertTrue(check_equal(s1, s2))
        self.assertFalse(check_equal(s1, s3))

if __name__ == '__main__':
    unittest.main()
