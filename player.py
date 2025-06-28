import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_IMAGE


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        self.original_image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.original_image = pygame.transform.smoothscale(
            self.original_image, (100, 100)
        )

        self.image = self.original_image

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

    def draw(self, surface):
        rotated_image = pygame.transform.rotozoom(
            self.original_image, -self.rotation, 1
        )
        rect = rotated_image.get_rect(center=self.position)
        surface.blit(rotated_image, rect)
