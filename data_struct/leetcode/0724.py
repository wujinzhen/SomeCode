"""
给你一个整数数组 nums ，请计算数组的 中心下标 。

数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。



示例 1：

输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
示例 2：

输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
示例 3：

输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。
"""

from typing import List


# 寻找数组的中心下标
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 总数和解法
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

        # 遍历解法
        left_p, right_p = 0, len(nums) - 1  # 初始化左右指针
        left_total, right_total = 0, 0  # 初始化左右侧的总和

        while left_p < right_p:  # 当左右指针未交叉时循环
            if left_total >= right_total:  # 如果左侧总和大于等于右侧总和
                right_total += nums[right_p]  # 将右指针指向的元素加到右侧总和
                right_p -= 1  # 右指针左移
            else:  # 如果左侧总和小于右侧总和
                left_total += nums[left_p]  # 将左指针指向的元素加到左侧总和
                left_p += 1  # 左指针右移

        if right_total == left_total:  # 如果左右总和相等，返回左指针位置
            return left_p
        return -1  # 如果不存在平衡点，返回-1



res = Solution().pivotIndex([1, -3, 3, -5])
print(res)