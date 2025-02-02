"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from algebra_and_calculus.vector import R3Vector

#-------------------------------- ESPACIO -------------------------------------
WIDTH = 940
HEIGHT = 850

#-------------------------------- CUERPOS -------------------------------------
N_ASTEROID = 200

#------------------------- CONSTANTES MATEMÁTICAS -----------------------------
PI = 3.14159265
e = 2.7182818284

i = R3Vector(1, 0, 0)
j = R3Vector(0, 1, 0)
k = R3Vector(0, 0, 1)

#------------------------- CONSTANTES UNIVERSALES -----------------------------
#Constante de gravitación universal de Newton:
G = 6.672 * 10**(-11)

#Permeabilidad dieléctrica del vacío:
EPSILON_0 = 9

#Constante de Coulomb:
K = 1/(4 * PI * EPSILON_0)

#--------------------------------- Graphics -----------------------------------

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)





