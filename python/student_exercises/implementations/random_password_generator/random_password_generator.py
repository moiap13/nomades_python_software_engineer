import random
import string

def generate_random_password(length=12):
    # Define the character sets to build the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine the character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Ensure the desired length is within range
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    # Generate the random password
    # Shuffle the password characters
    # Convert the list of characters into a string
    password = ""
    return password

# Example usage
password = generate_random_password()
print("Random Password:", password)
