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
    input_number = None

    while input_number != secret_number:
        input_string = input("Guess the number\n")
        input_number = int(input_string)
        if input_number > secret_number:
            print("Secret number is lower")
        elif input_number < secret_number:
            print("Secret number is higher")

    print("Bravo")
    
    # for _ in range(100):
    #     entry_number=int(input("please enter the number:"))
    #     if entry_number< secret_number:
    #          print("the number is higher")
    #     elif entry_number>secret_number:
    #         print("the number is lower")
    #     else:
    #         print("the number",secret_number,"is correct")
    #         break
        
    
if __name__ == '__main__':
    #Run the game
    guess_number()
