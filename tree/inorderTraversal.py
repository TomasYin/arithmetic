# -*- coding:utf-8 -*-

"""
file:二叉树的中序遍历

前序遍历:左,根,右
"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    path = []
    if root is None:
        return path
    stack = []
    while stack or root is not None:
        if root is not None:
        # 如果节点root不是空,把它存入栈中,然后将root指向它的左子树
            stack.append(root)
            root = root.left
        else:
        # 如果节点root是空,就将栈弹出一个值,就是一个左子树的部分,再将root指向它的右子树
            root = stack.pop()
            path.append(root.val)
            root = root.right
    return path   
