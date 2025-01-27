"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from multiprocessing.managers import Value

import pygame.base
from pygame.transform import scale

from algebra_and_calculus.vector import R3Vector
from constants import WIDTH, HEIGHT
from particle import Particle
from space import Space


class Simulation:
    def __init__(self, scale=5*10**5, t_increment=1000000, dt=1/60):
        self.__scale = scale  # meter / pixel
        self.__t_increment = t_increment  # time multiplier
        self.__dt = dt  # time unit between frames
        self.__bodies = []
        self.__space = Space(WIDTH, HEIGHT, self.__bodies)

    # Actualize elements
    def simulation_update(self):
        self.__space.update_space(self.__dt)

    # Draw elements
    def simulation_draw(self, surface, scale: int):
        self.__space.draw(surface, scale)

    def move_observer(self, direction: str, dist: float):
        """Moves the simulation "camera" moving everything in simulation"""

        if direction == "right":
            for particle in self.__bodies:
                particle.pos.i -= dist
        elif direction == "left":
            for particle in self.__bodies:
                particle.pos.i += dist
        elif direction == "up":
            for particle in self.__bodies:
                particle.pos.j += dist
        elif direction == "down":
            for particle in self.__bodies:
                particle.pos.j -= dist



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


class SunEarthMoonSim(Simulation):
    def __init__(self):
        # Definir valores específicos para esta simulación
        scale = 14.95*10**10 / 500  # example: distance from sun to earth / pixels
        t_increment = 60 * 60 * 24  # Day per second
        dt = 1 / 30  # 30 FPS
        super().__init__(scale=scale, t_increment=t_increment, dt=dt)

        # Creates all bodies
        self.__crear_sistema_tierra_luna()

    def __crear_sistema_tierra_luna(self):
        """Define los cuerpos de la simulación Tierra-Luna"""
        earth = Particle(
            pos=R3Vector(14.95*10**10 , 0, 0),
            vel=R3Vector(0, 29.78 * 10**3, 0),
            charge=0,
            mass=5.972 * 10 ** 24,
            radius=6371 * 10 ** 3,
            color=(0,20,200)
        )
        moon = Particle(
            pos=earth.pos + R3Vector(3.84 * 10 ** 8, 0, 0),
            vel=earth.vel + R3Vector(0, 10**3, 0),
            charge=0,
            mass=7.347 * 10 ** 22,
            radius=1737 * 10 ** 3,
            color=(200,200,200)
        )
        sun = Particle(
            pos=R3Vector(0,0,0),
            vel=R3Vector(0,0,0),
            charge=0,
            mass=1.989 * 10**30,
            radius=696340,
            color=(200,200,0)
        )
        mercurio = Particle(
            pos=R3Vector(5.89*10**10, 0, 0),
            vel=R3Vector(0, 47870, 0),
            charge=0,
            mass=3.3 * 10 ** 23,
            radius=2.4397*10**6,
            color=(200, 200, 200)
        )

        self._Simulation__bodies.extend( [sun, mercurio, earth, moon])
        # Add bodies to space
