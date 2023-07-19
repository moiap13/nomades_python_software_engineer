def generate_numbers():
    """
    Generate a list of numbers from 1 to 10.

    Returns:
        list: List of numbers from 1 to 10.
    """
    return [x for x in range(1,11)]
    #return list(range(1, 11))

# Example: generate_numbers() -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def generate_squares():
    """
    Generate a list of squares of numbers from 1 to 10.

    Returns:
        list: List of squares of numbers from 1 to 10.
    """
    return [x*x for x in range(1,11)]

# Example: generate_squares() -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def generate_even_numbers():
    """
    Generate a list of even numbers from 1 to 20.

    Returns:
        list: List of even numbers from 1 to 20.
    """
    return [x for x in range(1, 21) if x%2 == 0]

# Example: generate_even_numbers() -> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def generate_odd_numbers():
    """
    Generate a list of odd numbers from 1 to 20.

    Returns:
        list: List of odd numbers from 1 to 20.
    """
    return [x for x in range(1, 20) if x%2 == 1]

# Example: generate_odd_numbers() -> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def generate_uppercase_letters():
    """
    Generate a list of uppercase letters from 'A' to 'Z'.

    Returns:
        list: List of uppercase letters from 'A' to 'Z'.
    """
    import string
    return [chr(x) for x in range(ord('A'), ord('Z')+1)]
    return [letter.upper() for letter in string.ascii_lowercase]

# Example: generate_uppercase_letters() -> ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generate_lowercase_letters():
    """
    Generate a list of lowercase letters from 'a' to 'z'.

    Returns:
        list: List of lowercase letters from 'a' to 'z'.
    """
    return [chr(x) for x in range(ord('a'), ord('z')+1)]

# Example: generate_lowercase_letters() -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def generate_squared_even_numbers():
    """
    Generate a list of squared even numbers from 1 to 20.

    Returns:
        list: List of squared even numbers from 1 to 20.
    """
    return [x**2 for x in range(1, 21) if x%2==0]

# Example: generate_squared_even_numbers() -> [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


def generate_number_squares():
    """
    Generate a list of tuples containing numbers and their squares from 1 to 10.

    Returns:
        list: List of tuples containing numbers and their squares.
    """
    return [(x, x**2) for x in range(1, 11)]

# Example: generate_number_squares() -> [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]


def capitalize_words(sentence):
    """
    Generate a list of strings with the first letter of each word capitalized from a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: List of words with the first letter capitalized.
    """
    return [w.capitalize() for w in sentence.split()]

# Example: capitalize_words("hello world, how are you?") -> ['Hello', 'World,', 'How', 'Are', 'You?']


def generate_prime_numbers():
    """
    Generate a list of prime numbers from 1 to 50.

    Returns:
        list: List of prime numbers from 1 to 50.
    """
    l = []
    for x in range(2, 51):
        la = [x % i != 0 for i in range(2, int(x **0.5)+1)]
        print(la)
        
        a = all(la)
        if a:
          l.append(x)
    return l
    #return [x for x in range(2, 51) if all([x % i != 0 for i in range(2, int(x **0.5)+1)])]

# Example: generate_prime_numbers() -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def generate_divisible_by_3_or_5():
    """
    Generate a list of numbers that are divisible by 3 or 5 from 1 to 50.

    Returns:
        list: List of numbers divisible by 3 or 5 from 1 to 50.
    """
    l = [x for x in range(1, 51) if x%3==0 or x%5==0]
    print(l)
    return l

# Example: generate_divisible_by_3_or_5() -> [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50]


def generate_even_squares_odd_cubes():
    """
    Generate a list of even squares and odd cubes from 1 to 10.

    Returns:
        list: List of even squares and odd cubes from 1 to 10.
    """
    return [(x**2 if x%2==0 else x**3) for x in range(1,11)]

# Example: generate_even_squares_odd_cubes() -> [1, 4, 27, 16, 125, 36, 343, 64, 729, 100]


def generate_word_lengths(sentence):
    """
    Generate a list of lengths of words in a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: List of word lengths.
    """
    return [len(x) for x in sentence.split()]

# Example: generate_word_lengths("This is a sample sentence") -> [4, 2, 1, 6, 8]


def generate_numbers_excluding_multiples_of_3():
    """
    Generate a list of numbers from 1 to 10, excluding multiples of 3.

    Returns:
        list: List of numbers from 1 to 10, excluding multiples of 3.
    """
    return [x for x in range(1, 11) if not x%3==0]

# Example: generate_numbers_excluding_multiples_of_3() -> [1, 2, 4, 5, 7, 8, 10]


def generate_squares_of_even_numbers():
    """
    Generate a list of squares of numbers divisible by 2 from 1 to 10.

    Returns:
        list: List of squares of even numbers from 1 to 10.
    """
    return [x**2 for x in range(1,11) if x%2==0]

# Example: generate_squares_of_even_numbers() -> [4, 16, 36, 64, 100]


def generate_vowels(word):
    """
    Generate a list of vowels present in a given word.

    Args:
        word (str): The input word.

    Returns:
        list: List of vowels present in the word.
    """
    return [w for w in word if w in 'aeiouy']

# Example: generate_vowels("hello") -> ['e', 'o']

def generate_consonnes(word):
    """
    Generate a list of vowels present in a given word.

    Args:
        word (str): The input word.

    Returns:
        list: List of vowels present in the word.
    """
    return [w for w in word if w not in 'aeiouy']

# Example: generate_vowels("hello") -> ['e', 'o']


def generate_numbers_repeated():
    """
    Generate a list of numbers from 1 to 10, but with each number repeated twice.

    Returns:
        list: List of numbers from 1 to 10 repeated twice.
    """
    return [x for x in range(1,11) for _ in range(2)]

# Example: generate_numbers_repeated() -> [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]


def generate_squares_excluding_multiples_of_3():
    """
    Generate a list of squares of numbers from 1 to 10, but exclude squares divisible by 3.

    Returns:
        list: List of squares of numbers from 1 to 10, excluding squares divisible by 3.
    """
    return [x*x for x in range(1, 11) if not x%3==0]

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
    return [w.upper() for w in string if w not in 'aeiouyAEIOUY' if w in str.ascii_letters]

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
    return [x for x in range(start, end+1) if x%2==0]

# Example: generate_even_numbers_in_range(5, 15) -> [6, 8, 10, 12, 14]