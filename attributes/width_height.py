#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

This program uses width and height
attributes to set the size of widgets.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Frame, Button
from tkinter import BOTH, LEFT

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Width and height")
        self.pack(fill=BOTH)

        frame = Frame(self, borderwidth=10)
        frame.pack()

        btn1 = Button(frame, text='Button')
        btn1.pack(side=LEFT, padx=5)

        btn2 = Button(frame, text='Button', width=8)
        btn2.pack(side=LEFT, padx=5)

        btn3 = Button(frame, text='Button', width=5, height=4)
        btn3.pack(side=LEFT)

        self.pack()

def main():

    root = Tk()
    root.geometry("+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
