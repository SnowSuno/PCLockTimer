import tkinter as tk
from tkinter.font import Font

from math import sin, cos, radians

import config

class StartButton(tk.Canvas):
    def __init__(self, parent):
        self.size = parent.scale * 0.075
        super().__init__(
            parent,
            width=self.size, height=self.size,
            bg=config.BG, bd=0,
            relief=tk.SOLID,
            takefocus=True,
            highlightthickness=0,
        )
        self.shape()

        self.bind('<FocusIn>', lambda e: self.configure(bg=config.HIGHLIGHT))
        self.bind('<FocusOut>', lambda e: self.configure(bg=config.BG))

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
    def __init__(self, parent):
        super().__init__(
            parent, text='×',
            font=config.FONT(int(parent.scale * 0.025)),
            bg=config.BG, fg=config.FG, bd=0,
            padx=parent.scale * 0.0125
        )
