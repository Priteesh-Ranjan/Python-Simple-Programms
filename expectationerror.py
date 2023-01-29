# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:43:07 2023

@author: Lenovo
"""
# Expectations:
# T = int(input('No. of Test Cases: '))
# for i in range(T):    
#     a,b = map(str,input().split(" "))

# if b != 0:
#     print(int(a)/int(b))
    
# elif b==0:S
#     print('ZeroDivisionError: integer division or modulo by zero')

# else:
#     print("ValueError: invalid literal for int() with base 10: 'b'")

T =  int(input())
for i in range(T):
    a,b = map(int,input().split())
    
    try:
        print ((a)//(b))
    except Exception as e:
        print ("Error Code:",e)

