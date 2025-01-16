import random
import math

MAX_NUMBER = 100

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """
    # for dychtomy optimal search, the formula is the following: math.log2(MAX_NUMBER)

    # Generate a random number between 1 and 100
    secret_number: int = random.randint(1, MAX_NUMBER)
    print(secret_number)
    
    # hint 
    num: int = int(input("Enter a number: "))
    num_guess: int = 1

    while num !=secret_number :
        if num > secret_number:
            print("The guess number is lower")
        elif num < secret_number:
            print("The guess number is higher")
        
        num = int(input("Enter a number: "))
        num_guess += 1


    # WE FOUND THE NUMBER
    print("You find it")
    upper_bound: float = math.log2(MAX_NUMBER)
    if num_guess == 1: print("you are very lucky")
    elif num_guess > upper_bound: print("you are not optimal")
    elif num_guess < upper_bound: print("you are optimal")

if __name__ == '__main__':
    # Run the game
    guess_number()
