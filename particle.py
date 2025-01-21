"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
import pygame.draw

from algebra_and_calculus.vector import R3Vector
from constants import G, K

class Particle:
    def __init__(self, pos: R3Vector, vel: R3Vector, charge: float,
                 mass: float, size: float):
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
        self.__size = size #At current version: radius


    def g_field_generated(self, x, y, z) -> R3Vector:
        """Calculates the field in a point of the space"""
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

    def e_field_generated(self, x, y, z) -> R3Vector:
        dist_x =  x - self.pos.i
        dist_y = y - self.pos.j
        dist_z = z - self.pos.k
        # Distance vector between particles:
        r = R3Vector(dist_x, dist_y, dist_z)
        if r.mod() == 0:
            return R3Vector(0, 0, 0)
        else:
            # Electric field equation by Coulomb:
            E = r*((K*self.__q)/r.mod()**3)
            return E

    def actualize_velocity(self, dt: float):
        # dt represents the time (in seconds) between each main loop update
        self.__vel = self.__vel + (self.__a * dt)

    def actualize_position(self, dt: float):
        self.__pos = self.pos + (self.__vel * dt)

    def restart_acceleration(self):
        self.a = R3Vector(0,0,0)

    def draw(self, surface):

        color = (0, 200, 0)
        center = (self.pos.i, self.pos.j)
        #
        pygame.draw.circle(surface, color, center, self.size)

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
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != float:
            raise TypeError("Instance of size must be float: " + str(type(
                size)))
        elif size < 0:
            raise ValueError("The value of size must be positive. Value: " +
                             str(size))
        self.__size = size

    @property
    def q(self) -> float:
        return self.__q

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
            raise TypeError("Instance of velocity must be R3Vector: ", type(
                velocity))

    @property
    def a(self) -> R3Vector:
        return self.__a

    @a.setter
    def a(self, acceleration):
        if isinstance(acceleration, R3Vector):
            self.__a = acceleration
        else:
            raise TypeError("Instance of acceleration must be R3Vector: ",type(
                acceleration))