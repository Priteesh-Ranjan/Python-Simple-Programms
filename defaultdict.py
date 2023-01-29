# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:25:46 2023

@author: Lenovo
"""

# default_dectionary tutorial

from collections import defaultdict

# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)

# n,m = map(int,input().split())
# l1 = []
# l2 = []
# count = 0
# for i in range(n):
#     l1.append(input())
# for i in range(m):
#     l2.append(input())
    
# for l1 in l2:
#     if l2[i] == l1[i]:
#         print(i)
#     else:
#         print(-1)


# n,m = list(map(int, input().split()))
# a = [input() for i in range(n)]
# b = [input() for j in range(m)]
# ls = [(x,y) for x,y in enumerate(a)]
# print((ls))

# for i in b:
#     n = []
#     for j in ls:
#         if j[1] == i:
#             n.append(str(j[0]+1))
#     if n:
#         print(" ".join(n))
#     else:
#         print(-1)
            
#####
# # enumerate function
# # Python program to illustrate
# # enumerate function
# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"

# # creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)

# print (list((obj1)))
# print (list(enumerate(l1)))

# # changing start index to 2 from 0
# #print (list(enumerate(s1, 2)))


n,m = map(int,input().split())
d = defaultdict(list)
for i in range(n):
    s = input().rstrip()
    d[s].append(i+1)

for i in range(m):
    s = input().rstrip()

    if s in d:
        print(" ".join(map(str,d[s])))
    else:
        print('-1')

