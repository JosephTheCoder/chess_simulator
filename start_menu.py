import pygame
from init_gui import *
from text import *
from global_variables import *

def game_intro():

    intro = True
    background = pygame.image.load('media/menu_background.jpg')

    while intro:    
        gameDisplay.blit(background, (0, 0))
        startTitle = largeText.render("Chess Simulator", 1, BLACK)
        gameDisplay.blit(startTitle, (DISPLAY_WIDTH * 0.22, DISPLAY_HEIGHT * 0.2))

        #Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                x, y = event.pos
                if 300+200 > x > 300 and 250+80 > y > 250:
                    print("You pressed the button!")   #START THE GAME
                    intro = False

        mouse = pygame.mouse.get_pos()

        #Starting Button
        if 300+200 > mouse[0] > 300 and 250+80 > mouse[1] > 250:
            pygame.draw.rect(gameDisplay, BRIGHT_GREY, (300,250,200,80))
        else:
            pygame.draw.rect(gameDisplay, GREY, (300,250,200,80))

        startButton_text = smallText.render("START", 1, BLACK)
        gameDisplay.blit(startButton_text, (350, 270))





        pygame.display.update()
        clock.tick(15)

    gameDisplay.fill(WHITE)