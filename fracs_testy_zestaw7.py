import unittest

from circle import *
from fracs import Frac
import math

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1, 3)
        self.f2 = Frac(2, 6)
        self.f3 = Frac(3, 10)
        self.f0 = Frac(0, 1)

    def test_add_frac(self):
        self.assertEqual(self.f1 + self.f2 + self.f2, 1)
        self.assertEqual(self.f3 + 10, Frac(103, 10))
        self.assertEqual(10 + self.f3, Frac(103, 10))
        self.assertAlmostEqual(float(10.4 + self.f3), 10.7, places=3, msg=None)
        self.assertAlmostEqual(float(0.66666 + Frac(1,3)), 1, places=3, msg=None)

    def test_sub_frac(self):
        self.assertEqual(self.f2 - self.f3, Frac(1, 30))
        self.assertEqual(10 - self.f3, Frac(97, 10))
        self.assertEqual(self.f3 - 10, Frac(-97, 10))
        self.assertAlmostEqual(float(0.66666 - Frac(1, 3)), 0.3333, places=3, msg=None)

    def test_mul_frac(self):
        self.assertEqual(self.f1 * self.f3, Frac(1, 10))
        self.assertEqual(10 * self.f3, Frac(3, 1))
        self.assertEqual(10.2 * self.f3, Frac(31, 10))

    def test_div_frac(self):
        self.assertEqual(self.f1 / self.f3, Frac(20, 18))
        self.assertEqual(self.f1 / self.f3, Frac(10, 9))
        self.assertEqual(10 / self.f3, Frac(100, 3))
        self.assertEqual(10.5 / self.f3, Frac(35, 1))
        with self.assertRaises(ValueError):
            self.f1 / 0
        with self.assertRaises(ValueError):
            "abc" / self.f3

    def test_is_positive(self):
        f1 = Frac(-1, -5)
        f2 = Frac(1, -5)
        self.assertTrue(f1.is_positive())
        self.assertFalse(f2.is_positive())

    def test_is_zero(self):
        self.assertTrue(self.f0.is_zero())
        self.assertFalse(self.f1.is_zero())

    def test_cmp_frac(self):
        self.assertTrue(self.f2 > self.f3)
        self.assertFalse(Frac(20, 18) < Frac(10, 18))

    def test_frac2float(self):
        self.assertAlmostEqual(float(self.f1), 0.333, places=3, msg=None)

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