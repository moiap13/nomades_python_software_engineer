import os

# Function to draw the tic-tac-toe board
def draw_board(board: list[str]) -> None:
    """
    Function to draw the tic-tac-toe board.

    Arguments:
    - board (list): List representing the tic-tac-toe board.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    # TODO: Draw the board. PRO TIP: look at the example `tictactoe.310.py

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
    return False

# Function to play the game
def play_game():
    # The board variable store the state of the game, where board[0] is the top left corner and board[8] is the bottom right corner
    board = [' '] * 9
    current_player = None # TODO: choose player at random (the player value can be 'X' or 'O')
    # the game_over variable is used to know if the game is running or not
    game_over = False

    while not game_over:
        # TODO: Draw the board

        # TODO: Get player's move
        # Hint: Use input() to get the move from the player
        move = None

        # TODO: Check if move is valid
        # A valid move is an integer between 1 and 9 (both inclusive)
        # And the board for this integer is empty
        # if move is not valid, print "Invalid move. Try again!" and ask for a new moove

        # TODO: Update the board with the move
        # The borad is the list named board that contains state of the game
        
        # TODO: Check if the current player has won or draw or continue
        # Hint: Use the check_win() function to check if the current player has won
        # You need to think about something for the draw case
        # if no win and no draw the game continues, switch user 'X'->'O' || 'O'->'X'
# Start the game
play_game()
