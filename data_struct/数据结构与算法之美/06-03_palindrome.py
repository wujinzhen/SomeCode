"""
判断单链表是否为回文链表
"""

import sys
sys.path.append('base')
from base import reverse_linked_list


def is_palindrome(head):
    "使用翻转链表的方式实现"
    if not head or head.next is None:
        return True
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second_half = cur = reverse_linked_list(slow)
    first_half = head
    while first_half:
        if first_half.data != second_half.data:
            reverse_linked_list(cur)
            return False
        first_half = first_half.next
        second_half = second_half.next
    reverse_linked_list(cur)
    return True
