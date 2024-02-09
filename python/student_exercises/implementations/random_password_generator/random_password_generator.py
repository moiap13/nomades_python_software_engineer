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
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    print((lowercase_letters[0]))

# Example usage
password = generate_random_password()
print("Random Password:", password)
