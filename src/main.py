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

from timer import Timer
from button import StartButton, QuitButton
import config


class Lock(tk.Tk):
    def __init__(self):
        super(Lock, self).__init__()

        self.end_time = None

        # self.bg = 'black'
        # self.fg = 'white'

        self.wm_attributes('-fullscreen', True)
        self.wm_attributes('-topmost', True)
        self.title('Lock')
        self.configure(bg=config.BG)

        self.scale = self.winfo_screenwidth()
        self.font = config.FONT(self.scale // 10)


        self.timer = Timer(self)
        self.timer.place(relx=0.5, rely=0.43, anchor=tk.CENTER)

        self.start_btn = StartButton(self)
        self.start_btn.place(relx=0.5, rely=0.73, anchor=tk.CENTER)

        self.quit_btn = QuitButton(self)
        self.quit_btn.place(relx=1, rely=0, anchor=tk.NE)


if __name__ == '__main__':
    root = Lock()
    root.mainloop()
