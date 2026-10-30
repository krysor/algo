from math import isclose

class Disc:
    def __init__(self, center: float, radius: float):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        if not isinstance(other, Disc):
            return NotImplemented

        return (
            self.center == other.center
            and isclose(self.radius, other.radius)
        )

    def __repr__(self):
        return f"Point({self.x}, {self.y})"