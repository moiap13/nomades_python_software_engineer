def generate_numbers():
    """
    Generate a list of numbers from 1 to 10.

    Returns:
        list: List of numbers from 1 to 10.
    """
    numbers = [x for x in range(1, 11)]
    return numbers

# Example: generate_numbers() -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def generate_squares():
    """
    Generate a list of squares of numbers from 1 to 10.

    Returns:
        list: List of squares of numbers from 1 to 10.
    """
    squares = [x ** 2 for x in range(1, 11)]
    return squares

# Example: generate_squares() -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def generate_even_numbers():
    """
    Generate a list of even numbers from 1 to 20.

    Returns:
        list: List of even numbers from 1 to 20.
    """
    even_numbers = [x for x in range(1, 21) if x % 2 == 0]
    return even_numbers

# Example: generate_even_numbers() -> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def generate_odd_numbers():
    """
    Generate a list of odd numbers from 1 to 20.

    Returns:
        list: List of odd numbers from 1 to 20.
    """
    odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
    return odd_numbers

# Example: generate_odd_numbers() -> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def generate_uppercase_letters():
    """
    Generate a list of uppercase letters from 'A' to 'Z'.

    Returns:
        list: List of uppercase letters from 'A' to 'Z'.
    """
    uppercase_letters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    return uppercase_letters

# Example: generate_uppercase_letters() -> ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generate_lowercase_letters():
    """
    Generate a list of lowercase letters from 'a' to 'z'.

    Returns:
        list: List of lowercase letters from 'a' to 'z'.
    """
    lowercase_letters = [chr(x) for x in range(ord('a'), ord('z')+1)]
    return lowercase_letters

# Example: generate_lowercase_letters() -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def generate_squared_even_numbers():
    """
    Generate a list of squared even numbers from 1 to 20.

    Returns:
        list: List of squared even numbers from 1 to 20.
    """
    squared_even_numbers = [x ** 2 for x in range(1, 21) if x % 2 == 0]
    return squared_even_numbers

# Example: generate_squared_even_numbers() -> [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


def generate_number_squares():
    """
    Generate a list of tuples containing numbers and their squares from 1 to 10.

    Returns:
        list: List of tuples containing numbers and their squares.
    """
    number_squares = [(x, x ** 2) for x in range(1, 11)]
    return number_squares

# Example: generate_number_squares() -> [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]


def capitalize_words(sentence):
    """
    Generate a list of strings with the first letter of each word capitalized from a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: List of words with the first letter capitalized.
    """
    capitalized_words = [word.capitalize() for word in sentence.split()]
    return capitalized_words

# Example: capitalize_words("hello world, how are you?") -> ['Hello', 'World,', 'How', 'Are', 'You?']


def generate_prime_numbers():
    """
    Generate a list of prime numbers from 1 to 50.

    Returns:
        list: List of prime numbers from 1 to 50.
    """
    prime_numbers = [x for x in range(2, 51) if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]
    return prime_numbers

# Example: generate_prime_numbers() -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def generate_divisible_by_3_or_5():
    """
    Generate a list of numbers that are divisible by 3 or 5 from 1 to 50.

    Returns:
        list: List of numbers divisible by 3 or 5 from 1 to 50.
    """
    divisible_by_3_or_5 = [x for x in range(1, 51) if x % 3 == 0 or x % 5 == 0]
    return divisible_by_3_or_5

# Example: generate_divisible_by_3_or_5() -> [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50]


def generate_even_squares_odd_cubes():
    """
    Generate a list of even squares and odd cubes from 1 to 10.

    Returns:
        list: List of even squares and odd cubes from 1 to 10.
    """
    even_squares_odd_cubes = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)]
    return even_squares_odd_cubes

# Example: generate_even_squares_odd_cubes() -> [1, 4, 27, 16, 125, 36, 343, 64, 729, 100]


def generate_word_lengths(sentence):
    """
    Generate a list of lengths of words in a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: List of word lengths.
    """
    word_lengths = [len(word) for word in sentence.split()]
    return word_lengths

# Example: generate_word_lengths("This is a sample sentence") -> [4, 2, 1, 6, 8]


def generate_numbers_excluding_multiples_of_3():
    """
    Generate a list of numbers from 1 to 10, excluding multiples of 3.

    Returns:
        list: List of numbers from 1 to 10, excluding multiples of 3.
    """
    numbers_excluding_multiples_of_3 = [x for x in range(1, 11) if x % 3 != 0]
    return numbers_excluding_multiples_of_3

# Example: generate_numbers_excluding_multiples_of_3() -> [1, 2, 4, 5, 7, 8, 10]


def generate_squares_of_even_numbers():
    """
    Generate a list of squares of numbers divisible by 2 from 1 to 10.

    Returns:
        list: List of squares of even numbers from 1 to 10.
    """
    squares_of_even_numbers = [x ** 2 for x in range(1, 11) if x % 2 == 0]
    return squares_of_even_numbers

# Example: generate_squares_of_even_numbers() -> [4, 16, 36, 64, 100]


def generate_vowels(word):
    """
    Generate a list of vowels present in a given word.

    Args:
        word (str): The input word.

    Returns:
        list: List of vowels present in the word.
    """
    vowels = [char for char in word if char in 'aeiou']
    return vowels

# Example: generate_vowels("hello") -> ['e', 'o']


def generate_numbers_repeated():
    """
    Generate a list of numbers from 1 to 10, but with each number repeated twice.

    Returns:
        list: List of numbers from 1 to 10 repeated twice.
    """
    numbers_repeated = [x for x in range(1, 11) for _ in range(2)]
    return numbers_repeated

# Example: generate_numbers_repeated() -> [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]


def generate_squares_excluding_multiples_of_3():
    """
    Generate a list of squares of numbers from 1 to 10, but exclude squares divisible by 3.

    Returns:
        list: List of squares of numbers from 1 to 10, excluding squares divisible by 3.
    """
    squares_excluding_multiples_of_3 = [x ** 2 for x in range(1, 11) if (x ** 2) % 3 != 0]
    return squares_excluding_multiples_of_3

# Example: generate_squares_excluding_multiples_of_3() -> [1, 4, 16, 25, 49, 64, 100]


def generate_uppercase_consonants(string):
    """
    Generate a list of uppercase consonants from a given string, excluding vowels.

    Args:
        string (str): The input string.

    Returns:
        list: List of uppercase consonants from the string.
    """
    import string as str
    all_alpha = str.ascii_letters
    uppercase_consonants = [char.upper() for char in string if char in all_alpha and char not in 'aeiouAEIOU']
    return uppercase_consonants

# Example: generate_uppercase_consonants("Hello, World!") -> ['H', 'L', 'L', 'W', 'R', 'L', 'D']


def generate_even_numbers_in_range(start, end):
    """
    Generate a list of even numbers between two given numbers.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.

    Returns:
        list: List of even numbers between the given range (inclusive).
    """
    even_numbers_in_range = [x for x in range(start, end + 1) if x % 2 == 0]
    return even_numbers_in_range

# Example: generate_even_numbers_in_range(5, 15) -> [6, 8, 10, 12, 14]


# You can call the functions or write additional code here to test them

################# Object Parts #################
from users import persons

def get_firstnames():
    """
    Generate a list of first names of all users.

    Returns:
        list: List of first names of all users.
    """
    firstnames = [person['name'].split()[0] for person in persons]
    return firstnames

def get_lastnames():
    """
    Generate a list of last names of all users.

    Returns:
        list: List of last names of all users.
    """
    lastnames = [person['name'].split()[1] for person in persons]
    return lastnames