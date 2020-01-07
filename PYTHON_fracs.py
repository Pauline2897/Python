from math import gcd

class Frac:
    def __init__(self, numerator, *denominator):
        try:
            assert denominator[0] != 0
            self.numerator = int(numerator)
            self.denominator = int(denominator[0])
            g = gcd(self.denominator, self.numerator)
            if g > 1:
                self.denominator /= g
                self.numerator /= g
        except AssertionError:
            raise ValueError
        except IndexError:
            self.numerator = int(numerator)
            self.denominator = 1

    def __add__(self, other):
        return Frac(self.numerator * other.denominator + self.denominator * other.numerator,
                    self.denominator * other.denominator)

    def __sub__(self, other):
        return Frac(self.numerator * other.denominator - self.denominator * other.numerator,
                    self.denominator * other.denominator)

    def __mul__(self, other):
        return Frac(self.numerator * other.numerator,
                    self.denominator * other.denominator)

    def __truediv__(self, other):
        return Frac(self.numerator * other.denominator,
                    self.denominator * other.numerator)

    def __lt__(self, other):
        first = self.numerator * other.denominator
        second = self.denominator * other.numerator
        return first < second

    def is_positive(self):
        return False if self.numerator * self.denominator < 0 else True

    def is_zero(self):
        return False if self.numerator else True

    def __float__(self):
        return self.numerator / self.denominator

    def __repr__(self):
        return "{0} / {1}".format(self.numerator, self.denominator)

    def __eq__(self, other):
        if self.denominator == other.denominator and self.numerator == other.numerator:
            return True
        elif self.numerator == self.denominator and other.numerator == other.denominator:
            return True
        else:
            return False





import unittest

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.f1 = Frac(1, 3)
        self.f2 = Frac(2, 6)
        self.f3 = Frac(3, 10)
        self.f0 = Frac(0, 1)

    def test_add_frac(self):
        self.assertEqual(self.f1 + self.f2 + self.f2, Frac(1))

    def test_sub_frac(self):
        self.assertEqual(self.f2 - self.f3, Frac(1, 30))

    def test_mul_frac(self):
        self.assertEqual(self.f1 * self.f3, Frac(1, 10))

    def test_div_frac(self):
        self.assertEqual(self.f1 / self.f3, Frac(20, 18))
        self.assertEqual(self.f1 / self.f3, Frac(10, 9))
        with self.assertRaises(ValueError):
            self.f1 / 0

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

if __name__ == '__main__':
    unittest.main()
