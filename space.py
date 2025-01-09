"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from constants import *
from algebra_and_calculus.vector import R3Vector
from algebra_and_calculus.functions import *
from particle import Particle

class Space:
    def __init__(self, width: int, height: int, bodies: list[Particle]):
        self.__width = width
        self.__height = height

        # Particle list
        self.__bodies = bodies


    def magnetic_field_acceleration(self):
        """Method that calculates de acceleration due to all the masses in a space"""

        for particle in self.__bodies:
            # List of each body without the particle
            interact_with = self.__bodies.copy()
            interact_with.remove(particle)

            for body in interact_with:
                particle.a = particle.a +  body.g_field_generated(
                    particle.pos.i, particle.pos.j, particle.pos.k)