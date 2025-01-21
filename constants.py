"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from algebra_and_calculus.vector import R3Vector

#-------------------------------- ESPACIO -------------------------------------
WIDTH = 940
HEIGHT = 850

#-------------------------------- CUERPOS -------------------------------------

COLOR = 0
RADIUS  = 10
# Cuerpo 1
MASS_1 = 2
CHARGE_1 = 0
X_1 = WIDTH/2
Y_1 = HEIGHT/2

# Cuerpo 2
MASS_2 = 5
CHARGE_2 = 0
X_2 = X_1 + 100
Y_2 = Y_1 + 100

#Cuerpo 3
MASS_3 = 6
CHARGE_3 = 0
X_3 = X_1 - 100
Y_3 = Y_1 - 100

#------------------------- CONSTANTES MATEMÁTICAS -----------------------------
PI = 3.14159265
e = 2,7182818284

i = R3Vector(1, 0, 0)
j = R3Vector(0, 1, 0)
k = R3Vector(0, 0, 1)

#------------------------- CONSTANTES UNIVERSALES -----------------------------
#Constante de gravitación universal de Newton:
G = 10**(-31)

#Permeabilidad dieléctrica del vacío:
EPSILON_0 = 9

#Constante de Coulomb:
K = 1/(4 * PI * EPSILON_0)

#--------------------------------- Graphics -----------------------------------

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)





