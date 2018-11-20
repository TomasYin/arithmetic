# -*- coding:utf-8 -*-

"""
file:二级制相加
"""

def addBinary(a,b):
    res = []
    if len(a) < len(b):
        a,b = b,a
    n = len(a)
    m = len(b)
    # c用来保存进位情况
    c = 0
    # r用来表示计算后的每一位结果
    r = 0
    
    for k in range(n):
        # 二级制从后往前计算
        i = n - 1 - k
        if k < m:
            j = m - 1 - k
            r = (int(a[i])+int(b[j])+c)%2
            c = (int(a[i])+int(b[j])+c)//2
        else:
            r = (int(a[i])+int(b[j])+c)%2
            c = (int(a[i])+int(b[j])+c)//2
        res.insert(0,str(r))
    if c == 1:
        res.insert(0,str(r))
    return ''.join(res)

if __name__ == '__main__':
    a = '11'
    b = '1'
    print(addBinary(a,b))
        