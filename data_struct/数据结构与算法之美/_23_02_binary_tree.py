"""
二叉树的遍历
"""

# Pre-order traversal
def pre_order(root):
    if root:
        yield root.val
        yield from pre_order(root.left)
        yield from pre_order(root.right)

# In-order traversal
def in_order(root):
    if root:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)

# Post-order traversal
def post_order(root):
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.val
