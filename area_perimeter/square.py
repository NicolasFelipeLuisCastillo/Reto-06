from area_perimeter.rectangle import Rectangle
from area_perimeter.point import Point

class Square(Rectangle):
    def __init__(self, method: int, *args):
        # Exception: invalid method
        if method not in (1, 2, 3):
            raise ValueError(f"Invalid method '{method}'. Must be 1, 2, or 3.")

        # Exception: invalid number of arguments
        if (method in (1, 2) and len(args) != 2) or (method == 3 and len(args) != 2):
            raise TypeError(
                f"Invalid number of arguments for method {method}. Expected 2, got {len(args)}."
            )
        
        # Exception: first argument must be a Point
        if not isinstance(args[0], Point):
            raise TypeError("The first argument must be an instance of Point.")
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
