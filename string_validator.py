# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 17:42:23 2022

@author: Lenovo
"""

#String validator

# if __name__ == "__main__":
#     s = input()
#     alnum = False
#     alpha = False
#     digit = False
#     upper = False
#     lower = False
#     for i in range(len(s)):
#         if s[i].isalnum() == True:
#             alnum = True
#         if s[i].isalpha() == True:
#             alpha = True
#         if s[i].isdigit() == True:
#             digit == True
#         if s[i].isupper()== True:
#             upper = True
#         if s[i].islower() == True:
#             lower == True
            
#     print(alnum)
#     print(alpha)
#     print(digit)
#     print(upper)
#     print(lower)

s = input()
alnum = False
alpha = False
lower = False
upper = False
digit = False
for i in range(len(s)):
    if s[i].isalnum() == True:
        alnum = True
    if s[i].isalpha() == True:
        alpha = True
    if s[i].isdigit() == True:
        digit = True
    if s[i].islower() == True:
        lower = True
    if s[i].isupper() == True:
        upper = True
print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)