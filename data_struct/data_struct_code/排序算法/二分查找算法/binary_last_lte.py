"""
二分查找最后一个小于等于某个值
"""


def binary_search(array, value):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] <= value:
            if mid == high or array[mid+1] > value:
                return mid + 1
            else:
                low = mid + 1
        else:
            high = mid - 1


array = [3, 3,3, 3, 3, 7,7, 8]
print(binary_search(array,  3))