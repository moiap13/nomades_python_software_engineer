import random

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

if __name__ == '__main__':
    # Run the game
    guess_number()
