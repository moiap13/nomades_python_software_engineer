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
    optimal_guesses: int = math.ceil(math.log2(MAX_RANGE))
    tries = 1
    user_guess = int(input("A number has been generated, let's guesse it: "))
    while user_guess != secret_number:
        if user_guess > secret_number:
            user_guess = int(input("Go lower \nNext guess: "))
        elif user_guess < secret_number:
            user_guess = int(input("Go higher \nNext guess: "))
        
        tries += 1

    # At this point we found the secret number
    
    # to ask user to enter the number use the function input

    print(f"{'Bravo, y' if tries <= optimal_guesses else 'Y'}ou guessed it in {tries} tries")

if __name__ == '__main__':
    # Run the game
    guess_number()
