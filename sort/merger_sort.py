# -*- coding:utf-8 -*-

"""
归并排序
时间复杂度：平均O(nlog2(n))
稳定
"""

def merger(left,right):
    i,j = 0,0
    result = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merger_sort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = merger_sort(alist[:mid])
    right = merger_sort(alist[mid:])
    return merger(left,right)

if __name__ == '__main__':
    a = [5,4,6,3,1,0]
    b = merger_sort(a)
    print(b)
            