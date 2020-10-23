import tkinter as tk
from tkinter import *
import time
from PIL import Image, ImageTk
import numpy as np
import os
import ColorClass

class IconButton(Frame):
    def __init__(self, parent=None, image=None, fillcolor=None, hovercolor=None, foreground=None, hoverforeground=None, bordercolor=None, activebordercolor=None, text=None, imagedata=None):
        
        if imagedata ==None: 
            self.iconPIL = Image.open(image)
            self.icon = ImageTk.PhotoImage(self.iconPIL)
        else:
            self.icon = PhotoImage(data = imagedata)
        Frame.__init__(self, parent)
        self.config(cursor="hand2")
        self.colors2=ColorClass.Midnight()
        self.fillcolor = fillcolor
        self.hovercolor=hovercolor
        self.foreground=foreground
        self.hoverforeground = hoverforeground
        self.bordercolor=bordercolor
        self.activebordercolor=activebordercolor
        self.parent=parent
        self.text=text
        self.config(highlightbackground=self.bordercolor, highlightcolor=self.bordercolor, bg=self.fillcolor)
        self.label = Label(self, relief=FLAT)
        self.label.config(image = self.icon,  bg = self.fillcolor,  compound = 'left', foreground = self.foreground, wraplength=71, justify=CENTER, text=self.text, font=("Segoe UI", 12, 'roman'))
        self.label.grid(row=1, column=1, sticky='nsew')
        self.bind('<Enter>', self.hover)
        self.bind('<Leave>', self.leave)
        self.rowconfigure(1, weight=1)

    def hover(self, event):
            self.config(highlightbackground=self.activebordercolor, highlightcolor=self.activebordercolor, bg=self.hovercolor)
            self.label.config(bg = self.hovercolor, foreground = self.hoverforeground)
    def leave(self, event):
            self.config(highlightbackground=self.bordercolor, highlightcolor=self.bordercolor, bg=self.fillcolor)
            self.label.config(bg = self.fillcolor, foreground=self.foreground)

    def bind(self, event, command):
        self.label.bind(event, command)
    
    def changeIcon(self, imagepath=None, imageData = None):
        if imagepath != None:
            self.iconPIL = Image.open(imagepath)
            self.icon = ImageTk.PhotoImage(self.iconPIL)
            
            self.label.config(image = self.icon)
        elif imageData != None:
            self.icon = PhotoImage(data = imageData)
            self.label.config(image = self.icon)
        else: 
            return

    def changeColors(self, newfillcolor, newhovercolor, newforeground, newhoverforeground, newbordercolor, newactivebordercolor):
        self.fillcolor = newfillcolor
        self.hovercolor=newhovercolor
        self.foreground=newforeground
        self.hoverforeground = newhoverforeground
        self.bordercolor=newbordercolor
        self.activebordercolor=newactivebordercolor
        self.config(bg=self.fillcolor, highlightcolor = newactivebordercolor, highlightbackground = newbordercolor)
        self.label.config(bg=self.fillcolor)
