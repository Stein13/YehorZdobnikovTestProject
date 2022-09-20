import sys
import os
from pathlib import PurePath, PureWindowsPath

if sys.platform == 'win32':
    h = PureWindowsPath(os.getcwd()).parts
    home_dir = PureWindowsPath()
else:
    h = PurePath(os.getcwd()).parts
    home_dir = PurePath()


for i in h:
    home_dir = home_dir / i


class Setup:

    def __init__(self, setup):
        self.url = setup['server']['url']



