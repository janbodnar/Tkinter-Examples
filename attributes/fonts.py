#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we display text in three
different fonts.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Notebook, Style

from tkinter.font import Font

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Fonts")
        self.pack(fill=BOTH, expand=True)

        txt = "Today is a beautiful day"

        myfont = Font(family="Ubuntu Mono", size=16)
        label1 = Label(self, text=txt, font=myfont)
        label1.grid(row=0, column=0)

        label2 = Label(self, text=txt, font="TkTextFont")
        label2.grid(row=1, column=0)

        label3 = Label(self, text=txt, font=('Times', '18', 'italic'))
        label3.grid(row=2, column=0)


def main():

    root = Tk()
    ex = Example()
    root.geometry("+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
