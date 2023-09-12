"""
实现一个最近最少使用的缓存机制, 使用哈希表+双向链表实现
"""


# 双向列表节点
class DbListNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.pre = None


class LRUCache:
    """
    leet code: 146
        运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
        它应该支持以下操作： 获取数据 get 和 写入数据 put 。
        获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
        写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
            当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间

        当数据被访问时需要将数据移到链表头, 清除少用数据时从尾部开始清理

    哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)
    """

    def __init__(self, size) -> None:
        self.size = size
        # self.top和self.tail作为哨兵节点, 避免越界
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)
        self.hkey = {}
        self.top.next = self.tail
        self.tail.pre = self.top

    def _change_node_to_top(self, cur: DbListNode):
        """将当前节点放在首节点"""
        temp = self.top.next
        temp.pre = cur
        cur.next = temp
        self.top.next = cur
        cur.pre = self.top

    def get(self, key):
        if key in self.hkey.keys():
            cur: DbListNode = self.hkey[key]
            # 将cur节点的前后位置相连, cur跳出当前位置
            cur.next.pre = cur.pre
            cur.pre.next = cur.next
            self._change_node_to_top(cur)
            return cur.value
        return -1

    def put(self, key, value):
        if key in self.hkey.keys():
            cur: DbListNode = self.hkey[key]
            cur.value = value
            cur.next.pre = cur.pre
            cur.pre.next = cur.next
            self._change_node_to_top(cur)
        else:
            new_node = DbListNode(key, value)
            self._change_node_to_top(new_node)
            self.hkey[key] = new_node
            if len(self.hkey.keys()) > self.size:
                self.hkey.pop(self.tail.pre.key)
                self.tail.pre.pre.next = self.tail
                self.tail.pre = self.tail.pre.pre

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.value))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)