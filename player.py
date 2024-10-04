from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame

from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, delta):
        self.rotation += delta * PLAYER_TURN_SPEED

    def update(self, delta):
        self.shot_timer -= delta
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta)
        if keys[pygame.K_d]:
            self.rotate(delta)
        if keys[pygame.K_w]:
            self.move(delta)
        if keys[pygame.K_s]:
            self.move(-delta)
        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                self.shoot(delta)

    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta

    def shoot(self, delta):
        rotation = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = PLAYER_SHOOT_SPEED * rotation
        self.shot_timer = PLAYER_SHOOT_COOLDOWN