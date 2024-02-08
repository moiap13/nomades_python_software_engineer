import random
import math

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """

    # Generate a random number between 1 and 100
    secret_number: int = random.randint(1, 100)
    print(secret_number)
    user_number: int = int(input("Enter a number : "))

    while user_number != secret_number:
      # si je suis dans le while, j'ai pas trouvé le nombre secret
      if user_number > secret_number:
        print("The secret number is lower")
      else:
        print("Secret number is higher")

      user_number = int(input("Enter a number : ")) 

    # si je suis APRES le while, j'ai trouvé le nombre secret
    print("Bravo, you found the secret number")

if __name__ == '__main__':
    # Run the game
    guess_number()
