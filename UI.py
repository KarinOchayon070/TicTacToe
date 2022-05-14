from email import message
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from turtle import bgcolor
from matplotlib.ft2font import BOLD


# --------------------------------------------------------------------------------Init the window----------------------------------------------------------------------------#
root = tk.Tk()  # Create the window
root.title("Tic Tac Toe")  # Title of the window
root.configure(background='white')  # Set the background color
root.geometry('700x550')  # Set the size of the window
img = PhotoImage(file="images/title.png")  # "Tic Tac Toe" title as an image
# Create the label ("Tic Tac Toe" title)
label = Label(root, image=img, borderwidth=0)
label.pack(side="top")  # Pack the label
root.iconbitmap('images/icon.ico')


#---------------------------------------------------------------------------------When "human VS human"---------------------------------------------------------------------------------#


# Func when press
def human_VS_human():
    # Clear the board
    label.destroy()
    human_VS_human_but.destroy()
    human_VS_pc_but.destroy()
    # Create the users names
    create_widgets()
    # Create the board
    create_board()
    btnClick(buttons)
    checkForWin()


#--------------------------------------------------------------Buttons ("human VC humam", "human VC pc")--------------------------------------------------------------------#
# Import the images (buttons) using PhotoImage function
click_btn1 = PhotoImage(file="images/humanVShuman.png")
click_btn2 = PhotoImage(file="images/humanVSpc.png")

# Create a label for buttons event
img_label = Label(image=click_btn1)
img_labe2 = Label(image=click_btn2)

# Create the actual buttons
human_VS_human_but = tk.Button(root, image=click_btn1, bg="white",
                               borderwidth=0, command=human_VS_human)
human_VS_human_but.pack(side="right", padx=100, pady=0.01)
human_VS_pc_but = tk.Button(root, image=click_btn2, bg="white",
                            borderwidth=0)
human_VS_pc_but.pack(side="left", padx=110, pady=0.01)


#---------------------------------------------------------------------------------Function---------------------------------------------------------------------------------#
# Decleration of the variables
player1 = StringVar()
player2 = StringVar()
player_1_name = StringVar()
player_2_name = StringVar()
player_1_score = IntVar()
player_2_score = IntVar()
whos_turn = StringVar()
playerTurn = StringVar()
playerTurn.set("X")
flag = IntVar()


# Function to create the board (9 buttons in total)
def create_board():

    global buttons
    buttons = StringVar()

    global button1, button2, button3, button4, button5, button6, button7, button8, button9

    button1 = Button(root, text=" ", font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button1))
    button1.grid(row=0, column=0,  sticky=S+N+E+W)

    button2 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button2))
    button2.grid(row=0, column=1,  sticky=S+N+E+W)

    button3 = Button(root,  text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button3))
    button3.grid(row=0, column=2,  sticky=S+N+E+W)

    button4 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button4))
    button4.grid(row=1, column=0,  sticky=S+N+E+W)

    button5 = Button(root,  text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button5))
    button5.grid(row=1, column=1,  sticky=S+N+E+W)

    button6 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button6))
    button6.grid(row=1, column=2,  sticky=S+N+E+W)

    button7 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button7))
    button7.grid(row=2, column=0,  sticky=S+N+E+W)

    button8 = Button(root,  text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button8))
    button8.grid(row=2, column=1,  sticky=S+N+E+W)

    button9 = Button(root,  text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=2, width=5, command=lambda: btnClick(button9))
    button9.grid(row=2, column=2,  sticky=S+N+E+W)


def btnClick(buttons):

    whos_turn_label = Label(root, textvariable=whos_turn, width=20, borderwidth=2,
                            bg='white', font=('COMIC SANS MS', 15))
    whos_turn_label.grid(row=2, column=7)
    whos_turn.set(f'{player_1_name.get()} turn')

    if buttons["text"] == " " and playerTurn.get() == "X":
        buttons["text"] = "X"
        playerTurn.set("O")
        checkForWin()
        flag.set(flag.get() + 1)
        whos_turn.set(f'{player_2_name.get()} turn')

    elif(buttons["text"] == " " and playerTurn.get() == "O"):
        buttons["text"] = "O"
        playerTurn.set("X")
        checkForWin()
        flag.set(flag.get() + 1)

    else:
        messagebox.showinfo(
            "Tic Tac Toe", "Button already clicked, please try again")


def handleButtonState(state):
    button1.configure(state=state)
    button2.configure(state=state)
    button3.configure(state=state)
    button4.configure(state=state)
    button5.configure(state=state)
    button6.configure(state=state)
    button7.configure(state=state)
    button8.configure(state=state)
    button9.configure(state=state)


def checkForWin():

    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        handleButtonState(DISABLED)
        messagebox.showinfo("Tic Tac Toe", f'{player_1_name.get()} wins')
        player_1_score.set(player_1_score.get() + 2)

    elif(flag.get() == 8):
        handleButtonState(DISABLED)
        messagebox.showinfo("Tic Tac Toe", "Oh bummer! It's a tie")
        player_1_score.set(player_1_score.get() + 1)
        player_2_score.set(player_2_score.get() + 1)

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'):
        handleButtonState(DISABLED)
        messagebox.showinfo("Tic Tac Toe", f'{player_2_name.get()} wins')
        player_2_score.set(player_2_score.get() + 2)


def show_score():

    score_player1_label = Label(root, textvariable=player_1_score, width=5, borderwidth=2,
                                bg='white', font=('COMIC SANS MS', 15))
    score_player1_label.grid(row=0, column=8)

    score_player2_label = Label(root, textvariable=player_2_score, width=5, borderwidth=2,
                                bg='white', font=('COMIC SANS MS', 15))
    score_player2_label.grid(row=1, column=8)


def clear_board():
    flag.set(0)
    handleButtonState(NORMAL)
    whos_turn.set(f'{player_1_name.get()} turn')
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "


def new_game():
    clear_board()
    player_1_score.set(0)
    player_2_score.set(0)

# Create the labels and the input user names


def create_widgets():

    # Create the label + input for player 1
    label_player1_name = Label(root, text="Player 1 name: ",
                               font=('COMIC SANS MS', 15, 'bold'), borderwidth=0, background='white')
    label_player1_name.grid(row=0, column=6)

    input_player1_name = Entry(root, textvariable=player_1_name, width=15, borderwidth=2,
                               bg='white', font=('COMIC SANS MS', 15))
    input_player1_name.grid(row=0, column=7)
    input_player1_name.insert(0, "Player 1")

    # Create the label + input for player 2
    label_player2_name = Label(root, text="Player 2 name: ",
                               font=('COMIC SANS MS', 15, 'bold'), borderwidth=0, background='white')
    label_player2_name.grid(row=1, column=6)

    input_player2_name = Entry(root, textvariable=player_2_name, width=15, borderwidth=2,
                               bg='white', font=('COMIC SANS MS', 15))
    input_player2_name.grid(row=1, column=7)
    input_player2_name.insert(0, "Player 2")

    # show_score_btn_pic = PhotoImage(file="images/show_score.png")
    global show_score_btn_pic
    show_score_btn_pic = PhotoImage(file="images/show_score.png")
    show_score_btn = Button(
        root, image=show_score_btn_pic, bg="white", borderwidth=0, command=show_score)
    show_score_btn.grid(row=4, column=7)

    # Create the "clear board" button
    global clear_board_btn_pic
    clear_board_btn_pic = PhotoImage(file="images/clear.png")
    clear_board_btn = Button(root, image=clear_board_btn_pic,
                             bg="white", borderwidth=0, command=clear_board)
    clear_board_btn.grid(row=5, column=7)

    # Create the "new" button
    global new_btn_pic
    new_btn_pic = PhotoImage(file="images/new.png")
    new_btn = Button(root, image=new_btn_pic,
                     bg="white", borderwidth=0, command=new_game)
    new_btn.grid(row=3, column=7)


root.mainloop()
