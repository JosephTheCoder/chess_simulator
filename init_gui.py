import pygame
from global_variables import *

pygame.init()

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Chess Simulator')
clock = pygame.time.Clock()