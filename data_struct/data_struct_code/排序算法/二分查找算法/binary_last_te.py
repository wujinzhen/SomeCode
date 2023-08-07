"""
二分查找最后一个等于某个值
"""


def binary_search(array, value):
    """堆栈算法"""
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            if high == mid or array[mid+1] != value:
                return mid + 1
            else:
                low = mid + 1
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1


array = [3, 3,3, 3, 3, 7,7, 8]
print(binary_search(array,  7))