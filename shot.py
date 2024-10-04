import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = 0
        #self.rotation = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def update(self, delta):
        self.position += self.velocity * delta