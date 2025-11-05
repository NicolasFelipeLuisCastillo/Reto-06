from math import sqrt
from area_perimeter.point import Point

class Line(Point):
    def __init__(self, start: Point, end: Point) -> None:
        super().__init__(start._x, start._y)
        self._start = start
        self._end = end

    def compute_length(self) -> float:
        return sqrt((self._end._x - self._start._x) ** 2 + (self._end._y - self._start._y) ** 2)
    
    def compute_slope(self):
        if (self._end._x - self._start._x) == 0:
            return None
        return (self._end._y - self._start._y) / (self._end._x - self._start._x)
    
    def compute_vertical_crossing(self):
        slope = self.compute_slope()
        if slope is None:
            return None
        return self._start._y - (slope * self._start._x)

    def compute_horizontal_crossing(self):
        slope = self.compute_slope()
        if slope == 0 or slope is None:
            return None
        return -(self._start._y - (slope * self._start._x)) / slope
    
    def __str__(self) -> str:
        slope = self.compute_slope()
        slope_str = f"{slope:.2f}" if slope is not None else "∞"
        v_cross = self.compute_vertical_crossing()
        h_cross = self.compute_horizontal_crossing()
        return (
            f"Length: {self.compute_length():.2f}, "
            f"Slope: {slope_str}, "
            f"Vertical crossing: {v_cross}, "
            f"Horizontal crossing: {h_cross}"
        )
