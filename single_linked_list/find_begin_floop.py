# -*- coding:utf-8 -*-

"""
判断单链表是否有环
"""

class Node():
    #定义一个Node类作为单链表,其中包括两个属性item节点值,一个next节点的下一个指向
    def __init__(self,item=None):
        self.item = item
        self.next = None
    
def find_begin_floop(head):#判断是否为环结构并且找出环结构的入口节点
    slow = head     #将头指针指向slow
    fast = head     #将头指针指向fast
    loopExist = False   #默认头结点是空的
    
    if head == None:    #如果头指针就是空,那么就肯定不是环结构
        return False
    
    while fast.next != None and fast.next.next != None:
        slow = slow.next    #slow每次移动一个节点
        fast = fast.next.next   #fast每次移动两个节点
        if slow == fast:    #当fastPtr和slowPtr的节点相同时，也就是两个指针相遇了
            loopExist = True
            print("存在环结构")
            break
    
    if loopExist == True:   #如果存在环了
        slow = head     #将slow从新指向头结点
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
    
    print('不是环结构')
    return False

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(find_begin_floop(node1).item)
      
        
    
