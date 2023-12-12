from random import randint
import math

def ask_user_number() -> int:
  while True:
    try:
      user_input = int(input("Enter a number : "))
      if not 1 <= user_input <= 100:
        raise ValueError("Please enter a value in the range 1, 100")
    except ValueError as err:
      print(err)
    else:
      return user_input
   

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """

    # Generate a random number between 1 and 100
    secret_number = randint(1, 100)
    user_number = ask_user_number()
       
    
    while secret_number != user_number:
      # the user didn't guess the number
      if user_number > secret_number:
        print("The guess number is lower")
      else:
        print("The guess number is higher")
    
      user_number = ask_user_number()
      
    # assert that the user guessed the number
    print("bravo you find the number")
        
    

if __name__ == '__main__':
    # Run the game
    guess_number()
