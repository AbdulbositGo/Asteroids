import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_IMAGE, PLAYER_SPEED


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
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(-dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt)

    def draw(self, screen):
        rotated_image = pygame.transform.rotozoom(
            self.original_image, -self.rotation, 1
        )
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
