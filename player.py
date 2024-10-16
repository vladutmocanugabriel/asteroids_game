import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, color='white', points= self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def update_movement(self, dt):
        keys = pygame.key.get_pressed()

        if self.timer > 0:
             self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt=-1*dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt=-1*dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
            if self.timer > 0:
                 return
            shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
            shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN

        
    

    
