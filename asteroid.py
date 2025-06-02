import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid = pygame.draw.circle(screen, "white", self.position, self.radius, 2 )

    def update(self, dt):
        self.position +=  self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #Randomize the angle of the split
        angle = random.uniform(20, 50)
        new_vector_1 = self.position.rotate(angle)
        new_vector_2 = self.position.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_vector_1 * 1.2
        new_asteroid_2.velocity = new_vector_2 * 1.2

