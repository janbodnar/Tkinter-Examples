#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

This program uses sets various background
colours with bg attribute.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Frame, Label
from tkinter import BOTH, LEFT

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Background colours")
        self.pack(fill=BOTH)

        frame = Frame(self, borderwidth=10)
        frame.pack()

        lbl1 = Label(frame, bg='SlateGray3', width=15, height=10)
        lbl1.pack(side=LEFT, padx=3)

        lbl2 = Label(frame, bg='SlateGray4', width=15, height=10)
        lbl2.pack(side=LEFT)

        lbl3 = Label(frame, bg='DarkSeaGreen3', width=15, height=10)
        lbl3.pack(side=LEFT, padx=3)

        lbl4 = Label(frame, bg='DarkSeaGreen4', width=15, height=10)
        lbl4.pack(side=LEFT)

        self.pack()

def main():

    root = Tk()
    root.geometry("+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
