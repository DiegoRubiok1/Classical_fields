"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""

import pygame
from pygame.constants import (K_DOWN, K_SPACE, K_LSHIFT, K_RIGHT, K_UP,
                              K_LEFT, K_z, K_x, K_b)

from simulation import Simulation, SolarSystemSim, RandomParticleSimulation
from constants import WIDTH, HEIGHT, BLACK, WHITE

class Game:
    def __init__(self):

        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Alpha simulation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        # Simulation instance
        self.simulation = RandomParticleSimulation()

        # Space-time control (scale space or multiply time)
        self.time_multiplier = 1
        self.space_scale = self.simulation.scale
        self.last_key_pressed = None

        # Aspect
        self.fill_black = True

        # FPS control
        self.fps = 60

    def set_fill_background(self):
        keys = pygame.key.get_pressed()  # Get keys pressed

        # If key "b" pressed fill background with black
        if keys[K_b]:
            self.fill_black = not self.fill_black


    def set_time_multiplier(self):
        """Adjusts the time multiplier based on the key pressed."""
        keys = pygame.key.get_pressed()  # Get keys pressed


        for key in range(pygame.K_0, pygame.K_9 + 1):
            if keys[key]:
                # Multiplies time by the increment and the number key
                self.time_multiplier =(key - pygame.K_0) * self.simulation.t_increment
                return

        self.time_multiplier = 1

    def set_space_scale(self):
        """Adjust the space scale based on keys pressed."""
        keys = pygame.key.get_pressed()

        if (keys[K_x] and self.last_key_pressed != K_x and
                self.space_scale > self.simulation.scale):
            self.space_scale -= self.simulation.scale
            self.last_key_pressed = K_x

        elif (keys[K_x] and self.last_key_pressed != K_x and
                self.space_scale <= self.simulation.scale):
            self.space_scale -= self.space_scale / 4
            self.last_key_pressed = K_x


        elif keys[K_z] and self.last_key_pressed != K_z:
            self.space_scale += self.simulation.scale
            self.last_key_pressed = K_z

        # Reset last_key_pressed when no relevant key is pressed
        if not keys[K_z] and not keys[K_x]:
            self.last_key_pressed = None

    def handle_events(self):
        """Handle de events in screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        """Actualize the logic of the simulation."""
        self.set_fill_background()
        self.set_time_multiplier()
        self.set_space_scale()
        self.simulation.dt = (1/self.fps) * self.time_multiplier
        self.move_camera()
        self.simulation.simulation_update()

    def draw(self):
        """Draws elements in screen."""
        # Fill screen black (or not)
        if self.fill_black:
            self.screen.fill(BLACK)

        #Draw UHD
        self.draw_UHD()

        # Draw simulation
        self.simulation.simulation_draw(self.screen, self.space_scale)

        pygame.display.flip()

    def draw_UHD(self):
        # Draw FPS
        fps_text = self.font.render(f"FPS: {self.clock.get_fps():.2f}", True,
                                    WHITE)
        self.screen.blit(fps_text, (10, 10))

        # Draw time multiplier
        time_text = self.font.render("t x%.2f >> " % self.time_multiplier,
                                     True, WHITE)
        self.screen.blit(time_text, (10, 50))

        # Draw scale
        scale_text = self.font.render("scale: %.2f m/pixel" %
                                      self.space_scale,True, WHITE)

        self.screen.blit(scale_text, (10, 90))

    def move_camera(self):
        """Method that allows the user to move the vision using the
        direction keys"""

        keys = pygame.key.get_pressed()
        dist =  15 * self.space_scale

        if keys[K_UP]:      # Move up
            self.simulation.move_observer("up", dist)

        elif keys[K_DOWN]:      # Move down
            self.simulation.move_observer("down", dist)

        elif keys[K_RIGHT]:     # Move right
            self.simulation.move_observer("right", dist)

        elif keys[K_LEFT]:      # Move left
            self.simulation.move_observer("left", dist)


    def run(self):
        """Executes the main loop."""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


# Execute
if __name__ == "__main__":
    game = Game()
    game.run()