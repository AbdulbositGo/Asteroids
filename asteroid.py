import pygame
from circleshape import CircleShape
from constants import ASTEROID_IMAGE


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

    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += 30 * dt

    def draw(self, screen):
        rotated_image = pygame.transform.rotozoom(
            self.image_original, -self.rotation, 1
        )
        rect = self.image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)
