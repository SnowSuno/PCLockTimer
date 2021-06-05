import mouse
import time

def f(event):
    pass


print('hook')
mouse.hook(f)

time.sleep(5)

print('unhook')
mouse.unhook_all()
