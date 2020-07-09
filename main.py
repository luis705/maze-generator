import pygame

import sys
from random import randint

from tile import Tile


class Generator:
    def __init__(self):
        #  Screen setup
        self.width = 602
        self.height = 602
        self.win = pygame.display.set_mode((self.width, self.height))

        # CLock setup
        self.clock = pygame.time.Clock()

        # Tiles setup
        self.tile_width = 60
        self.tile_height = 60
        self.columns = self.width // self.tile_width
        self.rows = self.height // self.tile_height
        self.grid = []
        for j in range(self.rows):
            for i in range(self.columns):
                self.grid.append(Tile(i, j, self.tile_width, self.tile_height))
        self.grid[0].walls[0] = False
        self.grid[-1].walls[2] = False

        # Depth-first setup
        self.stack = []
        self.current = self.grid[0]

        # A* setup
        self.start = self.grid[0]
        self.finish = self.grid[-1]
        self.open_set = []
        self.closed_set = []
        self.path

        # States setup
        self.generated = False
        self.solved = False

    def run(self):
        """
        Program main loop
        """
        while True:
            self.draw(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if not self.generated:
                        if event.key == pygame.K_RETURN:
                            self.generate()
                            self.generated = True
                    else:
                        if event.key == 98:
                            pygame.image.save(self.win, 'maze.png')
                        elif event.key == 114:
                            self.__init__()
                        elif event.key == 115:
                            self.solve()

    def draw(self, highlight):
        """
        Draw every tile on the screen
        """
        # FIll the screen and show all tiles
        self.win.fill((141, 128, 173))
        for tile in self.grid:
            tile.show(self.win)

        if highlight and self.current:
            self.current.highlight(self.win, True)

        pygame.display.update()

    def generate(self):
        """
        Generate the maze based on the depth first search algorithm
        """
        while True:
            # Set clock and draw on the screen
            self.clock.tick(60)
            self.draw(True)

            # Check if window was closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Get neighbor cells list
            neighbors = self.current.check_neighbors(self.grid, self.columns, self.rows)
            neighbors = [neighbor for neighbor in neighbors if not neighbor.visited]

            # Choose random neighbor to go
            if len(neighbors) > 0:
                neighbor_index = randint(0, len(neighbors) - 1)
                next_visit = neighbors[neighbor_index]
            else:
                next_visit = False

            # Go to next visit or end algorithm running
            if next_visit:
                self.stack.append(self.current)
                self.current.remove_walls(next_visit)
                next_visit.visited = True
                self.current.highlight(self.win, False)
                self.current = next_visit
            elif len(self.stack) > 0:
                self.current = self.stack.pop()
            else:
                self.current.highlight(self.win, False)
                self.current = None
                return


if __name__ == '__main__':
    gen = Generator()
    gen.run()
