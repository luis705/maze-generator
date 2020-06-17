from constants import *

def get_index(i, j):
    if i < 0 or j < 0 or i > COLUMNS - 1 or j > ROWS - 1:
        return None
    return i + j * COLUMNS
