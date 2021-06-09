from datetime import datetime, timedelta
import tkinter as tk
from tkinter.font import Font
import time
import keyboard as kb
import pyvda
import sys
import _ctypes
import _thread
import pythoncom

import winshell
import os

class Lock(tk.Tk):
    def __init__(self):
        super(Lock, self).__init__()

        self.end_time = None

        self.bg = 'black'
        self.fg = 'white'

        self.wm_attributes('-fullscreen', True)
        self.wm_attributes('-topmost', True)
        self.title('Lock')
        self.configure(bg=self.bg)

        font_size = self.winfo_screenwidth() // 10
        self.font = Font(family='Consolas', size=font_size, weight='normal')


