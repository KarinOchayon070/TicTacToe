from tkinter import *
import tkinter as tk
from tkinter import ttk

# Init the window
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(background='white')
root.geometry('700x550')

# "Tic Tac Toe" title as an image
img = PhotoImage(file="images/title.png")
label = Label(root, image=img, borderwidth=0).pack(side="top")

# Import the images (buttons) using PhotoImage func
click_btn1 = PhotoImage(file="images/humanVShuman.png")
click_btn2 = PhotoImage(file="images/humanVSpc.png")

# Create a label for buttons event
img_label = Label(image=click_btn1)
img_labe2 = Label(image=click_btn2)

# Create the actual buttons
button1 = tk.Button(root, image=click_btn1, bg="white", borderwidth=0)
button1.pack(side="right", padx=100, pady=0.01)
button2 = tk.Button(root, image=click_btn2, bg="white", borderwidth=0)
button2.pack(side="left", padx=110, pady=0.01)


# p1 = StringVar()
# p2 = StringVar()


# def create_widgets():
#     first_label = tk.Label(root, text="Player 1:", font=(
#         "Helvetica", 20), bg="#ccffe6", fg="black", height=1, width=10)
#     first_label.grid(row=0, column=0)

#     first_player_name = tk.Entry(root, textvariable=p1, bd=5)
#     first_player_name.grid(row=0, column=1)

#     second_label = tk.Label(root, text="Player 2:", font=(
#         "Helvetica", 20), bg="#ccffe6", fg="black", height=1, width=10)
#     second_label.grid(row=2, column=0)

#     second_player_name = tk.Entry(root, textvariable=p2, bd=5)
#     second_player_name.grid(row=2, column=1)


# reate_widgets()
root.mainloop()
