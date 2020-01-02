import tkinter
from tkinter import *
import time
import os
import sys
from lib.sysinfo import version
import lib.title
from lib.title import *


def clear():
    if os.name == ('nt'):
        clr = os.system('cls')
    else:
        clr = os.system('clear')

clear()

TSS()

title()

