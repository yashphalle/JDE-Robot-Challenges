import pygame
import random
import math



WIDTH = 640
HEIGHT = 480
PARTICLE_RADIUS = 10
PARTICLE_COLOR = (255, 255, 255)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation")

# Define a particle class
class Particle:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def update(self):
        # Update position based on speed and direction
        self.x += self.dx
        self.y += self.dy
        # Bounce off walls
        #reverse directions so it will make angle of reflection to angle of incidence
        if self.x < 0 or self.x > WIDTH - PARTICLE_RADIUS:
            self.dx = -self.dx
        if self.y < 0 or self.y > HEIGHT - PARTICLE_RADIUS:
            self.dy = -self.dy

    def draw(self):
        # Draw particle as a rectangle
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), PARTICLE_RADIUS)

# Create a list of particles
x = WIDTH/2
y = HEIGHT/2
speed = 0.5
direction = random.uniform(0, 2 * math.pi)
dx = speed * math.cos(direction)
dy = speed * math.sin(direction)
particle = Particle(x, y, dx, dy)


# Start the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    particle.update()

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw particles
    particle.draw()

    # Update display
    pygame.display.update()

# Clean up pygame
pygame.quit()
