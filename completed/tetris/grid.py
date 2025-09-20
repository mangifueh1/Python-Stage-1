import pygame
from colors import Colors


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for _ in range(self.num_cols)]
                     for _ in range(self.num_rows)]
        self.colors = Colors.get_all_colors()

    def reset(self):
        self.grid = [[0 for _ in range(self.num_cols)]
                     for _ in range(self.num_rows)]

    def is_inside(self, row, column):
        return 0 <= row < self.num_rows and 0 <= column < self.num_cols

    def is_empty(self, row, column):
        return self.grid[row][column] == 0

    def is_row_full(self, row):
        return all(cell != 0 for cell in self.grid[row])

    def clear_rows(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_rows_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_rows(row)
                completed += 1
            elif completed > 0:
                self.move_rows_down(row, completed)
        return completed

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column*self.cell_size + 11, row*self.cell_size + 11, self.cell_size - 1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
