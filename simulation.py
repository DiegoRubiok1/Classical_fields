"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
import random

from algebra_and_calculus.vector import R3Vector
from constants import WIDTH, HEIGHT, G, PI, N_ASTEROID
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


class SolarSystemSim(Simulation):
    def __init__(self):
        # Define specific values for this simulation

        scale = 14.95*10**10 / 500  # example: distance from sun to earth / pixels
        t_increment = 4 * 7 * 60 * 60 * 24  # month per second
        dt = 1 / 60  # 60 FPS initially

        super().__init__(scale=scale, t_increment=t_increment, dt=dt)

        # Creates all bodies
        self.__create_solar_system()
        # Creates asteroid belt
        self.__create_asteroid_belt()

    def __create_solar_system(self):
        """Define bodies in the solar system simulation"""
        earth = Particle(
            pos=R3Vector(1.496*10**11 , 0, 0), # m
            vel=R3Vector(0, 29780, 0),    # m / s
            charge=0, # C
            mass=5.972 * 10 ** 24, # kg
            radius=6371 * 10 ** 3, # m
            color=(0,20,200) # R, G, B
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
            pos=R3Vector(5.7909*10**10, 0, 0),
            vel=R3Vector(0, 47870, 0),
            charge=0,
            mass=3.3011 * 10 ** 23,
            radius=2.4397*10**6,
            color=(200, 200, 200)
        )
        venus = Particle(
            pos=R3Vector(1.08209 * 10**11, 0, 0),
            vel=R3Vector(0, 35020, 0),
            charge=0,
            mass=4.8675 * 10**24,
            radius=6.0518*10**6,
            color=(200,200,200)
        )
        mars = Particle(
            pos=R3Vector(2.27943 * 10 ** 11, 0, 0),
            vel=R3Vector(0, 24070, 0),
            charge=0,
            mass=6.4171 * 10 ** 24, #originaly 24
            radius=3.3895 * 10 ** 6,
            color=(200, 0, 0)
        )

        # Add bodies to space
        self._Simulation__bodies.extend( [sun, mercurio, venus, earth, moon,
                                          mars])
    def __create_asteroid_belt(self):
        for i in range(N_ASTEROID):
            # Calculate de radius of the orbit for the asteroid
            r = random.randint(33*10**10, 48*10**10)
            # Generates a random x value in the orbit
            x = random.randint(-r, r)
            # Calculates y with x and r
            y_sign = random.choice((-1,1))
            y = y_sign*((r**2 - x**2)**(1/2))
            pos = R3Vector(x, y, 0)
            # mass of sun
            M = 1.989 * 10**30
            # velocity with mass of sun and radius
            v = (G*M/r)**(1/2)
            #v = 10000 * y_sign
            #vectorize in perpendicular direction of pos
            vel =  R3Vector(-y, x, 0) * (v/r)
            #generate a random radius for asteroid in meters
            radius = random.randint(20000, 940000)
            #calculates the mass with density
            d = 2000  # kg/m**3 (Silicates density)
            mass = 4*PI*radius**3 * d

            asteroid = Particle(
                pos= pos,
                vel= vel,
                charge= 0,
                mass= mass,
                radius= radius,
                color=(100,100,100)
            )
            self._Simulation__bodies.append(asteroid)

class RandomParticleSimulation(Simulation):
    def __init__(self):
        # Define specific values for this simulation

        scale = 100  # meter / pixels
        t_increment = 10  # month per second
        dt = 1 / 60  # 60 FPS initially

        super().__init__(scale=scale, t_increment=t_increment, dt=dt)








