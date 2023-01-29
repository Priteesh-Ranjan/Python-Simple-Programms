# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 11:24:55 2022

@author: Lenovo
"""

# string EX2 
# a = 'this is a string'
# a = a.split(" ")
# print(a)
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line 

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)