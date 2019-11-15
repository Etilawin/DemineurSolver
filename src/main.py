from demineur import Demineur
from solver import Solver

def test_nBombs(n_bombs, nb_tries,verbose = False):
    successes = 0
    first_fail = 0
    non_supposed_fails = 0
    random_bomb = 0
    no_second_pass = 0
    print("Solving for {} bombs".format(n_bombs))
    for i in range(nb_tries):
        dem = Demineur(size, n_bombs)
        solver = Solver(dem, verbose)
        res = solver.solve()
        if res == 5:
            no_second_pass += 1
        elif res == 4:
            random_bomb += 1
        elif res == 3:
            non_supposed_fails += 1
        elif res == 2:
            first_fail += 1
        elif res == 1:
            successes += 1
    print("Success percentage is of {}%".format(100 * float(successes)/float(nb_tries)))
    print("First fail percentage is of {}%".format(100 * float(first_fail) / float(nb_tries)))
    print("Non supposed fails percentage is of {}%".format(100 * float(non_supposed_fails) / float(nb_tries)))
    print("Random bomb percentage is of {}%".format(100 * float(random_bomb) / float(nb_tries)))
    print("No second pass percentage is of {}%".format(100 * float(no_second_pass) / float(nb_tries)))

if __name__ == "__main__":
    # dem.get_true_board()
    # print(dem)
    replay = True
    while replay:
        size = (10, 10)
        nb_tries = 100
        test_nBombs(2, nb_tries)
        # for n_bombs in range(1, 30):
        #     test_nBombs(n_bombs)
        #     print("------------------------")
        
        
        replay = False
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
