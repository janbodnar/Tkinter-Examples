#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this program, we show various
message boxes.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button
from tkinter import messagebox as mbox

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Message boxes")
        self.pack()

        error = Button(self, text="Error", command=self.onError)
        error.grid(padx=5, pady=5)
        warning = Button(self, text="Warning", command=self.onWarn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1)


    def onError(self):

        mbox.showerror("Error", "Could not open file")

    def onWarn(self):

        mbox.showwarning("Warning", "Deprecated function call")

    def onQuest(self):

        mbox.askquestion("Question", "Are you sure to quit?")

    def onInfo(self):

        mbox.showinfo("Information", "Download completed")


def main():

    root = Tk()
    ex = Example()
    root.geometry("300x150+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
