from lib import demineur, graphical

if __name__ == "__main__":
    size = (40, 40)
    dem = demineur.Demineur(size, 10)
    graphical.start(size, dem)
    # print(dem)
    # end = False
    # while not end:
    #     print(dem)
    #     coord = input("Please enter the coordinates y,x,[f,r] : ").strip().split(",")
    #     x, y = int(coord[0]), int(coord[1])
    #     if "f" in coord[2]:
    #         dem.set_flag(x, y)
    #     elif "r" in coord[2]:
    #         res = dem.reveal_bomb(x, y)
    #         if res:
    #             end = True
    #             print("Vous avez perdu... Vous avez révelé une bombe en {}, {}! ".format(x, y))
    #             continue
    #
    #     if dem.is_it_over():
    #         end = True
    #         print("Bravo tu as gagné !")
    #         continue
