# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 23:31:27 2023

@author: Lenovo
"""
# Cartesian Product
# from itertools import product
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# print(*(product(A,B)))

# itertools permutations
# from itertools import permutations
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# print(*permutations(A,2))

from itertools import permutations
A,S = input().split()
x = permutations(sorted(A),int(S))
for i in x:
    print("".join(i))