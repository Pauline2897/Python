
# zad 10.3


import unittest

STACK_SIZE = 10
max_int_value = 100


class Stack:
    __slots__ = {'c': 0, 'container': [None] * STACK_SIZE, 'used': set()}

    def __init__(self):
        self.size = 0
        self.container = [None] * STACK_SIZE
        self.used = set()

    def is_empty(self):
        return self.size == 0

    def push(self, item: int):
        try:
            assert item >= 0
            assert item < max_int_value
            if item not in self.used:
                self.container[self.size] = item
                self.used.add(item)
                self.size += 1
        except AssertionError:
            raise ValueError

    def pop(self)->int:
        try:
            if self.size == 0:
                raise ValueError("Empty stack")
            v = self.container[self.size]
            self.used.remove(v)
            self.size -= 1
            self.container[self.size] = None
            return v
        except ValueError:
            raise
        except KeyError:
            self.size -= 1
        except IndexError:
            raise ValueError("Empty stack")

    def size(self)->int:
        return self.size

    def printStack(self)->list:
        return self.container[:self.size]


class MyTestCase(unittest.TestCase):
    def test_stack_empty(self):
        s = Stack()
        s.push(13)
        s.push(90)
        with self.assertRaises(ValueError):
            for i in range(3):
                s.pop()

    def test_too_big_val(self):
        s = Stack()
        with self.assertRaises(ValueError):
            s.push(100)

    def test_print(self):
        start_list = [13, 90, 1, 8, 13]
        s = Stack()
        for el in start_list:
            s.push(el)
        s.pop()
        self.assertEqual(s.printStack(), start_list[:3])


if __name__ == '__main__':
    unittest.main()