# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:23:40 2022

@author: Lenovo
"""
# list compreshension
# code 1
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# lst = []
# for i in range(0,x+1):
#     for j in range(0,y+1):
#         for k in range(0,z+1):
#               if (i+j+k) != n:
#                   lst.append([i,j,k])
# print(lst)
    
## Code 2
x = int(input())
z = int(input())
y = int(input())
n = int(input())
i = [ a for a in range(x+1)]
j = [ b for b in range(y+1)]
k = [ c for c in range(z+1)]
#print([i,j,k])
ans  = [[a,b,c] for a in i for b in j for c in k if (a+b+c)!=n ]
print(ans)