# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 15:17:01 2022

@author: Lenovo
"""

#string_formatting
def print_string(number):
    space = len(bin(number))
    for i in range(1,number+1):
        print(str(i).rjust(space)+ " " + oct(i).rjust(space)+ " " + (hex(i).upper()).rjust(space)+ " " + bin(i).rjust(space))

# def print_string(number):
#     space = len(bin(number)[2:])
#     for i in range(1,number+1):
#         print(str(i).rjust(space) + " " + oct(i)[2:].rjust(space) + " " + (hex(i)[2:].upper()).rjust(space) + " " + bin(i)[2:].rjust(space))

if __name__ == '__main__':
    n = int(input())
    print_string(n)