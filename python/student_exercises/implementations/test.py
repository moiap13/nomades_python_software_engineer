def square(x: int) -> int:
    return x**2

def double(x: int) -> int:
    return 2*x

def main():
    x = int(input("Enter a number: "))
    print(square(x))

if __name__ == '__main__':
    main()
