################### Tests Tkinter - Main ###################

# -*- coding: utf8 -*-

import os
from tkinter import *
from Interface import *


Fenetre = Tk()
UI = MakeUI(Fenetre)

UI.mainloop()

try:
    UI.destroy()
except:
    pass
