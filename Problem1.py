# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:05:16 2022

@author: Lenovo
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):                
                if i+j+k != n:
                    a.append([i,j,k])
    print(a)
                    
        