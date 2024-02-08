import random
import math

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """
    MAX_RANGE = 100

    # Generate a random number between 1 and 100
    secret_number: int = random.randint(1, MAX_RANGE)
    optimal_tries = math.ceil(math.log2(MAX_RANGE))
    print(secret_number)

    user_number: int = int(input("Enter a number : "))
    tries = 1

    while user_number != secret_number:
      # si je suis dans le while, j'ai pas trouvé le nombre secret
      if user_number > secret_number:
        print("The secret number is lower")
      else:
        print("Secret number is higher")

      user_number = int(input("Enter a number : ")) 
      tries += 1 # tries = tries + 1

    # si je suis APRES le while, j'ai trouvé le nombre secret
    print(f"{'Bravo, y' if tries <= optimal_tries else 'Y'}ou found the secret number in {tries} {'try' if tries == 1 else 'tries'}")

if __name__ == '__main__':
    # Run the game
    guess_number()
