from math import sqrt
from point import Point
from disc import Disc

def find_smallest_disc(p1: Point, p2: Point) -> Disc:
    difference = p2 - p1
    center = p1 + 1/2 * difference
    radius = 1/2 * sqrt(difference.x * difference.x + difference.y * difference.y)
    return Disc(center, radius)

p1 = Point(0,0)
p2 = Point(1,0)
p3 = Point(0,1)
p4 = Point(1,1)
# disc = Disc()
assert(find_smallest_disc(p1,p2) == Disc(Point(0.5,0),0.5))