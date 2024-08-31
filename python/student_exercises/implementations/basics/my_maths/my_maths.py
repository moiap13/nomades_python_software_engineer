def is_even(number: int) -> str:
    """
    Function that checks if a number is even or odd.
    Return the string "The number is even" if the number is even, "The number is odd" otherwise.
    params:
      number: The number to check
    
    Returns:
      A string that says if the number is even or odd
    """

    # if number % 2 != 0:
    #     return "This number is odd"
    # else: 
    #     return "This number is even"

    return "This number is odd" if number % 2 else "This number is even"

def factorial(n: int) -> int:
    """
    Function that computes the factorial of a number.
    The factorial of n is the product of all positive integers less than or equal to n.
    :param n: The number to compute the factorial of
    :return: The factorial of n
    """
    # if n == 0 or n == 1:
    #     return 1
    # result = 1
    # for i in range(2, n + 1):
    #     result *= i
    # return result

    # if n == 0:
    #     return 1
    # return 


# def factorial(n: int) -> int:
#     """
#     Function that computes the factorial of a number.
#     The factorial of n is the product of all positive integers less than or equal to n.
#     :param n: The number to compute the factorial of
#     :return: The factorial of n
#     """
#     return None

def fibonacci(n: int) -> int:
    """
    Function that computes the nth Fibonacci number.
    :param n: The index of the Fibonacci number to compute
    :return: The nth Fibonacci number
    """
    return None


# def sum(n: int) -> int: # O(1); O(n); O(n^2); O(log n)
#     """
#     Function that computes the sum of all integers from 0 to n.
#     :param n: The number to compute the sum up to
#     :return: The sum of all integers from 0 to n
#     """
#     return None


def sum(n: int) -> int:
    """
    Function that computes the sum of all integers from 0 to n.
    :param n: The number to compute the sum up to
    :return: The sum of all integers from 0 to n
    """


    return 1 if n==1 else n+sum(n-1)


    # return n * (n + 1) // 2  # This is the O(1) solution


# def square(n: int) -> int:
#     """
#     Function that computes the square of a number.
#     :param n: The number to compute the square of
#     :return: The square of n
#     """
#     return None

def square(n: int) -> int:
    """
    Function that computes the square of a number.
    :param n: The number to compute the square of
    :return: The square of n
    """
    return n * n

    # return n**2



# def is_prime(n: int) -> bool:
#     """
#     Function that checks if a number is prime.
#     A prime number is a number that is divisible only by itself and 1.
#     :param n: The number to check
#     :return: True if the number is prime, False otherwise
#     """
#     return None


def is_prime(n: int) -> bool:
    """
    Function that checks if a number is prime.
    A prime number is a number that is divisible only by itself and 1.
    :param n: The number to check
    :return: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


