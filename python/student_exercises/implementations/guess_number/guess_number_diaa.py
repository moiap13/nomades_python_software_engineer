import random

MAX_RANGE = 100

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, MAX_RANGE)

    while True:
        # Ask the user for a number
        user_guess = int(input(f"Guess a number between 1 and {MAX_RANGE}: "))

        # Check if the user's number is equal to the secret number
        if user_guess < secret_number:
            print("The secret number is higher.")
        elif user_guess > secret_number:
            print("The secret number is lower.")
        else:
            print("Bravo! You've guessed the correct number!")
            break

if __name__ == '__main__':
    # Run the game
    guess_number()
