import tkinter
from tkinter import *
import time
import os
import sys
import lib.pktlad
from lib.pktlad import *
from lib.sysinfo import version

def clear():
    if os.name == ('nt'):
        clr = os.system('cls')
    else:
        clr = os.system('clear')


def title():
    root = Tk()
    root.resizable(0, 0)
    root.geometry('450x225')
    root.title('maybespyware '+ version)
    root.configure(background = 'gray15')
   
   
    # unitedshitofamerica = PhotoImage(file = 'lib/amazing.gif')
    # usa = Label(root, image = unitedshitofamerica, bg = 'gray15')
    # usa.grid(row = 0, column = 1, sticky = W)
   

    title = Label(root, text = 'maybespyware', bg = 'gray15', fg = 'white', font = "Arial 32 bold")
    title.grid(row = 0, column = 1, sticky = NW)

    # separator = Label(root, text = '---------------------------------------------------------------------------------------------------------------------------------------------', bg = 'gray15', fg = 'white')
    # separator.grid(row = 1, sticky = W)

    # versionlabel = Label(root, text = version, bg = 'gray15', fg = 'white', font = "Arial 8 bold")
    # versionlabel.grid(row = 1, column = 0, sticky = NW)

    w = Label(root, text = 'welcome', bg = 'gray15', fg = 'white', font = "Arial 20 bold")
    w.grid(row = 2, column = 1, sticky = W)

    welcome = Label(root, text = 'please select one of the following options', bg = 'gray15', fg = 'white', font = "Arial 15")
    welcome.grid(row = 3, column = 1, sticky = W)

    blank = Label(root, text = ' ', bg = 'gray15', font = "Arial 22")
    blank.grid(row = 4, column = 0)

    q = Label(root, text = 'Quotes', bg = 'gray15', fg = 'white', font = 'Arial 20 bold')
    q.grid(row = 5, column = 1, sticky = W)


    qselect = Button(root, text = 'Here', width = 4, activebackground = 'gray14', bg = 'gray14', fg = 'white', activeforeground = 'white', command = pktlad)
    qselect.configure(highlightthickness = 0, highlightbackground = 'gray15')
    qselect.grid(row = 6, column = 1, sticky = W)


    root.mainloop()