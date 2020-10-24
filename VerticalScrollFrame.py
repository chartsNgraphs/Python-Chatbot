import tkinter as tk
from tkinter import *
import time
import ColorClass

class AutoScrollbar(Scrollbar):
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError("cannot use pack with this widget")
    def place(self, **kw):
        raise TclError("cannot use place with this widget")

class vertScrollFrame(Frame):
    def __init__(self, master, fillcolor=None):
        self.colors = ColorClass.Midnight
        if fillcolor:
            self.fillcolor=fillcolor
        else: 
            self.fillcolor=self.colors.ghostwhite
        Frame.__init__(self, master)
        self.vscrollbar = AutoScrollbar(master)
        self.vscrollbar.grid(row=0, column=1, sticky=N+S+E)
        self.config(bg=self.fillcolor)
        self.canvas = Canvas(master, yscrollcommand=self.vscrollbar.set)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.canvas.config(bd=0, highlightthickness=0, bg=self.fillcolor)
        self.vscrollbar.config(command=self.canvas.yview)
        # make the canvas expandable
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        # create frame inside canvas
        self.frame = Frame(self.canvas)
        self.frame.bind("<Configure>", self.reset_scrollregion)
        self.frame.config(bg=self.fillcolor)
        self.canvas.bind('<Enter>', self._bound_to_mousewheel)
        self.canvas.bind('<Leave>', self.leave_unbind)
        self.canvas.bind_all("<MouseWheel>", self.default_mousewheel)
        self.frame.columnconfigure(0, weight=1)
    def update(self):
        self.mywindow = self.canvas.create_window(0, 0, anchor=NW, window=self.frame)
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        if self.frame.winfo_reqwidth() != self.canvas.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canvas.config(width = self.frame.winfo_reqwidth())
        if self.frame.winfo_reqheight() != self.canvas.winfo_height():
            # update the canvas's height to fit the inner frame
            self.canvas.config(height = self.frame.winfo_reqheight())

    def reset_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def destroy(self):
        print("nope")

    def FrameWidth(self, event):
        canvas_height = event.height
        self.canvas.itemconfig(self.mywindow,  height=canvas_height)

    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def default_mousewheel(self, event):
        if self.vscrollbar.winfo_ismapped():
            self._bound_to_mousewheel('<Enter>')
        
    def leave_unbind(self, event):
        self.canvas.unbind_all("<MouseWheel>")      

    def _bound_to_mousewheel(self, event):
        if self.vscrollbar.winfo_ismapped():
            self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        else:
            pass

    def _unbound_to_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.bind_all("<MouseWheel>", self.default_mousewheel)
        
    def _on_mousewheel(self, event):
        if self.vscrollbar.winfo_ismapped():
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            self._unbound_to_mousewheel('<Leave>')
