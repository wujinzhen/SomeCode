"""
寻找旋转数组中最小的元素,可能存在重复元素
"""


def fun(array):
    low, high = 0, len(array) - 1
    min_num = array[0]
    while low <= high:
        mid = (low + high) // 2
        min_num = min(array[mid], min_num)
        if array[low] <= array[mid-1]:
            min_num = min(array[low], min_num)
            low = mid + 1
        else:
            min_num = min(array[high], min_num)
            high = mid - 1
    return min_num


def fun2(array):
    low, high = 0, len(array) - 1
    while low < high:
        mid = (low + high) // 2
        # mid位置的数已经比最小的数大，排除
        if array[mid] > array[high]:
            low = mid + 1
        # mid位置的数可能是最小的数不能排除
        elif array[mid] < array[high]:
            high = mid
        # 遇到重复元素，跳前一个
        else:
            high -= 1
    return array[high]


li = [4, 5, 6, 1, 2, 2, 3, 4, 4]
print(fun2(li))