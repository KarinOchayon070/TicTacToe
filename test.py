from ast import Return
from constants import *
import random


board = [" ", " ", "X",
         " ", " ", " ",
         " ", " ", "O"]


def myTest():
    potential_attack_index = -1
    potential_defend_index = -1  # הוספתי

    for array in wins_array:
        potential_index_to_place = -1
        amount_of_O = 0
        amount_of_X = 0

        for cell in array:

            # Start with defence logic
            if (board[cell] == "X"):
                amount_of_X += 1
                # It's enough to have 1 X and the pc can't wins (so no need to "attack")

            if(board[cell] == "O"):
                amount_of_O += 1

            elif(board[cell] == " "):
                # If there is a space I need to save it, because maybe later I will need to place the O in this position ("defense")
                potential_index_to_place = cell

            if(amount_of_X == 2):
                potential_defend_index = potential_index_to_place

        if(amount_of_O == 2 and amount_of_X == 0):
            board[potential_index_to_place] = "O"
            return

        if(amount_of_X == 2 and amount_of_O == 0):
            potential_defend_index = potential_index_to_place

        if(amount_of_O == 1 and amount_of_X == 0):
            potential_attack_index = potential_index_to_place

    if(potential_defend_index != -1):
        board[potential_defend_index] = "O"
        return

    if(potential_attack_index != -1):
        board[potential_attack_index] = "O"
        return

    # If there is no need to defend or attack, randomize the PC choice
    empty_board = []
    for index, item in enumerate(board):
        if(item == " "):
            empty_board.append(index)

    board[random.choice(empty_board)] = "O"


myTest()
print(board)
