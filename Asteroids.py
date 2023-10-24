import numpy as np
import os
import matplotlib

from Dummy2 import Dummy2

if os.name == "darwin":
    matplotlib.use("MacOSX")  # for mac
else:
    matplotlib.use("TkAgg") # for unix/windows

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15, 15) # size of window
plt.ion() # interactive mode
plt.style.use('dark_background')


class Asteroids(Dummy2):

    def update_movement(self, dt):
        pass

