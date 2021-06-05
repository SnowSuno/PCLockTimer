import sys

import pylnk3

import winshell
import os

# print(winshell.startup())

path = os.path.join(
    os.path.dirname(sys.executable),
    os.path.basename(sys.executable)
)

winshell.CreateShortcut(
    Path=os.path.join(winshell.startup(), 'temp.lnk'),
    Target=path,
    Icon=(path, 0),
    Description="Temp startup"
)


