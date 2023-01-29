# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 14:05:46 2023

@author: Lenovo
"""

#Minion Game :

def mion_game(s):
    vov = 0
    cons = 0
    for i in range(len(s)):
        if s[i] in 'AEIOU':
            vov = vov + (len(s)-i)
        else:
            cons = cons + len(s)-i
            
    if vov>cons:
        print("Stuart", str(vov))
    elif cons>vov:
        print("Kevin", str(cons))
    else:
        print("Draw")
            
            
    
if __name__ == "__main__":
    s = input()
    
    result = mion_game(s)
    print(result)