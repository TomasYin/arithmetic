# -*- coding:utf-8 -*-

"""
file:找到一个列表中各个字符串的最长公共字符串
"""

def longestCommonPrefix(strs):
    if not strs:
        return ""
    res = strs[0]
    
    for s in strs[1:]:
        n = len(s)
        for i,c in enumerate(res):
            if i >= n or res[i] != s[i]:
                res = res[:i]
                break
    return res

if __name__ == '__main__':
    a = ['ascd','ascdd','asefd'] 
    print(longestCommonPrefix(a))