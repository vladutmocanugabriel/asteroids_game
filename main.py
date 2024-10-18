import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from background import Background

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    FPS_clock = pygame.time.Clock()
    dt = 0
    score = 0
    score_increment = 10

    pygame.init()

    background_image = pygame.image.load('assets/space.jpg')
    pygame.display.set_caption('Asteroid Invasion')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 36)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable, drawable)
    


    background = Background(background_image, [0,0])
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    

        # Draw background first
        screen.blit(background.image, background.rect)

        # Update and draw all the other sprites
        for item in updatable:
            item.update_movement(dt)

        for item in drawable:
            item.draw(screen)

        # Collision detection
        for asteroid in asteroids:
            if player.collide(asteroid):
                print('Game Over Broksi')
                exit()
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    score += score_increment
                    asteroid.split()

        # Render the score
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        # Update the display
        pygame.display.flip()

        # Cap the framerate
        dt = FPS_clock.tick(60) / 1000

        











if __name__ == '__main__':
    main()