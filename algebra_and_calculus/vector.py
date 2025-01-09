"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
class R2Vector:
    # Constructor method:
    def __init__(self, i: float, j: float):
        self.__i = i
        self.__j = j

    #Define the sum between R2Vector
    def __add__(self, other):
        if isinstance(other, R2Vector):
            return R2Vector(self.i + other.i, self.j + other.j)
        else:
            raise TypeError("Second must be a R2Vector, type")

    #Properties and setter
    @property
    def i(self):
        return self.__i
    @i.setter
    def i(self, value):
        if type(value) == float or type(value) == int:
            self.__i = value
        else:
            raise TypeError("The component <i> of the vector must be a "
                             "float or integer")

    @property
    def j(self):
        return self.__j

    @j.setter
    def j(self, value):
        if type(value) == float or type(value) == int:
            self.__j = value
        else:
            raise TypeError(
                "The component <j> of the vector must be a float or integer")

class R3Vector:
    def __init__(self, i: float, j: float, k: float):
        self.__i = i
        self.__j = j
        self.__k = k

    def __add__(self, other):
        if isinstance(other, R3Vector):
            i = self.__i + other.__i
            j = self.__j + other.__j
            k = self.__k + other.__k
            return R3Vector(i,j,k)
        else:
            raise TypeError("The sum type must be R3Vector: ", type(other))

    def __mul__(self, esc: float):
        if isinstance(esc, float):
            return R3Vector(esc * self.__i, esc * self.__j, esc * self.__k)
        else:
            raise TypeError("Product by escalar must be a float: ", type(esc))

    def mod(self) -> float:
        return (self.i**2 + self.j**2 + self.k**2)**0.5

    @property
    def i(self):
        return self.__i
    @i.setter
    def i(self, value):
        if type(value) == float or type(value) == int:
            self.__i = value
        else:
            raise TypeError("The component <i> of the vector must be a "
                             "float or integer")

    @property
    def j(self):
        return self.__j

    @j.setter
    def j(self, value):
        if type(value) == float or type(value) == int:
            self.__j = value
        else:
            raise TypeError(
                "The component <j> of the vector must be a float or integer")

    @property
    def k(self):
        return self.__k

    @k.setter
    def k(self, value):
        if type(value) == float or type(value) == int:
            self.__k = value
        else:
            raise TypeError(
                "The component <k> of the vector must be a float or integer")