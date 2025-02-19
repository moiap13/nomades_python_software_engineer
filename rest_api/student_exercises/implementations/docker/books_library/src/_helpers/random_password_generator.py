import string
import random

MIN_SIZE_ACCEPTED = 4

def generate_password(
    uppercase: bool, 
    lowercase: bool, 
    digits: bool, 
    specials_char: bool, 
    length: int
) -> str:
  if length < MIN_SIZE_ACCEPTED:
    return "Length too short" 
    # raise ValueError("Length too short")
  
  assert length >= MIN_SIZE_ACCEPTED, f"{length} is lower than {MIN_SIZE_ACCEPTED}"
  password: list[str] = []
  all_chars: str = ""
  condition: bool = False

  if uppercase:
    condition = True
    all_chars += string.ascii_uppercase
    password += [random.choice(string.ascii_uppercase)]
  if lowercase:
    condition = True
    all_chars += string.ascii_lowercase
    password += [random.choice(string.ascii_lowercase)]
  if digits:
    condition = True
    all_chars += string.digits
    password += [random.choice(string.digits)]
  if specials_char:
    condition = True
    all_chars += string.punctuation
    password += [random.choice(string.punctuation)]

  if not condition:
    return "Please choose at least one option"
  
  password += random.choices(all_chars, k=length-len(password))
  random.shuffle(password)
  return "".join(password)

if __name__ == '__main__':
  print(generate_password(True, True, True, True, 40))