def is_even(number: int) -> str:
    """
    Function that checks if a number is even or odd.
    Return the string "The number is even" if the number is even, "The number is odd" otherwise.
    params:
      number: The number to check
    
    Returns:
      A string that says if the number is even or odd
    """
    return "The number is even" if number % 2 == 0 else "The number is odd"
        

def factorial(n: int) -> int:
    """
    Function that computes the factorial of a number.
    The factorial of n is the product of all positive integers less than or equal to n.
    :param n: The number to compute the factorial of
    :return: The factorial of n
    """
    # fact = 1
    # for ni in range(2, n+1):
    #     fact *= ni
    # return fact
    if n == 0:
      return 1
    return n * factorial(n-1)

def fibonacci(n: int) -> int:
    """
    Function that computes the nth Fibonacci number.
    :param n: The index of the Fibonacci number to compute
    :return: The nth Fibonacci number
    """
    # if n == 0 or n == 1:
    #     return n
    
    # fib_2 = 0
    # fib_1 = 1
    # for _ in range(2, n+1):
    #     fib = fib_2 + fib_1
    #     fib_1,fib_2 = fib, fib_1
    # return fib

    if n == 0 or n == 1:
      return n
    return fibonacci(n-2) + fibonacci(n-1)

def sum(n: int) -> int: # O(1); O(n); O(n^2); O(log n)
    """
    Function that computes the sum of all integers from 0 to n.
    :param n: The number to compute the sum up to
    :return: The sum of all integers from 0 to n
    """
    # res = 0
    # for i in range(1, n+1):
    #   res += i
    # return res
    return n*(n+1)/2

def square(n: int) -> int:
    """
    Function that computes the square of a number.
    :param n: The number to compute the square of
    :return: The square of n
    """
    return n*n


def is_prime(n: int) -> bool:
    """
    Function that checks if a number is prime.
    A prime number is a number that is divisible only by itself and 1.
    :param n: The number to check
    :return: True if the number is prime, False otherwise
    """
    if n == 0 or n == 1:
        return False
    
    for i in range(2,n**0.5):
        if n%i==0:
            return False

    return True

import random
random.randrange()