# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:08:23 2022

@author: Lenovo
"""
# string example 2

# def mutate_string(string, position, character):
#     s = string
#     l = list(s) 
#     i = position
#     c = characterabracadabra
#     l[i] = c
#     s = ''.join(l)
#     s_new = s
#     return s_new

def mutate_string(string,position,charchter): 
    string = string[:position-1] + charchter +s[position:]
    s_new = string
    return s_new
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)