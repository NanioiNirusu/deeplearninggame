import numpy as np
import os
import matplotlib

from Asteroids import Asteroids
from Dummy import Dummy
from Dummy2 import Dummy2
from Planets import Planets
from Player import Player
from Rocket import Rocket

if os.name == "darwin":
    matplotlib.use("MacOSX")  # for mac
else:
    matplotlib.use("TkAgg")  # for unix/windows

import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (15, 15)  # size of window
plt.ion()  # interactive mode
plt.style.use('dark_background')


class Game:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super(Game, self).__init__()
        self.is_running = True
        self.score = 0
        self.lives = 0

        self.actors = [Dummy(), Dummy2(), Planets(), Asteroids(), Player(), Rocket()]  # TODO add Player, Planets and Asteroids

    def press(self, event):
        player = None  # TODO get player
        print('press', event.key)
        if event.key == 'escape':
            self.is_running = False  # quits app
        elif event.key == 'right':
            player.set_angle(player.get_angle() - 5)
        elif event.key == 'left':
            player.set_angle(player.get_angle() + 5)
        elif event.key == ' ':
            player.activate_thrusters()

    def on_close(self, event):
        self.is_running = False

    def main(self):

        fig, _ = plt.subplots()
        fig.canvas.mpl_connect('key_press_event', self.press)
        fig.canvas.mpl_connect('close_event', self.on_close)
        dt = 1e-3

        while self.is_running:
            plt.clf()
            plt.axis('off')
            plt.tight_layout(pad=0)

            plt.xlim(-10, 10)
            plt.ylim(-10, 10)

            for actor in self.actors:  # polymorhism
                actor.update_movment(dt)
                actor.draw()

            plt.draw()
            plt.pause(dt)


game = Game()
game.main()
