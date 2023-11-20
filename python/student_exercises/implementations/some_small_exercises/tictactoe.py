import os

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
    return False

# Function to play the game
def play_game():
    board = [' '] * 9
    current_player = 'X'
    game_over = False

    while not game_over:
        # TODO: Draw the board

        # TODO: Get player's move
        # Hint: Use input() to get the move from the player
        move = None

        # TODO: Check if move is valid
        # A valid move is an integer between 1 and 9 (both inclusive)
        # if move is not valid, print "Invalid move. Try again!" and ask for a new moove

        # TODO: Update the board with the move
        # The borad is the list named board that contains state of the game
        
        # TODO: Check if the current player has won or draw or continue
        # Hint: Use the check_win() function to check if the current player has won
        # You need to think about something for the draw case
        # if no win and no draw the game continues
# Start the game
play_game()
