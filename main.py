import pygame
from global_variables import *
from init_gui import *
from start_menu import *
from game_window import *


crashed = False

game_intro()

while not crashed:

    for event in pygame.event.get():  #get the events (keystrokes, mouse moves, clicks, etc)
        if event.type == pygame.QUIT:
            crashed = True

    
    init_engine()
    pygame.display.update()
    clock.tick(60)  #sets the clock of the game

pygame.quit()
quit()