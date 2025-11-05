from .triangle import Triangle
from .point import Point
import math

class Equilateral(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.is_regular = True

    def compute_area(self):
        side = self.edges[0].compute_length()
        return (math.sqrt(3) / 4) * (side ** 2)

    def compute_perimeter(self):
        side = self.edges[0].compute_length()
        return 3 * side

    def compute_inner_angles(self):
        return (60.0, 60.0, 60.0)
