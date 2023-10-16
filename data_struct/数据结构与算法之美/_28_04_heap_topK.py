"""
利用堆解决Top-K问题
如果是静态数据则生成一个K个数据的大根堆
如果是动态数据则维护一个只保存K个数据的小根堆, 保证前K大的数据
"""
from _28_02_heap import MaxHeap, MinHeap




def static_top_k(data, k):
    heap = MaxHeap(data, len(data))
    _list = []
    for i in range(k):
        _list.append(heap.remove_top())
    return _list


def dynamic_top_k(data, k):
    heap = MinHeap([], k)
    for i in data:
        if not heap.insert(i):
            # print(heap._data, i)
            top = heap.get_top()
            if top < i:
                heap.remove_top()
                heap.insert(i)
    return heap._data


if __name__ == '__main__':
    _list = [9, 8, 4, 5, 3, 1, 99, 44, 22, 100]
    print(static_top_k(data=_list, k=3))
    _list = [9, 8, 4, 5, 3, 1, 99, 44, 22, 100]
    print(dynamic_top_k(data=_list, k=3))