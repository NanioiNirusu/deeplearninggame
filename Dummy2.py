import numpy as np
import os
import matplotlib

from Dummy import Dummy

if os.name == "darwin":
    matplotlib.use("MacOSX")  # for mac
else:
    matplotlib.use("TkAgg") # for unix/windows

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15, 15) # size of window
plt.ion() # interactive mode
plt.style.use('dark_background')


class Dummy2(Dummy):
    def __init__(self, speed, game):
        self.speed=speed
        self.obj_game=game

    def update_movment(self, dt):
        pass
