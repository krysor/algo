from math import sqrt
from point import Point

def get_distance(p1: Point, p2: Point) -> float:
    difference = p2 - p1

    return sqrt(
        difference.x ** 2
        + difference.y ** 2
    )