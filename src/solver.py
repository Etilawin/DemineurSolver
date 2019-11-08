from random import randint
from demineur import Demineur


class Solver:
    def __init__(self, dem: Demineur, verbose=True):
        self.border = []
        self.dem = dem
        self.width, self.height = self.dem.get_board_size()
        self.random_sec_pass = 0
        self.v = verbose

    def solve(self):
        # First thing pick a random case
        x = randint(0, self.width - 1)
        y = randint(0, self.height - 1)
        end = self.dem.reveal_bomb(x, y)
        if not end:
            self.__init_border()
            assert len(self.border) != 0, "Logic exception border cannot be empty"
        else:
            if self.v: print("Sadly first guess was a bomb...")
            return 2

        while not end:
            second_pass = True
            third_pass = False
            # First pass simple check
            bordercpy = self.border.copy()
            for x, y in bordercpy:
                cell = self.dem.get_cell(x, y)
                neighbours = cell.get_neighbours()
                flagged_neighbours = [(x, y) for x, y in neighbours if self.dem.get_cell(x, y).is_flagged()]
                unrevealed_neighbours = [(x, y) for x, y in neighbours if not self.dem.get_cell(x, y).is_revealed()]
                nb_neighbour_bombs = cell.get_number_bombs()
                if len(flagged_neighbours) == nb_neighbour_bombs == len(unrevealed_neighbours):
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
                            if n_cell.reveal():
                                if self.v: print("The robot has lost miserably ...")
                                return 3
                            self.border.append((x2, y2))

            if self.dem.is_it_over():
                if self.v: print("Well done you won !")
                return 1

            if second_pass:
                bordercpy = self.border.copy()
                # This part works with probability, flagging the most probable cell
                # The idea is to try every possibility and see if there is one that works
                # For that we take the "2nd order neighbours"
                nb_zeros_cell = 0
                for y in range(self.height):
                    for x in range(self.width):
                        cell = self.dem.get_cell(x, y)
                        if cell.is_revealed() and cell.get_number_bombs() == 0:
                            nb_zeros_cell += 1

                if nb_zeros_cell == 0:
                    self.random_sec_pass += 1
                    if self.random_sec_pass >= 5:
                        if self.random_sec_pass % 5 == 0:
                            if self.v: print(self.dem)
                    # Well this I can't do a lot so random again !
                    if self.v: print("Need a random second pass sadly !")
                    x = randint(0, self.width - 1)
                    y = randint(0, self.height - 1)
                    end = self.dem.reveal_bomb(x, y)
                    if not end:
                        self.border.append((x, y))
                    else:
                        if self.v: print("Unluckily this was a bomb on the second pass")
                        return 4
                else:
                    if self.v: print("Need a true second pass...")
                    return 5
                    # for x, y in bordercpy:
                    #     cell = self.dem.get_cell(x, y)
                    #     neighbours = cell.get_neighbours()
                    #     second_order_neighbours = {}
                    #     for x2, y2 in neighbours:
                    #         second_order_neighbours[x2, y2] = self.dem.get_cell(x2, y2).get_neighbours()

            if third_pass:
                pass
        return False

    def __init_border(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.dem.get_cell(x, y)
                if cell.is_revealed() and cell.nb_neighbours_bombs != 0:
                    self.border.append((x, y))
