from datetime import datetime, timedelta
import tkinter as tk
from tkinter.font import Font
import time
import keyboard as kb
import pyvda

class Lock(tk.Tk):
    def __init__(self, end_timestamp=time.time()):
        super(Lock, self).__init__()

        self.end_time = datetime.fromtimestamp(end_timestamp)

        self.attributes('-fullscreen', True)
        self.wm_attributes('-topmost', 1)
        self.title('Lock')
        self.configure(bg='black')

        timer_font = Font(family='Arial', size=200, weight='bold')
        self.timer = tk.Label(self, text='', font=timer_font, bg='black', fg='white')
        self.timer.grid(column=0, row=0)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def set_timer(self, interval):
        self.end_time = datetime.now() + timedelta(seconds=interval)

    def timestamp(self):
        return time.mktime(self.end_time.timetuple())

    def _update(self):
        seconds_left = (self.end_time - datetime.now()).total_seconds()
        if seconds_left <= 0:
            self.quit()

        hours, remainder = divmod(seconds_left, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        self.timer['text'] = time_str
        self.after(10, self._update)

    def _block(self):
        for key in kb.all_modifiers:
            kb.block_key(key)

        pyvda.AppView.current().pin()
        self.overrideredirect(True)
        self.protocol('WM_DELETE_WINDOW', lambda: None)

    @staticmethod
    def unblock():
        kb.unhook_all()

    def run(self):
        self.after(0, self._update)
        self.after(1, self._block)

        self.mainloop()
        self.unblock()


if __name__ == '__main__':
    lock = Lock()
    lock.set_timer(10)
    lock.run()

