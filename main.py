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
import platform

# NOTE
# for when you have to setup
import tkinter

from maybespyware.mbspy.mddr.vv import *
from maybespyware.mbspy.mddr.pocketlad import *
from maybespyware.mbspy.sys.sysinfo import *
from time import sleep
from os import name
from platform import system

def clear():
    if name == ('nt'):
        clr = os.system('cls')
    else:
        clr = os.system('clear')

iios = system()

if name == ('nt'):
    pass
else:
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
    # print('"Special" Surprise // NOT FUNCTIONAL // (2)')
    print('Please select a number')
    optans = input('')
    if optans == '1':
        maybespyware.mbspy.mddr.pocketlad.pktlad()

    # NOTE ADD THIS IN 0.2
    # elif optans == '2':
        # maybespyware.mbspy.mddr.vv.injector()

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
    print('Please enter "u" to run the updater.')
    print('')
    ans = input('Please press enter to continue to script. ')
    if ans == 'u':
        if iios == 'Darwin':
            os.system('git clone https://github.com/maesyki/maybespyware.git')
            
        elif iios == 'Linux':
            os.system('git clone https://github.com/maesyki/maybespyware.git')

        elif iios == 'Windows':
            print('Sorry, the updater is not supported by windows. Please update manually through https://github.com/maesyki/maybespyware/releases')
            time.sleep(5)
            print(welscr())
    else:
        clear()

        optmenu()

welscr()















