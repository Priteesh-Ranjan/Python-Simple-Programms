# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:29:55 2022

@author: Lenovo
"""
# TextWrap
import textwrap

def wrap(string, max_width):   
    return '\n'.join(textwrap.wrap(string,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)