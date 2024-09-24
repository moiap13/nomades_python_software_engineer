import os
import random
import time

# Function to draw the tic-tac-toe board
def draw_board(board: list[str]) -> None:
    """
    Function to draw the tic-tac-toe board.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    # TODO: Draw the board. PRO TIP: look at the example `tictactoe.310.py
    lines: list[str] = [
        'Tic-Tac-Toe\n',
        '   |   |   ', f' {board[0]} | {board[1]} | {board[2]} ', '___|___|___', 
        '   |   |   ', f' {board[3]} | {board[4]} | {board[5]}\t|1|2|3', '___|___|___\t------',
        '   |   |\t|4|5|6', f' {board[6]} | {board[7]} | {board[8]}\t------', '   |   |\t|7|8|9'
    ]
    for line in lines:
        print(line)


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
    # return (
    #   (board[0] == board[1] == board[2] == player) or
    #   (board[3] == board[4] == board[5] == player) or
    #   (board[6] == board[7] == board[8] == player) or

    #   (board[0] == board[3] == board[6] == player) or
    #   (board[1] == board[4] == board[7] == player) or
    #   (board[2] == board[5] == board[8] == player) or

    #   (board[0] == board[4] == board[8] == player) or
    #   (board[6] == board[4] == board[2] == player)
    # )

    combos: list[tuple] = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (6, 4, 2),
    ]

    for combo in combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False



# Function to play the game
def play_game():
    # The board variable store the state of the game, where board[0] is the top left corner and board[8] is the bottom right corner
    board: list[str] = [' '] * 9
    current_player = random.choice(['X','O']) # TODO: choose player at random (the player value can be 'X' or 'O')
    # the game_over variable is used to know if the game is running or not
    game_over = False

    while not game_over:
        # TODO: Draw the board
        draw_board(board)

        # TODO: Get player's move
        # Hint: Use input() to get the move from the player
        move = input(f"Player {current_player}\nChoose a cell to play between 1 and 9: ")
        move = int(move) if move.isnumeric() else 0

        # TODO: Check if move is valid
        # A valid move is an integer between 1 and 9 (both inclusive)
        # And the board for this integer is empty
        # if move is not valid, print "Invalid move. Try again!" and ask for a new moove
        
        #if (0 < move < 10) and board[move-1] != " ":
        if not (move in range(1, 10) and board[move-1] == " "):
            print("Invalid move")
            time.sleep(0.3)
            continue
        
        # assert that the move is valid

        # TODO: Update the board with the move
        # The borad is the list named board that contains state of the game
        board[move-1] = current_player
        
        # TODO: Check if the current player has won or draw or continue
        # Hint: Use the check_win() function to check if the current player has won
        # You need to think about something for the draw case
        # if no win and no draw the game continues, switch user 'X'->'O' || 'O'->'X'
        if check_win(board, current_player):
            # WIN
            game_over = True
            draw_board(board)
            print(f"Winer is {current_player}")
        elif ' ' not in board:
            # TIE
            game_over = True
            draw_board(board)
            print("No winners, it's a tie")
        else:
            # Continue game
            # switch players
            current_player = "X" if current_player == "O" else "O"
# Start the game
play_game()
