

def exercice_1(string, numbers):
    """ find all the numbers divisible by 8 """
    res = [number for number in numbers if number % 8 == 0]
    print(res)

def exercice_2(string, numbers):
    """ find the numbers that contain the digit 6 in them """
    res = [number for number in numbers if '6' in str(number)]
    print(res)

def exercice_3(string, numbers):
    """ count the number of spaces in a sentence (without using .count()) """
    space_list = [s for s in string if s == " "]
    res = len(space_list)
    print(res)

def exercice_4(string, numbers):
    """ recreate a new string without the vowels """
    voyelles = ["A","E", "I", "O", "U","Y"]
    res = "".join([char for char in string if char.upper() not in voyelles])
    print(res)

def exercice_5(string, numbers):
    """ create a list of words that have less than 6 letters in them """
    words = string.split(' ')
    res = [word for word in words if len(word) < 6]
    print(res)

def exercice_6(string, numbers):
    """ create a dictionary from words in the sentence. For keys, use the word. For value, use the length of the word. """
    words = string.split(' ')
    res ={word : len(word) for word in words}
    print(res)

def exercice_7(string, numbers):
    """ make a list of numbers that are divisible by any digit beside 1 """
    divisors = [x for x in range(2, 10)]
    res = [n for n in numbers if True in [n % x == 0 for x in divisors]]
    print(res)

def exercice_8(string, numbers):
    """ meme exercice, mais stocker dans la dictionnaire le plus grand divieur possible. """
    # res = {n : max([d for d in divisors if n % d == 0]) for n in numbers}

    # EXPLIQUE:

    divisors = [x for x in range(1, 10)] # 0. on cree les diviseurs en amont (chiffres 1, 2, 3, 4, 5, 6, 7, 8, 9)
    res = {
        n : max( # 4. on prend celui qui est le plus grand (avec la fonction max())
            [d for d in divisors if n % d == 0] # 3. quels sont les diviseurs pour chaque n?
        ) 
        for n # 2. on les nomme n...
        in numbers # 1. on parcourt tous les nombres...
    }
    print(res)

def exercice_9(string, numbers):
    """ get the numbers whose cube is even. Then, if that number contains a 2, save it. Otherwise None """
    # positiveResult if condition == True else negativeResult

    # ==

    # if condition == True:
    #     return positiveResult
    # else:
    #     return negativeResult

    res = [(str(number) if '2' in str(number) else None) for number in numbers if (number ** 3) % 2 == 0]
    print(res)

def exercice_10(string, numbers):
    """ take the words, create a dictionary that holds the word as key, and whether the number of letters is odd or even. """
    words = string.split(" ")
    res = {word : ("even" if len(word) % 2 == 0 else "odd") for word in words}
    print(res)


if __name__ == '__main__':
    string = "Nous faisons le cours de Python a Nomades"
    numbers = [x for x in range(1001)]

    exercice_1(string, numbers)
    exercice_2(string, numbers)
    exercice_3(string, numbers)
    exercice_4(string, numbers)
    exercice_5(string, numbers)
    exercice_6(string, numbers)
    exercice_7(string, numbers)
    exercice_8(string, numbers)
    exercice_9(string, numbers)
    exercice_10(string, numbers)