def say_hello():
    print("Hello from callee.py!")

def say_hello2():
    print("Hello from callee.py 2!")

def say_hello3():
    print("Hello from callee.py 3!")


# Check if callee.py is executed as the main program
if __name__ == '__main__':
    say_hello()
