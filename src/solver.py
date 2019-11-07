from random import randint
from demineur import Demineur


class Solver:
    def __init__(self, dem: Demineur):
        self.border = []
        self.dem = dem
        self.width, self.height = self.dem.get_board_size()

    def solve(self):
        # First thing pick a random case
        x = randint(0, self.width - 1)
        y = randint(0, self.height - 1)
        end = self.dem.reveal_bomb(x, y)
        if not end:
            self.__init_border()
            assert len(self.border) != 0, "Logic exception border cannot be empty"

        while not end:
            second_pass = True
            # First pass simple check
            bordercpy = self.border.copy()
            for x, y in bordercpy:
                cell = self.dem.get_cell(x, y)
                neighbours = cell.get_neighbours()
                flagged_neighbours = [(x, y) for x, y in neighbours if self.dem.get_cell(x, y).is_flagged()]
                unrevealed_neighbours = [(x, y) for x, y in neighbours if not self.dem.get_cell(x, y).is_revealed()]
                nb_neighbour_bombs = cell.get_number_bombs()
                if len(flagged_neighbours) == nb_neighbour_bombs == len(unrevealed_neighbours) :
                    self.border.remove((x, y))
                elif len(unrevealed_neighbours) == nb_neighbour_bombs:
                    # Great easy one we just got a simple case there
                    self.border.remove((x, y))
                    for x2, y2 in unrevealed_neighbours:
                        n_cell = self.dem.get_cell(x2, y2)
                        if not n_cell.is_flagged():
                            n_cell.change_flag()
                elif len(flagged_neighbours) == nb_neighbour_bombs:
                    # Great again simple case !
                    second_pass = False
                    self.border.remove((x, y))
                    for x2, y2 in neighbours:
                        n_cell = self.dem.get_cell(x2, y2)
                        if not n_cell.is_revealed() and not n_cell.is_flagged():
                            end = end or n_cell.reveal()
                            self.border.append((x2, y2))
            if end:
                print("The robot has lost miserably ...")

            if second_pass:
                print("Second pass needed ...")
                end = True

            if self.dem.is_it_over():
                end = True
                print("Well done you won !")

    def __init_border(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.dem.get_cell(x, y)
                if cell.is_revealed() and cell.nb_neighbours_bombs != 0:
                    self.border.append((x, y))

