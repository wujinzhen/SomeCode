"""
单链表
"""


class Node:
    def __init__(self, data, next = None) -> None:
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.__head = None

    def find_by_value(self, value):
        """按照数据值在链表中查找"""
        node = self.__head
        if node != None and node.data != value:
            node = node.next
        else:
            return node

    def find_by_index(self, index):
        """按照索引值在链表中查找"""
        node = self.__head
        pos = 0
        while node != None and pos != index:
            pos += 1
            node = node.next
        return node

    def insert_to_head(self, value):
        """在链表头部插入一个节点"""
        node = Node(value)
        node.next = self.__head
        self.__head = node

    def insert_after(self, node, value):
        """在某个指定节点node后面插入一个节点"""
        if node == None:
            return
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node, value):
        """在某个指定节点node前面插入一个节点"""
        if node == None or self.__head is None:
            return
        if node == self.__head:
            self.insert_to_head(value)
            return

        new_node = Node(value)
        cur = self.__head
        not_found = False  # 是否能在链表中找到
        while cur.next != node:
            if cur.next is None:
                not_found = True
                break
            cur = cur.next
        if not_found is False:
            cur.next = new_node
            new_node.next = node

    def delete_by_node(self, node):
        """删除指定节点"""
        # 链表为空
        if self.__head is None:
            return
        # 删除节点为头节点
        if node == self.__head:
            self.__head = node.next
            return

        cur = self.__head
        not_found = False
        while cur.next != node:
            if cur.next is None:
                not_found = True
                break
            cur = cur.next
        if not_found is False:
            cur.next = node.next

    def delete_by_value(self, value):
        """删除指定值的节点"""
        if self.__head is None:
            return
        if self.__head.data == value:
            self.__head = self.__head.next

        pre = self.__head
        cur = self.__head.next
        not_found = False
        while cur.data != value:
            if cur.next is None:
                not_found = True
                break
            cur = cur.next
            pre = pre.next
        if not_found is False:
            pre.next = cur.next

    def delete_last_N_node(self, n):
        """删除链表倒数第N个节点
        利用两个指针, 快指针先走N步, 然后快慢一起走, 快指针到达尾部则慢指针位于倒数第N个节点上
        """
        fast = self.__head
        slow = self.__head
        # 快指针先走n步
        while n:
            fast = fast.next
            n -= 1
        # 快慢一起走直到快指针到达尾部, 同时记录slow的上一个位置
        while fast:
            temp = slow
            slow = slow.next
            fast = fast.next
        temp.next = slow.next

    def find_mid_node(self):
        """查找链表中间节点"""
        fast = self.__head
        slow = self.__head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reversed_self(self):
        """翻转链表"""
        if self.__head == None or self.__head.next == None:
            return
        cur = self.__head.next
        pre = self.__head
        while cur.next:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        self.__head.next = None
        self.__head = pre

    def has_ring(self):
        """检查链表中是否有环"""
        fast = self.__head
        slow = self.__head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
