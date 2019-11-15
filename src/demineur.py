from cell import Cell
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
                neighbours = [(x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                              if 0 <= y + dy <= self.height - 1 and 0 <= x+dx <= self.width - 1 and not dx == dy == 0]
                nb_bombs = sum([self.get_cell(x, y).is_bomb() for x, y in neighbours])
                self.board[y][x].set_neighbours(neighbours, nb_bombs)

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

    def get_board(self):
        return self.board

    def get_board_size(self):
        return self.width, self.height

    def get_true_board(self):
        for y in range(self.height):
            for x in range(self.width):
                print(" {} ".format(self.board[y][x].op_str()), end="")
            print()

    def get_cell(self, x: int, y: int) -> Cell:
        return self.board[y][x]

    def flag_bomb(self, x: int, y: int):
        self.board[y][x].set_flag()

    def unflag_bomb(self, x: int, y: int):
        self.board[y][x].unset_flag()

    def reveal_bomb(self, x: int, y: int):
        c = self.board[y][x]
        res = False
        if not c.is_revealed() and not c.is_flagged():
            res = c.reveal()
            assert c.is_revealed(), "This cell should be revealed"
            if not res:
                # If it is not a bomb reveal the other one
                if c.get_number_bombs() == 0:
                    for x2, y2 in c.get_neighbours():
                        if not self.board[y2][x2].is_revealed():
                            self.reveal_bomb(x2, y2)
        return res
        # if not c.is_revealed() and not c.is_flagged():
        #     if c.reveal():
        #         return True
        #     if c.get_number_bombs() == 0:
        #         for x2, y2 in c.get_neighbours():
        #             print(x2, y2)
        #             if not self.board[y2][x2].is_revealed():
        #                 self.reveal_bomb(x2, y2)
        #     return False

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



