import fractions

def reduce_frac(frac):
    div = fractions.gcd(frac[0], frac[1])
    frac[0] /= div
    frac[1] /= div
    return frac

def add_frac(frac1, frac2):
    numerator = frac1[0]*frac2[1] + frac2[0]*frac1[1]
    denominator = frac1[1]*frac2[1]
    return reduce_frac([numerator,denominator])

def sub_frac(frac1, frac2):
    numerator = frac1[0]*frac2[1]-frac2[0]*frac1[1]
    denominator = frac1[1]*frac2[1]
    return reduce_frac([numerator,denominator])


def mul_frac(frac1, frac2):
    numerator = frac1[0]*frac2[0]
    denominator = frac1[1]*frac2[1]
    return reduce_frac([numerator,denominator])

def div_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1]
    denominator = frac1[1] * frac2[0]
    return reduce_frac([numerator, denominator])

def is_positive(frac):
    return frac[0]/float(frac[1])>0

def is_zero(frac):
    return frac[0]==0 and frac[1]!=0

def cmp_frac(frac1, frac2):
    if frac1[0]/float(frac1[1])>frac2[0]/float(frac2[1]):
        return 1
    elif frac1[0]/float(frac1[1])<frac2[0]/float(frac2[1]):
        return -1
    else:
        return 0

def frac2float(frac):
    return frac[0]/float(frac[1])

#---------TEST-------------

import unittest
import fracs
class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([74, 14], [18, 7]), [19, 7])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([5,10],[1,3]),[1,6])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([5, 10], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([5,10]),True)
        self.assertEqual(fracs.is_positive([-5,10]),False)
        self.assertEqual(fracs.is_positive([-5,-10]),True)
        self.assertEqual(fracs.is_positive([5,-10]),False)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero([0, 1]),True)
        self.assertEqual(fracs.is_zero([3, 2]),False)

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1,2],[2,3]),-1)
        self.assertEqual(fracs.cmp_frac([2,3],[1,2]),1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1,2]),0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
