# Empty game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Global variables
game_still_going = True
winner = None
current_player = "X"


# Display board function
def disply_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Start the game
def play_game():

    disply_board()  # First I want to display the board

    #   While the game is still going keep looping through - handle turn, switch the player turn and constantly check if the game is over
    while game_still_going:

        # Handle a single turn
        handle_turn(current_player)

        # Check if game is over
        check_if_game_over()

        # Flip to other player
        flip_player()

    # Print the winner or tie
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Oh bummer! it's a tie.")


def handle_turn(player):
    print("It's " + player + "'s turn.")
    position = input("Choose a position from 1-9 please: ")

    valid = False  # Set to false until we know it's valid

    while not valid:  # Keep asking until we get a valid input
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Please enter a valid number between 1-9: ")
        position = int(position) - 1  # Convert to index (for our pretty board)

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player
    disply_board()


def check_if_game_over():
    check_win()
    check_tie()


def check_win():
    global winner
    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going
    first_row = board[0] == board[1] == board[2] != "-"
    second_row = board[3] == board[4] == board[5] != "-"
    third_row = board[6] == board[7] == board[8] != "-"
    if (first_row or second_row or third_row):
        game_still_going = False
    # Return the winner (X or O)
    if first_row:
        return board[0]
    elif second_row:
        return board[3]
    elif third_row:
        return board[6]


def check_columns():
    global game_still_going
    first_column = board[0] == board[3] == board[6] != "-"
    second_column = board[1] == board[4] == board[7] != "-"
    third_column = board[2] == board[5] == board[8] != "-"
    if (first_column or second_column or third_column):
        game_still_going = False
    # Return the winner (X or O)
    if first_column:
        return board[0]
    elif second_column:
        return board[1]
    elif third_column:
        return board[2]


def check_diagonals():
    global game_still_going
    first_diagonal = board[0] == board[4] == board[8] != "-"
    second_diagonal = board[2] == board[4] == board[6] != "-"
    if (first_diagonal or second_diagonal):
        game_still_going = False
    # Return the winner (X or O)
    if first_diagonal:
        return board[0]
    elif second_diagonal:
        return board[2]


def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


play_game()
