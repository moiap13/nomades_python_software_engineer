import random
import math

MAX_RANGE = 100
def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, MAX_RANGE)
    print(secret_number)

    # TODO: ask user for a number unisng `input` function /!\ hint don't forget to convert the result of input as int
    # TODO: check if user number is equal to secret number, if not display "The secret number is higher" or "The secret number is lower" accordingly

    # to ask user to enter the number use the function input
    print("bravo")

if __name__ == '__main__':
    # Run the game
    guess_number()
