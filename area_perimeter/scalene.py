from .triangle import Triangle

class Scalene(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.is_regular = False
