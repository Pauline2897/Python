class Queue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if (self.is_empty()):
            raise IndexError("Kolejka jest pusta")
        else:
            data = self.items[self.head]
            self.items[self.head] = None
            self.head = (self.head + 1) % self.n
            return data

#------------------------TEST------------------------------
import unittest



class TestStack(unittest.TestCase):

    def test_is_empty(self):
        kolejka = Queue()
        self.assertEqual(kolejka.is_empty(), True)
        kolejka.put(1)
        self.assertEqual(kolejka.is_empty(), False)

    def test_is_full(self):
        kolejka = Queue(1)
        self.assertEqual(kolejka.is_full(), False)
        kolejka.put(5)
        self.assertEqual(kolejka.is_full(), True)

    def test_put(self):
        kolejka = Queue()
        kolejka.put(5)
        self.assertEqual(5, kolejka.items[0])

    def test_get(self):
        kolejka = Queue()
        with self.assertRaises(IndexError):
            kolejka.get()
        kolejka.put(5)
        self.assertEqual(kolejka.get(), 5)


if __name__ == "__main__":
    unittest.main()