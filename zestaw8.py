import unittest

#8.1 a x + b y + c = 0

class RownanieSprzeczne(Exception): pass
class RownanieNieokreslone(Exception): pass

def solve1(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            raise RownanieNieokreslone
        else:
            raise RownanieSprzeczne
    if a == 0:
        return "y = " + str(-c/b)
    elif b == 0:
        return "x = " + str(-c/a)
    else:
        return "-({0} * x + {1})/{2}".format(a,c,b)

#zad 8.3

import random
def count_pi(shoots_num):
    aim_ok = 0
    for i in range(shoots_num):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x * x + y * y <= 1:
            aim_ok += 1
    return 4 * aim_ok / shoots_num

#zad 8.4


def heron(a, b, c):
    result = (((a + b + c) * (a + b - c) * (a - b + c) * (b + c - a)) ** 0.5) / 4
    if isinstance(result, complex):
        raise ValueError
    else:
        return result


#zad 8.6


def rekP(i, j):
    if i == 0 and j == 0: 
        return 0.5
    if i == 0 and j > 0: 
        return 1
    if j == 0 and i > 0: 
        return 0
    if j > 0 and i > 0: 
        return 0.5 * (rekP(i - 1, j) + rekP(i, j - 1))


def dynP(k, l):
    p = {}
    p[(0, 0)] = 0.5
    n = max(k, l)
    for i in range(n + 1):
        p[(i, 0)] = 0
        p[(0, i)] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            val = 0.5 * (p[(i - 1, j)] + p[(i, j - 1)])
            p[(i, j)] = val
    return p[(k, l)]


class MyTestCase(unittest.TestCase):
    def test_type(self):
        self.assertEqual(heron(3, 4, 5), 6)
        self.assertIsInstance(heron(3, 4, 5), float)
        with self.assertRaises(ValueError):
            heron(3, 4, 10)

    def test_dynP(self):
        self.assertEqual(dynP(2, 3), 0.6875)

    def test_rekP(self):
        self.assertEqual(rekP(2, 3), 0.6875)

    def test_pi(self):
        self.assertAlmostEqual(count_pi(100000), 3.14, places=3, msg=None)

if __name__ == '__main__':
    unittest.main()