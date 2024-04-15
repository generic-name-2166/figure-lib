import math

from figure_lib.lib import Circle


def test_circle():
    circle = Circle(1)
    assert circle == Circle(1)
    assert circle.get_area() == math.pi
    circle_2 = Circle(2)
    assert circle_2.get_area() == math.pi * 4
