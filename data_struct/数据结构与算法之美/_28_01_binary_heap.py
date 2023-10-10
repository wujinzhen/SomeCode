"""
二叉堆
"""
import math

class BinaryHeap:
    def __init__(self, data: list, capacity = 100) -> None:
        self._data = data
        self._capacity = capacity

    def heapify(self):
        "堆化,从上往下"
        self._heapify(self._data, len(self._data)-1)

    def _heapify(self, data, tail_idx):
        if tail_idx <= 0:
            return
        lp = (tail_idx-1) // 2
        for idx in range(lp, -1 , -1):
            self._heap_down(data, idx, tail_idx)

    @staticmethod
    def _heap_down(data, idx, tail_idx):
        """
        idx: 需要堆化的位置
        tail_idx: 堆化的右边界
        """
        parent = (tail_idx-1) // 2
        while idx <= parent:
            # 看下左右节点是否存在,存在了谁大,合父节点比较,大的交换,并把下次要比较节点往下调整
            left = idx * 2 + 1
            right = idx * 2 + 2
            if right <= tail_idx:
                if data[right] > data[left]:
                    tmp = right
                else:
                    tmp = left
            else:
                tmp = left
            if data[tmp] > data[idx]:
                data[tmp], data[idx] = data[idx], data[tmp]
                idx = tmp
            else:
                break  # 顺序对了退出

    def insert(self, num):
        "插入,从下往上堆化"
        if self._capacity > len(self._data):
            self._insert(self._data, num)
            return True
        return False

    @staticmethod
    def _insert(data, num):
        data.append(num)
        new_index = len(data) - 1
        while new_index > 0:
            parent = new_index // 2
            if data[new_index] > data[parent]:
                data[new_index], data[parent] = data[parent], data[new_index]
                new_index = parent
            else:
                break

    def remove_top(self):
        "弹出堆顶元素"
        "先将最后一个元素代替第一个元素,然后堆顶元素做一个至上往下的堆化过程"
        if not self._data:
            return
        if len(self._data) == 1:
            return self._data.pop()
        tmp = self._data[0]
        self._data[0] = self._data.pop(len(self._data)-1)
        BinaryHeap._heap_down(self._data, 0, len(self._data)-2)
        return tmp


    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)

        if length == 0:
            return 'empty heap'

        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            # 每行最后一个换行
            if i == 2**int(math.log(i+1, 2)+1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret


if __name__ == '__main__':
    _list = [9, 8, 4, 5, 3, 1, 99, 44, 22]
    bh = BinaryHeap(_list)
    bh.heapify()
    print(bh._data)
    bh.insert(100)
    print(bh._data)
    bh.remove_top()
    print(bh._data)
    print(bh._draw_heap(bh._data))