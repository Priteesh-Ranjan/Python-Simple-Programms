# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 19:28:40 2022

@author: Lenovo
"""

# Capitalize first letter 
def solve(s):
    lst = s.split(" ")
    print(lst)
    ls = [i.capitalize() for i in lst]
    return " ".join(ls)

if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)
