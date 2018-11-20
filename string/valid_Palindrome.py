# -*- coding:utf-8 -*-

"""
file:判断回文
"""

def valid_Palindrome(string):
    if not string:
        return True
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left].isalnum() and string[right].isalnum():
            if string[left].lower() != string[right]:
                return False
            left += 1 
            right -= 1
        else:
            if not string[left].isalnum():
                left += 1
            if not string[right].isalnum():
                right -= 1
        return True
                