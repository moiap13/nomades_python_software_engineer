import random
import math

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """
    MAX_RANGE = 10
    optimal_tries = int(math.log(MAX_RANGE) / math.log(2))

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, MAX_RANGE)
    user_number = int(input("Enter a number : "))
    counter = 1

    while user_number != secret_number:
      counter += 1
      if user_number < secret_number:
            user_number = int(input("Sorry, your number is too low. Try again : "))
      else :
            user_number = int(input("Sorry, your number is too big. Try again : "))
    
    if counter <= optimal_tries:
        print(f"Very Well done, the correct number was {secret_number}. You guessed it in {counter} tries")
    else:
        print(f"Well done, the correct number was {secret_number}. You guessed it in {counter} tries")
        

if __name__ == '__main__':
    # Run the game
    guess_number()
