from random import randint
from .cell import Cell
from .demineur import Demineur


class Solver:
    def __init__(self, board: [[Cell]], dem: Demineur):
        self.border = {}
        self.board = board
        self.dem = dem

    def solve(self):
        # First thing pick a random case
        x = randint(0, len(self.board))
        y = randint(0, len(self.board[0]))
        self.dem.reveal_bomb(x, y)

