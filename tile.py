import pygame


class Tile:
    def __init__(self, i, j, width, height):
        # Basic setup
        self.i = i
        self.j = j
        self.width = width
        self.height = height
        self.x = self.i * self.width
        self.y = self.j * self.height

        #  Depth-first setup
        self.walls = [True, True, True, True]
        self.visited = False
        self.previous = None

        # Color setup
        self.line_color = (0, 0, 0)
        self.highlight_color = (206, 233, 217)
        self.visited_color = (141, 128, 173)

    def show(self, win):
        """
        Show tile on the screen
        """
        # Set Color
        if self.visited:
            pygame.draw.rect(win, self.visited_color, (self.x + 2,
                                                       self.x + 2, self.width - 2, self.height - 2))

        # Draw walls
        if self.walls[0]:
            pygame.draw.line(win, self.line_color, (self.x, self.y), (self.x + self.width, self.y), 2)
        if self.walls[1]:
            pygame.draw.line(win, self.line_color, (self.x, self.y), (self.x, self.y + self.height), 2)
        if self.walls[2]:
            pygame.draw.line(win, self.line_color, (self.x, self.y + self.height),
                             (self.x + self.width, self.y + self.height), 2)
        if self.walls[3]:
            pygame.draw.line(win, self.line_color, (self.x + self.width, self.y),
                             (self.x + self.width, self.y + self.height), 2)

    def highlight(self, win, bool):
        """
        Change color of tile to highlight it or not
        """
        if bool:
            pygame.draw.rect(win, self.highlight_color, pygame.Rect(self.i * self.width + 2,
                                                                    self.j * self.height + 2, self.width - 2, self.height - 2))

        else:
            pygame.draw.rect(win, self.visited_color, pygame.Rect(self.i * self.width + 2,
                                                                  self.j * self.height + 2, self.width - 2, self.height - 2))

    @staticmethod
    def get_index(i, j, columns, rows):
        """
        Get the index of a tile on the 1 dimension list
        Parameters:
            i: integer -> tile column
            j: integer -> tile row
            columns: integer -> number of column
            rows: integer -> number of rows
        """
        if i < 0 or j < 0 or i > columns - 1 or j > rows - 1:
            return None
        return i + j * columns

    def check_neighbors(self, grid, columns, rows):
        """
        Get the tile neighbors
        Parameters:
            grid: list -> list with every tile
            columns: integer -> number of columns on grid
            rows: integer -> number of rows on grid
        Return:
            neighbors: list -> collection of at most 4 Tile objects
        """
        neighbors = []

        top_index = Tile.get_index(self.i, self.j - 1, columns, rows)
        right_index = Tile.get_index(self.i - 1, self.j, columns, rows)
        bottom_index = Tile.get_index(self.i, self.j + 1, columns, rows)
        left_index = Tile.get_index(self.i + 1, self.j, columns, rows)

        if top_index:
            top = grid[top_index]
            neighbors.append(top)

        if left_index:
            left = grid[left_index]
            neighbors.append(left)

        if right_index:
            right = grid[right_index]
            neighbors.append(right)

        if bottom_index:
            bottom = grid[bottom_index]
            neighbors.append(bottom)

        return neighbors

    def remove_walls(self, neighbor):
        """
        Remove the walls between to tiles
        Parameters:
            neighbor: Tile
        """
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
