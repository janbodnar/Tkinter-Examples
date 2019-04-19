#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we use the state attribute.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, BOTH, NORMAL, ACTIVE, DISABLED
from tkinter.ttk import Frame, Label


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Fonts")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)

        txt = "Today is a beautiful day"

        label1 = Label(self, text=txt, state=NORMAL)
        label1.grid(row=0, column=0)

        label2 = Label(self, text=txt, state=ACTIVE)
        label2.grid(row=0, column=1)

        label3 = Label(self, text=txt, state=DISABLED)
        label3.grid(row=0, column=2)


def main():

    root = Tk()
    ex = Example()
    root.geometry("+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
