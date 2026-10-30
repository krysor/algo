from point import Point
from disc import Disc
from find_smallest_disc import find_smallest_disc
from get_distance import get_distance

points: list[tuple[int, int]] = [
    (1, 2),
    (4, 5),
    (7, 3)
]

def MiniDiscWith2Points(points: list[Point], q1: Point, q2: Point):    
    disc = find_smallest_disc(q1, q2)
    
    for point in points:
        if (get_distance(disc.center, point) <= disc.radius):
            continue
        