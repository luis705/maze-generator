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
    current.visited = True
    stack = []

    while True:
        pygame.display.update()
        SCREEN.fill(VISITED_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        for tile in grid:
            tile.show(SCREEN)
        
        current.highlight(SCREEN)
        
        next_visit = current.check_neighbors(grid)

        if next_visit:
            stack.append(current)
            current.remove_walls(next_visit)
            next_visit.visited = True
            current = next_visit
        elif len(stack) > 0:
            current = stack.pop()
        #pygame.time.delay(10)



if __name__ == '__main__':
    main()
