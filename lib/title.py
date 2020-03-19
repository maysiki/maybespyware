import tkinter
from tkinter import *
from tkinter import ttk
import time
import os
import sys
import lib.pktlad
from lib.pktlad import *
from lib.sysinfo import version
from lib.spector import *
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
        clear()

    elif ios == 'Windows':
        pass

    elif ios == 'Linux':
        pass

def ghlink():

    def ntsupfunc():
        notsupported = Tk()
        notsupported.resizable(0, 0)
        notsupported.geometry('255x20')
        notsupported.title('maybespyware '+ version)
        notsupported.configure(background = 'gray8')

        w = 255
        h = 20
        ws = notsupported.winfo_screenwidth() # width of the screen
        hs = notsupported.winfo_screenheight() # height of the screen
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        notsupported.geometry('%dx%d+%d+%d' % (w, h, x, y))

        ntsup = Label(notsupported, text = ios + ' is not supported by this function.', bg = 'gray8', fg = '#DBDBDB')
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
    


    ########################################### NOTE ####################################################
    ############# I have no clue why this works, but it does. Don't touch it, i guess. ##################
    #####################################################################################################





    root = Tk()
    root.resizable(0, 0)
    root.geometry('50x50')
    w = 400
    h = 150
    root.title('maybespyware '+ version)
    root.configure(background = 'gray8')
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    z = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, z, y))
    # print('Note! If the buttons turn #DBDBDB, that is a bug. I have no clue how to fix it. Please ping me a message if its too annoying')

    topframe = Frame(root, bg = '#1E1E1E', width = 300, height = 50)
    topframe.pack()

    bottomestframe = Frame(root, bg = '#1E1E1E', width = 300, height = 50)
    bottomestframe.pack(side = BOTTOM)

    bottomframe = Frame(root, bg = 'gray8', width = 300, height = 50)
    bottomframe.pack(side = BOTTOM)

    title = Label(topframe, text = 'maybespyware', bg = 'gray8', fg = '#DBDBDB', font = "Arial 32 bold")
    title.pack(side = LEFT, expand = True, fill = X)

    blank0 = Label(bottomframe, text = '  ', bg = 'gray8', font = "Arial 18")
    blank0.pack(side = LEFT)

    gh = Label(bottomframe, text = 'Github', bg = 'gray8', fg = '#DBDBDB', font = 'Arial 20 bold')
    gh.pack(side = LEFT)

    blank1 = Label(bottomframe, text = '    ', bg = 'gray8', font = "Arial 18")
    blank1.pack(side = LEFT)

    q = Label(bottomframe, text = 'Quotes', bg = 'gray8', fg = '#DBDBDB', font = 'Arial 20 bold')
    q.pack(side = LEFT)

    blank2 = Label(bottomframe, text = '   ', bg = 'gray8', font = "Arial 18")
    blank2.pack(side = LEFT)

    spytext = Label(bottomframe, text = 'Spyware', bg = 'gray8', fg = '#DBDBDB', font = 'Arial 20 bold')
    spytext.pack(side = LEFT)

    Github = Button(bottomestframe, text = 'Here', width = 6, activebackground = 'gray14', bg = 'gray14', fg = '#DBDBDB', activeforeground = '#DBDBDB', command = ghlink)
    Github.configure(highlightthickness = 0, highlightbackground = 'gray8')
    Github.pack(side = LEFT)

    blank3 = Label(bottomestframe, text = '       ', bg = 'gray8', font = "Arial 18")
    blank3.pack(side = LEFT)

    qselect = Button(bottomestframe, text = 'Here', width = 6, activebackground = 'gray14', bg = 'gray14', activeforeground = '#DBDBDB', fg = '#DBDBDB', command = pktlad)
    qselect.configure(highlightthickness = 0, highlightbackground = 'gray8')
    qselect.pack(side = LEFT)

    blank4 = Label(bottomestframe, text = '       ', bg = 'gray8', font = "Arial 18")
    blank4.pack(side = LEFT)

    sselect = Button(bottomestframe, text = 'Here', width = 6, activebackground = 'gray14', bg = 'gray14', activeforeground = '#DBDBDB', fg = '#DBDBDB', command = spector)
    sselect.configure(highlightthickness = 0, highlightbackground = 'gray8')
    sselect.pack(side = LEFT)

    root.mainloop()