from numpy import block
from block import *
from grid import Grid
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = Block.get_all_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.game_speed = 200

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800
        self.score += move_down_points

    def reset(self):
        self.grid.reset()
        self.blocks = Block.get_all_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = Block.get_all_blocks()
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_fits():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_fits():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_fits():
            self.current_block.move(-1, 0)
            self.lock_in_place()

    def lock_in_place(self):
        for cell in self.current_block.get_cell_positions():
            self.grid.grid[cell.row][cell.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared, 0)
        if self.score > 0 and (self.score/100) % 10 == 0 and self.game_speed > 100 and rows_cleared > 0:
            self.game_speed -= 100
        if not self.block_fits():
            self.game_over = True

    def block_fits(self):
        for cell in self.current_block.get_cell_positions():
            if not self.grid.is_inside(cell.row, cell.col) or not self.grid.is_empty(cell.row, cell.col):
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside():
            for _ in range(3):
                self.current_block.rotate()

    def block_inside(self):
        for cell in self.current_block.get_cell_positions():
            if not self.grid.is_inside(cell.row, cell.col):
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 2:
            self.next_block.draw(screen, 270, 250)
        elif self.next_block.id == 3:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
