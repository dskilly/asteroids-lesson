import pygame
import circleshape
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity = self.velocity
        v1 = velocity.rotate(angle)
        v2 = velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y
        asteroid1 = Asteroid(x, y, radius)
        asteroid2 = Asteroid(x, y, radius)
        asteroid1.velocity = v1 * 1.2
        asteroid2.velocity = v2 * 1.2