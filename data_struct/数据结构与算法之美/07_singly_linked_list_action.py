"""
单链表一些操作
"""

class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next


# 反转单链表
def reversed_link(head):
    if not head or head.next is None:
        return
    pre = head
    cur = head.next
    while cur:
        tmp = cur.next
        cur.next = pre
        cur = tmp
        pre = cur
    head.next = None
    head = pre
    return head


# 检查链表是否有环
def has_ring(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow.data == fast.data:
            return True
    return False


# 有序列表合并
def merge_sort_link(link1, link2):
    p1, p2 = link1, link2
    head = cur = Node(None)
    while p1 and p2:
        if p1.data > p2.data:
            cur.next = p2
            p2 = p2.next
        else:
            cur.next = p1
            p1 = p1.next
        cur = cur.next
    if p1:
        cur.next = p1
    else:
        cur.next = p2
    return head.next


# 删除链表中倒数第N个
def remove_last_n_node(head, n):
    fast, slow = head, head
    while n:
        fast = fast.next
        n -= 1
    if n > 0:
        return head
    if n == 0:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


def print_all(head: Node):
    nums = []
    current = head
    while current:
        nums.append(current.data)
        current = current._next
    print("->".join(str(num) for num in nums))
