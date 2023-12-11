def say_hello() -> None:
    """
    function that say hello
    """
    print("Hello from callee.py! 0")
  
def say_hello_2():
    print("Hello from callee.py! 1")
    
# Check if callee.py is executed as the main program
if __name__ == '__main__':
    say_hello()
    print("__name__", __name__)