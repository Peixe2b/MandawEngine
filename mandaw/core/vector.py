from math import sqrt
from typing import Union
from dataclasses import dataclass


@dataclass
class Vector2:
    x: int
    y: int

@dataclass
class NamedVector2:
    x: int
    y: int
    name: str


def vector_distance(vector1: Vector2, vector2: Vector2) -> float:
    dx = (vector1.x - vector2.x)**2
    dy = (vector1.y - vector2.y)**2
    return sqrt(dx + dy)


def make_vector(x: int, y: int, name: Union[None, str]="") -> Union[Vector2, NamedVector2]:
    if name == "" or name is None:
        return Vector2(x, y)
    return NamedVector2(x, y, name)


def make_vector_zero() -> Vector2:
    return Vector2(0, 0)


def vector_sum(vector1: Union[Vector2, NamedVector2],
               vector2: Union[Vector2, NamedVector2]):
    return Vector2(
        vector1.x + vector2.x,
        vector1.y + vector2.y
    )
