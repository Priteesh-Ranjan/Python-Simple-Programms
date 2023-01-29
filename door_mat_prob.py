# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:30:08 2022

@author: Lenovo
"""

#door_mat_problem
r,c = map(int,input().split(' '))

# for top layer
for i in range(1,r,2):
    print(("_|_"*i).center(c))

# for middle layer
print(' BABA '.center(c))

#for bottom layer
for i in range(r-2,-1,-2):
    print(("_|_"*i).center(c))

