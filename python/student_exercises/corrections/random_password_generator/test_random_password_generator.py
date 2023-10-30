import unittest
import string

from random_password_generator import generate_random_password

class TestRandomPasswordGenerator(unittest.TestCase):

    def test_generate_random_password(self):
        # Test default length
        password = generate_random_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

        # Test custom length
        password = generate_random_password(16)
        self.assertEqual(len(password), 16)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

        # Test invalid length
        with self.assertRaises(ValueError):
            generate_random_password(5)

if __name__ == '__main__':
    unittest.main()
