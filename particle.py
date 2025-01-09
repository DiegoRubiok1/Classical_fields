"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from algebra_and_calculus.vector import R3Vector
from constants import G

class Particle:
    def __init__(self, pos: R3Vector, vel: R3Vector, charge: float,
                 mass: float):
        # Cinematic Attributes
        self.__pos =  pos
        self.__vel = vel
        self.__a = R3Vector(0, 0, 0)   #Acceleration

        # Dynamic Attributes
        self.__F = 0
        self.Ec = 0
        self.Ep = 0

        # Field Attributes
        self.__q = charge
        self.__m = mass

    # Calculates the field in a point of the space
    def g_field_generated(self, x, y, z) -> R3Vector:
        dist_x = self.pos.i - x
        dist_y = self.pos.j - y
        dist_z = self.pos.k - z
        # Distance vector between particles:
        r = R3Vector(dist_x, dist_y, dist_z)
        if r.mod() == 0:
            return R3Vector(0, 0, 0)
        else:
            # Gravity field equation by Newton:
            g = r*((G*self.m)/r.mod()**3)
            return g

    def actualize_velocity(self, dt: float):
        # dt represents the time (in seconds) between each main loop update
        self.__vel = self.__vel + (self.__a * dt)

    def actualize_position(self, dt: float):
        self.__pos = self.pos + (self.__vel * dt)

    def restar_acceleration(self):
        self.a = R3Vector(0,0,0)

    @property
    def m(self) -> float:
        return self.__m

    @m.setter
    def m(self, mass):
        if isinstance(mass, float) and mass >= 0:
            self.__m = mass
        else:
            raise TypeError("Instance of mass must be R3Vector: ", type(
                mass))

    @property
    def pos(self) -> R3Vector:
        return self.__pos

    @pos.setter
    def pos(self, position):
        if isinstance(position, R3Vector):
            self.__pos = position
        else:
            raise TypeError("Instance of mass must be R3Vector: ", type(
                position))

    @property
    def vel(self) -> R3Vector:
        return self.__vel

    @vel.setter
    def vel(self, velocity):
        if isinstance(velocity, R3Vector):
            self.__vel = velocity
        else:
            raise TypeError("Instance of mass must be R3Vector: ", type(
                velocity))

    @property
    def a(self) -> R3Vector:
        return self.__a

    @a.setter
    def a(self, acceleration):
        if isinstance(acceleration, R3Vector):
            self.__a = acceleration
        else:
            raise TypeError("Instance of mass must be R3Vector: ", type(
                acceleration))





