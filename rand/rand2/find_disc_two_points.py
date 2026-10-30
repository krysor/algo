from math import sqrt
from point import Point
from disc import Disc
from get_distance import get_distance

def find_disc_two_points(p1: Point, p2: Point) -> Disc:
    difference = p2 - p1
    center = p1 + 1/2 * difference
    radius = 1/2 * get_distance(p1, p2)
    return Disc(center, radius)

p1 = Point(0,0)
p2 = Point(1,0)
p3 = Point(0,1)
p4 = Point(1,1)

# Horizontal pairs
assert find_disc_two_points(p1, p2) == Disc(
    Point(0.5, 0),
    0.5
)

assert find_disc_two_points(p3, p4) == Disc(
    Point(0.5, 1),
    0.5
)

# Vertical pairs
assert find_disc_two_points(p1, p3) == Disc(
    Point(0, 0.5),
    0.5
)

assert find_disc_two_points(p2, p4) == Disc(
    Point(1, 0.5),
    0.5
)

# Diagonal pairs
assert find_disc_two_points(p1, p4) == Disc(
    Point(0.5, 0.5),
    sqrt(2) / 2
)

assert find_disc_two_points(p2, p3) == Disc(
    Point(0.5, 0.5),
    sqrt(2) / 2
)