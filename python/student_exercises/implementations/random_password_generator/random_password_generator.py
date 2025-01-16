import string
import random

def generate_password(
    uppercase: bool, 
    lowercase: bool, 
    digits: bool, 
    specials_char: bool, 
    length: int
) -> str:
  # TODO: Generate a random password
  # TODO: test if the password legth greater than 4
  print(random.choices(string.ascii_uppercase, k=23))
  print(uppercase)
  print(lowercase)
  print(digits)
  print(specials_char)
  print(length)

  return "None"

if __name__ == '__main__':
  print(generate_password(True, True, True, False, 4))