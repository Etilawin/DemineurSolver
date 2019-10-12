from Cell import Cell

class Demineur:
    def __init__(self, size, nbBombs):
        assert isinstance(size, tuple), "__init__: Demineur: size is not a tuple"
        assert len(size) == 2, "__init__: Demineur: size is not of size 2"
        self.width, self.height = size
        self.nbBombs = nbBombs
        this.board = [[Cell() for y in range(size[1])] for x in range(size[0])]
        this.__initBoard()

    def __initBoard(self):

        pass
