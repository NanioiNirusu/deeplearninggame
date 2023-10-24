import os
import matplotlib

from Dummy2 import Dummy2
from Player import Player

if os.name == "darwin":
    matplotlib.use("MacOSX")  # for mac
else:
    matplotlib.use("TkAgg") # for unix/windows

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15, 15) # size of window
plt.ion() # interactive mode
plt.style.use('dark_background')


class Rocket(Dummy2):

    def __init__(self, player):
        self.obj_player=player

    def update_movment(self, dt):
        pass