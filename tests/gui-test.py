import tkinter as tk
from tkinter.font import Font

class Interface(tk.Tk):
    def __init__(self):
        super(Interface, self).__init__()
        self.geometry("640x480+100+100")
        self.configure(bg='black')

        timer_font = Font(family='Arial', size=200, weight='bold')

        self.entry = tk.Entry(
            self, width=2, font=timer_font,
            bg='black', fg='white',
            bd=0
        )
        self.entry.grid(row=0, column=0)



        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)




if __name__ == '__main__':
    root = Interface()
    root.mainloop()
