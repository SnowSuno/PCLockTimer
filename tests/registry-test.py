import winreg
import os
import sys

# file_path = sys.argv[0]
def create():
    file_path = r'"C:\Python projects\Computer_Lock\dist\main.exe" 1623217259.1301239'

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', access=winreg.KEY_ALL_ACCESS
    )

    winreg.SetValueEx(key, 'temp', 0, winreg.REG_SZ, file_path)
    key.Close()

def delete():
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', access=winreg.KEY_ALL_ACCESS
    )

    winreg.DeleteValue(key, 'temp')
    key.Close()

def contains(value):
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run', access=winreg.KEY_ALL_ACCESS
    )
    # try:
    #     while value != winreg.EnumValue(key, 0)[0]:
    #         pass
    #     else:
    #         return True
    # except OSError:
    #     return False
    # finally:
    #     key.Close()

    i = 0
    while True:
        try:
            if value == winreg.EnumValue(key, i)[0]:
                key.Close()
                return True
        except OSError:
            key.Close()
            return False
        i += 1



if __name__ == '__main__':
    create()
    # print(contains('temp'))
    # delete()
