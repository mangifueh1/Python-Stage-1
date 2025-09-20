import random
from tile import Tile


class Snake(Tile):
    def __init__(self):
        self.body = [Tile(0, 0, 'down')]

    def move(self):
        for tile in self.body:
            self.move_direction = tile.move_direction
            tile.move()

    def draw(self, screen):
        for tile in self.body:
            tile.draw(screen)
