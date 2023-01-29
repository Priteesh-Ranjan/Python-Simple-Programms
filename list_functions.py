# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 09:58:20 2022

@author: Lenovo
"""
# list operations
n = int(input())
arr = []
for i in range(n):
    #arr.append(int(input()))
    c = input().split()
    if 'insert' in c:
        arr.insert(int(c[1]),int(c[2]))
    if 'remove' in c:
        arr.remove(int(c[1]))
    if 'append' in c:
        arr.append(int(c[1]))
    if 'sort' in c:
        arr.sort()
    if 'pop' in c:
        arr.pop()
    if 'reverse' in c:
        arr.reverse()

print(arr)
        