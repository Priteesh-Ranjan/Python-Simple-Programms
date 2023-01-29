# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:11:34 2022

@author: Lenovo
"""
# finding_string
def count_substring(string, sub_string):
    string.split()
    count = 0
    for i in range(len(string)):
        if sub_string in string[i:i+len(sub_string)]:
            count = count+1 
    return count       
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)