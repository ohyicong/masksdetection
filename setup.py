# -*- coding: utf-8 -*-
"""
Created on Tue May 26 08:00:03 2020

@author: OHyic
"""


import sys
from cx_Freeze import setup, Executable


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Masks Detection",
        version = "0.1",
        description = "A Masks Detection Software developed by oh yicong",
        executables = [Executable("detect_mask_video.py", base=base)])