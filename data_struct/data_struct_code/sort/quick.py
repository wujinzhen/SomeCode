"""
快速排序
    快排也是利用的分治思想。
    排序数组下标从P到R,我们选择从P到R之间任意一个数据作为point分区,
    遍历到P到R的数据,将小于point的放到左边,将大于point的放到右边,
    将point放到中间,这样P到R的数据分为三部分:小于等于大于。
"""


def quick_sort(array, l, r):
    if l >= r:
        return

    i = partition(array, l, r)
    quick_sort(array, l, i-1)
    quick_sort(array, i+1, r)
    return array


def partition(array, l, r):
    i = l
    value = array[r]
    for j in range(l, r):
        if array[j] < value:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[r] = array[r], array[i]
    return i


from utils import get_random_list
l = get_random_list()
print(l)
print(quick_sort(l, 0, len(l)-1))