"""
二分查找循环有序数组中的值

循环数组,以中间为分区点,可以分为一个有序数组和一个循环数组
    分区后,如果首元素小于mid, 则说明左边为有序数组, 右边为循环数组
          如果首元素大于mid, 则说明左边为循环数组, 右边为有序数组
    如果目标元素在有序数组中, 则用二分查找
    如果目标元素在循环数组中, 继续用中间分点划分循环数组,直到找到目标值
"""


def fun(array, value):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            return mid + 1
        elif array[low] > array[mid-1]:
            if array[mid+1] <= value <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if array[low] >= value >= array[mid-1]:
                high = mid - 1
            else:
                low = mid + 1



def search(array, value) -> int:
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            return mid
        if array[low] > array[mid]:
            if array[mid+1] <= value <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if array[low] <= value < array[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1


li = [1,3]
# [7, 1, 2, ,4]
print(search(li, 3))