import pygame
from init_gui import *
from text import *
from global_variables import *

def init_engine():

	game_over = False
	start_board()



def start_board():
	board_img = pygame.image.load('media/board.jpg')
	gameDisplay.blit(board_img, (0, 0))

	pygame.display.update()
