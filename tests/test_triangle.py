from figure_lib.lib import Triangle


def test_triangle():
    triangle = Triangle((1, 1, 1))
    assert triangle.sides == (1, 1, 1)
    assert triangle == Triangle([1, 1, 1])
    assert round(triangle.get_area(), 3) == 0.433
    assert triangle.is_right is not None


def test_invalid():
    triangle = Triangle((0, 0, 0))
    assert triangle.get_area() == 0
    assert Triangle((1, 0, 0)).get_area() == 0
    assert Triangle((-1, 0, -1)).get_area() == 0


def test_right_triangle():
    right = Triangle((3, 4, 5))
    assert right.get_area() == 6
    assert right.is_right
