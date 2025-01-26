"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from multiprocessing.managers import Value

import pygame.base

from algebra_and_calculus.vector import R3Vector
from constants import WIDTH, HEIGHT
from particle import Particle
from space import Space


class Simulation:
    def __init__(self):
        self.__scale = 5*10**5 # m / pixel
        self.__t_increment = 1000000 # time multiplier
        self.__dt = 1/60 # time unit between frames

        self.__bod_1 = Particle(R3Vector(self.__scale * WIDTH/2, self.__scale
                    * HEIGHT/2, 0), R3Vector(0,0, 0) ,
                                0, 5.972 * 10**24, 6378000)

        self.__bod_2 = Particle(
            R3Vector(self.__scale * WIDTH/2 + 384400000, self.__scale * HEIGHT / 2, 0),
            R3Vector(0, 1000, 0),
            0, 7.349 * 10**22, 1740000)

        self.__bodies = [self.__bod_1, self.__bod_2]

        self.__space1 = Space(WIDTH, HEIGHT, self.__bodies)

    # Actualize elements
    def simulation_update(self):
        self.__space1.update_space(self.__dt)

    # Draw elements
    def simulation_draw(self, surface, scale: int):
        self.__space1.draw(surface, scale)

    def move_observer(self, direction: str, dist: float):
        """Moves the simulation "camera" moving everything in simulation"""

        if direction == "right":
            for particle in self.__bodies:
                particle.pos.i -= self.scale * dist
        elif direction == "left":
            for particle in self.__bodies:
                particle.pos.i += self.scale * dist
        elif direction == "up":
            for particle in self.__bodies:
                particle.pos.j += self.scale * dist
        elif direction == "down":
            for particle in self.__bodies:
                particle.pos.j -= self.scale * dist



    @property
    def dt(self):
        return self.__dt

    @dt.setter
    def dt(self, time):
        if type(time) != float:
            raise TypeError("dt must be a float")
        else:
            self.__dt = time

    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale):
        if type(scale) != float:
            raise TypeError("scale must be a float")
        elif scale < 0:
            raise ValueError("scale must be positive")
        else:
            self.__scale = scale

    @property
    def t_increment(self):
        return self.__t_increment

    @t_increment.setter
    def t_increment(self, increment):
        if type(increment) != float:
            raise TypeError("t_increment must be a float")
        elif increment < 0:
            raise ValueError("t_increment must be positive")
        else:
            self.__t_increment = increment