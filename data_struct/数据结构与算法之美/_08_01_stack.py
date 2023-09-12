"""
栈
"""


class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next


class LinkedStack:
    "链表栈"
    def __init__(self):
        self._top = None

    def push(self, value):
        node = Node(value)
        node.next = self._top
        self._top = node

    def pop(self):
        if not self._top:
            return None
        tmp = self._top
        self._top = self._top.next
        return tmp.data

    def is_empty(self):
        return not self._top


class ArrayStack:
    "数组栈"
    def __init__(self):
        self._top = []

    def push(self, value):
        self._top.append(value)

    def pop(self):
        return self._top.pop()

    def is_empty(self):
        return not self._top
