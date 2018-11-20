# -*- coding:utf-8 -*-

"""
file:找出一个字符串中最长的回形文

设置一个二维数组来记录回形文的情况
"""

def longestPalindromicSubstring(str):
    n = len(s)
    #创建布尔类型二维数组temp[i][j],记录保存从i 到 j 的字串,是否是回文串,如果为回文串则为True，否则为False
    temp = [[False for i in range(n)] for j in range(n)]
    
    # 起始位置
    start = 0
    # 最长的距离
    mex_length = 1
    
    # 单个字符自己就是回文
    for i in range(n):
        temp[i][i] = True
    
    # 判断相邻元素是否相同,如果相同则设置temp[i][i+1]=True,否则为False
    for i in range(n-1):
        j = i + 1
        if s[i] == s[j]:
            t[i][j] = True
            start = i
            mex_length = 2
    
    # 如果s[i] == s[j],那么是否回文决定于temp[i+1][j-1]
    for l in range(3,n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if s[i] == s[j] and temp[i+1][j-1]:
                temp[i][j] == True
                start = i
                mex_length = l
    return s[start:(start+mex_length)]
    