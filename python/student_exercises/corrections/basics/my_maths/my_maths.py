def is_even(number: int) -> str:
    """
    Function that checks if a number is even or odd.
    Return the string "The number is even" if the number is even, "The number is odd" otherwise.
    params:
      number: The number to check
    
    Returns:
      A string that says if the number is even or odd
    """
    # if number % 2 == 0: # Even number
    #     return "The number is even"
    # else: # Odd number
    #     return "The number is odd" 
    
    # if number % 2 == 0: # Even number
    #     return "The number is even"

    # return "The number is odd"

    return "The number is even" if number%2==0 else "The number is odd"

def factorial(n: int) -> int:
    """
    Function that computes the factorial of a number.
    The factorial of n is the product of all positive integers less than or equal to n.
    :param n: The number to compute the factorial of
    :return: The factorial of n
    """
    # result = 1
    # for number in range(1, n+1):
    #     result = result * number
    # return result
    if n < 0:
        return -1
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)
    

    

def fibonacci(n: int) -> int: # O(2^n)
    """
    Function that computes the nth Fibonacci number.
    :param n: The index of the Fibonacci number to compute
    :return: The nth Fibonacci number
    """
    # if n == 0 or n == 1:
    #     return n

    # a = 0
    # b = 1
    # for _ in range(1, n):
    #     c = a + b
    #     a = b
    #     b = c
    
    # return c

    if n == 0 or n == 1:                    # 0(1)
        return n                            # 0(1)
    return fibonacci(n-1) + fibonacci(n-2)  # O(2*O(fibonnaci))
        


def sum(n: int) -> int: # O(n); O(1)
    """
    Function that computes the sum of all integers from 0 to n.
    :param n: The number to compute the sum up to
    :return: The sum of all integers from 0 to n
    """
    # sum_ = 0                # O(1)
    # for i in range(1, n+1): # O(n)
    #     sum_ += i             # O(1)
    # return sum_             # O(1)

    return (n*(n+1))/2        # O(1)

def square(n: int) -> int:
    """
    Function that computes the square of a number.
    :param n: The number to compute the square of
    :return: The square of n
    """
    return pow(n, 2)



def is_prime(n: int) -> bool: # O(n); O(sqrt(n))
    """
    Function that checks if a number is prime.
    A prime number is a number that is divisible only by itself and 1.
    :param n: The number to check
    :return: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True