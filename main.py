import sys

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([400, 300])
icon = pygame.image.load("bjarte.jpg")
pygame.display.set_icon(icon)
pygame.display.set_caption("Bjarte's Amazing Game!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
