import secrets
from tile import Tile


class Snake():
    def __init__(self):
        self.direction = 'right'
        self.startX = 0
        self.startY = 0
        self.segments = [Tile(self.startX, self.startY,
                              self.direction, self.direction)]

    def change_direction(self, direction):
        self.direction = direction
        self.segments[0].old_direction = self.direction

    def add_segment(self, x, y):
        last = self.segments[-1]
        self.segments.append(Tile(x, y, last.old_direction, ''))

    def get_direction(self):
        return self.direction

    def move(self):
        for segment in self.segments:
            index = self.segments.index(segment)
            if index == 0:
                segment.move(self.direction)
            else:
                segment.move(self.segments[index - 1].old_direction)

    def draw(self, screen):
        for segment in self.segments:
            segment.draw(screen)
