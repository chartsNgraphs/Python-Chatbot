from tkinter import *
from ColorClass import Midnight
from tkinter import scrolledtext
from ChatBubble import SquareBubble
from VerticalScrollFrame import vertScrollFrame
from IconButton import IconButton
from Engine import ConversationalEngine
from Conversation import Conversation
from ScrollableFrame import ScrollableFrame
from stroke_separator import strokeSeparator, DynamicStrokeSeparator


class Chatbot(Frame):
    def __init__(self, parent, app, trainingdata: str, articulationdata: str):
        Frame.__init__(self, parent)
        self.parent = parent
        self.app = app
        self.trainingdata = trainingdata
        self.articulationdata = articulationdata
        self.config(bg=Midnight.white)
        self.sendimagedata = b'iVBORw0KGgoAAAANSUhEUgAAACIAAAAiCAMAAAANmfvwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAwUExURQAAADBAYDBAWDA6Wiw8WC09WS09WC49WS48WC49WS89Wi09WS4+WS49WS49WS49WYbQlfkAAAAPdFJOUwAQIDBAUGBwgI+fv8/f76R8WAwAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAC2SURBVDhPrZFLAoMgDAX9IdAouf9tS83TAgmsnI0CoyM4vYPDdUDiOOO2R2LmuGJg81OYacfQQpRMv/coWVow11AovV6lMJ9Gr1EyqqcV1bOUpndgUlH2FreHD2GhRO9vcyHSiWXB2l+meal1nvPqfKQD20hU/OJ52Xx4loQURKgfKyAvX0L2wZQF27gLF5ZyF4BSqj1cNEpVAJXSFMBf0QVwK1YBiGIXQFa6BZAGBbAPCu8xTV88KBhwUQ3P3AAAAABJRU5ErkJggg=='
        self.scrollframecontainter = Frame(self, relief=FLAT, bg=Midnight.white)
        self.scrollframecontainter.grid(row=1, column=1, sticky='nsew', columnspan=2)
        self.scrollframecontainter.rowconfigure(0, weight=1)
        self.scrollframecontainter.columnconfigure(1, weight=1)
        self.scrollframe = vertScrollFrame(self.scrollframecontainter, fillcolor=Midnight.white)
        self.scrollframe.grid(row=0, column=1, sticky='nsew', columnspan=2)
        self.entry = Entry(self,  width=50, font=('Segoe UI', 13, 'roman'), relief=FLAT, bd=1, highlightthickness=1, highlightcolor=Midnight.navy, highlightbackground=Midnight.fadednavy)
        self.entry.grid(row=3, column=1, padx=2, pady=2)
        self.btnSend = IconButton(self, image=None, fillcolor=Midnight.white, hovercolor=Midnight.staticLighter(Midnight.navy, percent=0.9), imagedata=self.sendimagedata)
        self.btnSend.grid(row=3, column=2)
        self.engine = ConversationalEngine(app=self.app, lemmatize_data=True, filepath=trainingdata)
        self.countBubbles = 1
        self.btnSend.bind('<Button-1>', self.sendEvent)
        self.start()
        self.scrollframe.update()
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.config(width = 345, height=600)
        self.grid_propagate(False)
        self.entry.bind('<Return>', self.sendEvent)
        self.scrollframe.frame.columnconfigure(2, weight=1)
        self.stroke = strokeSeparator(self.scrollframe.frame, length=330, width=1, color= Midnight.white, orientation='horizontal')
        self.stroke.grid(row=0, column=1, columnspan=2, sticky='n')
        self.scrollframe.canvas.config(width=330)
        self.entry.focus_set()
    
    def start(self):
        self.currentConversation = Conversation(self.app, self.engine, trainingdata=self.trainingdata, articulationdata=self.articulationdata)
        self.respond(None, force=True)
    
    def send(self, utterance):
        self.entry.delete(0, END)
        userbubble = SquareBubble(self.scrollframe.frame, text=utterance, user = 'Me', fill=Midnight.fadednavy)
        userbubble.grid(row=self.countBubbles + 1, column=1, sticky='e', pady=3, padx=(5, 5), columnspan=2)
        self.countBubbles += 1
        self.respond(utterance)
    
    def respond(self, utterance, force=False):
        if force == False:
            payload = self.currentConversation.interact(utterance, returnPayload=True)
            response = payload.get('articulation')
        else:
            response = "Hi! Ask me anything:"
        botBubble = SquareBubble(self.scrollframe.frame, text=response, user = 'Bot', fill=Midnight.seaweed)
        botBubble.grid(row=self.countBubbles + 1, column=1, sticky='w', pady=3, padx=(5, 5))
        self.countBubbles += 1

    def sendEvent(self, event):
        cur_inp = self.entry.get().strip()
        if cur_inp == "":
            return
        self.send(cur_inp)
        self.entry.delete(0, END)
        self.scrollframe.update()
        self.scrollframe.canvas.yview_moveto('1.0')

