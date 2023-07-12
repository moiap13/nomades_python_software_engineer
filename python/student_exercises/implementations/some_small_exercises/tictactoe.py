import os

# Function to draw the tic-tac-toe board
def draw_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

# Function to check if a player has won
def check_win(board, player):
    return None

def check_draw(board):
    return None

# Function to play the game
def play_game():
    board = [' '] * 9
    current_player = 'X'
    game_over = False

    while not game_over:
        draw_board(board)

        # TODO: Get player's move
        move = input("Player {}: Enter your move (1-9): ".format(current_player))

        # TODO: Check if move is valid


        # TODO: Update the board with the move

        # TODO: Check if the current player has won
        if check_win(board, current_player):
            pass
        # TODO: Check if it's a draw
        elif check_draw(board):
            pass
        else:
            # TODO: Switch players
            pass

# Start the game
play_game()
