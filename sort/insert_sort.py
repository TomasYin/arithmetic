# -*- coding:utf-8 -*-

"""
插入排序
时间复杂度：最好O(n),平均O(n2)
稳定
"""

def insert_sort(alist):
    length = len(alist)
    for current in range(1,length):
        key = alist[current]
        position = current
        while position > 0 and alist[position-1] > key:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = key
    return alist

if __name__ == "__main__":
    a = [5,4,6,3,1,0]
    b = insert_sort(a)
    print(b)
