import pygame
import random
import math


WIDTH = 640
HEIGHT = 480
PARTICLE_RADIUS = 10
speed = 0.3

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
        self.x += self.dx
        self.y += self.dy
        # Bounce off walls

        if self.x < PARTICLE_RADIUS:
            direction= random.uniform(math.pi,2*math.pi)
            dx = speed * math.cos(direction)
            dy = speed * math.sin(direction)
            self.dx = dx
            print("x<0")
        
        if self.x > WIDTH-PARTICLE_RADIUS:
            direction= random.uniform(math.pi/4,math.pi)
            dx = speed * math.cos(direction)
            dy = speed * math.sin(direction)
            self.dx = dx
            print("x>width")

        if self.y < PARTICLE_RADIUS:
            direction = random.uniform(math.pi/2,3*math.pi/2)
            dx = speed * math.cos(direction)
            dy = speed * math.sin(direction)
            self.dy = dy
            print("y<0")

        if self.y > HEIGHT-PARTICLE_RADIUS:
            direction = random.uniform(3*math.pi/2,2*math.pi-3*math.pi/4)
            dx = speed * math.cos(direction)
            dy = speed * math.sin(direction)
            self.dy = dy
            print("y>height")


    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), PARTICLE_RADIUS)

# Create a list of particles
direction = random.uniform(0, 2 * math.pi)
dx = speed * math.cos(direction)
dy = speed * math.sin(direction)
particle = Particle(WIDTH/2,HEIGHT/2,dx,dy)

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

