#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we show how to
use the Listbox widget.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Listbox")

        self.pack(fill=BOTH, expand=1)

        acts = ['Scarlett Johansson', 'Rachel Weiss',
            'Natalie Portman', 'Jessica Alba']

        lb = Listbox(self)

        for i in acts:
            lb.insert(END, i)

        lb.bind("<<ListboxSelect>>", self.onSelect)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()


    def onSelect(self, val):

        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)


def main():

    root = Tk()
    ex = Example()
    root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
