# -*- coding:utf-8 -*-

"""
file:二叉树的前序遍历

前序遍历:根,左,右
"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def preorderTraversal(root):
    path = []
    if root is None:
        return path
    # 利用一个栈来存储二叉树信息
    stack = []
    stack.append(root)
    while stack:
        root = stack.pop()
        path.append(root.val)
        if root.right is not None:
            stack.append(root.right)
        if root.left is not None:
            stack.append(root.left)
    return path