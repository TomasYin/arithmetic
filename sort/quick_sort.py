# -*- coding:utf-8 -*-

"""
快速排序
时间复杂度：最坏O(n2),平均O(nlog2(n))
不稳定
"""

def quick_sort(alist,left,right):
    # 结束递归的条件
    if left >= right:
        return alist
    low = left
    high = right
    key = alist[left]
    
    while left < right:
        while left < right and alist[right] >= key:
            right -= 1
        alist[left] =  alist[right]
        
        while left < right and alist[left] <= key:
            left += 1
        alist[right] = alist[left]
    
    alist[left] = key
    #print(alist)
    
    quick_sort(alist,low,left-1)
    quick_sort(alist,right+1,high)

if __name__ == '__main__':
    a = [5,4,6,3,1,0]
    b = quick_sort(a,0,len(a)-1)
    print(a)    