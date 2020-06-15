import pygame
from pygame.locals import *

import sys

from tile import Tile

#  Initialize pygame
pygame.init()

#  Defining constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TILE_WIDTH = 40
TILE_HEIGHT = 40
COLUMNS  = SCREEN_WIDTH // TILE_WIDTH
ROWS = SCREEN_HEIGHT // TILE_HEIGHT


def setup():
    SCREEN.fill((0, 150, 0))

    grid = []

    for j in range(ROWS):
        for i in range(COLUMNS):
            tile = Tile(i, j, TILE_WIDTH, TILE_HEIGHT) 
            grid.append(tile)
    
    for tile in grid:
        tile.show(SCREEN)


def main():
    setup()

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
