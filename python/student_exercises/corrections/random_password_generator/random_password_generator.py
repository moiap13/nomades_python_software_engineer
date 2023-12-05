import random
import string

"""
Write a Python program that genrate a random password.
Your random password need to contains at least:
  - 1 upper char
  - 1 lower char
  - 1 digit
  - 1 special char

Also your password needs to be at least 8 char long
"""

def generate_random_password(length=12):
    # Define the character sets to build the password
    if length < 8:
        raise ValueError
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # requirements = [lowercase_letters, uppercase_letters, digits, special_chars]
    # a = []
    # random.shuffle(requirements)
    # for _ in range(length):
    #     while len(a) < length:
    #         for i in requirements:
    #             char = random.choice(i)
    #             a.append(char)
    #             random.shuffle(a)
    # return "".join(a)
    
    # Combine the character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate the random password
    password = random.sample(lowercase_letters, 1) + \
               random.sample(uppercase_letters, 1) + \
               random.sample(digits, 1) + \
               random.sample(special_chars, 1) + \
               random.sample(all_chars, length - 4)

    # Shuffle the password characters
    random.shuffle(password)

    # Convert the list of characters into a string
    password = ''.join(password)

    return password

# Example usage
password = generate_random_password(16)
print("Random Password:", password)
