from .triangle import Triangle
from .line import Line
from .point import Point
import math

class IsoscelesTriangle(Triangle):
    def __init__(self, base_start: Point, base_end: Point, vertex: Point):
        super().__init__(base_start, base_end, vertex)
        self.is_regular = False

    def compute_area(self):
        base_length = self.edges[0].compute_length()
        side_length = self.edges[1].compute_length()
        h = (side_length ** 2 - (base_length ** 2) / 4) ** 0.5
        return (base_length * h) / 2
