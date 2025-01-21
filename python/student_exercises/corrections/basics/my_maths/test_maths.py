import unittest

from my_maths import is_even, factorial, fibonacci, sum, square, is_prime


class TestFunctions(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(is_even(2), "The number is even")
        self.assertEqual(is_even(3), "The number is odd")

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(
            factorial(25),
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

    def test_sum(self):
        self.assertEqual(sum(0), 0)
        self.assertEqual(sum(1), 1)
        self.assertEqual(sum(2), 3)
        self.assertEqual(sum(3), 6)
        self.assertEqual(sum(4), 10)
        self.assertEqual(sum(5), 15)
        self.assertEqual(sum(10), 55)
        self.assertEqual(sum(50), 1275)

    def test_square(self):
        self.assertEqual(square(0), 0)
        self.assertEqual(square(1), 1)
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)
        self.assertEqual(square(5), 25)
        self.assertEqual(square(10), 100)
        self.assertEqual(square(50), 2500)

    def test_is_prime(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)


if __name__ == "__main__":
    unittest.main()
