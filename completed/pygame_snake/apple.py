from tile import Tile
import random
from colors import Colors
import pygame


class Apple:
    def __init__(self):
        self.color = Colors.red
        self.size = 25
        self.x = random.randint(0, 24)
        self.y = random.randint(0, 24)

    def move(self):
        self.x = random.randint(0, 24)
        self.y = random.randint(0, 24)

    def draw(self, screen):
        apple = pygame.Rect(
            (self.x * self.size + 1, self.y * self.size + 1), (self.size - 1, self.size-1))
        pygame.draw.rect(screen, self.color, apple)
