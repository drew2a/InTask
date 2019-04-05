from geomerty import line_problem


def remove_repeats(polygon):
    if len(polygon) <= 1:
        return polygon

    previous_point = polygon[-1]
    new_polygon = []
    for point in polygon:
        if point is not previous_point:
            new_polygon.append(point)
        previous_point = point

    return new_polygon


def is_convex_polygon_contains_point(polygon, point):
    polygon = remove_repeats(polygon)

    size = len(polygon)

    if size < 3:
        return False

    current_side = line_problem.get_side(point, (polygon[0], polygon[1]))

    for i in range(1, size - 1):
        next_side = line_problem.get_side(point, (polygon[i], polygon[i + 1]))
        if current_side * next_side < 0:
            return False
        current_side = next_side

    return current_side * line_problem.get_side(point, (polygon[size - 1], polygon[0])) >= 0


if __name__ == "__main__":
    # test move_to_00
    assert 0 == len(remove_repeats([]))
    assert 1 == len(remove_repeats([(1, 1)]))
    assert 2 == len(remove_repeats([(1, 1), (2, 2), (1, 1)]))
    assert 2 == len(remove_repeats([(1, 1), (1, 1), (2, 2), (1, 1), (1, 1)]))
    # print(remove_repeats([(1, 1), (1, 1), (2, 2), (1, 1), (1, 1)]))
    assert not is_convex_polygon_contains_point([(0, 0)], (0, 0))
    assert not is_convex_polygon_contains_point([(0, 0), (0, 0)], (0, 0))
    assert not is_convex_polygon_contains_point([(0, 0), (0, 0), (0, 0)], (1, 1))
    assert not is_convex_polygon_contains_point([(0, 0), (0, 0), (0, 0)], (0, 0))
    assert not is_convex_polygon_contains_point([(0, 0), (1, 1), (0, 0)], (0, 0))

    assert is_convex_polygon_contains_point([(0, 0), (5, 5), (10, 0), (5, -5)], (0, 0))
    assert is_convex_polygon_contains_point([(0, 0), (5, 5), (10, 0), (5, -5)], (1, 0))

    assert not is_convex_polygon_contains_point([(0, 0), (5, 5), (10, 0), (5, -5)], (0, 1))
    assert not is_convex_polygon_contains_point([(0, 0), (5, 5), (10, 0), (5, -5)], (11, 0))

    print("Everything passed")
