"""
堆排序
"""

class HeapSort:
    def __init__(self, data):
        self._data = data
        self._heapify()

    def _heapify(self):
        tail_idx = len(self._data) - 1
        mid = (tail_idx-1) // 2
        for i in range(mid, -1, -1):
            self._heap_down(i, tail_idx)

    def _heap_down(self, idx, tail_idx):
        parent = (tail_idx-1) // 2  # 因为子节点是2N+2, 所以父节点是(x-1)//2
        while idx <= parent:
            left = idx * 2 + 1
            right = idx * 2 + 2
            if right <= tail_idx:
                if self._data[right] > self._data[left]:
                    tmp = right
                else:
                    tmp = left
            else:
                tmp = left
            if self._data[idx] < self._data[tmp]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break

    def _pop_top(self, tail_idx):
        self._data[tail_idx], self._data[0] = self._data[0], self._data[tail_idx]
        self._heap_down(0, tail_idx - 1)

    def sort(self):
        count = len(self._data) - 1
        for i in range(count, -1, -1):
            print(i)
            self._pop_top(i)
        return self._data



if __name__ == '__main__':
    _list = [9, 8, 4, 5, 3, 1, 99, 44, 22, 100]
    bh = HeapSort(_list)
    # print(bh._data)
    print(bh.sort())
    # print(bh._data)