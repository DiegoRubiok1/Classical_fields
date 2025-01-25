"""
Created by Diego Rubio Canales in ene 2025
Universidad Carlos III de Madrid
"""
import pygame
from simulation import Simulation
from constants import WIDTH, HEIGHT, BLACK, WHITE

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Try Graphs")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.time_multiplier = 1

        # Simulation instance
        self.simulation = Simulation()

        # FPS CONTROL
        self.fps = 60

    def set_time_multiplier(self):
        """Adjusts the time multiplier based on the key pressed."""
        keys = pygame.key.get_pressed()  # Get keys pressed

        for key in range(pygame.K_0, pygame.K_9 + 1):
            if keys[key]: # If key pressed
                self.time_multiplier =(key - pygame.K_0) * 10
                return

        self.time_multiplier = 1

    def handle_events(self):
        """Maneja los eventos de la ventana."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        """Actualiza la lógica del juego."""
        for i in range(self.time_multiplier):
            self.set_time_multiplier()
            self.simulation.dt = (1/self.fps)
            self.simulation.simulation_update()

    def draw(self):
        """Dibuja los elementos en la pantalla."""
        self.screen.fill(BLACK)

        # Mostrar FPS
        fps_text = self.font.render(f"FPS: {self.clock.get_fps():.2f}", True, WHITE)
        self.screen.blit(fps_text, (10, 10))

        time_text = self.font.render("t x%.2f >> " %self.time_multiplier,
                                     True, WHITE)
        self.screen.blit(time_text, (10, 50))

        # Dibujar simulación
        self.simulation.simulation_draw(self.screen)

        pygame.display.flip()

    def run(self):
        """Ejecuta el bucle principal del juego."""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


# Ejecutar el juego
if __name__ == "__main__":
    game = Game()
    game.run()