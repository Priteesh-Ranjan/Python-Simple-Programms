# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:06:51 2023

@author: Lenovo
"""

# ordered dictionary
from collections import OrderedDict
N = int(input())  #No. of items
#item_name,item_price = input().split() # item name and item price
d = OrderedDict()
for _ in range(N):
    item,_,price = input().rpartition(' ')
    d[item] = d.get(item,0)  + int(price)
for item,price in d.item():
    print(item,price)
