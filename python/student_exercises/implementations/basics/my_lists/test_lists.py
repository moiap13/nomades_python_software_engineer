import unittest
from my_lists import (
    get_first_three_elements,
    get_last_two_elements,
    reverse_list,
    get_even_index_elements,
    get_odd_index_elements,
    remove_duplicates,
    square_elements,
    double_elements,
    sum_of_elements,
    is_sorted,
    count_occurrences,
    find_maximum,
    find_minimum,
    combine_lists,
    is_palindrome,
)

class TestListFunctions(unittest.TestCase):

    def test_get_first_three_elements(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(get_first_three_elements(lst), [1, 2, 3])
        self.assertEqual(get_first_three_elements([]), [])
        self.assertEqual(get_first_three_elements([1]), [1])
        self.assertEqual(get_first_three_elements([1, 2]), [1, 2])

    def test_get_last_two_elements(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(get_last_two_elements(lst), [4, 5])
        self.assertEqual(get_last_two_elements([]), [])
        self.assertEqual(get_last_two_elements([1]), [1])
        self.assertEqual(get_last_two_elements([1, 2]), [1, 2])

    def test_reverse_list(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(reverse_list(lst), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_list([]), [])
        self.assertEqual(reverse_list([1]), [1])
        self.assertEqual(reverse_list([1, 2]), [2, 1])

    def test_get_even_index_elements(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(get_even_index_elements(lst), [1, 3, 5])
        self.assertEqual(get_even_index_elements([]), [])
        self.assertEqual(get_even_index_elements([1]), [1])
        self.assertEqual(get_even_index_elements([1, 2]), [1])

    def test_get_odd_index_elements(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(get_odd_index_elements(lst), [2, 4])
        self.assertEqual(get_odd_index_elements([]), [])
        self.assertEqual(get_odd_index_elements([1]), [])
        self.assertEqual(get_odd_index_elements([1, 2]), [2])

    def test_remove_duplicates(self):
        lst = [1, 2, 2, 3, 3, 4, 5]
        self.assertEqual(remove_duplicates(lst), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1]), [1])
        self.assertEqual(remove_duplicates([1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_square_elements(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(square_elements(lst), [1, 4, 9, 16, 25])
        self.assertEqual(square_elements([]), [])
        self.assertEqual(square_elements([0]), [0])
        self.assertEqual(square_elements([-1, 2, -3]), [1, 4, 9])

    def test_double_elements(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(double_elements(lst), [2, 4, 6, 8, 10])
        self.assertEqual(double_elements([]), [])
        self.assertEqual(double_elements([0]), [0])
        self.assertEqual(double_elements([-1, 2, -3]), [-2, 4, -6])

    def test_sum_of_elements(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(sum_of_elements(lst), 15)
        self.assertEqual(sum_of_elements([]), 0)
        self.assertEqual(sum_of_elements([1]), 1)
        self.assertEqual(sum_of_elements([1, -1]), 0)

    def test_is_sorted(self):
        lst1 = [1, 2, 3, 4, 5]
        lst2 = [5, 4, 3, 2, 1]
        self.assertTrue(is_sorted(lst1))
        self.assertFalse(is_sorted(lst2))
        self.assertTrue(is_sorted([]))
        self.assertTrue(is_sorted([1]))
        self.assertTrue(is_sorted([1, 1, 1]))
        self.assertFalse(is_sorted([1, 2, 1]))

    def test_count_occurrences(self):
        lst = [1, 2, 2, 3, 3, 3, 4, 5]
        self.assertEqual(count_occurrences(lst, 2), 2)
        self.assertEqual(count_occurrences(lst, 3), 3)
        self.assertEqual(count_occurrences(lst, 6), 0)
        self.assertEqual(count_occurrences([], 1), 0)
        self.assertEqual(count_occurrences([1, 1, 1], 1), 3)

    def test_find_maximum(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(find_maximum(lst), 5)
        self.assertEqual(find_maximum([]), None)
        self.assertEqual(find_maximum([1]), 1)
        self.assertEqual(find_maximum([-1, -2, -3]), -1)

    def test_find_minimum(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(find_minimum(lst), 1)
        self.assertEqual(find_minimum([]), None)
        self.assertEqual(find_minimum([1]), 1)
        self.assertEqual(find_minimum([-1, -2, -3]), -3)

    def test_combine_lists(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        self.assertEqual(combine_lists(lst1, lst2), [1, 4, 2, 5, 3, 6])
        self.assertEqual(combine_lists([], []), [])
        self.assertEqual(combine_lists([1], [2]), [1, 2])

    def test_is_palindrome(self):
        lst1 = [1, 2, 3, 2, 1]
        lst2 = [1, 2, 3, 4, 5]
        self.assertTrue(is_palindrome(lst1))
        self.assertFalse(is_palindrome(lst2))
        self.assertTrue(is_palindrome([]))
        self.assertTrue(is_palindrome([1]))
        self.assertFalse(is_palindrome([2, 2, 1]))

if __name__ == '__main__':
    unittest.main()
