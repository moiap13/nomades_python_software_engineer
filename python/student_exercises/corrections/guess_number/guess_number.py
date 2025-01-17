import random
import math

MAX_RANGE = 100
def guess_number() -> None:
    """
    Function that generates a random number between 1 and 100 and asks the user to guess it.
    :return: None
    """
    # for dychtomy optimal search, the formula is the following: log2(100)

    # Generate a random number between 1 and 100
    secret_number: int = random.randint(1, MAX_RANGE)
    # selected_number: int = -1
    optimal_tries: int = math.floor(math.log2(MAX_RANGE))
    selected_number: int = int(input("enter a number: "))
    tries: int = 1
    print("you chose the number :", selected_number)

    while secret_number != selected_number:  
        if selected_number < secret_number:
            print("the secret number is higher")
        elif selected_number > secret_number:
            print("the secret number is lower")
        
        selected_number = int(input("enter a number: "))
        print("you chose the number :", selected_number)
        tries += 1
        
    # We found the secret number
    print(f"{'Bravo, y' if tries <= optimal_tries else 'Y'}ou found the secret number in {tries} {'tries' if tries > 1 else 'try'}")

if __name__ == '__main__':
    # Run the game
    guess_number()
