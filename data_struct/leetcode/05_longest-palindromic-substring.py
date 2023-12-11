"""
给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

标签: 动态规划
"""
import copy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2:
            return s

        max_len = 1  # 最长回文长度
        begin = 0  # 最长回文开始位置
        # 二维列表,用来存储i到j之间知否是回文, dp[i][j] = True表示i到j之间是回文
        dp = [[False]*s_len for i in range(s_len)]
        # 字符长度为1都是回文
        for i in range(s_len):
            dp[i][i] = True
        # # 先枚举回文子串的长度, 然后根据左边界和长度确定右边界
        for L in range(2, s_len+1):
            # 确定左边界
            for i in range(s_len):
                # 确定右边界,由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界超过则结束
                if j >= s_len:
                    break
                if s[i] == s[j]:
                    # 如果字符串长度超过3则需要看中间的子串是否是回文
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin+max_len]


if __name__ == '__main__':
    s = '1234545432'
    res = Solution().longestPalindrome(s)
    print(res)
