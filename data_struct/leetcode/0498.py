"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]
示例 2：

输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]
"""


from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        length = len(mat[1])
        hight = len(mat)
        direct = 'up'
        x, y = 0, 0
        _list = []
        while True:
            if x == length - 1 and y == hight - 1:
                _list.append(mat[y][x])
                break
            if direct == 'up':
                _list.append(mat[y][x])
                if x == length - 1:
                    y += 1
                    direct = 'down'
                    continue
                if y == 0:
                    x += 1
                    direct = 'down'
                    continue
                x += 1
                y -= 1
            if direct == 'down':
                _list.append(mat[y][x])
                if y == hight - 1:
                    x += 1
                    direct = 'up'
                    continue
                if x == 0:
                    y += 1
                    direct = 'up'
                    continue
                x -= 1
                y += 1
        return _list

"""
[1,2,3, 9],
[4,5,6, 8]
"""
res = Solution().findDiagonalOrder([[1,2,3, 9],[4,5,6, 8]])
print(res)