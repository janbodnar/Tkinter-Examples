#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

This program uses the padx and pady
widget attributes.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Frame, Button
from tkinter import BOTH, LEFT, TOP

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Padding")
        self.pack(fill=BOTH)

        frame = Frame(self, bd=5)
        frame.pack()

        btn1 = Button(frame, text='Button')
        btn1.pack(side=LEFT, padx=5)

        btn2 = Button(frame, text='Button')
        btn2.pack(side=LEFT, padx=5)

        frame2 = Frame(self)
        frame2.pack()

        btn1 = Button(frame2, text='Button')
        btn1.pack(side=TOP, pady=15)

        btn2 = Button(frame2, text='Button')
        btn2.pack(side=TOP, pady=15)

        self.pack()

def main():

    root = Tk()
    root.geometry("300x250+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
