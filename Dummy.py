import numpy as np
import os
import matplotlib

if os.name == "darwin":
    matplotlib.use("MacOSX")  # for mac
else:
    matplotlib.use("TkAgg") # for unix/windows

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15, 15) # size of window
plt.ion() # interactive mode
plt.style.use('dark_background')


class Dummy:
    def __init__(self, angle):
        self.vec_pos=np.array([0., 0.])
        self.vec_dir_init=np.array([0., 0.])
        self.vec_dir=np.array([0., 0.])
        self.geometry = [
            np.array([-1, -1]),
            np.array([-1, 1]),
            np.array([1, 1]),
            np.array([1, -1]),
            np.array([-1, -1]),
        ]
        self.__angle=angle
    def set_angle(self, angle):
        pass

    def get_angle(self, angle2):
        pass

    def update_movment(self, dt):
        pass

    def draw(self):
        x_data = []  # temporary variable use instead self.geometry
        y_data = []
        for vec2 in self.geometry:
            x_data.append(vec2[0])
            y_data.append(vec2[1])
        plt.plot(x_data, y_data)
