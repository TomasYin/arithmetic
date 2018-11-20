# -*- coding:utf-8 -*-

"""
选择排序
时间复杂度:O(n2)
不稳定
"""

def seclect_sort(alist):
    length = len(alist)
    for current in range(length):
        small = current
        for position in range(current+1,length):
            if alist[position] < alist[small]:
                small = position
        if small != current:
            alist[small],alist[current] = alist[current],alist[small]
    return alist

if __name__ == "__main__":
    a = [5,4,6,3,1,0]
    b = seclect_sort(a)
    print(b)
    
                
