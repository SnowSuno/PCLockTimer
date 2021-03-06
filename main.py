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

from src import startup


class Lock(tk.Tk):
    def __init__(self):
        super(Lock, self).__init__()

        self.end_time = None

        self.wm_attributes('-fullscreen', True)
        self.wm_attributes('-topmost', True)
        self.title('Lock')
        self.configure(bg='black')

        font_size = self.winfo_screenwidth() // 10
        timer_font = Font(family='Consolas', size=font_size, weight='normal')
        self.timer = tk.Label(self, text='', font=timer_font, bg='black', fg='white')
        self.timer.grid(column=0, row=0)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def set_timer(self, end_timestamp=None, interval=None):
        if end_timestamp:
            self.end_time = datetime.fromtimestamp(end_timestamp)
        else:
            self.end_time = datetime.now() + timedelta(seconds=interval)


    def timestamp(self):
        return str(time.mktime(self.end_time.timetuple()))



    def _update(self):
        kb.hook(lambda *args: False, suppress=True)

        seconds_left = (self.end_time - datetime.now()).total_seconds()
        if seconds_left <= 0:
            self.end()

        hours, remainder = divmod(seconds_left+1, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        self.timer['text'] = time_str
        self.after(100, self._update)

    def _block(self):
        def _block_thread(root):
            pythoncom.CoInitialize()

            while True:
                try:
                    hwnd = int(root.frame(), 16)
                    pyvda.AppView(hwnd=hwnd).pin()
                except _ctypes.COMError:
                    time.sleep(0.001)
                else:
                    break

            root.overrideredirect(True)
            root.protocol('WM_DELETE_WINDOW', lambda: None)

        _thread.start_new_thread(_block_thread, (self,))


    @staticmethod
    def _unblock():
        kb.unhook_all()

    def start(self):
        startup.create(self.timestamp())

        self.after(0, self._update)
        self.after(0, self._block)

        self.mainloop()


    def end(self):
        self._unblock()
        startup.delete()

        self.quit()


def main():
    lock = Lock()

    if len(sys.argv) > 1:
        timestamp = float(sys.argv[1])
        lock.set_timer(end_timestamp=timestamp)

    else:
        timestamp = startup.find()
        if timestamp:
            if datetime.now() < datetime.fromtimestamp(timestamp):
                lock.quit()
                return
            else:
                startup.delete()

        with open('setting.txt', 'r') as f:
            lock_interval = int(f.readline().strip())

        lock.set_timer(interval=lock_interval)

    lock.start()


if __name__ == '__main__':
    main()
