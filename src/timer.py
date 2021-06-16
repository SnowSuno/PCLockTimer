import tkinter as tk
import config


class Timer(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.scale = root.scale

        self.hour = self.Digits(self, 24)
        self.minute = self.Digits(self, 60)
        self.second = self.Digits(self, 60)

        self.hour.grid(column=0, row=0)
        self.minute.grid(column=2, row=0)
        self.second.grid(column=4, row=0)

        self.Separator(self).grid(column=1, row=0)
        self.Separator(self).grid(column=3, row=0)


    class Digits(tk.Entry):
        SEL_COL = 'gray25'

        def __init__(self, parent, limit):
            self.value = tk.StringVar(value='00')
            self.prev_value = '00'
            self.limit = limit
            self.focused = False

            super().__init__(
                parent, width=2, font=config.FONT(parent.scale // 10),
                bg=config.BG, fg=config.FG, bd=0,
                textvariable=self.value,
                insertbackground=config.HIGHLIGHT, selectbackground=config.HIGHLIGHT,
                disabledbackground=config.BG, disabledforeground=config.FG,
                insertwidth=parent.scale*0.3, insertofftime=0
            )

            self.reset_value()
            self.value.trace('w', lambda *e: self.validate_value())

            self.bind('<Delete>', lambda *e: self.reset_value())
            self.bind('<BackSpace>', lambda *e: self.reset_value())
            self.bind('<Up>', lambda *e: self.vary_value(1))
            self.bind('<Down>', lambda *e: self.vary_value(-1))
            self.bind('<Right>', lambda e: self.tk_focusNext().focus())
            self.bind('<Left>', lambda e: self.tk_focusPrev().focus())

            self.bind('<Button-1>', lambda e: self.focus())
            self.bind('<FocusIn>', lambda e: self.focus())


        def disable(self):
            self['state'] = tk.DISABLED

        def validate_value(self):
            self.select_clear()
            value = self.value.get()

            if value.isdigit():
                if len(value) == 3:
                    cursor_index = self.index(tk.INSERT)

                    prev = '0' if self.focused else self.prev_value[-1]
                    value = prev + value[cursor_index - 1]

                    if int(value) >= self.limit:
                        value = str(self.limit - 1).zfill(2)

                    self.set_value(value)

                elif len(value) == 1:
                    self.reset_value()

                self.focused = False

            else:
                self.set_value(self.prev_value)

        def reset_value(self):
            pass

        def set_value(self, value):
            self.value.set(value)
            self.prev_value = value

        def vary_value(self, increment):
            self.set_value(
                str((int(self.value.get()) + increment) % self.limit).zfill(2))

    class Separator(tk.Label):
        def __init__(self, parent):
            super().__init__(
                parent, font=config.FONT(parent.scale // 10),
                bg=config.BG, fg=config.FG, bd=0,
                text=':'
            )
