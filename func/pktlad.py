import tkinter
from tkinter import *
import time
import os
import sys
import random
from func.sysinfo import version

from time import sleep
from os import system, name


page = open("syquot.txt", 'r')

lines = page.readlines()

def clear():
    if name == ('nt'):
        clr = system('cls')
    else:
        clr = system('clear')

def pktlad():

    pktladroot = Tk()
    pktladroot.resizable(0, 0)
    pktladroot.geometry('700x100')
    pktladroot.title('maybespyware '+ version)
    pktladroot.configure(background = 'gray15')

    def quoteloop():
        quote = random.randint(3, 32)

        diquote = Label(pktladroot, text = lines[quote], bg = 'gray15', fg = 'white', font = 'Arial 14 italic')
        diquote.grid(row = 0, column = 1, sticky = NW)

        blank = Label(pktladroot, text = '', bg = 'gray15')
        blank.grid(row = 0, column = 0)

        moreb = Button(pktladroot, text = 'More?', width = 5, activebackground = 'gray14', bg = 'gray14', fg = 'white', activeforeground = 'white', command = quoteloop)
        moreb.configure(highlightthickness = 0, highlightbackground = 'gray15')
        moreb.grid(row = 1, column = 1, sticky = W)
    
    quoteloop()

    pktladroot.mainloop()

