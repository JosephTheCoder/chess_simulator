import pygame
from global_variables import *

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Chess Simulator')
clock = pygame.time.Clock()