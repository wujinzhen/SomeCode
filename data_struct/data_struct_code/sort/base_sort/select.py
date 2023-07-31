"""
    原地 非稳定排序
    时间复杂度O(n^2)
    外层for循环用于轮数, 内层for将列表分为排序好和未排序两部分, 每轮从未排序的部分中找出一个最小的元素加入排序好的区域
"""


def select_sort(array):
    length = len(array)
    for i in range(length):
        cur = i
        for j in range(i, length):
            if array[j] < array[cur]:
                cur = j
        if cur != i:
            array[cur], array[i] = array[i], array[cur]
    return array


from utils import get_random_list
l = get_random_list()
print(select_sort(l))