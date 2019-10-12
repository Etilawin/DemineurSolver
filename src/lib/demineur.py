from Cell import Cell
from random import randint, random

class Demineur:
    def __init__(self, size, nbBombs):
        assert isinstance(size, tuple), "__init__: Demineur: size is not a tuple"
        assert len(size) == 2, "__init__: Demineur: size is not of size 2"
        assert isinstance(nbBombs, int), "__init__: Demineur: nbBombs is not an int"
        assert nbBombs < size[0] * size[1]
        self.width, self.height = size
        self.nbBombs = nbBombs
        this.board = [[Cell() for y in range(size[1])] for x in range(size[0])]
        this.__initBoard()

    def __initBoard(self):
        # Random generator of bombs
        bombsToPlace = self.nbBombs
        while bombsToPlace != 0:
            placed = self.placeBomb()
            if placed:
                bombsToPlace -= 1

    def placeBomb(self):
        pass
