import os
import random 
from time import sleep
# Function to draw the tic-tac-toe board
def draw_board(board):
    """
    Function to draw the tic-tac-toe board.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print("Tic-Tac-Toe\n")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} \t|1|2|3".format(board[3], board[4], board[5]))
    print("___|___|___\t------")
    print("   |   |    \t|4|5|6")
    print(" {} | {} | {} \t------".format(board[6], board[7], board[8]))
    print("   |   |   \t|7|8|9\n")

# Function to check if a player has won
def check_win(board: list, player: str) -> bool:
    """
    Function to check if a player has won.
    A player wins if they have 3 consecutive marks in a row, column or diagonal.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    - player (str): Player's mark ('X' or 'O').

    Returns:
    - win (bool): True if the player has won, False otherwise.
    """
    # if board.count(player) >= 3:
    #     marks = 0
    #     for i in range(0,7,3):
    #         for j in range(0,3):
    #             if board[i+j]==player:
    #                 marks+=1
    #         if marks == 3:
    #             return True
    #         else:
    #             marks = 0
        
    #     for i in range(0,3):
    #         for j in range(0,5,3):
    #             if board[i+j]==player:
    #                 marks+=1
    #         if marks == 3:
    #             return True
    #         else:
    #             marks = 0 

    #     # if board[0] == player and board[4] == player and board[8] == player:
    #     if board[0] == board[4] == board[8] == player:
    #         return True
    #     if board[2] == player and board[4] == player and board[6] == player:
    #         return True 
    # return False

    wins = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ]

    for win in wins:
      if board[win[0]] == board[win[1]] == board[win[2]]:
        return True
    return False

# Function to play the game
def play_game():
    board: list = [' '] * 9
    # choose player at random between X and O
    current_player: str = random.choice(["O", "X"])
    game_over: bool = False

    while not game_over:
        # TODO: Draw the board
        draw_board(board)

        # TODO: Get player's move
        # Hint: Use input() to get the move from the player
        move = int(input(f"Enter the wanted position (1-9) for player {current_player} : "))
        # TODO: Check if move is valid
        # A valid move is an integer between 1 and 9 (both inclusive)
        # if move is not valid, print "Invalid move. Try again!" and ask for a new moove
        if (move not in range(1, 10)) or (board[move-1] != ' '):
            print("Invalid moove")
            sleep(1)
            continue
        
        # assert move is valid

        # TODO: Update the board with the move
        # The borad is the list named board that contains state of the game
        board[move-1] = current_player
        
        # TODO: Check if the current player has won or draw or continue
        # Hint: Use the check_win() function to check if the current player has won
        # You need to think about something for the draw case
        # if no win and no draw the game continues
        if check_win(board, current_player):
            # current_player has won
            draw_board(board)
            print(f"{current_player} won bravo !")
            game_over = True
        elif " " not in board:
            # there is a tie
            draw_board(board)
            print("No one won !")
            game_over = True
        else:
            current_player = "X" if current_player == "O" else "O"
# Start the game
play_game()
