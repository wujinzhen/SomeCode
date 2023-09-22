"""
冒泡排序
    原地 稳定排序
    时间复杂度为 O(n^2)
    两个for循环, 外层循环是比较轮数, 内层循环是将两个相邻元素进行比较
        每轮过后最后一个元素是最大的, 因为每往后一轮比较的元素就会减少一个
"""
def bubble_sort(array):
    length = len(array)
    for i in range(length):
        is_sort = False
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sort = True
        if not is_sort:
            break
    return array
