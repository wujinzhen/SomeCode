"""
基础二分查找, 基于有序连续存储空间的数据结构, 用于快速定位某个值在数据中的位置
"""


def binary_search_1(array, low, high, value):
    """递归算法"""
    if low > high:
        return
    mid = (low + high) // 2
    if array[mid] == value:
        return mid + 1
    elif array[mid] < value:
        return binary_search_1(array, mid+1, high, value)
    else:
        return binary_search_1(array, low, mid-1, value)


array = [1, 2,3, 4, 5, 7, 8, 10]
# print(binary_search_1(array, 0, len(array)-1, 6))



def binary_search_2(array, value):
    """堆栈算法"""
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            return mid + 1
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1


array = [1, 2,3, 4, 5, 7, 8, 10]
print(binary_search_2(array,  1))