# -*- coding:utf-8 -*-

"""
file:翻转部分单链表
"""

class Node():
    def __init__(self,data,nextpostion=None):
        self.data = data
        self.nextposition = nextpostion

class Solution():
    def reverse_Linked_List2(head,m,n):
        i = 1
        res = head  #设定头结点
        res_end = head  #设定翻转前的位置
        rev = None  #设定翻转部分的头位置
        rev_end = None  #设定翻转部分的尾位置
        
        while head:
            next_node = head.nextposition
            
            if i < m:
                res_end = head
            elif i >= m and i <= n:
                head.nextposition = rev
                rev = head
                if i == m:
                    rev_end = head
            else:
                break
            head = next_node
            i += 1
        
        if m == 1:
        # 当m=1的时候头结点不再是res指向的最开始的head位置,所以将res指针重新指向
            res = rev
        else:
            res_end.nextposition = rev
        rev_end.nextposition = head
        return res