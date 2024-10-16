import pygame
from constants import *
from circleshape import *
from player import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color='white', center=self.position, radius=self.radius, width=2)

    def update_movement(self, dt):
        self.position += self.velocity * dt