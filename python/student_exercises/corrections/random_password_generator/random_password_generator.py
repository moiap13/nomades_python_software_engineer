import string
import random

def generate_password(
    uppercase: bool, 
    lowercase: bool, 
    digits: bool, 
    specials_char: bool, 
    length: int
) -> str:
  if length < 4:
    return "Please enter a length bigger than 3"

  pwd: str = ""
  population: str = ""
  counter: int = 0

  if uppercase:
    pwd += random.choice(string.ascii_uppercase)
    population += string.ascii_uppercase
    counter += 1
  if lowercase:
    pwd += random.choice(string.ascii_lowercase)
    population += string.ascii_lowercase
    counter += 1
  if digits:
    pwd += random.choice(string.digits)
    population += string.digits
    counter += 1
  if specials_char:
    pwd += random.choice(string.punctuation)
    population += string.punctuation
    counter += 1

  if counter == 0:
    return "Please choose at least one population"

  remaining: str = "".join(random.choices(population, k=int(length)-len(pwd)))
  pwd += remaining

  pwd_l: list[str] = list(pwd)
  random.shuffle(pwd_l)
  return "".join(pwd_l)

if __name__ == '__main__':
  print(generate_password(True, True, False, False, 12))