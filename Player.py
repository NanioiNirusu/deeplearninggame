import numpy as np
import os
import matplotlib

from Dummy2 import Dummy2
from Rocket import Rocket

if os.name == "darwin":
    matplotlib.use("MacOSX")  # for mac
else:
    matplotlib.use("TkAgg") # for unix/windows

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15, 15) # size of window
plt.ion() # interactive mode
plt.style.use('dark_background')


class Player(Dummy2):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.actors = [Rocket()]

    def activate_thrusters(self):
        pass

    def fire_rocket(self):
        pass

    def update_movment(self, dt):
        pass