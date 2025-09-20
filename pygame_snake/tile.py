import pygame
from colors import Colors


class Tile:
    def __init__(self, x, y, direction):
        self.color = Colors.yellow
        self.size = 25
        self.x = x*self.size
        self.y = y*self.size
        self.velocity = 25
        self.move_direction = direction

    def move(self):
        if self.move_direction == 'right':
            self.move_right()
        elif self.move_direction == 'left':
            self.move_left()
        elif self.move_direction == 'up':
            self.move_up()
        elif self.move_direction == 'down':
            self.move_down()

    def move_left(self):
        self.x += -self.velocity

    def move_right(self):
        self.x += self.velocity

    def move_up(self):
        self.y += -self.velocity

    def move_down(self):
        self.y += self.velocity

    def draw(self, screen):
        tile = pygame.Rect(
            (self.x + 1, self.y + 1), (self.size - 1, self.size-1))
        pygame.draw.rect(screen, self.color, tile)
