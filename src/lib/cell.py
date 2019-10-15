class Cell:
    def __init__(self, x, y, size):
        self.bomb = False
        self.flag = False
        self.revealed = False
        self.neighbours = []
        self.nb_neighbours_bombs = 0

    def set_bomb(self):
        self.bomb = True

    def is_bomb(self):
        return self.bomb

    def set_flag(self, b):
        assert isinstance(b, bool), "setFlag: Cell: b is not a boolean"
        self.flag = b

    def is_flagged(self):
        return self.flag

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours
        self.nb_neighbours_bombs = sum([c.is_bomb() for c in self.get_neighbours()])

    def get_neighbours(self):
        return self.neighbours

    def __str__(self):
        if self.flag:
            return "!"
        elif self.revealed:
            if self.bomb:
                return "o"
            return "{}".format(self.nb_neighbours_bombs)  #  if self.nb_neighbours_bombs != 0 else " "
        return " "
