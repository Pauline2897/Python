
# zad 10.8


from collections import deque
import random


class RandomQueue:
    __slots__ = {'data'}

    def __init__(self):
        self.data = deque()

    def insert(self, item: int):
        self.data.append(item)
        self.data.rotate(random.randint(-5, 5))

    def remove(self)->int:
        self.data.rotate(random.randint(-5, 5))
        return self.data.pop()

    def is_empty(self)->bool:
        return len(self.data) == 0

    def is_full(self):
        return False



if __name__ == '__main__':
    start_list = [13, 90, 1, 8, 13]
    rq = RandomQueue()
    for el in start_list:
        rq.insert(el)
    r = rq.remove()
    print(r)