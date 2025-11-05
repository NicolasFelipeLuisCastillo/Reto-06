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
