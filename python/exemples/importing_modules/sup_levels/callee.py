def say_hello():
    print("Hello from callee.py!")


# Check if callee.py is executed as the main program
if __name__ == '__main__':
    say_hello()