# -*- coding:utf-8 -*-

"""
file:二叉树的后序遍历

前序遍历:左,右,根
"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
def postorderTraversal(root):
    # 思路是使用两个栈,使用前序遍历的思路让stack2中存储的顺序是根,右,左最后再将stack2逆向输出到path中
    
    path = []
    if root is None:
        return path
    stack1 = []
    stack2 = []
    stack1.append(root)
    
    while stack1:
        root = stack1.pop()
        stack2.append(root.val)
        if root.left:
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)
    
    while stack2:
        path.append(stack2.pop())
    return path