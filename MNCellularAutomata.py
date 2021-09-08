import numpy as np

matrixA = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])


def relative_position_generator(matrix):
    relative_position = []
    middle = np.array([int(len(matrix) / 2), int(len(matrix) / 2)])

    for i in range(len(matrix[0])):
        for j in range(len(matrix[1])):
            if matrix[i][j] == 1:
                relative_position.append(np.array([i, j]) - middle)

    return relative_position


def multi_neighborhood_sum(pattern_matrix, idx, idy):
    sum = 0

    relative_position = relative_position_generator(pattern_matrix)
    for position in relative_position:
        rel_x, rel_y = position[0], position[1]

        # reaches the point from the relative position set.
        x, y = idx + rel_x, idy + rel_y
        if 0 <= x < self.window_width / self.blocksize and 0 <= y < self.window_height / self.blocksize:
            sum += self.current_state[x][y]
    return sum