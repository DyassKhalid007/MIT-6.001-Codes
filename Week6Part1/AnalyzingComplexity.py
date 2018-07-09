# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 17:23:17 2018

@author: Dyass
"""
"""
    Polynomial Complexity:
        Most common polynomial algorithms are quadratic.
        i.e completely grows with square of size of input.
        
        Commonly occurs when we have nested loops or recursive calls
"""
"""Examples"""
def isSubset(L1,L2):
    for e1 in L1:
        matched=False
        for e2 in L2:
            if e1==e2:
                matched=True
                break
        if not matched:
            return False
    return True
#Complexity is O(n^2)
def intersect(L1,L2):
    tmp=[]
    for e1 in L1:
        for e2 in L2:
            if e1==e2:
                tmp.append(e1)
    res=[]
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
#Complexity is O(n^2)
def g(n):
    x=0
    for i in range(n):
        for j in range(n):
            x+=1
        return x
"""
    Computes n^2 very inefficiently
    When dealing with nested loop,look at the ranges
    Nested loops each iterating n times.
"""