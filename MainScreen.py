import tkinter as tk
from tkinter import *
from Game import *


# This file is for the main screen of the game - inclouding the buttons and the title.
# In this file I caled the "humanVShuman" function & "humanVSmachine" function.

class MainScreen (Game):

    # Initializing the main screen
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(background='white')
        self.root.geometry('700x550')
        self.img = PhotoImage(file="images/title.png")
        self.label = Label(self.root, image=self.img, borderwidth=0)
        self.label.grid(row=0, column=0, columnspan=2)
        self.root.iconbitmap('images/icon.ico')
        self.createHomeScreen()

    # The whole game is in the same window (root). when the game starts - the home screen is deleted and u go to the screen of the game itself.

    def clearScreen(self):
        for widget in root.winfo_children():
            widget.destroy()

    # When the user press the button "human vs human" - all of this is done.

    def humanVShuman(self):
        self.randomStart()
        self.clearScreen()
        self.createWidgets()
        self.createBoard()

    # When the user press the button "human vs pc" - all of this is done.
    def humanVCpc(self):
        self.is_against_pc.set(True)
        self.randomStart()
        self.clearScreen()
        self.createWidgets()
        self.createBoard()

    # Home page of the game (main screen - buttons and title).
    def createHomeScreen(self):
        # Import the images (buttons) using PhotoImage function
        global human_vs_human_image, human_vs_pc_image
        human_vs_human_image = PhotoImage(file="images/humanVShuman.png")
        human_vs_pc_image = PhotoImage(file="images/humanVSpc.png")

        human_VS_human_but = tk.Button(self.root, image=human_vs_human_image, bg="white",
                                       borderwidth=0, command=self.humanVShuman)
        human_VS_human_but.grid(row=2, column=0, padx=100, pady=0.01, sticky=S)

        human_VS_pc_but = tk.Button(self.root, image=human_vs_pc_image, bg="white",
                                    borderwidth=0, command=self.humanVCpc)
        human_VS_pc_but.grid(row=2, column=1, padx=110, pady=0.01, sticky=S)


# Create the window
root = Tk()
mainScreen = MainScreen(root)

root.mainloop()
