import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    SPACESHIP_IMAGE,
    FLAME_IMAGE,
    PLAYER_SPEED,
)


class Player(CircleShape):
    continers = []

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.thrusting = False

        self.image = pygame.image.load(SPACESHIP_IMAGE).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        self.flame_image = pygame.image.load(FLAME_IMAGE).convert_alpha()
        self.flame_image = pygame.transform.smoothscale(self.flame_image, (32, 32))
        self.flame_image = pygame.transform.rotate(self.flame_image, 180)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.thrusting = False

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.thrusting = True
            self.move(-dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt)

    def draw(self, screen):
        if self.thrusting:
            forward = pygame.Vector2(0, -1).rotate(self.rotation)
            flame_offset = -forward * (self.radius + 30)
            flame_pos = self.position + flame_offset

            rotated_flame = pygame.transform.rotozoom(
                self.flame_image, -self.rotation, 1
            )
            flame_rect = rotated_flame.get_rect(center=flame_pos)
            screen.blit(rotated_flame, flame_rect)

        rotated_image = pygame.transform.rotozoom(self.image, -self.rotation, 1)
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
