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
        self.image = pygame.image.load('assets/ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  
        self.image = pygame.transform.rotate(self.image, 210)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def draw(self, screen):
        # Draw the hitbox as a white triangle
        self.triangle()

        # Rotate the image to match the player's direction
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)  # Negative rotation to match Pygame's coordinate system
        new_rect = rotated_image.get_rect(center=self.position)  # Set the new rect to be centered on the player's position

        # Draw the rotated image on top of the hitbox
        screen.blit(rotated_image, new_rect)

        
    
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

        
    

    
