import math

from data_structure.problem.matrix.matrix_problems import print_matrix


def get_angle(v1, v2):
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    det = v1[0] * v2[1] - v1[1] * v2[0]

    return math.atan2(det, dot)


def get_outside_sheep(point, sheeps):
    max = (-2 * math.pi, point)
    for sheep in sheeps:
        value = get_angle(point, sheep)
        if value != 0 and value > max[0]:
            max = (value, sheep)

    return max[1]


def get_sheepfold(sheeps):
    uniq_sheeps = set(sheeps)
    sheepfold = []

    size = len(uniq_sheeps)
    if size < 3:
        return []

    sheeps = list(uniq_sheeps)

    first_outsider = get_outside_sheep(sheeps[0], sheeps)
    last_outsider = first_outsider

    sheepfold.append(first_outsider)

    for i in range(size - 1):
        last_outsider = get_outside_sheep(last_outsider, sheeps)
        if last_outsider == first_outsider:
            return sheepfold

        sheepfold.append(last_outsider)

    return sheepfold


if __name__ == "__main__":
    assert 0 > get_angle((0, 1), (1, 0))
    assert 0 == get_angle((0, 1), (0, 1))
    assert 0 < get_angle((0, 1), (0, -1))

    sheeps = [(6, 4), (6, 4), (6, 4), (0, 1), (2, 2), (4, 0), (3, 3), (7, 1), (4, 6), (7, 5)]
    sheepfold = get_sheepfold(sheeps)

    output = [['`'] * 10 for i in range(10)]
    for sheep in sheeps:
        output[sheep[0]][sheep[1]] = '˘ꈊ˘'

    for fold in sheepfold:
        output[fold[0]][fold[1]] = '⚐'

    print_matrix(output)
    print(sheeps)
