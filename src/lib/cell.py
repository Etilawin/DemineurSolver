class Cell:
    def __init__(self, b=False):
        self.__bomb = b
        self.flag = False
        self.revealed = False
        self.neighbours = []
        self.nb_neighbours_bombs = 0

    def change_flag(self):
        if not self.revealed:
            self.flag = not self.flag

    def is_flagged(self):
        return self.flag

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours
        self.nb_neighbours_bombs = sum([c.__bomb for c in self.neighbours])

    def get_neighbours(self):
        return self.neighbours

    def nb_neighbour_bombs(self):
        return self.nb_neighbours_bombs

    def reveal(self):
        if not self.flag:
            self.revealed = True
            if self.nb_neighbours_bombs == 0:
                for c in self.neighbours:
                    if not c.is_revealed():
                        c.reveal()
            return self.__bomb
        return None

    def is_revealed(self):
        return self.revealed

    def __str__(self):
        if self.flag:
            return "!"
        elif self.revealed:
            if self.__bomb:
                return "o"
            return "{}".format(self.nb_neighbours_bombs)  #  if self.nb_neighbours_bombs != 0 else " "
        return " "
