#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

This program uses relief styles.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Frame, Label
from tkinter import BOTH, LEFT, FLAT, SUNKEN, RAISED, GROOVE, RIDGE

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Reliefs")
        self.pack(fill=BOTH)

        frame = Frame(self, borderwidth=10)
        frame.pack()

        lbl1 = Label(frame, bg='LightSteelBlue3', width=15, height=10, relief=FLAT)
        lbl1.pack(side=LEFT, padx=3)

        lbl2 = Label(frame, bg='LightSteelBlue3', bd=2, width=15,
            height=10, relief=SUNKEN)
        lbl2.pack(side=LEFT)

        lbl3 = Label(frame, bg='LightSteelBlue3', bd=2, width=15,
            height=10, relief=RAISED)
        lbl3.pack(side=LEFT, padx=3)

        lbl4 = Label(frame, bg='LightSteelBlue3', bd=3, width=15,
            height=10, relief=GROOVE)
        lbl4.pack(side=LEFT)

        lbl5 = Label(frame, bg='LightSteelBlue3', bd=3, width=15,
            height=10, relief=RIDGE)
        lbl5.pack(side=LEFT, padx=3)

        self.pack()

def main():

    root = Tk()
    root.geometry("+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
