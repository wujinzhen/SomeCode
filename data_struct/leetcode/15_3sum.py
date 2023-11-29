"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""
from typing import List
import sys
sys.path.append('_tools.py')
from _tools import get_random_list


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        该种写法执行时间过长
        """
        _hash = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                tmp = nums[i] + nums[j]
                if tmp in _hash:
                    _hash[tmp].append((i, j))
                else:
                    _hash[tmp] = [(i, j)]
        _list = []
        for index, i in enumerate(nums):
            tmp = 0 - i
            if tmp in _hash:
                for j in _hash[tmp]:
                    if index == j[0] or index == j[1]:
                        continue
                    _tmp = sorted([i, nums[j[0]], nums[j[1]]])
                    if _tmp not in _list:
                        _list.append(_tmp)
        return _list

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """
        本题的重点是去重，排序后的数据可以跳过重复数据
        1. 特判，对于数组长度n, 如果数组为 null或者数组长度小于 3，返回 []。
        2. 对数组进行排序。
        3. 遍历排序后数组：
            1. 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
            2. 对于重复元素：跳过，避免出现重复解
            3. 令左指针 L=i+1 右指针 R=n−1，当 L<R时，执行循环：
                当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R移到下一位置，寻找新的解
                若和大于 0，说明 nums[R]太大，R 左移
                若和小于 0，说明 nums[L]太小，L 右移
        """
        nums.sort()
        total = len(nums)
        res = []
        for i in range(total):
            # 如果大于0则不可能在出现和小于0的了
            if nums[i] > 0:
                return res
            # 跳过重复的i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = total - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 跳过重复的数
                    while L<R and nums[L] == nums[L+1]:
                        L += 1
                    while L<R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                # 如果大则R左移, 如果小则L右移
                elif nums[i]+nums[L]+nums[R]>0:
                    R -= 1
                else:
                    L += 1
        return res


if __name__ == "__main__":
    for i in range(1):
        for i in range(10):
            nums = get_random_list(count=50, up=4, low=-4)
            res = Solution().threeSum2(nums)
            print(f"nums:{nums}, res: {res}")
