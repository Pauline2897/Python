#Zad 6.1
class Time:

    def __init__(self, s=0):
        #Zwraca instancję klasy Time.
        self.s = int(s)

    def __str__(self):
        #Zwraca string w postaci'hh:mm:ss'.
        h = int(self.s / 3600)
        sec = int(self.s - h * 3600)
        m = int(sec / 60)
        sec = int(sec - m * 60)
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        #Zwraca string 'Time(s)'.
        return "Time({0})".format(self.s)

    def __add__(self, other):
        #Dodawanie odcinków czasu.
        return Time(self.s + other.s)

    def __int__(self):                  # int(time1)
        #Konwersja odcinka czasu do int.
        return self.s

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return not(self == other)

    def __lt__(self, other):
        return self.s < other.s

# Kod testujący moduł.

import unittest

class TestTime(unittest.TestCase):

    def test_print(self):
        self.assertEqual(str(Time(1)), '00:00:01')
        self.assertEqual(str(Time(60)), '00:01:00')
        self.assertEqual(str(Time(3661)), '01:01:01')

    def test_add(self):
        self.assertEqual(int(Time(1) + Time(2)), int(Time(3)))

    def test_cmp(self):
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3600) > Time(60))
        self.assertFalse(Time(54) < Time(32))

    def test_int(self):
        self.assertEqual(int(Time(3600)), 3600)
        self.assertEqual(int(Time(100)), 100)


#Zad 6.5 zrobiłam w piątym zestawie:

from fracs import Frac

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
