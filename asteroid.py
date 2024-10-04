import pygame, random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, delta):
        self.position += self.velocity * delta

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        scatter = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(scatter)
        velocity2 = self.velocity.rotate(-scatter)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2.velocity = velocity2 * 1.2