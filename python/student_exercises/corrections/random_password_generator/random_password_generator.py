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
    if length < 8:
       return None
    # Define the character sets to build the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    rand0 = random.choice(digits)
    rand1 = random.choice(uppercase_letters)
    rand2 = random.choice(lowercase_letters)
    rand3 = random.choice(special_chars)

    t = list(rand0+rand1+rand2+rand3 + "".join(random.sample(all_chars, length-4)))
    random.shuffle(t)
    return "".join(t)

# def gen_rdm_ord(l=12):
#   basic = [1,2,3,4]
#   order = [random.randint(1,4) for x in range(l)]

#   if not set(basic).issubset(order):
#     return gen_rdm_ord(len)
  
#   return order

# Example usage
password = generate_random_password()
print("Random Password:", password)
