"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from algebra_and_calculus.vector import R3Vector
from constants import WIDTH, HEIGHT
from particle import Particle
from space import Space
import time
import pyxel

bod_1 = Particle(R3Vector(WIDTH//2, HEIGHT//2, 0), R3Vector(0, 0, 0)
                 ,0, 100)
bod_2 = Particle(R3Vector(50, 100, 0), R3Vector(0, 1, 0),
                 0, 10)
bod_3 = Particle(R3Vector(200, 100, 0), R3Vector(0, 1, 0),
                 0, 0.0001)
bodies = [bod_1, bod_2, bod_3]
space1 = Space(WIDTH, HEIGHT, bodies)

