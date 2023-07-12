import random
import math

def guess_number():
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 10)
    a = None

    while a != secret_number:
        a = int(input("Select your number:"))
        if a < secret_number:
            print("Failed, you are under")
        elif a > secret_number:
            print("Failed, you are above")
    else:
        print("You won")

def guess_number_axel():
    guess = True
    while guess:
        number_total = int( input("Nombre maximum :"))
    
        secret_number = random.randint(1, number_total)
        # Log
        number_entrie = math.ceil(math.log(number_total)/math.log(2))
        
        i = 1
        a = None
        tries = 0
        #for i in range(1,number_entrie+1):
        while (i <= (number_entrie)) and (a != secret_number):
            a = int(input("Select your number:"))
            
            if a < secret_number:
                print("Failed, you are under")
            elif a > secret_number:
                print("Failed, you are above")
            # elif a == secret_number:
            #     print("ok")
            i += 1
            tries += 1
        
        if i > (number_entrie):
            print(f"You lost you made {tries} wrong tries and the optimal guessing tries was : {number_entrie}")
        else:
            print(f"You win ! you made {tries} right tries and the optimal guessing tries was : {number_entrie}")
        
        guess = int(input("Do you want to play again ? [1, 0]"))
    

if __name__ == '__main__':
    # Run the game
    # guess_number()
    guess_number_axel()
