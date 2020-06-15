import pygame
from pygame.locals import *

LINE_COLOR = (30, 100, 30)

class Tile:
    def __init__(self, i, j, width, height):
        self.i = i
        self.j = j
        self.width = width
        self.height = height
        self.walls = [True, True, True, True]
    
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
