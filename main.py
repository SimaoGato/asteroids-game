from constants import *
from player import *

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!\n"
    f"Screen width: {SCREEN_WIDTH}\n"
    f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        t = clock.tick(60)
        dt = t / 1000


if __name__ == "__main__":
    main()
