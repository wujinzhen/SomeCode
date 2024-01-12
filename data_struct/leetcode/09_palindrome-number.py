"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        _str = str(x)
        l, r = 0, len(_str) - 1
        while l < r:
            if _str[l] != _str[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(10))
