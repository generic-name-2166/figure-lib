from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import math
from collections.abc import Sequence
from typing import Optional


class Figure(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_area(self):
        pass


@dataclass(slots=True)
class Circle(Figure):
    radius: float

    def get_area(self) -> float:
        return (self.radius**2) * math.pi


@dataclass(slots=True)
class Triangle(Figure):
    sides: Sequence[float, float, float]
    is_right: bool = field(default=False, init=False)

    def __post_init__(self):
        self.sides = tuple(self.sides)
        self.is_right = (
            sum(side**2 for side in self.sides) == (max(self.sides) ** 2) * 2
        )

    def get_area(self) -> Optional[float]:
        if (
            self.sides[0] + self.sides[1] <= self.sides[2]
            or self.sides[0] + self.sides[2] <= self.sides[1]
            or self.sides[1] + self.sides[2] <= self.sides[0]
        ):
            print("Invalid triangle")
            return 0.0

        sp = sum(self.sides) / 2.0
        a = sp - self.sides[0]
        b = sp - self.sides[1]
        c = sp - self.sides[2]
        return math.sqrt(sp * a * b * c)
