from random import randint
import math

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """

    # Generate a random number between 1 and 100
    secret_number = randint(1, 100)
    user_number = (input("Enter a number : "))
    
    while secret_number != user_number:
      # the user didn't guess the number
      if user_number > secret_number:
        print("The guess number is lower")
      else:
        print("The guess number is higher")
    
      user_number = int(input("Enter a number : "))
      
    # assert that the user guessed the number
    print("bravo you find the number")
        
    

if __name__ == '__main__':
    # Run the game
    guess_number()
