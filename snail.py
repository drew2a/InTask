import itertools


def print_matrix(matrix):
    for row in range(len(matrix)):
        print(" ".join('{:^5}'.format(i) for i in matrix[row]))


def create_snail_matrix(size):
    matrix = [[0] * size for i in range(size)]
    ix, iy = size - 1, 0
    n = size * size
    directions = itertools.cycle([
        (0, 1),  # down
        (-1, 0),  # left
        (0, -1),  # up
        (1, 0)])  # right

    for i in range(size):
        matrix[0][i] = n - i

    n -= ix
    for step in range(size - 1, 0, -1):
        for direction_change in range(2):
            direction = next(directions)
            for index in range(step):
                ix, iy = ix + direction[0], iy + direction[1]
                n -= 1
                matrix[iy][ix] = n

    return matrix
