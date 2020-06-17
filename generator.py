import pygame
from pygame.locals import *

import sys
from random import randint

from tile import Tile
from utils import get_index
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
        
        current.highlight(SCREEN, True)
        
        neighbors = current.check_neighbors(grid)
        neighbors = [neighbor for neighbor in neighbors if neighbor.visited == False and neighbor.i != -1]
        
        if len(neighbors) > 0:
            neighbor_index = randint(0, len(neighbors) - 1)
            next_visit = neighbors[neighbor_index]
        else:
            next_visit = False

        if next_visit:
            stack.append(current)
            current.remove_walls(next_visit)
            next_visit.visited = True
            current = next_visit
        elif len(stack) > 0:
            current = stack.pop()
        else:
            SCREEN.fill(VISITED_COLOR)
            for tile in grid:
                tile.show(SCREEN)
            
            grid[0].highlight(SCREEN, True)
            grid[-1].highlight(SCREEN, True)
            
            pygame.image.save(SCREEN, 'maze.png')
            



if __name__ == '__main__':
    main()
