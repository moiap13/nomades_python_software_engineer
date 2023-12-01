import unittest
from my_strings import compteMots, inverser, estPalindrome, compteCaracteres, compterLesLettres, compteVoyelles, compteConsonnes, concatenation

class StringFunctionsTestCase(unittest.TestCase):
    def test_compteMots(self):
        self.assertEqual(compteMots("Hello World"), 2)
        self.assertEqual(compteMots(" Hello World "), 2)
        self.assertEqual(compteMots("This is a test"), 4)
        self.assertEqual(compteMots("One"), 1)

    def test_inverser(self):
        self.assertEqual(inverser("hello"), "olleh")
        self.assertEqual(inverser("hello world"), "dlrow olleh")
        self.assertEqual(inverser("12345"), "54321")
        self.assertEqual(inverser("racecar"), "racecar")

    def test_estPalindrome(self):
        self.assertTrue(estPalindrome("kayak"))
        self.assertFalse(estPalindrome("hello"))
        self.assertTrue(estPalindrome("racecar"))
        self.assertTrue(estPalindrome("12321"))

    def test_compteCaracteres(self):
        self.assertEqual(compteCaracteres("hello"), 5)
        self.assertEqual(compteCaracteres("hello world"), 11)
        self.assertEqual(compteCaracteres("12345"), 5)
        self.assertEqual(compteCaracteres(""), 0)

    def test_compterLesLettres(self):
        self.assertEqual(compterLesLettres("hello"), 5)
        self.assertEqual(compterLesLettres("hello world"), 10)
        self.assertEqual(compterLesLettres("12345"), 0)
        self.assertEqual(compterLesLettres("  "), 0)

    def test_compteVoyelles(self):
        self.assertEqual(compteVoyelles("hello"), 2)
        self.assertEqual(compteVoyelles("hello world"), 3)
        self.assertEqual(compteVoyelles("HellO World"), 3)
        self.assertEqual(compteVoyelles("bcd"), 0)

    def test_compteConsonnes(self):
        self.assertEqual(compteConsonnes("hello"), 3)
        self.assertEqual(compteConsonnes("hello world"), 7)
        self.assertEqual(compteConsonnes("HellO World"), 7)
        self.assertEqual(compteConsonnes("aeiouy"), 0)

    def test_concatenation(self):
        self.assertEqual(concatenation("hello", "world"), "helloworld")
        self.assertEqual(concatenation("abc", ""), "abc")
        self.assertEqual(concatenation("", "xyz"), "xyz")
        self.assertEqual(concatenation("", ""), "")


if __name__ == '__main__':
    unittest.main()
