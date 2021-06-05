import pythoncom
import pyWinhook
import time

def uMad(event):
    return False

def qwer(event):
    return True


hm = pyWinhook.HookManager()
hm.MouseAll = uMad
hm.KeyAll = uMad
hm.HookMouse()
hm.HookKeyboard()
# pythoncom.PumpMessages()

time.sleep(5)


hm.MouseAll = qwer
hm.KeyAll = qwer
hm.HookMouse()
hm.HookKeyboard()
# pythoncom.PumpMessages()
