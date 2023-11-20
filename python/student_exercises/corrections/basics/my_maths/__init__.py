def is_prime(n: int) -> bool:
    """
    Function that checks if a number is prime.
    A prime number is a number that is divisible only by itself and 1.
    :param n: The number to check
    :return: True if the number is prime, False otherwise
    """
    if n == 1 or n < 1:
        return False

    for num in range(2, int(n**0.5)+1):
        if n%num == 0:
            return False
    
    return True

print("hello from __file__")