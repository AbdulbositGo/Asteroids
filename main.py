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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player1 = Player(SCREEN_WIDTH / 2.15, SCREEN_HEIGHT / 2)
    player2 = Player(SCREEN_WIDTH / 1.85, SCREEN_HEIGHT / 2)

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        screen.blit(background, (0, 0))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
