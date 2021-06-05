import sys

import pylnk3

import winshell
import os

# print(winshell.startup())

# path = os.path.join(
#     os.path.dirname(sys.executable),
#     os.path.basename(sys.executable)
# )

def create():
    path = r'C:\Python projects\Computer_Lock\dist/main.exe'

    winshell.CreateShortcut(
        Path=os.path.join(winshell.startup(), 'temp.lnk'),
        Target=path,
        Icon=(path, 0),
        Arguments='1622900129.8488095',
        Description="Temp startup"
    )


def delete():
    path = os.path.join(winshell.startup(), 'temp.lnk')

    if os.path.isfile(path):
        os.remove(path)


if __name__ == '__main__':
    print(winshell.shortcut(os.path.join(winshell.startup(), 'temp.lnk')).arguments == '')
