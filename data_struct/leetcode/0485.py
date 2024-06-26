"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
示例 1：

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：2
"""


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)


res = Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1, 1, 1])
print(res)