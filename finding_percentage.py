# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:58:57 2022

@author: Lenovo
"""

# finding the percentage 

if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float,line))
        student_marks[name] = scores
    query_name = input()
    
    result = sum(student_marks[query_name])/len(scores)
    print(result)
    