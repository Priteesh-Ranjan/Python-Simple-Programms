# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:02:39 2022

@author: Lenovo
"""

def print_rangoli(size):
 
    # for i in range(size):        
    #     s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))          
    #     print((s+s[::-1][1:]).center(4*size-3,"-"))
    
    # for i in range(size-1):
    #     s = '-'.join(chr(ord('a')+size-j-1) for j in range(size-i-1))
    #     print((s+s[::-1][1:]).center(4*size-3,"-"))

#code 2 
    import string
    alp = list(string.ascii_lowercase)[:size]
    #print(alp)
    x = size*4 - 3 
    for i in range(size-1,0,-1):
        letters = alp[i:]
        letters = letters[len(letters):0:-1] + letters
        #print(letters5)
        print("-".join(letters).center(x,"-"))
    for i in range(size):
        letters = alp[i:]
        letters = letters[len(letters):0:-1] + letters
        print("-".join(letters).center(x,"-"))
   
# def print_rangoli(size):
#     # your code goes here
#     for i in range(size):
#         s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
#         print((s+s[::-1][1:]).center(4*size-3, "-"))
#############################################################
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)