### pocketlad ###
# This module does all the quotes 'n shit.

import time
import os
import sys
import itertools
import threading
import random
import tkinter

from time import sleep
from os import system, name

page = open("syquot.txt", 'r')

lines = page.readlines()

def clear():
    if name == ('nt'):
        clr = system('cls')
    else:
        clr = system('clear')

def quotegen():
    clear()
    quote = random.randint(3, 32)
    print(lines[quote])
    print('')
    print('More quotes? (y/n)')
    repeatans = input('')
    if repeatans == 'y':
        quotegen()
    elif repeatans == 'Y':
        quotegen()
    else:
        clear()
        print('Do you want to quit? (y/n)')
        ans = input('')
        if ans == 'y':
            page.close()
            exit()
        elif ans == 'Y':
            page.close()
            exit()
        else:
            print(pktlad())
        



def pktlad():
    clear()
    print('These quotes are home-grown and grassfed. Please enjoy.')
    print("")
    print('Would you like to receive one? (y/n)     ')
    ans = input('')

    if ans == 'y':
        quotegen()

    elif ans == 'Y':
        quotegen()
        page.close

    else:
        clear()
        print('Would you like to exit? (y/n)     ')
        ans = input('')
        if ans == 'y':
            print('Exiting...')
            exit()

        elif ans == 'Y':
            print('Exiting...')
            exit()
        else:
            print(pktlad())
            

