import unittest
from my_list_comprehension import *

class TestListComprehensions(unittest.TestCase):

    def test_generate_numbers(self):
        self.assertEqual(generate_numbers(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_generate_squares(self):
        self.assertEqual(generate_squares(), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

    def test_generate_even_numbers(self):
        self.assertEqual(generate_even_numbers(), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_generate_odd_numbers(self):
        self.assertEqual(generate_odd_numbers(), [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_generate_uppercase_letters(self):
        self.assertEqual(generate_uppercase_letters(), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    def test_generate_lowercase_letters(self):
        self.assertEqual(generate_lowercase_letters(), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

    def test_generate_squared_even_numbers(self):
        self.assertEqual(generate_squared_even_numbers(), [4, 16, 36, 64, 100, 144, 196, 256, 324, 400])

    def test_generate_number_squares(self):
        self.assertEqual(generate_number_squares(), [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)])

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world, how are you?"), ['Hello', 'World,', 'How', 'Are', 'You?'])

    def test_generate_prime_numbers(self):
        self.assertEqual(generate_prime_numbers(), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

    def test_generate_divisible_by_3_or_5(self):
        self.assertEqual(generate_divisible_by_3_or_5(), [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50])

    def test_generate_even_squares_odd_cubes(self):
        self.assertEqual(generate_even_squares_odd_cubes(), [1, 4, 27, 16, 125, 36, 343, 64, 729, 100])

    def test_generate_word_lengths(self):
        self.assertEqual(generate_word_lengths("This is a sample sentence"), [4, 2, 1, 6, 8])

    def test_generate_numbers_excluding_multiples_of_3(self):
        self.assertEqual(generate_numbers_excluding_multiples_of_3(), [1, 2, 4, 5, 7, 8, 10])

    def test_generate_squares_of_even_numbers(self):
        self.assertEqual(generate_squares_of_even_numbers(), [4, 16, 36, 64, 100])

    def test_generate_vowels(self):
        self.assertEqual(generate_vowels("hello"), ['e', 'o'])

    def test_generate_numbers_repeated(self):
        self.assertEqual(generate_numbers_repeated(), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])

    def test_generate_squares_excluding_multiples_of_3(self):
        self.assertEqual(generate_squares_excluding_multiples_of_3(), [1, 4, 16, 25, 49, 64, 100])

    def test_generate_uppercase_consonants(self):
        self.assertEqual(generate_uppercase_consonants("Hello, World!"), ['H', 'L', 'L', 'W', 'R', 'L', 'D'])

    def test_generate_even_numbers_in_range(self):
        self.assertEqual(generate_even_numbers_in_range(5, 15), [6, 8, 10, 12, 14])


if __name__ == '__main__':
    unittest.main()
