import sys
import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_dir, '../')
sys.path.append(relative_path)
from utils import Stack, Queue


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def pre_order(root):
    """前序"""
    if root:
        yield root.val
        yield from pre_order(root.left)
        yield from pre_order(root.right)


def in_order(root):
    """中序"""
    if root:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)


def post_order(root):
    """后序"""
    if root:
        yield from in_order(root.left)
        yield from in_order(root.right)
        yield root.val


def level_order(robot):
    """层次遍历"""
    queue = Queue(10)
    queue.push(robot)
    while queue.cur_size:
        cur = queue.pop()
        yield cur.val
        if cur.left:
            queue.push(cur.left)
        if cur.right:
            queue.push(cur.right)


def get_high(robot):
    """求二叉树的高度
    每一层记录节点个数, 当达到节点个数时说明该层遍历完, 层次+1
    """
    queue = Queue(10)
    queue.push(robot)
    high, start, end = 0, 0, 1
    while queue.cur_size:
        cur = queue.pop()
        if cur.left:
            queue.push(cur.left)
        if cur.right:
            queue.push(cur.right)
        start += 1
        if start == end:
            high += 1
            start = 0
            end = queue.cur_size
    return high




if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left = node10

    # print(list(level_order(node1)))
    # print(list(level_order(node1)))
    print(get_high(node1))