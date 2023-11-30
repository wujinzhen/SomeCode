"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""

from typing import List
import sys
sys.path.append('_tools.py')
from _tools import get_random_str


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        cur_l = 0
        cur_dict = {}
        i = 0
        while i < len(s):
            if s[i] in cur_dict:
                max_l = max(max_l, cur_l)
                i = cur_dict[s[i]] + 1
                if not i < len(s):
                    break
                cur_l = 0
                cur_dict = {}
            else:
                cur_dict[s[i]] = i
                cur_l += 1
                i += 1
        max_l = max(max_l, cur_l)
        return max_l

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        滑动窗口做法
        用lookup记录窗口的数据, cur_len记录窗口的大小
        往后滑动每次判断最新的数据是否在窗口中, 如果是的话将窗口左滑, 当前窗口大小-1
        """
        if not s:
            return 0
        # 记录左滑位置
        left = 0
        # 记录窗口的数据
        lookup = set()
        n = len(s)
        # 最大窗口
        max_len = 0
        # 当前滑动窗口大小
        cur_len = 0
        for i in range(n):
            # 左滑窗口+1
            cur_len += 1
            if s[i] in lookup:
                # 如果是已经存在于窗口的元素则移除同时窗口减一
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            # 判断最大窗口
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len



if __name__ == '__main__':
    for i in range(10):
        s = get_random_str(10)
        res = Solution().lengthOfLongestSubstring2(s)
        print(f"字符串: {s}, 最长不重复长度: {res}")
