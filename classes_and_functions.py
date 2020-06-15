import pygame
from pygame.locals import *

from constants import *

from random import randint

class Tile:
    def __init__(self, i, j, width, height):
        self.i = i
        self.j = j
        self.width = width
        self.height = height
        self.walls = [True, True, True, True]
        self.visited = False
    
    def show(self, screen):
        x = self.i * self.width
        y = self.j * self.height

        if self.walls[0]:
            pygame.draw.line(screen, LINE_COLOR, (x, y), (x + self.width, y), 2)
        if self.walls[1]:
            pygame.draw.line(screen, LINE_COLOR, (x, y), (x, y + self.height), 2)
        if self.walls[2]:
            pygame.draw.line(screen, LINE_COLOR, (x, y + self.height), (x + self.width, y +self.height), 2)
        if self.walls[3]:
            pygame.draw.line(screen, LINE_COLOR, (x + self.width, y), (x + self.width, y + self.height), 2)
        
        if self.visited:
            pygame.draw.rect(screen, VISITED_COLOR, (x + 2, y + 2, self.width - 2, self.height - 2))

    def check_neighbors(self, grid):
        neighbors = []

        top_index = get_index(self.i, self.j - 1)
        right_index = get_index(self.i - 1, self.j)
        bottom_index = get_index(self.i, self.j + 1)
        left_index = get_index(self.i + 1, self.j)

        if top_index != -1:
            top = grid[top_index]
            neighbors.append(top)

        if right_index != -1:
            right = grid[right_index]
            neighbors.append(right)

        if  bottom_index != -1:
            bottom = grid[bottom_index]
            neighbors.append(bottom)

        if  left_index!= -1:
            left = grid[left_index]
            neighbors.append(left)

        neighbors = [neighbor for neighbor in neighbors if neighbor.visited == False]

        if len(neighbors) > 0:
            index = randint(0, len(neighbors) - 1)
            return neighbors[index]
        else:
            return None

    def remove_walls(self, neighbor):
        x = self.i - neighbor.i
        if x == 1:
            self.walls[1] = False
            neighbor.walls[3] = False
        elif x == -1:
            self.walls[3] = False
            neighbor.walls[1] = False
        y = self.j - neighbor.j
        if y == 1:
            self.walls[0] = False
            neighbor.walls[2] = False
        elif y == -1:
            self.walls[2] = False
            neighbor.walls[0] = False

    def highlight(self, screen):
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, pygame.Rect(self.i * self.width + 2, self.j * self.height + 2, self.width - 2, self.height - 2))

def get_index(i, j):
    if i < 0 or j < 0 or i > COLUMNS - 1 or j > ROWS - 1:
        return -1
    return i + j * COLUMNS
