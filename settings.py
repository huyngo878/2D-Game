import pygame
import sys
import os

#game setup
FPS = 60
WIDTH = 800
HEIGHT = 600
VELOCITY = 3
MAP_IMAGE = pygame.image.load(os.path.join('maps', 'map1.png'))

#size of screen
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

#name of application
pygame.display.set_caption("Client Game")
