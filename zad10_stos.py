class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise IndexError("Stos jest pelny")
        else:
            self.items[self.n] = data
            self.n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stos jest pusty")
        else:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None
            return data
			
#------------------------TEST------------------------------		
import unittest


class TestStack(unittest.TestCase):

    def test_is_empty(self):
        self.assertEqual(Stack().is_empty(), True)
        stos = Stack()
        stos.push(10)
        self.assertEqual(stos.is_empty(), False)
        stos.pop()
        self.assertEqual(Stack().is_empty(), True)

    def test_is_full(self):
        stos = Stack(1)
        self.assertEqual(stos.is_full(), False)
        stos.push(5)
        self.assertEqual(stos.is_full(), True)

    def test_push(self):
        stos = Stack(0)
        with self.assertRaises(IndexError):
            stos.push(1)
        stos = Stack(2)
        stos.push(1)
        self.assertEqual(stos.n, 1)

    def test_pop(self):
        stos = Stack()
        with self.assertRaises(IndexError):
            stos.pop()
        stos.push(5)
        stos.pop()
        self.assertEqual(stos.n, 0)


if __name__ == "__main__":
    unittest.main()			