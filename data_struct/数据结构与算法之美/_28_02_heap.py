"""
堆
"""


class Heap:
    def __init__(self, data: list, capacity) -> None:
        self._data = data
        self._capacity = capacity
        self._heapify()

    def _heapify(self):
        tail_idx = len(self._data)-1
        if tail_idx <= 0:
            return
        lp = (tail_idx-1) // 2
        for idx in range(lp, -1 , -1):
            self._heap_down(idx, tail_idx)

    def _heap_down(self, idx, tail_idx):
        pass

    def insert(self, num):
        if self._capacity > len(self._data):
            self._insert(num)
            return True
        return False

    def _insert(self, num):
        pass

    def remove_top(self):
        if not self._data:
            return
        if len(self._data) == 1:
            return self._data.pop()
        tmp = self._data[0]
        self._data[0] = self._data.pop(len(self._data)-1)
        self._heap_down(self._data, 0, len(self._data)-2)
        return tmp


class MaxHeap(Heap):
    def _heap_down(self, idx, tail_idx):
        pass

    def _insert(num):
        pass


class MinHeap(Heap):
    def _heap_down(self, idx, tail_idx):
        pass

    def _insert(num):
        pass
