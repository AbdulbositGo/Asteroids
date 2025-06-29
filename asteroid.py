import random
import pygame

from circleshape import CircleShape
from constants import ASTEROID_IMAGE, ASTEROID_MIN_RADIUS, CRASH_SOUND


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.image_original = pygame.image.load(ASTEROID_IMAGE).convert_alpha()
        self.image_original = pygame.transform.smoothscale(
            self.image_original, (radius * 2, radius * 2)
        )
        self.image = self.image_original
        self.rect = self.image.get_rect(center=self.position)
        self.sound = pygame.mixer.Sound(CRASH_SOUND)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += 30 * dt

    def draw(self, screen):
        rotated_image = pygame.transform.rotozoom(
            self.image_original, -self.rotation, 1
        )
        rect = self.image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)

    def split(self):
        self.sound.play()
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            return

        new_angel = random.uniform(20, 50)
        vektor1 = self.velocity.rotate(new_angel)
        vektor2 = self.velocity.rotate(-new_angel)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vektor1 * 1.2
        asteroid2.velocity = vektor2 * 1.2

    def kill(self):
        return super().kill()
