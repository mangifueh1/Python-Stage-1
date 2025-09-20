import pygame
from colors import Colors
from position import Position


class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.size = 30
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_all_colors()

    def move(self, rows, colums):
        self.row_offset += rows
        self.col_offset += colums

    def get_cell_positions(self):
        moved_tiles = []
        tiles = self.cells[self.rotation_state]
        for position in tiles:
            moved_tiles.append(
                Position(position.row + self.row_offset, position.col + self.col_offset))
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state >= len(self.cells):
            self.rotation_state = 0  

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            cell_rect = pygame.Rect(
                offset_x + tile.col*self.size, offset_y + tile.row*self.size, self.size - 1, self.size-1)
            pygame.draw.rect(screen, self.colors[self.id], cell_rect)

    @staticmethod
    def get_all_blocks():
        return [IBlock(), OBlock(), TBlock(), SBlock(),
                       ZBlock(), JBlock(), LBlock()]


class LBlock(Block):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)
    # def rotate(self):
    #     self.rotation_state = (self.rotation_state + 1) % 4


class IBlock(Block):
    def __init__(self):
        super().__init__(id=2)
        self.cells = {
            0: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],
            1: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            2: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],
            3: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)]
        }
        self.move(0, 3)

class OBlock(Block):
    def __init__(self):
        super().__init__(id=3)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        }
        self.move(0, 4)


class TBlock(Block):
    def __init__(self):
        super().__init__(id=4)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        self.move(0, 3)


class SBlock(Block):
    def __init__(self):
        super().__init__(id=5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            3: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)]
        }
        self.move(0, 3)


class ZBlock(Block):
    def __init__(self):
        super().__init__(id=6)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            3: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)]
        }
        self.move(0, 3)


class JBlock(Block):
    def __init__(self):
        super().__init__(id=7)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        self.move(0, 3)
