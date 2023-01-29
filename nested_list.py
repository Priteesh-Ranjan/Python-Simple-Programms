# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:44:22 2022

@author: Lenovo
"""

# nested list
l1 = []
l2 = set()
for _ in range(int(input())):
    name = input()
    score = float(input())
    l1.append((name,score))
    l1.sort()
print(l1)
#print(score)       
for items in l1:
    l2.add(items[1])

#l2.remove(min(l2))
for items in l1:
    if(items[1]==min(l2)):
        print(items[0])