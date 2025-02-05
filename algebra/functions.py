"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from algebra.vector import R3Vector, R2Vector

#-------------------------- Algebraic functions -------------------------------
def vectorial_p(first: R3Vector, second: R3Vector) -> R3Vector:
    i = first.j * second.k - first.k *  second.j
    j = first.k * second.i - first.i * second.k
    k = first.i * second.j - first.j * second.i
    return R3Vector(i, j, k)

def scalar_p(first: R3Vector, second: R3Vector) -> float:
    i = first.i * second.i
    j = first.j * second.j
    k = first.k * second.k
    return i + j + k

def to_R3(r2_vector: R2Vector, k: float):
    if isinstance(r2_vector, R2Vector):
        return R3Vector(r2_vector.i, r2_vector.j, k)
    else:
        raise TypeError("Object must be R2Vector: ", type(r2_vector))