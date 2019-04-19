#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this program, we create
a popup menu.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Frame, Menu

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Popup menu")
        self.menu = Menu(self.master, tearoff=0)
        self.menu.add_command(label="Beep", command=self.bell)
        self.menu.add_command(label="Exit", command=self.onExit)

        self.master.bind("<Button-3>", self.showMenu)
        self.pack()


    def showMenu(self, e):

        self.menu.post(e.x_root, e.y_root)


    def onExit(self):

        self.quit()


def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
