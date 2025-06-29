import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, START_SOUND, OVER_SOUND
from player import Player
from shot import Shot
from time import sleep


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    background = pygame.image.load('assets/images/background.jpg').convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2.15, SCREEN_HEIGHT / 2)
    start_sound = pygame.mixer.Sound(START_SOUND)
    start_sound.play()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                over_sound = pygame.mixer.Sound(OVER_SOUND)
                over_sound.play()
                sleep(3)
                print('Game over!')
                over_sound.stop()
                pygame.quit()
                exit()
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()

        screen.blit(background, (0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
