import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load('assets/images/background.jpg').convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == '__main__':
    main()
