import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    global gameDisplay

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    # if x+w > mouse[0] > x and y+h > mouse[1] > y:
    #    pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

    if click[0] == 1 and action is not None:
        action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    small_text = pygame.font.SysFont("comicsansms",20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(text_surf, text_rect)


def start():
    pass
