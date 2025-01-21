import string
import random

def generate_password(
    is_uppercase: bool, 
    is_lowercase: bool, 
    is_digits: bool, 
    is_specials_char: bool, 
    length: int
) -> str:
  if length < 4:
    return "Please enter a password length >= 4"

  pwd: str = ''
  population: str = ''

  if is_uppercase:
    pwd += random.choice(string.ascii_uppercase)
    population += string.ascii_uppercase

  if is_lowercase:
    pwd += random.choice(string.ascii_lowercase)
    population += string.ascii_lowercase

  if is_digits:
    pwd += random.choice(string.digits)
    population += string.digits

  if is_specials_char:
    pwd += random.choice(string.punctuation)
    population += string.punctuation
  
  if not pwd:
    return 'Please choose at least one population' 

  remaining: str = "".join(random.choices(population, k=length-len(pwd)))
  pwd += remaining
  
  pwd_list: list[str] = list(pwd)
  random.shuffle(pwd_list)
  return "".join(pwd_list)

if __name__ == '__main__':
  print(generate_password(True, True, False, False, 12))