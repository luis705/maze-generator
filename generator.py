import pygame
from pygame.locals import *

import sys

from classes_and_functions import Tile, get_index
from constants import *

#  Initialize pygame
pygame.init()

def setup():
    grid = []

    for j in range(ROWS):
        for i in range(COLUMNS):
            tile = Tile(i, j, TILE_WIDTH, TILE_HEIGHT) 
            grid.append(tile)
    
    return grid, grid[0]
    

def main():
    grid, current = setup()

    while True:
        pygame.display.update()
        SCREEN.fill(UNVISITED_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        for tile in grid:
            tile.show(SCREEN)
        
        current.visited = True
        next_visit = current.check_neighbors(grid)

        if next_visit:
            current.remove_walls(next_visit)
            next_visit.visited = True
            current = next_visit

        pygame.time.delay(200)



if __name__ == '__main__':
    main()
