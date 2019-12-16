import tkinter
from tkinter import *
import time
import os
import sys
from func.sysinfo import version
import func.title
from func.title import *

def clear():
    if os.name == ('nt'):
        clr = os.system('cls')
    else:
        clr = os.system('clear')

clear()

height = 500
width = 700
### WINDOW ELEMENTS ###

title()

