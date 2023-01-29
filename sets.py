# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 09:45:23 2023

@author: Lenovo
"""

n1 = int(input())
lst1 = set(map(int,input().split()))
    
n2 = int(input()) 
lst2 = set(map(int,input().split()))

x1 = lst2.difference(lst1)
x2 = lst1.difference(lst2)

for i in sorted(x1.union(x2)):
    print(i)