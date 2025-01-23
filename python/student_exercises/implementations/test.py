def square(x: int) -> int:
    """
    Function used to square a number

    Params:
      x (int): integer to be squared
    Return:
      int: the square value of x
    """
    return x**2

def main():
    x = int(input("Enter a number: "))
    print(square)

if __name__ == '__main__':
    main()
