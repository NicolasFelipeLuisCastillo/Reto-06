from Reto_05.rectangle import Rectangle
from Reto_05.point import Point

class Square(Rectangle):
    def __init__(self, method: int, *args):
        if method == 1:
            bottom_left, side = args
            super().__init__(1, bottom_left, side, side)
        elif method == 2:
            center, side = args
            super().__init__(2, center, side, side)
        elif method == 3:
            p1, p2 = args
            side = max(abs(p2._x - p1._x), abs(p2._y - p1._y))
            center = Point((p1._x + p2._x)/2, (p1._y + p2._y)/2)
            super().__init__(2, center, side, side)
        else:
            raise ValueError("Invalid method")
