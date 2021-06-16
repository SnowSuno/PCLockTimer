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

from math import sin, cos, radians

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

        self.font_size = self.winfo_screenheight() // 5
        self.font = Font(family='Consolas', size=self.font_size, weight='normal')
        # self.timer = tk.Label(self, text='00', font=timer_font, bg='black', fg='white')


        self.timer = tk.Frame(self)
        self.timer.place(relx=0.5, rely=0.43, anchor=tk.CENTER)

        self.hour = self.TimeSetter(self, 24)
        self.hour.grid(column=0, row=0)

        self.Seperator(self).grid(column=1, row=0)

        self.minute = self.TimeSetter(self, 60)
        self.minute.grid(column=2, row=0)

        self.Seperator(self).grid(column=3, row=0)

        self.second = self.TimeSetter(self, 60)
        self.second.grid(column=4, row=0)


        # self.start_btn = tk.Button(
        #     self, text='START',
        #     font=Font(family='Consolas', size=self.font_size//5, weight='normal'),
        #     bg=self.bg, fg=self.fg, bd=5,
        #     pady=0, padx=0
        # )
        # self.start_btn = RoundedButton(self, 200, 100, 30, 0, 'white', 'black')
        self.start_btn = self.StartButton(self)
        self.start_btn.place(relx=0.5, rely=0.73, anchor=tk.CENTER)

        self.quit_btn = self.QuitButton(self)
        self.quit_btn.place(relx=1, rely=0, anchor=tk.NE)




    def run(self):
        # self.after(0, self._update)
        # self.after(1, self._block)

        self.mainloop()
        # self.unblock()


    class TimeSetter(tk.Entry):
        def __init__(self, root, limit):
            self.value = tk.StringVar()
            self.old = '00'
            self.limit = limit
            self.focused = False

            super().__init__(
                root.timer, width=2, font=root.font,
                bg=root.bg, fg=root.fg, bd=0,
                textvariable=self.value,
                insertbackground='gray25', selectbackground='gray25',
                disabledbackground=root.bg, disabledforeground=root.fg,
                insertwidth=root.font_size*3, insertontime=1000, insertofftime=0
            )
            self.value_reset()
            self.value.trace('w', lambda *args: self.value_check())

            self.bind('<Delete>', self.value_reset)
            self.bind('<BackSpace>', self.value_reset)
            self.bind('<Up>', self.increase_value)
            self.bind('<Down>', self.decrease_value)
            self.bind('<Right>', lambda e: self.tk_focusNext().focus())
            self.bind('<Left>', lambda e: self.tk_focusPrev().focus())

            self.bind('<Button-1>', lambda e: self.focus())
            self.bind('<FocusIn>', lambda e: self.focus())

            # self.disable()

        def disable(self):
            self['state'] = tk.DISABLED

        def focus(self):
            self.focused = True
            super().focus()

        def value_reset(self, *e):
            self.set_value('00')

        def set_value(self, value):
            self.value.set(value)
            self.old = value

        def increase_value(self, *e):
            value = str((int(self.value.get()) + 1) % self.limit).zfill(2)
            self.set_value(value)

        def decrease_value(self, *e):
            value = str((int(self.value.get()) - 1) % self.limit).zfill(2)
            self.set_value(value)

        def value_check(self):
            self.select_clear()
            value = self.value.get()

            if value.isdigit():
                if len(value) == 3:
                    cursor_index = self.index(tk.INSERT)

                    old = '0' if self.focused else self.old[-1]
                    value = old + value[cursor_index-1]

                    if int(value) >= self.limit:
                        value = str(self.limit - 1).zfill(2)

                    self.set_value(value)

                elif len(value) == 1:
                    self.value_reset()

                self.focused = False
            else:
                self.set_value(self.old)


    class Seperator(tk.Label):
        def __init__(self, root):
            super().__init__(
                root.timer, font=root.font,
                bg=root.bg, fg=root.fg, bd=0,
                text=':'
            )

    class StartButton(tk.Canvas):
        def __init__(self, root):
            self.size = root.font_size * 0.75
            super().__init__(
                root,
                width=self.size, height=self.size,
                bg=root.bg, bd=0,
                relief=tk.SOLID,
                takefocus=True,
                highlightthickness=0,
            )
            self.shape()

            self.bind('<FocusIn>', lambda e: self.configure(bg='gray25'))
            self.bind('<FocusOut>', lambda e: self.configure(bg='black'))


        def shape(self):
            xc = self.size * 0.45
            yc = self.size * 0.5
            r = self.size * 0.4
            a = [radians(0), radians(120), radians(240)]

            self.create_polygon(
                xc + r * cos(a[0]), yc + r * sin(a[0]),
                xc + r * cos(a[1]), yc + r * sin(a[1]),
                xc + r * cos(a[2]), yc + r * sin(a[2]),
                width=0, fill='white'
            )

    class QuitButton(tk.Label):
        def __init__(self, root):
            super().__init__(
                root, text='×',
                font=Font(family='Consolas', size=int(root.font_size * 0.25), weight='normal'),
                bg=root.bg, fg=root.fg, bd=0,
                padx=root.font_size * 0.125
            )



class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
            relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()


if __name__ == '__main__':

    lock = Lock()
    lock.run()

