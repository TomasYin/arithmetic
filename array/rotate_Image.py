# -*- coding:utf-8 -*-

"""
file:顺时针旋转n*n的二维数组
"""

def rotate_Image(nums):
    new_list = []
    n = len(nums)
    for i in range(n):
        new_list.append([])
        for j in range(n):
            new_list[i].append(nums[n-1-j][i])
            #print(new_list)
    return new_list

if __name__ == '__main__':
    a = [[1,2],[3,4]]
    print(rotate_Image(a))