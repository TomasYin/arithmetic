# -*- coding:utf-8 -*-

"""
冒泡排序
时间复杂度：最坏O(n2),平均O(nlog2(n))
不稳定
"""

def bubble_sort(alist):
    length = len(alist)
    for current in range(length-1):
        flag = True
        for position in range(length-1-current):
            if alist[position] > alist[position + 1]:
                alist[position],alist[position + 1] = alist[position + 1],alist[position]
                flag = False
        if flag:
            break
    return alist

    
