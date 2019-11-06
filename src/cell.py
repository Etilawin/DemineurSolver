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

    def get_neighbours(self) -> []:
        return self.neighbours

    def nb_neighbour_bombs(self) -> int:
        if self.revealed:
            return self.nb_neighbours_bombs

    def reveal(self) -> bool:
        # print(self.nb_neighbours_bombs)
        if not self.flag and not self.revealed:
            self.revealed = True
            if self.nb_neighbours_bombs == 0:
                for c in self.neighbours:
                    c.reveal()
            return self.__bomb

    def is_revealed(self):
        return self.revealed

    def op_str(self):
        if self.__bomb:
            return "o"
        return "{}".format(self.nb_neighbours_bombs)  #  if self.nb_neighbours_bombs != 0 else " "

    def __str__(self):
        if self.flag:
            return "!"
        elif self.revealed:
            if self.__bomb:
                return "o"
            return "{}".format(self.nb_neighbours_bombs)  #  if self.nb_neighbours_bombs != 0 else " "
        return " "
