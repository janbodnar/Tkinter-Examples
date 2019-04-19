#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we use the Label
widget to show an image.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.ttk import Frame, Label
import sys

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.loadImage()
        self.initUI()


    def loadImage(self):
        try:
            self.img = Image.open("tatras.jpg")

        except IOError:
            print("Unable to load image")
            sys.exit(1)


    def initUI(self):

        self.master.title("Label")

        tatras = ImageTk.PhotoImage(self.img)
        label = Label(self, image=tatras)

        # reference must be stored
        label.image = tatras

        label.pack()
        self.pack()


    def setGeometry(self):

        w, h = self.img.size
        self.master.geometry(("%dx%d+300+300") % (w, h))


def main():

    root = Tk()
    ex = Example()
    ex.setGeometry()
    root.mainloop()


if __name__ == '__main__':
    main()
