from tkinter import *
import math
from ColorClass import Midnight

class SquareBubble(Frame):
    def __init__(self, parent, text=None, user=None, fill=None):
        Frame.__init__(self, parent)
        self.text=text
        self.fill = Midnight.ghostwhite if fill == None else fill
        self.config(bg=Midnight.white)
        self.frame = Frame(self, bg=self.fill, relief=FLAT)
        self.frame.grid(row=2, column=1, sticky='nw', pady=5, padx=3)
        self.lblMessage = Label(self.frame, text=self.text, bg=self.fill, fg=Midnight.white, wrap=290, font=('Segoe UI', 14, 'roman'), justify=LEFT)
        self.lblMessage.grid(row=2, column=1, sticky='nw', pady=5, padx=10)
        self.lblUser = Label(self, bg=Midnight.white, text = user, font = ('Segoe UI', 11, 'italic'))
        self.lblUser.grid(row=1, column=1, sticky='w' if user != 'Me' else 'e')
        self.frame.config(width=300)

