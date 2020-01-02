import tkinter
from tkinter import *
import time
import os
import sys
import lib.pktlad
from lib.pktlad import *
from lib.sysinfo import version
from lib.spector import injector_version
from os import name
from platform import system

ios = system()

def clear():
    

    if os.name == ('nt'):
        clr = os.system('cls')
    else:
        clr = os.system('clear')

def TSS():

    if ios == 'Darwin':
        clear()
        os.system('sudo systemsetup -setremotelogin on')
        print("You're not supposed to see this. Please contact the developer lol.")

    elif ios == 'Windows':
        pass

    elif ios == 'Linux':
        print('TSS complete!')
        pass

def ghlink():

    def ntsupfunc():
        notsupported = Tk()
        notsupported.resizable(0, 0)
        notsupported.geometry('255x20')
        notsupported.title('maybespyware '+ version)
        notsupported.configure(background = 'gray15')

        w = 255
        h = 20
        ws = notsupported.winfo_screenwidth() # width of the screen
        hs = notsupported.winfo_screenheight() # height of the screen
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        notsupported.geometry('%dx%d+%d+%d' % (w, h, x, y))

        ntsup = Label(notsupported, text = ios + ' is not supported by this function.', bg = 'gray15', fg = 'white')
        ntsup.pack()

        notsupported.mainloop()

    
    if ios == 'Darwin':
        clear()
        os.system('open https://github.com/maesyki/maybespyware/releases')

    elif ios == 'Windows':
        os.system('start "https://github.com/maesyki/maybespyware/releases"')
        pass

    elif ios == 'Linux':
        ntsupfunc()


        pass
       
def title():

    # NOTE 
    # comment out for public release
    # print('running pk '+ pk_version)
    # print('running injector ' + injector_version)

    root = Tk()
    root.resizable(0, 0)
    root.geometry('500x230')
    w = 500
    h = 230
    root.title('maybespyware '+ version)
    root.configure(background = 'gray15')
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


    title = Label(root, text = 'maybespyware', bg = 'gray15', fg = 'white', font = "Arial 32 bold")
    title.grid(row = 0, column = 1, sticky = NW)

    gh = Label(root, text = 'Github', bg = 'gray15', fg = 'white', font = 'Arial 20 bold')
    gh.grid(row = 1, column = 1, sticky = W)

    Github = Button(root, text = 'Here', width = 6, activebackground = 'gray14', bg = 'gray14', fg = 'white', activeforeground = 'white', command = ghlink)
    Github.configure(highlightthickness = 0, highlightbackground = 'gray15')
    Github.grid(row = 2, column = 1, sticky = W)

    blank = Label(root, text = ' ', bg = 'gray15', font = "Arial 22")
    blank.grid(row = 3, column = 0)

    q = Label(root, text = 'Quotes', bg = 'gray15', fg = 'white', font = 'Arial 20 bold')
    q.grid(row = 4, column = 1, sticky = W)

    qselect = Button(root, text = 'Here', width = 6, activebackground = 'gray14', bg = 'gray14', fg = 'white', activeforeground = 'white', command = pktlad)
    qselect.configure(highlightthickness = 0, highlightbackground = 'gray15')
    qselect.grid(row = 5, column = 1, sticky = W)


    root.mainloop()