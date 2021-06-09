import winreg
import sys

def _open_key():
    return winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', access=winreg.KEY_ALL_ACCESS)

def create(timestamp):
    key = _open_key()
    winreg.SetValueEx(key, 'temp', 0, winreg.REG_SZ, f'"{sys.argv[0]}" {timestamp}')
    key.Close()

def delete():
    key = _open_key()
    winreg.DeleteValue(key, 'temp')
    key.Close()

def find():
    key = _open_key()
    i = 0
    while True:
        try:
            data = winreg.EnumValue(key, i)
            if data[0] == 'temp':
                key.Close()
                return float(data[1].split()[-1])
        except OSError:
            key.Close()
            return False
        i += 1
