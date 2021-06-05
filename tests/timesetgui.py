import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.title('Time Lock')
root.geometry('200x100')
root.resizable(False, False)
root['bg'] = 'white'

root_font = tkFont.Font(family='Malgun Gothic', size=12)

label = tk.Label(root, text="숫자를 입력하세요.", height=1, font=root_font, bg='white')
label.pack()


hour_text = tk.Label(root, text='시간', font=root_font, bg='white')
min_text = tk.Label(root, text='분', font=root_font, bg='white')


def value_check(self):
    label.config(text="숫자를 입력하세요.")
    valid = False
    if self.isdigit():
        if (int(self) <= 24 and int(self) >= 0):
            valid = True
    elif self == '':
        valid = True
    return valid

def value_error(self):
    label.config(text=str(self) + "를 입력하셨습니다.\n올바른 값을 입력하세요.")


validate_command = (root.register(value_check), '%P')
invalid_command = (root.register(value_error), '%P')

hour_spinbox = tk.Spinbox(root, font=root_font, width=5, from_=0, to=24, validate='all')
min_spinbox = tk.Spinbox(root, font=root_font, width=5, from_=0, to=59, validate='all',
                         validatecommand=validate_command, invalidcommand=invalid_command)



hour_spinbox.pack(side='left')
hour_text.pack(side='left')
min_spinbox.pack(side='left')
min_text.pack(side='right')



root.mainloop()
