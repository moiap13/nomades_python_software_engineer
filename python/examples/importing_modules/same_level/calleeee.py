def say_hello(): # doc-string
    """
    function that says hello
    """
    print(f"Hello from callee.py!")

def say_hello2():
    """
    say hello 2 is the updated function of say hello
    """
    print(f"Hello from callee.py!")

print(__name__)

if __name__ == "__main__":
  print("Calle called")