from random import randint
from .cell import Cell
from .demineur import Demineur


class Solver:
    def __init__(self, dem: Demineur):
        self.border = []
        self.dem = dem
        self.width, self.height = self.dem.get_board_size()

    def solve(self):
        # First thing pick a random case
        x = randint(0, self.width)
        y = randint(0, self.height)
        end = self.dem.reveal_bomb(x, y)
        if not end:
            self.__init_border()
            assert len(self.border) != 0, "Logic exception border cannot be empty"

        print(end)
        print(x, y)
        print(self.border)

        # while not end:
        #     pass
            # coord = input("Please enter the coordinates x,y,[f,r] : ").strip().split(",")
            # x, y = int(coord[0]), int(coord[1])
            # if "f" in coord[2]:
            #     self.dem.set_flag(x, y)
            # elif "r" in coord[2]:
            #     res = dem.reveal_bomb(x, y)
            #     if res:
            #         end = True
            #         print("You have lost by revealing a bomb in {}, {}! ".format(x, y))
            #         continue
            #
            # if dem.is_it_over():
            #     end = True
            #     print("Well done you won !")

    def __init_border(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.dem.get_cell(x, y)
                if cell.is_revealed() and cell.nb_neighbours_bombs != 0:
                    self.border.append((x, y))

