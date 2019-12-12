### pocketlad ###
# This module does all the quotes 'n shit.

import time
import os
import sys
import itertools
import threading
import random

page = open("syquot.txt", 'r')

lines = page.readlines()


from time import sleep
from os import system, name

def clear():
    if name == ('nt'):
        clr = system('cls')
    else:
        clr = system('clear')

def pktlad():
    clear()
    print('Currently, there are only', lines[0], 'quotes from', lines[1],' authors.')
    print('Would you like to receive one? (y/n)')
    ans = input('')

    if ans == 'y':
        quote = random.randint(0, 33)
        print(quote)
        page.close

    elif ans == 'Y':
        quote = random.randint(0, 33)
        print(quote)
        page.close

    else:
        clear()
        print('Would you like to exit? (y/n)')
        ans = input('')
        if ans == 'y':
            print('Exiting...')
            time.sleep(1)
            exit()
        elif ans == 'Y':
            print('Exiting...')
            time.sleep(1)
            exit()
        else:
            print(pktlad())
            

