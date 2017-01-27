import pygame
from init_gui import *
from text import *
from global_variables import *

def game_intro():

    intro = True
    background = pygame.image.load('media/menu_background.jpg')

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(background, (0, 0))
        startTitle = largeText.render("Chess Simulator", 1, black)
        gameDisplay.blit(startTitle, (display_width * 0.22, display_height * 0.2))

        mouse = pygame.mouse.get_pos()

        if 300+200 > mouse[0] > 300 and 250+80 > mouse[1] > 250:
            pygame.draw.rect(gameDisplay, bright_grey, (300,250,200,80))
        else:
            pygame.draw.rect(gameDisplay, grey, (300,250,200,80))


        pygame.display.update()
        clock.tick(15)


