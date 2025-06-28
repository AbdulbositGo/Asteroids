import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        rotated_image = pygame.transform.rotozoom(
            self.original_image, -self.rotation, 1
        )
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)

    def update(self, dt):
        # sub-classes must override
        pass
