# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:33:00 2022

@author: Lenovo
"""
import math
# Leet code ex1
# x = []
# arr = [5,4,9]
# arr.sort(reverse = True)
# arr[0] = math.floor(arr[0]/2)
# print(arr)
# def minstonesum(piles,k):
#     for i in range(0,k-1):
#         piles = piles.sort(reverse = True)
#         piles[0] = math.floor(piles[0]/2)
class Solution(object):
    def minStoneSum(self,piles,k):
        pq = piles.sort(reverse = True)
        n = len(piles)     
        for i in range(0,n):
            pq.append(piles[i])
        
        for j in range(k,-1,-1):            
            p = math.floor(max(pq))/2
            pq.pop()
            pq.append(p)
        ans = sum(pq)
    
        return ans
            
    piles = [5,4,9]
    k = 2