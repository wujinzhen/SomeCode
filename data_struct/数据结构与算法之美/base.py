def reverse_linked_list(head):
    """翻转单链表
    用两个指针交替走过链表,每走一步就将前后两个节点的指向翻转
    next_node = cur.next  记住下一个节点
    cur.next = prev  翻转当前指针的指向
    prev = cur + cur = next_node 这两步将两个指针向前推进
    """
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev
