"""
    a simple browser realize
    解答：我们使用两个栈，X 和 Y，我们把首次浏览的页面依次压入栈 X，当点击后退按钮时，再依次从栈 X 中出栈，
    并将出栈的数据依次放入栈 Y。当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
    当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。当栈 Y 中没有数据，
    那就说明没有页面可以点击前进按钮浏览了。
"""

import os
os.path.append('_08_01_stack.py')
from _08_01_stack import ArrayStack


class Browser:
    def __init__(self):
        self.back_stack = ArrayStack()
        self.forward_stack = ArrayStack()

    def open(self, value):
        self.forward_stack.push(value)

    def can_forward(self):
        if self.forward.is_empty():
            return False
        return True

    def forward(self):
        if self.forward.is_empty():
            return
        tmp = self.forward_stack.pop()
        self.back_stack.push(tmp)

    def can_back(self):
        if self.back_stack.is_empty():
            return False
        return True

    def back(self):
        if self.back_stack.is_empty():
            return
        tmp = self.back_stack.pop()
        self.forward_stack.push(tmp)
