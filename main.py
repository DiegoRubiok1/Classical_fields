"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
from simulation import Simulation
import pygame
from constants import WIDTH, HEIGHT, BLACK, BLUE


# Initialize Pygame
pygame.init()
simulation_1 = Simulation()

# Screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Try graphs")

#Main loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

    simulation_1.simulation_update()

    screen.fill(BLACK)  # Limpiar pantalla
    pygame.draw.circle(screen, BLUE, (, circle_y),
                       circle_radius)  # Dibujar círculo

    pygame.display.flip()  # Actualizar pantalla
    clock.tick(60)  # Limitar a 60 FPS

pygame.quit()




