"""
利用堆求中位数
构建两个堆, 大根堆存储小的半部分, 小根堆存储大的半部分
        如果堆个数为偶数, 大根堆的大小为为n/2, 小根堆的大小为n/2
        如果堆个数为偶数, 大根堆的大小为为n/2+1, 小根堆的大小为n/2
            保持这个规则则堆的中位数就是大根堆的堆顶
    如果一个数小于等于大根堆堆顶则这个数入大根堆,否则数进小根堆
    当入完堆后需要判断两个堆是否符合堆个数的分布
        如果大根堆的个数比小根堆大2个, 则从大根堆弹出一个元素进小堆
        如果小堆的个数比大堆多1个, 则从小堆弹出一个进大堆
"""

from _28_02_heap import MaxHeap, MinHeap


def get_mid_num(data):
    min_heap = MinHeap([])
    max_heap = MaxHeap([])
    max_heap.insert(data.pop())
    for i in data:
        if i <= max_heap.get_top():
            max_heap.insert(i)
            if max_heap.get_count() - min_heap.get_count() > 1:
                min_heap.insert(max_heap.remove_top())
        else:
            min_heap.insert(i)
            if min_heap.get_count() - max_heap.get_count() > 0:
                max_heap.insert(min_heap.remove_top())

    print(min_heap._data)
    print(max_heap._data)


if __name__ == '__main__':
    _list = [9, 8, 4, 5, 3, 1, 99, 44, 22, 100]
    get_mid_num(_list)