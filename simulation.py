"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
import pygame.base

from algebra_and_calculus.vector import R3Vector
from constants import WIDTH, HEIGHT
from particle import Particle
from space import Space


class Simulation:
    def __init__(self):

        #TODO: Add a user friendly way to add bodies and spaces to simulation
        self.__dt = 1/60 # time unit between frames

        self.__bod_1 = Particle(R3Vector(WIDTH//2, HEIGHT//2, 0),
                    R3Vector(0,0, 0) ,0, 10**35, 10)
        self.__bod_2 = Particle(R3Vector(199, 100, 0), R3Vector(0, 5, 0),
                 -10, 1, 5)
        self.__bod_3 = Particle(R3Vector(200, 100, 0), R3Vector(0, 1, 0),
                 0, 1, 5)

        self.__bodies = [self.__bod_1, self.__bod_2, self.__bod_3]

        self.__space1 = Space(WIDTH, HEIGHT, self.__bodies)

    # Actualize elements
    def simulation_update(self):
        self.__space1.update_space(self.__dt)

    # Draw elements
    def simulation_draw(self, surface):
        self.__space1.draw(surface)

    @property
    def dt(self):
        return self.__dt

    @dt.setter
    def dt(self, time):
        if type(time) != float:
            raise TypeError("dt must be a float")
        else:
            self.__dt = time