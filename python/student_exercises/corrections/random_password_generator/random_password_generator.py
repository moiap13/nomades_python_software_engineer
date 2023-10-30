import random
import string

def generate_random_password(length=12):
    # Define the character sets to build the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

password = generate_random_password()
print("Random Password:", password)
