"""

"""

import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, '../')
sys.path.append(relative_path)
from utils import Stack


class Heap:
    def __init__(self):
        """大根堆"""
        self.array = [None]

    def insert(self, data):
        """插入"""
        if not self.array:
            self.array.append(data)
            return
        index = len(self.array)
        self.array.append(data)
        while index // 2 and self.array[index] > self.array[index//2]:
            self.array[index], self.array[index//2] = self.array[index//2], self.array[index]
            index = index // 2

    def display(self):
        high = 1
        count = 0
        _list = []
        for i in self.array[1:]:
            count += 1
            _list.append(i)
            if count == high:
                print(_list)
                _list = []
                count = 0
                high += 1
        print(_list)

        # return self.array

    def heapify(self, ):
        """"""


heap = Heap()
for i in range(6):
    heap.insert(i)
heap.display()

