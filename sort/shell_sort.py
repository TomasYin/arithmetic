# -*- coding:utf-8 -*-

"""
希尔排序
时间复杂度：平均O(nlog2(n)),最坏O(n2)
不稳定
"""

def shell_Sort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gaplnsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gaplnsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        
        while position >= gap and alist[position-gap] >currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position ] = currentvalue

if __name__ == '__main__':
    a = [5,4,6,3,1,0]
    shell_Sort(a)
    print(a)