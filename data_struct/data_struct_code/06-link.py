from utils import Linked, Stack, reverse_linked_list


_list = [1, 2, 4, 2, 1]
l = Linked()
for i in _list:
    l.push(i)


def symmetry_linked(head):
    """回文链表, 利用栈存储前半段数据进行对比"""
    l, r = head, head
    s = Stack(100)
    s.push(l.data)
    while r.next and r.next.next is not None:
        print(r.next.data, r.next.next.data)
        r = r.next.next
        l = l.next
        s.push(l.data)

    if r.next is None:
        s.pop()

    while l.next is not None:
        l = l.next
        if l.data != s.pop():
            return False
    return True


def symmetry_linked2(head):
    """回文链表, 利用翻转前半段链表进行对比"""
    if not head or not head.next:
        return True

    slow = fast = head
    # 使用快慢指针找到链表的中间节点
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 反转链表的后半部分, 此时两个链表的结构都是1>2>4, 指向共同节点
    second_half = cur = reverse_linked_list(slow)
    first_half = head

    # 比较前半部分和反转后的后半部分的节点值
    while second_half:
        if second_half.data != first_half.data:
            reverse_linked_list(cur)
            return False
        second_half = second_half.next
        first_half = first_half.next

    reverse_linked_list(cur)
    return True


print(l.head)
print(symmetry_linked2(l.head))
print(l.display())
