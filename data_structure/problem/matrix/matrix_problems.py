import itertools
import random


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


def create_snail_matrix2(size):
    matrix = [[0] * size for i in range(size)]
    x_directions = itertools.cycle([0, 1, 0, -1])
    y_directions = itertools.cycle([1, 0, -1, 0])
    x_increment, y_increment = next(x_directions), next(y_directions)
    x, y = 0, -1
    n = 0
    for corner in range(size, 0, -1):
        for line in range(2):
            for _ in range(corner - line):
                x += x_increment
                y += y_increment
                n += 1
                matrix[x][y] = n
            x_increment, y_increment = next(x_directions), next(y_directions)

    return matrix


def sort_snail_matrix(matrix):
    # sort the array (quick sort, why not?)
    quick_sort_array = []
    for item in itertools.chain(*matrix):
        array_len = len(quick_sort_array)
        if item >= array_len:
            quick_sort_array.extend(itertools.repeat(0, times=item - array_len + 1))
        quick_sort_array[item] += 1

    # fill the matrix
    x_directions = itertools.cycle([0, 1, 0, -1])
    y_directions = itertools.cycle([1, 0, -1, 0])
    x_increment, y_increment = next(x_directions), next(y_directions)
    x, y, i = 0, -1, 0
    for corner in range(len(matrix[0]), 0, -1):
        for line in range(2):
            for _ in range(corner - line):
                x, y = x + x_increment, y + y_increment
                while quick_sort_array[i] <= 0 and i + 1 < len(quick_sort_array):
                    i += 1
                matrix[x][y] = i
                quick_sort_array[i] -= 1
            x_increment, y_increment = next(x_directions), next(y_directions)