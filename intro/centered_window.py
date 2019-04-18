#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

This script centers a small
window on the screen.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, BOTH
from tkinter.ttk import Frame

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Centered window")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()


    def centerWindow(self):

        w = 290
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():

    root = Tk()
    ex = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
