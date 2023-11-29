"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""
from typing import List
import sys
sys.path.append('_tools.py')
from _tools import get_random_list


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """利用双层for循环遍历列表找到双数和.
        这里注意j的起始位置应该大于i, 因为之前的数据前面循环已经遍历过了"""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        利用哈希表存储每一个遍历过的数和位置, 从hash表中找另一半
        """
        _hash = {}
        for index, i in enumerate(nums):
            tmp = target - i
            if tmp in _hash:
                return index, _hash[tmp]
            _hash[i] = index


if __name__ == "__main__":
    for i in range(10):
        nums = get_random_list(5, 10)
        target = 10
        res = Solution().twoSum2(nums, target)
        print(f"nums:{nums}, target:{target}, res: {res}")
