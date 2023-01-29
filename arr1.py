# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 20:02:11 2023

@author: Lenovo
"""

#numpy array
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    return numpy.array(arr,float)
   

arr = input().strip().split(' ')
result = arrays(arr)
print(result)