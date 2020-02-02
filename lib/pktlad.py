import tkinter
from tkinter import *
import time
import os
import sys
import random
from lib.sysinfo import version

from time import sleep
from os import system, name

pk_version = 'v1.1.1'

page = open("syquot.txt", 'r')

lines = page.readlines()

def clear():
    if name == ('nt'):
        clr = system('cls')
    else:
        clr = system('clear')

def pktlad():

    pktladroot = Tk()
    pktladroot.geometry('650x80')
    pktladroot.title('maybespyware '+ version)
    pktladroot.configure(background = 'gray10')
    w = 650
    h = 80
    ws = pktladroot.winfo_screenwidth() # width of the screen
    hs = pktladroot.winfo_screenheight() # height of the screen
    z = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    pktladroot.geometry('%dx%d+%d+%d' % (w, h, z, y))
    

    def quoteloop():
        quote = random.randint(3, 36)

        diquote = Label(pktladroot, text = lines[quote], bg = 'gray10', fg = 'white', font = 'Arial 14 italic')
        diquote.grid(row = 0, column = 1, sticky = W)

        blank = Label(pktladroot, text = '', bg = 'gray10')
        blank.grid(row = 0, column = 0)

        moreb = Button(pktladroot, text = 'More?', width = 5, activebackground = 'gray14', bg = 'gray14', fg = 'white', activeforeground = 'white', command = quoteloop)
        moreb.configure(highlightthickness = 0, highlightbackground = 'gray10')
        moreb.grid(row = 1, column = 1, sticky = W)
    
    quoteloop()

    pktladroot.mainloop()

