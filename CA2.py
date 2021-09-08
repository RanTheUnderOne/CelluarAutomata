import gc
import profile

import numpy as np
import pygame
from MNCellularAutomata import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

matrixA = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])

matrixB = np.array([[0, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0]])

class Board:

    def __init__(self, initial_values, window_width, window_height, blocksize, screen, ):
        # Define the x,y grid
        self.x_cord = np.linspace(0, window_width, int(window_width / blocksize))
        self.y_cord = np.linspace(0, window_height, int(window_height / blocksize))

        self.current_state = initial_values
        self.window_width = window_width
        self.window_height = window_height
        self.blocksize = blocksize
        self.screen = screen

        self.relative_position = relative_position_generator(matrixA)

    # Draws all the pixels.
    def drawGrid(self):
        for xindex, x in enumerate(self.x_cord):
            for yindex, y in enumerate(self.y_cord):
                rect = pygame.Rect(x, y, self.blocksize - 1, self.blocksize - 1)
                if self.current_state[xindex][yindex] == 0:
                    pygame.draw.rect(self.screen, BLACK, rect)
                if self.current_state[xindex][yindex] == 1:
                    pygame.draw.rect(self.screen, WHITE, rect)

    # sum all the values of the neighbor cells.
    def multi_neighborhood_sum(self, idx, idy):
        sum = 0

        for position in self.relative_position:
            rel_x, rel_y = position[0], position[1]

            # reaches the point from the relative position set.
            x, y = idx + rel_x, idy + rel_y
            if 0 <= x < self.window_width / self.blocksize and 0 <= y < self.window_height / self.blocksize:
                sum += self.current_state[x][y]
        return sum

    # updates the grid according to the game's rules.
    def update_grid(self):

        next_matrix = np.zeros_like(self.current_state)
        for xindex in range(len(self.x_cord)):
            for yindex in range(len(self.y_cord)):
                sum = self.multi_neighborhood_sum(xindex, yindex)
                # calculating what is the next value for this current pace in matrix.
                next_matrix[xindex][yindex] = self.game_rules(sum, self.current_state[xindex][yindex])
        self.current_state = next_matrix


    def game_rules(self, neighbors_sum, state):
        if state == 1:
            if 0 <= neighbors_sum < 2 or 3 < neighbors_sum <= 8:
                return 0
            else:
                return 1
        if state == 0:
            if 3 <= neighbors_sum <= 3:
                return 1
            else:
                return 0
