# ##
# #  Example of Skip List source code for c
# ##
# import random
# import sys

# minint=0
# maxint=65535
# class Node(object):
#     def __init__(self, key=minint, value=None, level=1):
#         self.key = key
#         self.value = value
#         self.level = level
#         self.right = None
#         self.down = None

# class SkipList(object):
#     def __init__(self):
#         self.top = Node(minint)
#         self.top.right = Node(maxint)
#         self.nodenum = 0
#         pass

#     def getNode(self, key):
#         node = self.top
#         while 1:
#             while key >= node.right.key :
#                 node = node.right
#             if( key == node.key):
#                 return node
#             if node.down == None:
#                 return None
#             node = node.down

#     def findNode(self, key):
#         return self.searchNode(self.top,key)

#     def searchNode(self, node, key):
#         while key >= node.right.key:
#             node = node.right
#         if key == node.key:
#             return node
#         if node.down == None:
#             return None
#         return self.searchNode(node.down, key)

#     def insertNode(self, top, key, value):
#         while key >= top.right.key:
#             top = top.right
#         if key == top.key:
#             return None
#         if top.down == None:
#             node = Node(key, value)
#             node.right = top.right
#             top.right = node
#             node.level = top.level
#             self.nodenum = self.nodenum + 1
#             return node
#         downnode = self.insertNode(top.down, key, value)
#         if downnode:
#             node = Node(key, value)
#             node.right = top.right
#             top.right = node
#             node.down = downnode
#             node.level = top.level
#             return node
#         return None

#     def insert(self, key, value):
#         k = self.getK()
#         for l in range(self.top.level+1,k+1):
#             topleft = Node(minint, level=l)
#             topright = Node(maxint, level=l)
#             topleft.right = topright
#             topleft.down = self.top
#             self.top = topleft
#             print("l="+str(self.top.level))
#         top = self.top
#         while top.level != k:
#             top = top.down

#         self.insertNode(top, key, value)
#         print("num="+str(self.nodenum)+" "+str(k)+" "+str(key)+" "+str(value)+" insert OK")

#     def getK(self):
#         k = 1
#         while random.randint(0,1):
#             k = k + 1
#         return k

# def printNode(node):
#     print("level="+str(node.level)+" key="+str(node.key)+" value="+str(node.value))
#     pass

# if __name__ == '__main__':
#     skiplist = SkipList()
#     for x in range(1,10):
#         skiplist.insert(x, random.randint(3,1000))
#     # printNode(skiplist.getNode(4))
#     # printNode(skiplist.findNode(4))


import random

class Node:
    def __init__(self, value=None, level=0):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self):
        self.max_level = 16  # 最大索引层数
        self.head = Node(float("-inf"), self.max_level)  # 头结点，value设置为负无穷
        self.level = 0  # 当前索引层数

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def search(self, value):
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.value == value:
            return current
        return None

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.head
            self.level = level

        new_node = Node(value, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def delete(self, value):
        update = [None] * (self.max_level + 1)
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current and current.value == value:
            for i in range(len(current.forward)):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            # 更新索引层数
            while self.level > 0 and not self.head.forward[self.level]:
                self.level -= 1

    def display(self):
        for i in range(self.level, -1, -1):
            current = self.head.forward[i]
            print("Level {}: ".format(i), end="")
            while current:
                print(current.value, end=" -> ")
                current = current.forward[i]
            print("None")

if __name__ == "__main__":
    skip_list = SkipList()

    elements = [3, 6, 9, 2, 7, 11, 5, 13, 8, 15]
    for element in elements:
        skip_list.insert(element)

    print("Skip List:")
    skip_list.display()

    value_to_search = 7
    result = skip_list.search(value_to_search)
    if result:
        print(f"Found {value_to_search} in the Skip List.")
    else:
        print(f"{value_to_search} not found in the Skip List.")

    value_to_delete = 9
    skip_list.delete(value_to_delete)

    print("Skip List after deletion:")
    skip_list.display()
