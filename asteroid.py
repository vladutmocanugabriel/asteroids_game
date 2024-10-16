import pygame
import random
from constants import *
from circleshape import *
from player import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(surface=screen, color='white', center=self.position, radius=self.radius, width=2)

    def update_movement(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = int(random.uniform(20, 50))
            first_a_radius = pygame.math.Vector2.rotate(self.velocity, random_angle)
            second_a_radius = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first_a = Asteroid(self.position[0], self.position[1], new_radius)
            first_a.velocity = first_a_radius * 1.2
            second_a = Asteroid(self.position[0], self.position[1], new_radius)
            second_a.velocity = second_a_radius * -1.2



    
