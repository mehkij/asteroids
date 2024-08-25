import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    while pygame.init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
