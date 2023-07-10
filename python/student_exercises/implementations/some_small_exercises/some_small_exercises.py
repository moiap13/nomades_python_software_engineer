import datetime

# Code Generator
def encode_message(message, secret_key):
    encoded_message = ""
    for char in message:
        encoded_char = chr(ord(char) + secret_key)
        encoded_message += encoded_char
    return encoded_message

def decode_message(encoded_message, secret_key):
    decoded_message = ""
    for char in encoded_message:
        decoded_char = chr(ord(char) - secret_key)
        decoded_message += decoded_char
    return decoded_message

# Countdown Calculator
def calculate_time_difference(start_date, end_date):
    time_difference = end_date - start_date
    return time_difference

# Sorting Method
def custom_sort(lst):
    sorted_lst = []
    while lst:
        min_value = lst[0]
        for num in lst:
            if num < min_value:
                min_value = num
        sorted_lst.append(min_value)
        lst.remove(min_value)
    return sorted_lst

# Interactive Quiz
def avenger_quiz():
    questions = [
        "1. What is your favorite color?",
        "2. What is your preferred superpower?",
        "3. What is your ideal vacation destination?"
    ]
    answers = []

    for question in questions:
        print(question)
        answer = input("Your answer: ")
        answers.append(answer)

    # Perform calculation or recommendation based on answers
    result = "Iron Man"  # Placeholder result, replace with actual calculation

    print("Congratulations! You are", result)

# Tic-Tac-Toe by Text
def print_board(board):
    for row in board:
        print(" ".join(row))

def play_tic_tac_toe():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    player = "X"

    while True:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Invalid move. Try again.")
            continue

        # Check for winning condition or draw
        # Code for checking winning condition goes here

        # Switch player
        player = "O" if player == "X" else "X"

# Temperature/Measurement Converter
def convert_temperature():
    while True:
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print("Temperature in Celsius:", celsius)
        elif choice == 2:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print("Temperature in Fahrenheit:", fahrenheit)
        else:
            print("Invalid choice. Try again.")
            continue

        break

# Counter App
import tkinter as tk

def increment_counter():
    counter.set(counter.get() + 1)

window = tk.Tk()
window.title("Counter App")

counter = tk.IntVar()
counter.set(0)

label = tk.Label(window, textvariable=counter, font=("Arial", 24))
label.pack(padx=20, pady=20)

button = tk.Button(window, text="Click to Count", command=increment_counter)
button.pack(padx=20, pady=10)

window.mainloop()

# Alarm Clock
import time

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            break
        time.sleep(1)

# Main program
def main():
    while True:
        print("1. Code Generator")
        print("2. Countdown Calculator")
        print("3. Sorting Method")
        print("4. Interactive Quiz")
        print("5. Tic-Tac-Toe by Text")
        print("6. Temperature/Measurement Converter")
        print("7. Counter App")
        print("8. Number Guessing Game")
        print("9. Alarm Clock")

        choice = int(input("Enter your choice (1-9): "))

        if choice == 1:
            message = input("Enter the message: ")
            key = int(input("Enter the secret key: "))
            encoded_message = encode_message(message, key)
            print("Encoded message:", encoded_message)
            decoded_message = decode_message(encoded_message, key)
            print("Decoded message:", decoded_message)
        elif choice == 2:
            start_date = datetime.datetime.strptime(input("Enter the start date (YYYY-MM-DD): "), "%Y-%m-%d")
            end_date = datetime.datetime.strptime(input("Enter the end date (YYYY-MM-DD): "), "%Y-%m-%d")
            time_difference = calculate_time_difference(start_date, end_date)
            print("Time difference:", time_difference)
        elif choice == 3:
            lst = input("Enter a list of numbers or strings (comma-separated): ").split(",")
            sorted_lst = custom_sort(lst)
            print("Sorted list:", sorted_lst)
        elif choice == 4:
            avenger_quiz()
        elif choice == 5:
            play_tic_tac_toe()
        elif choice == 6:
            convert_temperature()
        elif choice == 7:
            # Run the counter app code in this case
            pass
        elif choice == 8:
            alarm_time = input("Enter the alarm time (HH:MM:SS): ")
            set_alarm(alarm_time)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
