
def exercice_1(fruits, numbers):
    fruits_upper_simple = [fruit.upper() for fruit in fruits]
    print(fruits_upper_simple)

def exercice_2(fruits, numbers):
    # ['Mango', 'Kiwi', 'Strawberry', etc...]
    fruits_upper_capitalized = [fruit.capitalize() for fruit in fruits]
    fruits_upper_capitalized = [fruit[0].upper() + fruit[1:] for fruit in fruits]
    print(fruits_upper_capitalized)

def exercice_3(fruits, numbers):
    # make a list that contains each fruit with more than 5 characters
    fruits_longer_than_5 = [fruit for fruit in fruits if len(fruit) >= 5]
    print(fruits_longer_than_5)

def exercice_4(fruits, numbers):
    # make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
    char_count_lst =[len(fruit) for fruit in fruits]
    print(char_count_lst)

def exercice_5(fruits, numbers):
    # Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
    with_a = [fruit for fruit in fruits if("a" in fruit)]
    print(with_a)

def exercice_6(fruits, numbers):
    # [operation - declaration - collection - condition]
    even_numbers_plus_1 = [x + 1 for x in numbers if x %2 == 0]
    print(even_numbers_plus_1)

def exercice_7(fruits, numbers):
    # Make a variable named positive_numbers that holds only the positive numbers, 0 included
    only_positive = [number for number in numbers if number >= 0]
    print(only_positive)


if __name__ == '__main__':
    
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

    exercice_1(fruits, numbers)
    exercice_2(fruits, numbers)
    exercice_3(fruits, numbers)
    exercice_4(fruits, numbers)
    exercice_5(fruits, numbers)
    exercice_6(fruits, numbers)
    exercice_7(fruits, numbers)







