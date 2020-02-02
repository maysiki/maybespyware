injector_version = 'North Korea'

import tkinter
from tkinter import *
import time
import os
import sys
import random
from lib.sysinfo import version

wcount = 50

def spector():

    def windowloop():
        for i in range(wcount):
            inRoot = Tk()
            inRoot.title('most likely spyware time')
            inRoot.configure(bg = 'gray10')

            title = Label(inRoot, text = 'spyware time!', bg = 'gray15', fg = 'white', font = "Arial 32 bold")
            title.grid(row = 0, column = 1, sticky = NW)
        
    windowloop()

    def titlescreen():
        tiscreen = Tk()
        tiscreen.title('computer hacked noot noot >:D')
        tiscreen.overrideredirect(True)
        title = Label(tiscreen, text = 'computer hacked n00t n00t >:D', bg = 'gray15', fg = 'white', font = "Arial 32 bold")
        title.grid(row = 0, column = 1, sticky = NW)

    def password():
        root = Tk()
        root.overrideredirect(True)
        title = Label(root, text = 'guess the password lol', bg = 'gray15', fg = 'white', font = "Arial 32 bold")
        title.grid(row = 0, column = 1, sticky = NW)

        

    
    titlescreen()
