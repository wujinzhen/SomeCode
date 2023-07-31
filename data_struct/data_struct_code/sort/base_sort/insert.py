"""
插入排序
    原地 稳定排序
    时间复杂度为O(n^2)
    两个for循环, 第一个for代表循环轮数, 第二个循环用于比较数据
        将列表分为两个区域, 左边是排序好的区域, 每轮从右边区域第一个数往左边区域插入
"""

def insert_sort(array):
    length = len(array)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array


from utils import get_random_list
l = get_random_list()
print(insert_sort(l))