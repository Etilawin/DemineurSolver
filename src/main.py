from lib.demineur import Demineur
from lib.solver import Solver

if __name__ == "__main__":
    # dem.get_true_board()
    # print(dem)
    replay = True
    while replay:
        size = (10, 10)
        dem = Demineur(size, 1)
        solver = Solver(dem)

        # end = False
        # while not end:
        #     print(dem)
        #     coord = input("Please enter the coordinates x,y,[f,r] : ").strip().split(",")
        #     x, y = int(coord[0]), int(coord[1])
        #     if "f" in coord[2]:
        #         dem.set_flag(x, y)
        #     elif "r" in coord[2]:
        #         res = dem.reveal_bomb(x, y)
        #         if res:
        #             end = True
        #             print("You have lost by revealing a bomb in {}, {}! ".format(x, y))
        #             continue
        #
        #     if dem.is_it_over():
        #         end = True
        #         print("Well done you won !")
        # replay = input("Do you want to replay ? (y/n)").strip().lower() == "y"
