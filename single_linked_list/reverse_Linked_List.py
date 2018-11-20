# -*- coding:utf-8 -*-

"""
file:翻转单链表
"""

class Node():
    def __init__(self,data,nextpostion=None):
        self.data = data
        self.nextposition = nextpostion

class Solution():
    def reverse_Linked_List(self,nums):
        rev = None
        while nums:
            next_node = nums.nextposition
            nums.nextposition = rev
            rev = nums
            nums = next_node
        return rev

if __name__ == '__main__':
    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a4 = Node(4)
    a5 = Node(5)
    
    A = Solution()
    new_Node = A.reverse_Linked_List2(a1)
    
    while new_Node:
        print(new_Node.data)
        new_Node = new_Node.nextposition