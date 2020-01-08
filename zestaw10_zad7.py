
# zad 10.7


import unittest


def cmp1(x, y):
    return x > y


def cmp2(x, y):
    return x < y


class PriorityQueue:
    __slots__ = {'cmpfunc': cmp1, 'container': [], 'size': 0}

    def __init__(self, cmpfunc=cmp1):
        self.container = []
        self.cmpfunc = cmpfunc
        self.size = 0

    def __str__(self):
        return str(self.container)

    def insert(self, item):
        self.size += 1
        self.container.append(item)
        map(self.cmpfunc, self.container)

    def remove(self):
        max_i = 0
        for i in range(1, self.size):
            if self.cmpfunc(self.container[i], self.container[max_i]) > 0:
                max_i = i
        return self.container.pop(max_i)

    def print_queue(self):
        return self.container


class MyTestCase(unittest.TestCase):
    def test_delete_min(self):
        start_list = [13, 90, 1, 8]
        k1 = PriorityQueue(cmp1)
        for i in start_list:
            k1.insert(i)
        k1.remove()
        print(k1.print_queue())
        self.assertEqual(k1.print_queue(), [13, 1, 8])

    def test_delete_max(self):
        start_list = [13, 90, 1, 8]
        k1 = PriorityQueue(cmp2)
        for i in start_list:
            k1.insert(i)
        k1.remove()
        print(k1.print_queue())
        self.assertEqual(k1.print_queue(), [13, 90, 8])


if __name__ == '__main__':
    unittest.main()