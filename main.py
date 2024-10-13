import pygame
from constants import *

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    FPS_clock = pygame.time.Clock()
    dt = 0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        pygame.Surface.fill(screen, 'black')
        pygame.display.flip()
        dt = FPS_clock.tick(60) / 1000
        











if __name__ == '__main__':
    main()