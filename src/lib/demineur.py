from .cell import Cell
from random import randint, random
from copy import deepcopy


class Demineur:
    def __init__(self, size, nb_bombs):
        assert isinstance(size, tuple), "__init__: Demineur: size is not a tuple"
        assert len(size) == 2, "__init__: Demineur: size is not of size 2"
        assert isinstance(nb_bombs, int), "__init__: Demineur: nbBombs is not an int"
        assert nb_bombs < size[0] * size[1]
        self.width, self.height = size
        self.nb_bombs = nb_bombs
        self.board = []
        self.__init_board()
        self.__create_neighbours()

    def __create_neighbours(self):
        for y in range(self.height):
            for x in range(self.width):
                neighbours = [self.board[y+dy][x+dx] for dy in [-1, 0, 1] for dx in [-1, 0, 1]
                              if 0 <= x+dx <= self.width - 1 and 0 <= y + dy <= self.height - 1]
                self.board[y][x].set_neighbours(neighbours)

    def __init_board(self):
        # Random generator of bombs
        bombs_to_place = self.nb_bombs
        placed_bombs = []
        while bombs_to_place != 0:
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            if not (x, y) in placed_bombs:
                placed_bombs.append((x, y))
                bombs_to_place -= 1
        assert len(placed_bombs) == self.nb_bombs, "__init_board: Demineur: Logic exception"
        for y in range(self.height):
            self.board.append([])
            for x in range(self.width):
                if (x, y) in placed_bombs:
                    self.board[y].append(Cell(True))
                else:
                    self.board[y].append(Cell())

    def set_flag(self, x, y):
        c = self.board[y][x]
        c.set_flag(not c.is_flagged())

    def reveal_bomb(self, x, y):
        c = self.board[y][x]
        return c.reveal()  # True if c is a bomb False otherwise

    def is_it_over(self):
        nb_revealed = 0
        for y in range(self.height):
            for x in range(self.width):
                if not self.board[y][x].is_revealed():
                    nb_revealed += 1
        return nb_revealed == self.nb_bombs

    def __str__(self):
        ret = ""
        for y in range(self.height):
            ret += "*-"*self.width + "*\n"
            for x in range(self.width):
                ret += "|{}".format(self.board[y][x])
            ret += "|\n"
        return ret + "*-"*self.width + "*"



