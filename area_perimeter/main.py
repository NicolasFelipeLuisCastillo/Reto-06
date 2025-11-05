from area_perimeter.point import Point
from area_perimeter.line import Line
from area_perimeter.rectangle import Rectangle
from area_perimeter.square import Square
from area_perimeter.triangle import Triangle
from area_perimeter.isosceles import IsoscelesTriangle
from area_perimeter.equilateral import Equilateral
from area_perimeter.scalene import Scalene

def main():
    # Points
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    # Rectangles
    rect = Rectangle(1, p1, 10, 5)
    print(f"Rectángulo: área = {rect.compute_area()}, perímetro = {rect.compute_perimeter()}")

    # Squares
    sq = Square(1, p1, 5)
    print(f"Cuadrado: área = {sq.compute_area()}, perímetro = {sq.compute_perimeter()}")

    # Traingles
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
