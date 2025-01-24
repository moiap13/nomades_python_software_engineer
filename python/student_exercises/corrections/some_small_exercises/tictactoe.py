import os
import time
import random

# Function to draw the tic-tac-toe board
def draw_board(board: list[str]) -> None:
    """
    Function to draw the tic-tac-toe board.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(
f"""Tic-Tac-Toe

   |   |   
 {board[0]} | {board[1]} | {board[2]} 
___|___|___
   |   |   
 {board[3]} | {board[4]} | {board[5]}   1|2|3
___|___|___  -----
   |   |     4|5|6
 {board[6]} | {board[7]} | {board[8]}   -----
   |   |     7|8|9
""")

def check_win(board: list[str], player: str) -> bool:
    """
    Function to check if a player has won.
    A player wins if they have 3 consecutive marks in a row, column or diagonal.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    - player (str): Player's mark ('X' or 'O').

    Returns:
    - win (bool): True if the player has won, False otherwise.
    """
    # if (board[0] == player and board[1] == player and board[2] == player \
    #   or board[3] == player and board[4] == player and board[5] == player \
    #   or board[6] == player and board[7] == player and board[8] == player \
    #   or board[0] == player and board[3] == player and board[6] == player \
    #   or board[1] == player and board[4] == player and board[7] == player \
    #   or board[2] == player and board[5] == player and board[8] == player \
    #   or board[0] == player and board[4] == player and board[8] == player \
    #   or board[2] == player and board[4] == player and board[6] == player):
    #     return True
    # return False
    # return board[0] == board[1] == board[2] == player \
    #   or board[3] == player and board[4] == player and board[5] == player \
    #   or board[6] == player and board[7] == player and board[8] == player \
    #   or board[0] == player and board[3] == player and board[6] == player \
    #   or board[1] == player and board[4] == player and board[7] == player \
    #   or board[2] == player and board[5] == player and board[8] == player \
    #   or board[0] == player and board[4] == player and board[8] == player \
    #   or board[2] == player and board[4] == player and board[6] == player

    combos: list[tuple[int]] = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (2, 4, 6),
    ]

    # for combo in combos:
    #     if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
    #         return True
    # return False

    for combo in combos:
        val: list[bool] = [board[pos] == player for pos in combo]
        if all(val):
            return True
    return False
        


# Function to play the game
def play_game():
    # The board variable store the state of the game, where board[0] is the top left corner and board[8] is the bottom right corner
    board: list[str] = [' '] * 9
    current_player: str = random.choice(["X", "O"])
    # the game_over variable is used to know if the game is running or not
    game_over = False

    while not game_over:
        draw_board(board)

        # Hint: Use input() to get the move from the player
        try:
            move: int = int(input("Enter a value between 1 and 9 (both inclusive): "))
        except ValueError:
            print("Invalid input. Try again!")
            time.sleep(0.6)
            continue
            

        # A valid move is an integer between 1 and 9 (both inclusive)
        # And the board for this integer is empty
        # if move is not valid, print "Invalid move. Try again!" and ask for a new moove
        
        # if not ((move >= 1 and move <= 9) and board[move-1] == ' '):
        # if not (move in range(1, 10) and board[move-1] == ' '):
        if not (1 <= move <= 9 and board[move-1] == ' '):
            print("Invalid move. Try again!")
            time.sleep(0.3)
            continue
        
        # assert move is valid
        
        # The borad is the list named board that contains state of the game
        board[move-1] = current_player
        
        # Hint: Use the check_win() function to check if the current player has won
        # You need to think about something for the draw case
        # if no win and no draw the game continues, switch user 'X'->'O' || 'O'->'X'

        if check_win(board, current_player):
            draw_board(board)
            print(f"User {current_player}: WON !!")
            game_over = True
        elif ' ' not in board:
            draw_board(board)
            print("It's a tie !!")
            game_over = True
        else:
            current_player = "X" if current_player == "O" else "O"
# Start the game
play_game()
