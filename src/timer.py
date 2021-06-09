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


class Timer(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


    class Digits(tk.Entry):
        SEL_COL = 'gray25'

        def __init__(self, root, frame):
            self.value = tk.StringVar()
            self.value.old = '00'

            super().__init__(
                frame, width=2, font=root.font,
                bg=root.bg, fg=root.fg, bd=0,
                textvariable=self.value,
                insertbackground=self.SEL_COL, selectbackground=self.SEL_COL,
                disabledbackground=root.bg, disabledforeground=root.fg,
                insertwidth=root.font_size*3, insertofftime=0
            )

            self.value


