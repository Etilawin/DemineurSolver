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
                flagged_neighbours = [c for c in neighbours if c.is_flagged()]
                unrevealed_neighbours = [c for c in neighbours if not c.is_revealed()]
                nb_neighbour_bombs = cell.nb_neighbours_bombs()
                if len(flagged_neighbours) == nb_neighbour_bombs == len(unrevealed_neighbours) :
                    self.border.remove((x, y))
                else:
                    if len(unrevealed_neighbours) == nb_neighbour_bombs:
                        # great easy one we just got a simple case there
                        second_pass = False
                        self.border.remove((x, y))
                        for c in unrevealed_neighbours:
                            if not c.is_flagged():
                                c.change_flag()
                        break
                    # if len(flagged_neighbours) ==

            if second_pass:
                #  Second pass if first pass failed to find something
                pass

    def __init_border(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.dem.get_cell(x, y)
                if cell.is_revealed() and cell.nb_neighbours_bombs != 0:
                    self.border.append((x, y))

