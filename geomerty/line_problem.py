# the function moves vector `v` to the point (0, 0)
def move_to_00(v):
    return (0, 0), \
           (v[1][0] - v[0][0], v[1][1] - v[0][1])


# the function calculates cross product (or vector product) of `v1` and `v2` vectors
def cross_product(v1, v2):
    a = move_to_00(v1)
    b = move_to_00(v2)

    # [a, b] = x1y2 — x2y1
    return a[1][0] * b[1][1] - b[1][0] * a[1][1]


# the function calculate position of point with respect to a vector
# return <0 if point on the left side
# return  0 if point on the line
# return >0 if point on the right side
def get_side(point, vector):
    return cross_product(((vector[0][0], vector[0][1]), point), vector)


if __name__ == "__main__":
    # test move_to_00
    assert ((0, 0), (1, 1)) == move_to_00(((0, 0), (1, 1)))
    assert ((0, 0), (0, 0)) == move_to_00(((1, 1), (1, 1)))
    assert ((0, 0), (2, 3)) == move_to_00(((1, 1), (3, 4)))

    # test cross_product
    assert 0 == cross_product(v1=((0, 0), (0, 0)), v2=((0, 0), (0, 0)))
    assert 0 == cross_product(v1=((0, 0), (0, 0)), v2=((0, 0), (1, 1)))
    assert 0 == cross_product(v1=((0, 0), (1, 1)), v2=((0, 0), (1, 1)))
    assert 0 == cross_product(v1=((0, 0), (1, 1)), v2=((2, 2), (1, 1)))
    assert 0 == cross_product(v2=((0, 0), (1, 1)), v1=((0, 1), (1, 2)))

    assert 0 > cross_product(v1=((0, 0), (1, 1)), v2=((0, 2), (1, 1)))
    assert 0 < cross_product(v1=((0, 0), (1, 1)), v2=((0, 0), (1, 3)))
    assert 0 > cross_product(v2=((0, 0), (1, 1)), v1=((0, 0), (1, 3)))

    assert 0 == get_side(point=(1, 1), vector=((1, 1), (2, 2)))
    assert 0 == get_side(point=(1, 1), vector=((1, 1), (2, 2)))
    assert 0 == get_side(point=(0, 0), vector=((1, 1), (2, 2)))
    assert 0 > get_side(point=(2, 3), vector=((1, 1), (2, 2)))
    assert 0 > get_side(point=(0, 1), vector=((1, 1), (2, 2)))
    assert 0 < get_side(point=(1, 0), vector=((1, 1), (2, 2)))
    assert 0 < get_side(point=(3, 2), vector=((1, 1), (2, 2)))
    print("Everything passed")
