"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

输入：l1 = [0], l2 = [0]
输出：[0]

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""
from typing import List, Optional
import sys
sys.path.append('_tools.py')
from _tools import gen_link


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        逆序存储正好地位相加, 进位留着下一次用, 长度不同, 不足的地方就补0
        """
        head = ListNode(0)
        cur = head
        carry = 0  # 进位
        while l1 or l2:
            # 如果没有就补0
            x = 0 if not l1 else l1.val
            y = 0 if not l2 else l2.val
            # 加上上一轮的进位
            sum = x + y + carry
            # 下一轮的进位
            carry = sum // 10
            # 这一轮的数字
            n = sum % 10

            cur.next = ListNode(n)
            # 指针指向下一位
            cur = cur.next
            # 两个链表指向下一位
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # 如果最高位还有进位
        if carry:
            cur.next = ListNode(carry)
        # 返回头链表
        return head.next


if __name__ == "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]
    h1 = gen_link(l1)
    h2 = gen_link(l2)
    res = Solution().addTwoNumbers(h1, h2)
    while res is not None:
        print(res.val)
        res = res.next
