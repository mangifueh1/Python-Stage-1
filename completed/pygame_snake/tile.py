import pygame
from colors import Colors


class Tile:
    def __init__(self, x, y, direction, old_direction):
        self.color = Colors.yellow
        self.size = 25
        self.x = x
        self.y = y
        self.oldx = 0
        self.oldy = 0
        self.current_direction = direction
        self.old_direction = old_direction
        self.velocity = 1

    def move(self, direction):
        self.oldx = self.x
        self.oldy = self.y
        self.old_direction = self.current_direction
        if direction == 'right':
            self.x += self.velocity
            self.current_direction = 'right'
        elif direction == 'left':
            self.x += -self.velocity
            self.current_direction = 'left'
        elif direction == 'up':
            self.y += -self.velocity
            self.current_direction = 'up'
        elif direction == 'down':
            self.y += self.velocity
            self.current_direction = 'down'

    def draw(self, screen):
        tile = pygame.Rect(
            (self.x * self.size) + 1, (self.y * self.size) + 1, self.size - 1, self.size-1)
        pygame.draw.rect(screen, self.color, tile)
