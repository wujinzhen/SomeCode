"""tool"""
import random

def get_random_list(count=10, up=100, low=0):
    """获取随机列表"""
    return [random.randint(low, up) for i in range(count)]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def gen_link(_list):
    """列表生成链表"""
    h1 = ListNode(0)
    h1_cur = h1
    for i in _list:
        h1_cur.next = ListNode(i)
        h1_cur = h1_cur.next
    return h1.next


def get_random_str(count=10, sub_str=['a', 'b', 'c', 'd']):
    return ''.join([random.choice(sub_str) for i in range(count)])
