def add(a: int, b: int):
    """
    Function that returns the sum of two numbers
    :param a: the first number
    :param b: the second number
    :return: the sum of the two numbers
    """
    return a+b


def sub(a, b):
    """
    Function that returns the subtraction of two numbers
    :param a: the first number
    :param b: the second number
    :return: the subtraction of the two numbers
    """
    return a-b


def mul(a, b):
    """
    Function that returns the multiplication of two numbers
    :param a: the first number
    :param b: the second number
    :return: the multiplication of the two numbers
    """
    return a * b


def div(a, b):
    """
    Function that returns the division of two numbers
    :param a: the first number
    :param b: the second number
    :return: the division of the two numbers
    :raises ZeroDivisionError: if the second number is zero
    """
    if b == 0:
        raise ZeroDivisionError('Division by zero')
    
    return a / b

print("NAME", __name__)

if __name__ == "__main__": 
    # this mean that i'm executing the python file
    number1 = int(input("Enter number 1 "))
    number2 = input("Enter number 2 ")

    result = mul(number1, (number2))

    print(f"Number1: {number1} * Number2 {(number2)} = {result}")


print("hello from outside if")