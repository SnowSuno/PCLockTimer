import tkinter as tk
import tkinter.font as tkFont
import time
import _thread
# import keyboard as kb
from ctypes import windll
import pyvda


lock = tk.Tk()


class Timer:
    def __init__(self, time):
        self.time = time

    def __str__(self):
        sec = self.time

        hour = sec // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60

        H = str(hour).zfill(2)
        M = str(min).zfill(2)
        S = str(sec).zfill(2)

        return H + ':' + M + ':' + S

    def update(self):
        if self.time > 0:
            self.time -= 1


def time_update(t_init):
    tmr = Timer(t_init)
    while True:
        clock['text'] = tmr
        tmr.update()
        time.sleep(1)

        if tmr.time == 0:
            lock.quit()


def disable_event():
    pass



lock.attributes('-fullscreen', True)
lock.wm_attributes('-topmost', 1)
lock.title('LOCK')
lock.configure(bg='black')




clock_font = tkFont.Font(family='Arial', size=200, weight='bold')
clock = tk.Label(lock, text='00:00', font=clock_font, bg='black', fg='white')

clock.grid(column=0, row=0)

lock.columnconfigure(0, weight=1)
lock.rowconfigure(0, weight=1)





_thread.start_new_thread(time_update, (10,))
# _thread.start_new_thread(desktop_fix, ())


def pin():
    pyvda.AppView.current().pin()
    lock.overrideredirect(True)
    lock.protocol("WM_DELETE_WINDOW", disable_event)

def main():
    windll.user32.BlockInput(True)

    lock.after(1, pin)
    lock.mainloop()

    windll.user32.BlockInput(False)


main()
