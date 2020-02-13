
#ZADANIE 7.5 KLASA CIRCLE

from points import Point
from math import PI


class Circle:
    def __init__(self, x=0, y=0, radius=1):
        try:
            assert radius > 0
        except AssertionError:
            raise ValueError("promień ujemny")
        self.pt = Point(int(x), int(y))
        self.radius = radius

    def __str__(self):
        return "Circle with radius of {:.2f}".format(self.radius)

    def __repr__(self):
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return PI*self.radius**2

    def move(self, x, y):
        return self.pt + Point(x,y)
"""
do funkcji cover:
obliczam nowy srodek okregu
sprawdzam, ktory z promieni jest wiekszy, self.radius, czy other.radius
biore pod uwage okrag o wiekszym promieniu
obliczam odleglosc miedzy nowym srodkiem a srodkiem wiekszego okregu
do tej odleglosci dodaje dluzszy promien
"""
    def cover(self, other):
        new_x = abs(self.pt.x - other.pt.x)/2
        new_y = abs(self.pt.y - other.pt.y)/2
        
        if self.radius >= other.radius:
            new_radius = (math.sqrt((new_x - self.pt.x)**2 + (new_y - self.pt.y)**2)) + self.radius
        else:
            new_radius = (math.sqrt((new_x - other.pt.x)**2 + (new_y - other.pt.y)**2)) + other.radius
        return Circle(new_x, new_y, new_radius)

# ---------- TEST -----------------
import unittest
import math

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(1, 3, 5)
        self.c2 = Circle(0, 0, 10)
        self.c3 = Circle(4, 3, 2)

    def test_equal(self):
        self.assertFalse(self.c1 == self.c2)
        self.assertTrue(self.c1 == Circle(1, 3, 5))

    def test_move(self):
        self.assertEqual(self.c1.move(2, 3), Circle(3, 6, 5))
        self.assertEqual(self.c3.move(-2, -3), Circle(2, 0, 2))

    def test_area(self):
        self.assertEqual(self.c1.area(), 78.5)

    def test_cover(self):
        self.assertEqual(self.c2.cover(self.c3), Circle(2, 1.5, 8.5))

if __name__ == '__main__':
    unittest.main()
