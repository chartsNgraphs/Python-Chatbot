from tkinter import Tk
from Chatbot import Chatbot

def main():
    root = Tk()
    bot = Chatbot(root, app=None, trainingdata='training.csv', articulationdata='articulations.csv')
    bot.pack()
    root.rowconfigure(1, weight=1)
    root.mainloop()
if __name__=="__main__":
    main()