#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we use colorchooser
dialog to change the background of a frame.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Color chooser")
        self.pack(fill=BOTH, expand=1)

        self.btn = Button(self, text="Choose Color",
            command=self.onChoose)
        self.btn.place(x=30, y=30)

        self.frame = Frame(self, border=1,
            relief=SUNKEN, width=100, height=100)
        self.frame.place(x=160, y=30)


    def onChoose(self):

        (rgb, hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)


def main():

    root = Tk()
    ex = Example()
    root.geometry("300x150+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
