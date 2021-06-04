import keyboard as kb
import time

kb.send('ctrl+alt+del')


'''
def close():
    time.sleep(1)
    kb.send('esc')
    print('a')


kb.add_hotkey('ctrl+alt+delete', close)
'''


'''
blocklist = ['ctrl', 'alt', 'delete']
for key in blocklist:
    kb.block_key(key)
'''

kb.wait()
