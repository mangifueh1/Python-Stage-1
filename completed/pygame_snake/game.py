import pygame
from apple import Apple
from colors import Colors
from snake import Snake


class Game:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
        self.game_over = False
        self.paused = False
        self.score = 0

    def change_direction(self, direction):
        if not self.is_opposite(direction, self.snake.get_direction()):
            self.snake.change_direction(direction)

    def reset(self):
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.game_over = False

    def pause(self):
        self.paused = not self.paused

    def move(self):
        self.snake.move()

    def is_game_end(self):
        for segment in self.snake.segments:
            index = self.snake.segments.index(segment)
            head = self.snake.segments[0]
            if segment.x < 0 or segment.x > segment.size - 1 or segment.y < 0 or segment.y > segment.size - 1:
                self.game_over = True
            if index != 0 and segment.x == head.x and segment.y == head.y:
                self.game_over = True

    def is_collision(self):
        return self.apple.x == self.snake.segments[0].x and self.apple.y == self.snake.segments[0].y

    def is_body(self):
        for segment in self.snake.segments:
            if self.apple.x == segment.x and self.apple.y == segment.y:
                self.apple.move()

    def extend_snake(self):
        last = self.snake.segments[-1]
        self.snake.add_segment(
            last.oldx, last.oldy
        )

    def is_opposite(self, a, b):
        return (a == 'left' and b == 'right') or (a == 'right' and b == 'left') or (a == 'up' and b == 'down') or (a == 'down' and b == 'up')

    def text(self, text, coordinates, size=int, screen=pygame.SurfaceType, centered=False):
        font = pygame.font.Font(None, size)
        surface = font.render(text, True, Colors.white)
        if not centered:
            screen.blit(surface, coordinates)
        else:
            screen.blit(surface, surface.get_rect(
                centerx=screen.get_width()/2, centery=screen.get_height()/2
            ))

    def draw(self, screen):
        self.apple.draw(screen)
        self.snake.draw(screen)
