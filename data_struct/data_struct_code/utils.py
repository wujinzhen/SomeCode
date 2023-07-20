
class Stack(object):
    def __init__(self, size):
        self.size = size      # 初始化数组的大小
        self.array = list()
        self.cur_size = 0     # 代表当前数组的大小

    def push(self, num):
        if self.size <= self.cur_size:
            print('can not push')
            return
        self.array.append(num)
        self.cur_size += 1

    def pop(self):
        if self.cur_size == 0:
            print('can not pop')
            return
        self.cur_size -= 1
        return self.array.pop()


class Queue(object):
    def __init__(self, size):
        self.array = list()
        self.size = size
        self.cur_size = 0  # 代表当前数组的大小
        self.add = 0    # 指向添加的位置
        self.delete = 0  # 指向弹出的位置

    def push(self, num):
        if self.size <= self.cur_size:
            print('can not push')
            return
        self.array.append(num)
        self.cur_size += 1
        # 当add位置到达边界时，返回0位置
        self.add = 0 if self.add == self.size - 1 else self.add + 1

    def pop(self):
        if self.cur_size == 0:
            print('can not pop')
            return
        tmp = self.array[self.delete]  # 这里不要将数pop,这样会减少数组的长度，导致原本指针指向的位置不存在
        self.cur_size -= 1
        self.delete = 0 if self.delete == self.size - 1 else self.delete + 1
        return tmp



# 单链表
class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked:
    """链表"""
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        node = SingleNode(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def display(self):
        cur = self.head
        _list = []
        while cur:
            _list.append(str(cur.data))
            cur = cur.next
        return ' > '.join(_list)


def reverse_linked_list(head):
    """翻转单链表
    用两个指针交替走过链表,每走一步就将前后两个节点的指向翻转
    next_node = cur.next + cur.next = prev  这两步翻转下一个指针的指向
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
