"""
question:
假设我们现在需要对 D,a,F,B,c,A,z 这个字符串进行排序,要求将其中所有小写字母都排在
大写字母的前面,但小写字母内部和大写字母内部不要求有序。
比如经过排序之后为 a,c,z,D,F,B,A,这个如何来实现呢？

果字符串中存储的不仅有大小写字母，还有数字。要将小写字母的放到前面，
大写字母放在最后，数字放在中间，不用排序算法，又该怎么解决呢？

answer:
由于内部不需要排序,只需要分区就行了,可以利用快排的思想
"""

def partition_sort2(array):
    s_point = 0
    e_point = len(array)
    while s_point < e_point:
        if 'a' <= array[s_point] <= 'z':
            s_point += 1
        else:
            e_point -= 1
            array[e_point], array[s_point] = array[s_point], array[e_point]
    return array


# print(partition_sort2(["D","a","F","B","c","A","z"]))


def partition_sort3(array):
    # 初始化三个指针：low指向字符串的起始位置，high指向字符串的末尾，cur指向字符串的当前位置。
    # 如果cur是小写字母则与low交换， 如果大写字母则与high交换，知道cur=high
    low, cur, high = 0, 0, len(array)-1
    while cur <= high:
        if array[cur].islower():
            array[cur], array[low] = array[low], array[cur]
            cur += 1
            low += 1
        elif array[cur].isupper():
            array[cur], array[high] = array[high], array[cur]
            high -= 1
        else:
            cur += 1

    return array



print(partition_sort3(["D","a","3","F","B","c","A","1","z"]))
