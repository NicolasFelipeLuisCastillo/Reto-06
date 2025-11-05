# Reto-06

This repository contains documented and explained practical exercises in OOP in Python.

---

In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

### `main.py`
```python
from Reto_05.point import Point
from Reto_05.line import Line
from Reto_05.rectangle import Rectangle
from Reto_05.square import Square
from Reto_05.triangle import Triangle
from Reto_05.isosceles import IsoscelesTriangle
from Reto_05.equilateral import Equilateral
from Reto_05.scalene import Scalene

def main():
    # Puntos base
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    # --- RECTÁNGULO ---
    rect = Rectangle(1, p1, 10, 5)
    print(f"Rectángulo: área = {rect.compute_area()}, perímetro = {rect.compute_perimeter()}")

    # --- CUADRADO ---
    sq = Square(1, p1, 5)
    print(f"Cuadrado: área = {sq.compute_area()}, perímetro = {sq.compute_perimeter()}")

    # --- TRIÁNGULOS ---
    t = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
    print(f"Triángulo: área = {t.compute_area()}, perímetro = {t.compute_perimeter()}")

    iso = IsoscelesTriangle(Point(0, 0), Point(4, 0), Point(2, 3))
    print(f"Triángulo isósceles: área = {iso.compute_area()}, perímetro = {iso.compute_perimeter()}")

    scal = Scalene(Point(0, 0), Point(4, 0), Point(3, 2))
    print(f"Triángulo escaleno: área = {scal.compute_area()}, perímetro = {scal.compute_perimeter()}")

    equi = Equilateral(Point(0, 0), Point(4, 0), Point(2, 3.46))
    print(f"Triángulo equilátero: área = {equi.compute_area()}, perímetro = {equi.compute_perimeter()}")

if __name__ == "__main__":
    main()

```
### `__init__.py`
```python
from .point import Point
from .line import Line
from .shape import Shape
from .rectangle import Rectangle
from .square import Square
from .triangle import Triangle
from .isosceles import IsoscelesTriangle
from .equilateral import Equilateral
from .scalene import Scalene

```
### `shape.py`
```python
class Shape:
    def __init__(self, is_regular: bool):
        self.is_regular = is_regular
        self.vertices: list = []
        self.edges: list = []

    def compute_area(self):
        return 0
    
    def compute_perimeter(self):
        if not self.edges:
            return 0
        return sum(edge.compute_length() for edge in self.edges)
    
    def inner_angle(self, sides: int) -> float:
        if sides < 3:
            return 0
        return (sides - 2) * 180 / sides
    
    def compute_inner_angles(self):
        sides = len(self.vertices)
        if sides < 3:
            return 0
        return (sides - 2) * 180

```

### `point.py`
```python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

```
### `line.py`
```python
from math import sqrt
from Reto_05.point import Point

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

```
### `rectangle.py`
```python
from Reto_05.shape import Shape
from Reto_05.point import Point

class Rectangle(Shape):
    def __init__(self, method: int, *args):
        super().__init__(is_regular=False)

        if method == 1:
            bottom_left, width, height = args
            self.width = width
            self.height = height
            self.center = Point(bottom_left._x + width/2, bottom_left._y + height/2)

        elif method == 2:
            center, width, height = args
            self.width = width
            self.height = height
            self.center = center

        elif method == 3:
            p1, p2 = args
            self.width = abs(p2._x - p1._x)
            self.height = abs(p2._y - p1._y)
            self.center = Point((p1._x + p2._x)/2, (p1._y + p2._y)/2)

        elif method == 4:
            lines = args
            points = [p for line in lines for p in (line._start, line._end)]
            xs, ys = [p._x for p in points], [p._y for p in points]
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)
            self.width = max_x - min_x
            self.height = max_y - min_y
            self.center = Point((min_x + max_x)/2, (min_y + max_y)/2)
        else:
            raise ValueError("Invalid method")

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_interference_point(self, point: Point) -> bool:
        x_min = self.center._x - self.width/2
        x_max = self.center._x + self.width/2
        y_min = self.center._y - self.height/2
        y_max = self.center._y + self.height/2
        return x_min <= point._x <= x_max and y_min <= point._y <= y_max

```
### `square.py`
```python
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

```
### `triangle.py`
```python
from .shape import Shape
from .line import Line
from .point import Point
import math

class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(is_regular=False)
        self.vertices = [p1, p2, p3]
        self.edges = [
            Line(p1, p2),
            Line(p2, p3),
            Line(p3, p1)
        ]

    def compute_perimeter(self):
        return sum(edge.compute_length() for edge in self.edges)

    def compute_area(self):
        a, b, c = [edge.compute_length() for edge in self.edges]
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Fórmula de Herón

    def compute_inner_angles(self):
        a, b, c = [edge.compute_length() for edge in self.edges]
        A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
        C = 180 - A - B
        return A, B, C

```
### `isosceles.py`
```python
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

```
### `scalene.py`
```python
from .triangle import Triangle

class Scalene(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.is_regular = False

```
### `equilateral.py`
```python
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

```

