from dataclasses import dataclass

from figure_lib.lib import Figure


def test_subclass():
    @dataclass(slots=True, eq=True, frozen=True)
    class Line(Figure):
        length: float

        def get_area(self) -> float:
            return 0.0

    line = Line(2)
    assert line.get_area() == 0
