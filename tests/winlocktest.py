import tkinter as tk
import tkinter.font as tkFont
import time
import _thread

lock = tk.Tk()

def time_update():
    while True:
        t = time.strftime('%I:%M:%S', time.localtime())
        clock['text'] = t


lock.attributes('-fullscreen', True)
lock.title('LOCK')
lock.configure(bg='black')

clock_font = tkFont.Font(family='Arial', size=200, weight='bold')
clock = tk.Label(lock, text='00:00', font=clock_font, bg='black', fg='white')
#clock.place(relx=0.5, rely=0.5, anchor='center')
#clock.pack()
clock.grid(column=0, row=0)

lock.columnconfigure(0, weight=1)
lock.rowconfigure(0, weight=1)

_thread.start_new_thread(time_update, ())


lock.mainloop()
