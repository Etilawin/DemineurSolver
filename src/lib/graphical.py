import pygame
from .cell import Cell
from .demineur import Demineur

display_width = 800
display_height = 900

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
grey = (125, 125, 125)

gameDisplay = pygame.display.set_mode((display_width, display_height))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(pos_x, pos_y, w, h, ic, dem: Demineur, x, y):
    global gameDisplay

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    b = False

    if pos_x + w > mouse[0] > pos_x and pos_y + h > mouse[1] > pos_y:
        if click[0] == 1:
            b = dem.reveal_bomb(x, y)
            if b:
                print("You lost... Because of a bomb !")
                pygame.quit()
        elif click[2] == 1:
            dem.set_flag(x, y)

    pygame.draw.rect(gameDisplay, ic, (pos_x, pos_y, w, h))

    if cell.is_revealed():
        msg = str(cell.nb_neighbours_bombs())
    elif cell.is_flagged():
        msg = "!"
    else:
        msg = ""

    small_text = pygame.font.SysFont("comicsansms", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((pos_x + (w / 2)), (pos_y + (h / 2)))
    gameDisplay.blit(text_surf, text_rect)


def start(size: (int, int), dem: Demineur):
    pygame.init()

    pygame.display.set_caption('Minesweeper !')
    clock = pygame.time.Clock()

    board = dem.get_board()

    width, height = size
    square_size = display_width // width

    try:
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

            gameDisplay.fill(white)

            for y in range(height):
                for x in range(width):
                    button(x * square_size, y * square_size, square_size, square_size, grey, dem, x, y)

            pygame.display.update()

            if dem.is_it_over():
                crashed = True
                print("Bravo tu as gagné")

            clock.tick(15)
    finally:
        pygame.quit()




