import tkinter as tk
from tkinter import *
from Game import *


class MainScreen (Game):
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

    def clearScreen(self):
        for widget in root.winfo_children():
            widget.destroy()

    def humanVShuman(self):
        self.clearScreen()
        # Create the users names
        self.createWidgets()
        self.createBoard()

    def humanVCpc(self):
        pass
        # self.clearScreen()
        # Create the users names
        # createWidgets(root)
        # createBoard()

    def createHomeScreen(self):
        # Import the images (buttons) using PhotoImage function

        global human_vs_human_image, human_vs_pc_image
        human_vs_human_image = PhotoImage(file="images/humanVShuman.png")
        human_vs_pc_image = PhotoImage(file="images/humanVSpc.png")

        human_VS_human_but = tk.Button(self.root, image=human_vs_human_image, bg="white",
                                       borderwidth=0, command=self.humanVShuman)
        human_VS_human_but.grid(row=0, column=0, padx=100, pady=0.01, sticky=S)

        human_VS_pc_but = tk.Button(self.root, image=human_vs_pc_image, bg="white",
                                    borderwidth=0, command=self.humanVCpc)
        human_VS_pc_but.grid(row=0, column=1, padx=110, pady=0.01, sticky=S)


root = Tk()  # Create the window
mainScreen = MainScreen(root)

root.mainloop()
