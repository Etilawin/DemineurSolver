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

    def set_neighbours(self, neighbours: [(int, int)], nb_neighbour_bombs: int):
        self.neighbours = neighbours
        self.nb_neighbours_bombs = nb_neighbour_bombs

    def get_neighbours(self) -> []:
        return self.neighbours

    def get_number_bombs(self) -> int:
        return self.nb_neighbours_bombs

    def reveal(self) -> bool:
        if not self.flag and not self.revealed:
            self.revealed = True
            return self.__bomb
        if self.flag : print("Didn't reveal because flagged")
        if self.revealed : print("Didn't reveal because already revealed")

    def is_revealed(self):
        return self.revealed

    def is_bomb(self):
        return self.__bomb

    # def op_str(self):
    #     if self.__bomb:
    #         return "o"
    #     return "{}".format(self.nb_neighbours_bombs)  #  if self.nb_neighbours_bombs != 0 else " "

    def __str__(self):
        if self.flag:
            return "!"
        elif self.revealed:
            if self.__bomb:
                return "o"
            return "{}".format(self.nb_neighbours_bombs)  #  if self.nb_neighbours_bombs != 0 else " "
        return " "
