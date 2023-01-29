# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 11:38:24 2022

@author: Lenovo
"""

# Ssubstring and string
# def count_substring(string, sub_string):
#     count = 0
#     for i in string:
#         for j in sub_string:
            
#             count = count+1
            
#     return

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

# string = 'ABCBCBCBCBBC'
# sub_string = 'BC'
# string=string.split(sub_string)
# print(string)
# if(sub_string[0]==sub_string[len(sub_string)-1]):
#     print(len(string))
# else:
#     print(len(string)-1)

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(0, len(string)):
#         if sub_string in string[i: i + len(sub_string)]:
#             count += 1
#     return count


def c_str(string,sub_string):
    count = 0
    for i in range(0,len(string)):
        if sub_string in string[i : i + len(sub_string)]:
            count+=1            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = c_str(string, sub_string)
    print(count)        
