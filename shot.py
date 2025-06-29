from circleshape import CircleShape
import pygame
from constants import SHOT_IMAGE, SHOT_RADIUS, SHOT_SOUND


class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.image = pygame.image.load(SHOT_IMAGE).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (SHOT_RADIUS * 20, SHOT_RADIUS * 20)
        )
        self.image = pygame.transform.rotate(self.image, 90)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        offset = -forward * (self.radius + 75)
        pos = self.position + offset
        rotated = pygame.transform.rotozoom(self.image, -self.rotation, 1)
        rect = rotated.get_rect(center=pos)
        screen.blit(rotated, rect)
