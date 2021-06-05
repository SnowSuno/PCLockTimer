import datetime
import tkinter as tk
from tkinter.font import Font
import time
import keyboard as kb
import pyvda

import _thread


class Lock:
    def __init__(self, timestamp=None):
        end_time = datetime.datetime.fromtimestamp(timestamp) if timestamp is not None else None

        self.end_time = end_time

        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.wm_attributes('-topmost', 1)
        self.window.title('Lock')
        self.window.configure(bg='black')

        font = Font(family='Arial', size=200, weight='bold')
        self.timer = tk.Label(self.window, text='', font=font, bg='black', fg='white')
        self.timer.grid(column=0, row=0)

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

    def set_timer(self, interval):
        self.end_time = datetime.datetime.now() + datetime.timedelta(seconds=interval)

    def timestamp(self):
        return time.mktime(self.end_time.timetuple())

    def _update(self):
        seconds_left = (self.end_time - datetime.datetime.now()).total_seconds()
        if seconds_left <= 0:
            self.window.quit()

        hours, remainder = divmod(seconds_left, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        self.timer['text'] = time_str
        self.window.after(100, self._update)

    # def qwer(self):
    #     _thread.start_new_thread(self._update, (self,))

    def _block(self):
        # for key in kb.all_modifiers:
        #     kb.block_key(key)

        pyvda.AppView.current().pin()
        # self.window.overrideredirect(True)
        # self.window.protocol('WM_DELETE_WINDOW', lambda: None)

    @staticmethod
    def unblock():
        kb.unhook_all()

    def run(self):
        self.window.after(0, self._update)
        self.window.after(1, self._block)

        self.window.mainloop()
        self.unblock()


if __name__ == '__main__':
    lock = Lock()
    lock.set_timer(10)
    lock.run()
