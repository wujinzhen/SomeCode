"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
"""
from typing import List
import sys
sys.path.append('_tools.py')
from _tools import get_random_str


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        https://algo.itcharge.cn/Solutions/0001-0099/median-of-two-sorted-arrays/#%E6%80%9D%E8%B7%AF-1-%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE

        两个正序数组满足以下条件就可以确定中位数, 在|两边就能找到
        nums1[1:m1], nums2[1:m2] | nums1[m1:], nums2[m2:]

        因为是排好序的数组, 符合O(log (m+n))时间复杂度只能用二分法, 找到这个中分的位置
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:  # 选择数量少的数组作为二分的数组,减少二分次数
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2  # 代表在两个数组中中位数所处的个数位置
        left = 0  # 二分数组的左右边界
        right = n1
        while left < right:
            m1 = left + (right - left) // 2  # 数组1的二分点
            m2 = k - m1  # 数组2的二分点
            if nums1[m1] < nums2[m2-1]:  # 如果数组1小于数组2说明当前的二分点左边的个数小于K个, 要继续往右移
                left = m1 + 1
            else:
                right = m1
        # 最终得出的二分点
        m1 = left
        m2 = k - m1

        # 如果两个数组的总个数为奇数, 则取二分点左边的最大数
        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1], float('-inf') if m2 <= 0 else nums2[m2 - 1])
        if (n1 + n2) % 2 == 1:
            return c1
        # 如果总个数为偶数, 则取二分点右边的最大数
        c2 = min(float('inf') if m1 >= n1 else nums1[m1], float('inf') if m2 >= n2 else nums2[m2])
        return (c1 + c2) / 2


if __name__ == '__main__':
    nums1 = [-1, 0, 4, 9, 10]
    nums2 = [2, 3, 5, 19, 30, 98]
    res = Solution().findMedianSortedArrays(nums1, nums2)
    print(res)
