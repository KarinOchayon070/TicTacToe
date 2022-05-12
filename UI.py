from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.ft2font import BOLD


# --------------------------------------------------------------------------------Init the window----------------------------------------------------------------------------#
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(background='white')
root.geometry('700x550')
img = PhotoImage(file="images/title.png")  # "Tic Tac Toe" title as an image
label = Label(root, image=img, borderwidth=0)
label.pack(side="top")


#---------------------------------------------------------------------------------Function---------------------------------------------------------------------------------#


# Decleration of the variables
pa = StringVar()
playerb = StringVar()
name1_var = tk.StringVar()
name2_var = tk.StringVar()


# Func when press
def human_VS_human():
    # Clear the board

    label.destroy()
    human_VS_human_but.destroy()
    human_VS_pc_but.destroy()
    # Create the users names
    create_widgets()
    # Create the board
    # create_board()
    btnClick(buttons)
    checkForWin()
    disableButton()


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

bclick = True
flag = 0
# Function to create the board (9 buttons in total)


def create_board():

    global buttons
    buttons = StringVar()

    global button1, button2, button3, button4, button5, button6, button7, button8, button9

    button1 = Button(root, text=" ", font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(root, text=' ', font=('COMIC SANS MS', 20),
                     bg='gray', fg='black', height=3, width=10, command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)


def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def checkForWin():

    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        messagebox.showinfo("Tic Tac Toe", pa)

    elif(flag == 8):
        messagebox.showinfo("Tic Tac Toe", "Oh bummer! It is a tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        messagebox.showinfo("Tic Tac Toe", playerb)


def btnClick(buttons):
    global bclick, flag, name1_var, name2_var, playerb, pa

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = name2_var.get() + " Wins!"
        pa = name1_var.get() + " Wins!"
        checkForWin()
        flag += 1

    elif(buttons["text"] == " " and bclick == False):
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


# Create the labels and the input user names
def create_widgets():

    # Create the label + input for player 1
    label_player1_name = Label(root, text="Player 1 name: ",
                               font=('COMIC SANS MS', 15, 'bold'), borderwidth=0, background='white')
    label_player1_name.grid(row=0, column=0)
    input_player1_name = Entry(root, textvariable=name1_var, width=15, borderwidth=2,
                               bg='white', font=('COMIC SANS MS', 15))
    input_player1_name.grid(row=0, column=1)

    # Create the label + input for player 2
    label_player2_name = Label(root, text="Player 2 name: ",
                               font=('COMIC SANS MS', 15, 'bold'), borderwidth=0, background='white')
    label_player2_name.grid(row=1, column=0)
    input_player2_name = Entry(root, textvariable=name2_var, width=15, borderwidth=2,
                               bg='white', font=('COMIC SANS MS', 15))
    input_player2_name.grid(row=1, column=1)

    # Create the "start!" button
    start_btn = Button(root, text='Start!', command=create_board)
    start_btn.grid(row=2, column=1)

    # x = input_player1_name.get()
    # y = input_player2_name.get()

    # if (x and y):
    #     start_btn.configure(state=NORMAL)
    # else:
    #     start_btn.configure(state=DISABLED)


root.mainloop()
