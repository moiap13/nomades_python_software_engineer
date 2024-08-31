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

def generate_random_password(length: int = 12) -> str:
    # Define the character sets to build the password
    if length < 8:
        raise ValueError("Password must be at least 8 chars")

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + special_chars

    password: list[str] = [    
      random.choice(lowercase_letters),
      random.choice(uppercase_letters),
      random.choice(digits),
      random.choice(special_chars)
    ]

    #  password += random.choices(all_characters, k=length-4)

    for _ in range(length-4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return ''.join(password)


password = generate_random_password(10)
print("Random Password:", password)
