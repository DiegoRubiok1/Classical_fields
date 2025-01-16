"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from algebra_and_calculus.vector import R3Vector
from constants import WIDTH, HEIGHT
from particle import Particle
from space import Space
import pyxel


class Simulation:
    def __init__(self):
        self.__bod_1 = Particle(R3Vector(WIDTH//2, HEIGHT//2, 0),
                                R3Vector(0,0, 0) ,0, 100
                                )
        self.__bod_2 = Particle(R3Vector(50, 100, 0), R3Vector(0, 1, 0),
                 -10, 1)
        self.__bod_3 = Particle(R3Vector(200, 100, 0), R3Vector(0, 1, 0),
                 0, 1)

        self.__bodies = [self.__bod_1, self.__bod_2, self.__bod_3]

        self.__space1 = Space(WIDTH, HEIGHT, self.__bodies)

        # Initialize graphics
        pyxel.init(WIDTH, HEIGHT, title="3 Cuerpos")
        pyxel.load("resources.pyxres")
        pyxel.run(self.update, self.draw)


    def update(self):
        pyxel.mouse(True)
        self.__space1.update_space()


    def draw(self):
        self.__space1.draw_space()