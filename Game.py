from tkinter import *
from tkinter import messagebox
from constants import *
import random
import time


class Game:

    def __init__(self, root):

        # Decleration of the variables
        self.root = root
        self.is_against_pc = BooleanVar(value=False)
        self.player_1_name = StringVar(value="Player 1")
        self.player_2_name = StringVar(value="Player 2")
        self.player_1_score = IntVar(value=0)
        self.player_2_score = IntVar(value=0)
        self.buttons_state = StringVar(value=NORMAL)
        self.player_turn = StringVar(value=self.player_1_name.get())

        self.board = [
            StringVar(value=" "),
            StringVar(value=" "),
            StringVar(value=" "),
            StringVar(value=" "),
            StringVar(value=" "),
            StringVar(value=" "),
            StringVar(value=" "),
            StringVar(value=" "),
            StringVar(value=" "),
        ]

    def randomStart(self):
        if(self.is_against_pc.get() == True):
            if(random.randint(0, 1) == 0):
                self.pcLogic()
        elif(random.randint(0, 1) == 0):
            self.player_turn.set(self.player_2_name.get())

    def changePlayerTurn(self):
        if(self.player_turn.get() == self.player_1_name.get()):
            self.player_turn.set(self.player_2_name.get())

        elif(self.player_turn.get() == self.player_2_name.get()):
            self.player_turn.set(self.player_1_name.get())

    # Function that checks if there is a winner - checks if there is a winner (rows, columns, diagonals)
    def checkForWin(self):
        if (
            self.board[0].get() == "X" and self.board[1].get() == "X" and self.board[2].get() == "X" or
            self.board[3].get() == "X" and self.board[4].get() == "X" and self.board[5].get() == "X" or
            self.board[6].get() == "X" and self.board[7].get() == "X" and self.board[8].get() == "X" or
            self.board[0].get() == "X" and self.board[3].get() == "X" and self.board[6].get() == "X" or
            self.board[1].get() == "X" and self.board[4].get() == "X" and self.board[7].get() == "X" or
            self.board[2].get() == "X" and self.board[5].get() == "X" and self.board[8].get() == "X" or
            self.board[0].get() == "X" and self.board[4].get() == "X" and self.board[8].get() == "X" or
            self.board[2].get() == "X" and self.board[4].get(
            ) == "X" and self.board[6].get() == "X"
        ):
            self.buttons_state.set(DISABLED)
            messagebox.showinfo(
                "Tic Tac Toe", f'{self.player_1_name.get()} wins')
            self.player_1_score.set(self.player_1_score.get() + 2)

        elif (
                self.board[0].get() == "O" and self.board[1].get() == "O" and self.board[2].get() == "O" or
                self.board[3].get() == "O" and self.board[4].get() == "O" and self.board[5].get() == "O" or
                self.board[6].get() == "O" and self.board[7].get() == "O" and self.board[8].get() == "O" or
                self.board[0].get() == "O" and self.board[3].get() == "O" and self.board[6].get() == "O" or
                self.board[1].get() == "O" and self.board[4].get() == "O" and self.board[7].get() == "O" or
                self.board[2].get() == "O" and self.board[5].get() == "O" and self.board[8].get() == "O" or
                self.board[0].get() == "O" and self.board[4].get() == "O" and self.board[8].get() == "O" or
                self.board[2].get() == "O" and self.board[4].get() == "O" and self.board[6].get() == "O"):
            self.buttons_state.set(DISABLED)
            self.player_2_score.set(self.player_2_score.get() + 2)

            if(self.is_against_pc.get() == True):
                messagebox.showinfo(
                    "Tic Tac Toe", "The coolest PC on earth wins. PATHETIC!")
            else:
                messagebox.showinfo(
                    "Tic Tac Toe", f'{self.player_2_name.get()} wins')

        elif(self.isTie()):
            self.buttons_state.set(DISABLED)
            messagebox.showinfo("Tic Tac Toe", "Oh bummer! It's a tie")
            self.player_1_score.set(self.player_1_score.get() + 1)
            self.player_2_score.set(self.player_2_score.get() + 1)

        self.createBoard()

    def btnClick(self, index):

        if(self.board[index].get() != " "):
            return messagebox.showinfo(
                "Tic Tac Toe", "Button already clicked, please try again")

        if(self.player_turn.get() == self.player_1_name.get()):
            self.board[index].set("X")

        elif(self.player_turn.get() == self.player_2_name.get()):
            self.board[index].set("O")

        if(self.is_against_pc.get() == False):
            self.changePlayerTurn()

        else:
            time.sleep(0.1)
            self.pcLogic()

        self.createBoard()
        self.checkForWin()

    # Function that checks if there is a tie - if in one of the wining array there is X and O, this specific combination is a tie and we need to check the next combination

    def pcLogic(self):

        potential_attack_index = -1
        potential_defend_index = -1

        for array in wins_array:
            potential_index_to_place = -1
            amount_of_O = 0
            amount_of_X = 0

            for cell in array:

                # Start with defence logic
                if (self.board[cell].get() == "X"):
                    amount_of_X += 1
                    # It's enough to have 1 X and the pc can't wins (so no need to "attack")

                if(self.board[cell].get() == "O"):
                    amount_of_O += 1

                elif(self.board[cell].get() == " "):
                    # If there is a space I need to save it, because maybe later I will need to place the O in this position ("defense")
                    potential_index_to_place = cell

                if(amount_of_X == 2):
                    potential_defend_index = potential_index_to_place

            if(amount_of_O == 2 and amount_of_X == 0):
                self.board[potential_index_to_place].set("O")
                return

            if(amount_of_X == 2 and amount_of_O == 0):
                potential_defend_index = potential_index_to_place

            if(amount_of_O == 1 and amount_of_X == 0):
                potential_attack_index = potential_index_to_place

        if(potential_defend_index != -1):
            self.board[potential_defend_index].set("O")
            return

        if(potential_attack_index != -1):
            self.board[potential_attack_index].set("O")
            return

        # If there is no need to defend or attack, randomize the PC choice
        empty_board = []
        for index, item in enumerate(self.board):
            if(item.get() == " "):
                empty_board.append(index)

        self.board[random.choice(empty_board)].set("O")

    def isTie(self):
        is_tie = True
        for array in wins_array:
            board_array = [
                self.board[array[0]].get(),
                self.board[array[1]].get(),
                self.board[array[2]].get(),
            ]

            if("X" and "O" not in board_array):
                is_tie = False

        return is_tie

    # Function that clears the board (THIS FUNCTION DO NOT SETS THE SCORE TO 0!!!)

    def clearBoard(self):
        for cell in self.board:
            cell.set(" ")
        # Buttons are enabled again
        self.randomStart()
        self.buttons_state.set(NORMAL)
        # Rerender the board
        self.createBoard()


# Function that creates a new game (scores are set to 0)


    def newGame(self):
        self.clearBoard()
        self.player_1_score.set(0)
        self.player_2_score.set(0)
        self.player_1_name.set("Player 1")
        self.player_2_name.set("Player 2")

    def showScore(self):
        score_player1_label = Label(self.root, textvariable=self.player_1_score, width=2, borderwidth=2,
                                    bg='white', font=('COMIC SANS MS', 15))
        score_player1_label.grid(row=0, column=9)

        score_player2_label = Label(self.root, textvariable=self.player_2_score, width=2, borderwidth=2,
                                    bg='white', font=('COMIC SANS MS', 15))
        score_player2_label.grid(row=1, column=9)

    def createWidgets(self):
        # Create the label + input for player 1
        label_player1_name = Label(self.root, text="Player 1 name: ",
                                   font=('COMIC SANS MS', 15, 'bold'), borderwidth=0, background='white')
        label_player1_name.grid(row=0, column=7)

        input_player1_name = Entry(self.root, textvariable=self.player_1_name, width=10, borderwidth=2,
                                   bg='white', font=('COMIC SANS MS', 15))
        input_player1_name.grid(row=0, column=8)

        # Create the label + input for player 2
        player_2_name_label = "Coolest PC on earth" if self.is_against_pc.get(
        ) else "Player 2 name: "
        label_player2_name = Label(self.root, text=player_2_name_label,
                                   font=('COMIC SANS MS', 15, 'bold'), borderwidth=0, background='white')
        label_player2_name.grid(row=1, column=7)

        if(not self.is_against_pc.get()):
            input_player2_name = Entry(self.root, textvariable=self.player_2_name, width=10, borderwidth=2,
                                       bg='white', font=('COMIC SANS MS', 15))
            input_player2_name.grid(row=1, column=8)

            # Create the label that sets the turn
            player_turn_label = Label(self.root, textvariable=self.player_turn, width=20, borderwidth=2,
                                      bg='white', font=('COMIC SANS MS', 15))
            player_turn_label.grid(row=2, column=8)

        # Create the "show score" button
        global show_score_btn_pic
        show_score_btn_pic = PhotoImage(file="images/show_score.png")
        show_score_btn = Button(
            self.root, image=show_score_btn_pic, bg="white", borderwidth=0, command=self.showScore)
        show_score_btn.grid(row=4, column=8)

        # Create the "clear board" button
        global clear_board_btn_pic
        clear_board_btn_pic = PhotoImage(file="images/clear.png")
        clear_board_btn = Button(self.root, image=clear_board_btn_pic,
                                 bg="white", borderwidth=0, command=self.clearBoard)
        clear_board_btn.grid(row=5, column=8)

        # Create the "new game" button
        global new_btn_pic
        new_btn_pic = PhotoImage(file="images/new.png")
        new_btn = Button(self.root, image=new_btn_pic,
                         bg="white", borderwidth=0, command=self.newGame)
        new_btn.grid(row=3, column=8)

    def createBoard(self):
        # Init the row and column
        row = 0
        column = 0

        for index, cell in enumerate(self.board):
            button = Button(self.root, text=cell.get(), font=('COMIC SANS MS', 20), state=self.buttons_state.get(),
                            bg='gray', fg='black', height=2, width=5, command=lambda index=index: self.btnClick(index))
            button.grid(row=row, column=column,  sticky=S+N+E+W)
            # Increase the column until it reaches 3 (3x3 board) and than start a new row
            column += 1
            if column == 3:
                row += 1
                column = 0
