"""
归并排序
    利用递归的思想, 将列表分为两边, 假设两边已经排好序, 将两个排好序的列表整理成一个
        每次将列表中分,当中分到只剩下一个元素时, 那么该列表就是有序的了
"""


def merge_sort(array):
    length = len(array)
    if length < 2:
        return array
    mid = length // 2
    l_list = merge_sort(array[:mid])
    r_list = merge_sort(array[mid:])

    new_list = []
    l_pos = 0
    r_pos = 0
    while l_pos < len(l_list) and r_pos < len(r_list):
        if l_list[l_pos] < r_list[r_pos]:
            new_list.append(l_list[l_pos])
            l_pos += 1
        else:
            new_list.append(r_list[r_pos])
            r_pos += 1
    new_list.extend(l_list[l_pos:])
    new_list.extend(r_list[r_pos:])
    return new_list


from utils import get_random_list
l = get_random_list()
print(l)
print(merge_sort(l))