#####################################                                       maybespyware                                            #################################

# My shitty meme project. 
#
# Made by maesyki
# 
# You're not supposed to read this, right?

# Imports
import time
import os
import maybespyware.mbspy.mddr.pocketlad
import maybespyware.mbspy.mddr.vv
import maybespyware.mbspy.sys.sysinfo
import sys
import itertools
import threading

# NOTE
# for when you have to setup
# import tkinter
# package = tkinter
# try:
#   return __import__(package)
# except importerror:
#   return none

from maybespyware.mbspy.mddr.vv import *
from maybespyware.mbspy.mddr.pocketlad import *
from maybespyware.mbspy.sys.sysinfo import *
from time import sleep
from os import system, name

def clear():
    if name == ('nt'):
        clr = system('cls')
    else:
        clr = system('clear')



if os.geteuid() != 0:
    done = True
    clear()
    sleep(0.1)
    clear()
    sleep(0.1)
    clear()
    print('Please run this script as root. Use the sudo command to do so. Thanks.')
    sleep(2)
    exit()


done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone! Starting now.')

t = threading.Thread(target=animate)
t.start()


# System Info
if name == 'posix':
    OS = 'macOS'
else:
    OS = 'Windows'

#loading
clear()
done = True
sleep(0.5)

clear()

# Welcome Screen and Options
def optmenu():
    print('Choose one option by typing the number corresponding to it.')
    print('Quotes // (1)')
    print('"Special" Surprise // NOT FUNCTIONAL // (2)')
    print('Please select a number')
    optans = input('')
    if optans == '1':
        maybespyware.mbspy.mddr.pocketlad.pktlad()
    elif optans == '2':
        maybespyware.mbspy.mddr.vv.injector()
    else:
        clear()
        print('I said select a number. Lets retry that.')
        sleep(2)
        clear()
        optmenu()


        
def welscr():
    print('///////////////////// maybespyware //////////////////////////// ', version, ' //////////////////////////////')
    print('')
    print('')
    print("Hello, and welcome to my script, which might just be spyware. It probably isn't though. This is a beta version, so it might not even work lol")
    print('I recommend you check for updates at my GitHub repository: https://github.com/maesyki/maybespyware')
    print('')
    input('Please press enter to continue ')

    clear()

    optmenu()

welscr()















