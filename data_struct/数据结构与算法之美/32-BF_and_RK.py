'''
Author: your name
Date: 2020-12-13 13:23:40
LastEditTime: 2020-12-13 13:24:17
LastEditors: your name
Description: In User Settings Edit
FilePath: \SomeCode\data_struct\32-BM_and_RK.py
'''
# 字符串匹配算法


def BF(max_str, min_str):
    """
     BF 暴力破解
    :param max_str: 主串
    :param min_str: 模式串
    :return: 返回模式串在主串总匹配的字符位置元组
    """
    min_len = len(min_str)
    for i in range(len(max_str) - min_len + 1):
        is_match = True
        for j in range(i, i + min_len):
            if max_str[j] != min_str[j - i]:
                is_match = False
                break
        if is_match:
            return i, i + min_len


def RK(max_str, min_str):
    """
    RK算法，是bf算法的改进，利用hash算法
    :param max_str: 主串
    :param min_str: 模式串
    :return: 返回模式串在主串总匹配的字符位置元组
    """
    min_hash, min_len = hash(min_str), len(min_str)
    for i in range(len(max_str) - min_len + 1):
        if min_hash == hash(max_str[i:min_len + i]):  # 一边比较是否匹配，如果匹配了就return
            return i, min_len + i


def RK2(max_arr, min_arr):
    """
    RK算法，二维矩阵, 降维计算，只能计算数值矩阵，因为在转为字符串之后没办法区分int和str
    :param max_arr: 主串矩阵
    :param min_arr: 模式串矩阵
    :return: 返回模式串在主串总匹配的字符位置元组
    """
    def arr2str(arr):
        """将二位数组转成字符串"""
        return ''.join([str(i) for item in arr for i in item])

    n_str = arr2str(min_arr)  # 将矩阵的比较转为字符串的比较
    min_arr_len, min_arr_len0 = len(min_arr), len(min_arr[0])
    for i in range(len(max_arr) - min_arr_len + 1):
        for j in range(len(max_arr[0]) - min_arr_len0 + 1):
            x_str = arr2str([max_arr[k][j:min_arr_len0 + j] for k in range(i, min_arr_len + i)])
            if x_str == n_str:
                return [i, min_arr_len + i - 1], [j, min_arr_len0 + j - 1]


if __name__ == "__main__":
    max_str = 'asdfjkzhol;'
    min_str = 'zho'
    # print(BF(max_str, min_str))
    # print(RK(max_str, min_str))

    max_arr = [
        [3, 5, 6, 7],
        [3, 5, 2, 3],
        [1, 2, 3, 4]
    ]
    min_arr = [
        [2, 3],
        [3, 4]
    ]
    print(RK2(max_arr, min_arr))