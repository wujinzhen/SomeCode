"""
堆
"""


class Heap:
    def __init__(self, data: list, capacity = 100) -> None:
        self._data = data
        self._capacity = capacity
        self._heapify()

    def get_count(self):
        return len(self._data)

    def _heapify(self):
        """堆化"""
        tail_idx = len(self._data) - 1
        if tail_idx <= 0:
            return
        # 折半, lp后都是叶子节点
        lp = (tail_idx-1) // 2
        # 从下往上堆化
        for idx in range(lp, -1 , -1):
            self._heap_down(idx, tail_idx)

    def _heap_down(self, idx, tail_idx):
        """将位置idx的元素向下递推直到符合堆的特性, 下边界为tail_idx"""
        pass

    def insert(self, num):
        if self._capacity > len(self._data):
            self._insert(num)
            return True
        return False

    def _insert(self, num):
        """将num插入到堆中"""
        pass

    def remove_top(self):
        """移除堆顶元素"""
        if not self._data:
            return
        if len(self._data) == 1:
            return self._data.pop()
        tmp = self._data[0]
        self._data[0] = self._data.pop()
        self._heap_down(0, len(self._data)-1)
        return tmp

    def get_top(self):
        return self._data[0]


class MaxHeap(Heap):
    def _heap_down(self, idx, tail_idx):
        mid = (tail_idx-1) // 2
        while idx <= mid:
            left = idx * 2 + 1
            right = idx * 2 + 2
            if right <= tail_idx:
                if self._data[right] >= self._data[left]:
                    tmp = right
                else:
                    tmp = left
            else:
                tmp = left
            if self._data[tmp] > self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break

    def _insert(self, num):
        self._data.append(num)
        tail_idx = len(self._data) - 1
        while tail_idx > 0:
            parent = (tail_idx-1) // 2
            if self._data[parent] < self._data[tail_idx]:
                self._data[parent], self._data[tail_idx]= self._data[tail_idx], self._data[parent]
                tail_idx = parent
            else:
                break



class MinHeap(Heap):
    def _heap_down(self, idx, tail_idx):
        mid = (tail_idx-1) // 2
        while idx <= mid:
            left = idx * 2 + 1
            right = idx * 2 + 2
            if right <= tail_idx:
                if self._data[right] < self._data[left]:
                    tmp = right
                else:
                    tmp = left
            else:
                tmp = left
            if self._data[tmp] < self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break

    def _insert(self, num):
        self._data.append(num)
        tail_idx = len(self._data) - 1
        while tail_idx > 0:
            parent = (tail_idx-1) // 2
            if self._data[parent] > self._data[tail_idx]:
                self._data[parent], self._data[tail_idx]= self._data[tail_idx], self._data[parent]
                tail_idx = parent
            else:
                break


if __name__ == '__main__':
    _list = [9, 8, 5, 3, 1, 99, 44, 22]
    bh = MinHeap(_list)
    print(bh._data)
    bh.insert(100)
    print(bh._data)
    bh.remove_top()
    print(bh._data)
    # print(bh._draw_heap(bh._data))