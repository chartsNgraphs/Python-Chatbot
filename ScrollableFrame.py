from tkinter import *

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        Frame.__init__(self, container, *args, **kwargs)
        canvas = Canvas(self, bg=self.cget('bg'))
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg = self.cget('bg'))

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        window = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.grid(row=1, column=1, sticky='nsew')
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        canvas.itemconfig(window, width=500)
        self.scrollable_frame.config(width=500)
        scrollbar.grid(row=1, column=2, sticky='ns')