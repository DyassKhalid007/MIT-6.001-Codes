# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 18:53:18 2018

@author: Dyass
"""
"""
    Topics:
        Analyzing More Complexity
"""
"""
    Exponential Complexity:
        Recursive functions where more than one
        recursive call for each size of problem:
            Towers of Hanoi
        Many important problems are inherenlty exponential:
            unfortunate as cost can be high
            will lead us to consider approximate solutions
            more quickly.
"""
def genSubsets(L):
    if len(L)==0:
        return [[]]
    smaller=genSubsets(L[:-1])
    extra=L[-1:]
    new=[]
    for small in smaller:
        new.append(small+extra)
    return smaller+new
