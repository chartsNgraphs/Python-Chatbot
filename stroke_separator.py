import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import ColorClass

class strokeSeparator(Frame):
    def __init__(self, parent=None, length=None, width=None, color=None, orientation=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.colors = ColorClass.Midnight()
        self.orientation = orientation
        self.length = length
        self.width=width
        if color == None: 
            self.theme = self.colors.fadednavy
        else:
            self.theme = color
        self.config(bd=0, highlightthickness=0, bg=self.theme)
        if self.orientation == 'vertical':
            self.config(height=self.length, width=self.width)
        else:
            self.config(height=self.width, width=self.length)
        print(str(self.length))

class DynamicStrokeSeparator(Frame):
    def __init__(self, parent=None, width=None, color=None, orientation=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.colors = ColorClass.ColorCube()
        self.orientation = orientation
        self.width=width
        if color == None: 
            self.theme = self.colors.fadednavy
        else:
            self.theme = color
        self.config(bd=0, highlightthickness=0, bg=self.theme)
        if self.orientation == 'vertical':
            self.config( width=self.width)
        else:
            self.config(height=self.width)
