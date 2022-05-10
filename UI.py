import tkinter as tk
from tkinter import *

from turtle import bgcolor
from zipapp import create_archive

root = tk.Tk()
root.title("Tic Tac Toe")
# change root bg to white
root.configure(background='white')
root.geometry('700x550')


img = PhotoImage(file="images/title.png")
label = Label(root, image=img, borderwidth=0)
label.grid(row=0, column=0)

# Import the image using PhotoImage function
click_btn1 = PhotoImage(file="images/humanVShuman.png")
click_btn2 = PhotoImage(file="images/humanVSpc.png")

# Let us create a label for button event
img_label = Label(image=click_btn1)
img_labe2 = Label(image=click_btn2)

# Let us create a dummy button and pass the image
button1 = Button(root, image=click_btn1, bg="white",
                 borderwidth=0, ).grid(row=1, column=0, padx=10, pady=10)

button2 = Button(root, image=click_btn2, bg="white",
                 borderwidth=0).grid(row=1, column=1)

# button.pack(pady=10)

text = Label(root, text="")
# text.pack(pady=30)


# photo = PhotoImage(file="images/humanVShuman.png")
# w = Label(root, image=photo)
# w.grid(row=10, column=10, columnspan=2)


# canvas = Canvas(root, width=1000, height=1000)
# canvas.pack()
# img = PhotoImage(file="images/humanVShuman.png")
# canvas.create_image(260, 125, anchor=NW, image=img)


p1 = StringVar()
p2 = StringVar()


def create_widgets():
    first_label = tk.Label(root, text="Player 1:", font=(
        "Helvetica", 20), bg="#ccffe6", fg="black", height=1, width=10)
    first_label.grid(row=0, column=0)

    first_player_name = tk.Entry(root, textvariable=p1, bd=5)
    first_player_name.grid(row=0, column=1)

    second_label = tk.Label(root, text="Player 2:", font=(
        "Helvetica", 20), bg="#ccffe6", fg="black", height=1, width=10)
    second_label.grid(row=2, column=0)

    second_player_name = tk.Entry(root, textvariable=p2, bd=5)
    second_player_name.grid(row=2, column=1)


# reate_widgets()
root.mainloop()
