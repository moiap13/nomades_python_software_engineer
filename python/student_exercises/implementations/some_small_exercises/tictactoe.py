import os

# Function to draw the tic-tac-toe board
def draw_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    # TODO: Draw the board with the values at the rigth places
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diags
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return ' ' not in board

# Function to play the game
def play_game():
    board = [' '] * 9
    current_player = 'X'
    game_over = False

    while not game_over:
        draw_board(board)

        # TODO: Get player's move
        move = int(input("Player {}: Enter your move (1-9): ".format(current_player)))-1

       # TODO: Check if move is valid
        if (not (move >= 0 and move <= 8)) or board[move] != ' ':
            print("Invalid input. Try again")
            continue 
        
        # assert que le moove est ok

        # TODO: Update the board with the move
        board[move] = current_player

        # TODO: Check if the current player has won
        if check_win(board, current_player):
            draw_board(board)
            print(f"{current_player} Won")
            game_over = True
        # TODO: Check if it's a draw
        elif check_draw(board): # assert no winners
            draw_board(board)
            print("It's a Draw")
            game_over = True
        else:
            # TODO: Switch players
            # Assert game is still playing
            current_player = "X" if current_player == "O" else "O"

# Start the game
play_game()
