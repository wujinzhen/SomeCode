"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。



示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 从数组末尾开始遍历，如果当前数字不为9，则将其加一并立即返回
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        # 如果数组的第一个元素是0，说明对所有位数都进行了加一操作，需要在数组前插入一个1
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits

print(Solution().plusOne([9,9,9]))