from datetime import datetime, timedelta
import tkinter as tk
from tkinter.font import Font
import time
import keyboard as kb
import pyvda
import sys

class Lock(tk.Tk):
    def __init__(self, end_timestamp=time.time()):
        super(Lock, self).__init__()

        self.end_time = datetime.fromtimestamp(end_timestamp)

        self.attributes('-fullscreen', True)
        self.wm_attributes('-topmost', 1)
        self.title('Lock')
        # self.configure(bg='black')

        self.start_screen = tk.Frame(self)
        self.timer_screen = tk.Frame(self)

        self.start_screen.grid(row=0, column=0, sticky='news')
        self.timer_screen.grid(row=0, column=0, sticky='news')

        self.start_screen.configure(bg='black')
        self.timer_screen.configure(bg='black')

        startbtn = tk.Button(self.start_screen, text='start', command=self.start_timer)
        startbtn.pack()



        timer_font = Font(family='Arial', size=200, weight='bold')
        self.timer = tk.Label(self.timer_screen, text='00:00:00', font=timer_font, bg='black', fg='white')
        self.timer.grid(column=0, row=0)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


    def start_timer(self):
        self.timer_screen.tkraise()

    def run(self):
        # self.after(0, self._update)
        # self.after(1, self._block)

        self.mainloop()
        # self.unblock()


if __name__ == '__main__':

    lock = Lock()
    lock.run()

