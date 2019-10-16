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
        self.nbBombs = nb_bombs
        self.board = [[Cell(size, x, y) for y in range(size[1])] for x in range(size[0])]
        self.__init_board()
        self.__create_neighbours()

    def __create_neighbours(self):
        for x in range(self.width):
            for y in range(self.height):
                neighbours = [self.board[y+dy][x+dx] for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                              if 0 <= x+dx <= self.width - 1 and 0 <= y + dy <= self.height - 1]
                self.board[y][x].set_neighbours(neighbours)

    def __init_board(self):
        # Random generator of bombs
        bombs_to_place = self.nbBombs
        while bombs_to_place != 0:
            x = randint(0, self.width-1)
            y = randint(0, self.height-1)
            placed = self.__place_bomb(x, y)
            if placed:
                bombs_to_place -= 1

    def __place_bomb(self, x, y):
        if self.board[y][x].is_bomb():
            return False

        self.board[y][x].set_bomb()
        return True

    def set_flag(self, x, y):
        c = self.board[y][x]
        c.set_flag(not c.is_flagged())

    def reveal_bomb(self, x, y):
        c = self.board[y][x]
        c.reveal()
        return c.is_bomb()

    def is_it_over(self):
        res = []
        for x in range(self.width):
            res.append(all((self.board[y][x].is_bomb() and self.board[y][x].is_flagged()) or (not self.board[y][x].is_bomb() and self.board[y][x].is_revealed()) for y in range(self.height)))
        return all(res)

    def __str__(self):
        ret = ""
        for x in range(self.width):
            ret += "*-"*self.width + "*\n"
            for y in range(self.height):
                ret += "|{}".format(self.board[y][x])
            ret += "|\n"
        return ret + "*-"*self.width + "*"



