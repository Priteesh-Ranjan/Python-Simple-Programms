# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:29:06 2022

@author: Lenovo
"""

## Swap case without using "swapcase"
s = 'HackerRank.com presents "Pythonist 2".'
# def swap_case(s):
    # string  = s
    # newstring = ''
    # for i in string:
    #     if (i.isupper()) == True:
    #         newstring+=(i.lower())
    #     elif (i.islower()) == True:
    #         newstring+=(i.upper())
    #     elif (i.ispace()) == True:
    #         newstring+=i
    #     else:
    #         newstring+=i
    # return newstring

s = "Bnahsb bvgh hHjbmnb"
string  = s
newstring = ''
for i in string:
    if (i.isupper()) == True:
        newstring+=(i.lower())
    elif (i.islower()) == True:
        newstring+=(i.upper())
    elif (i.isspace()) == True:
        newstring+=i
    else:
        newstring+=i
print(newstring)