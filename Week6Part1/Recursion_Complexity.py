# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 19:16:39 2018

@author: Dyass
"""
"""
    Topics:
        Recursion Complexity
"""
"""Tricky Complexity Example"""
def h(n):
    answer=0
    s=str(n)
    for c in s:
        answer+=int(c)
    return answer
#Complexity is log(n)
"""Complexity of Iterative Fibonacci"""
def fib_iter(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fib_i=0
        fib_ii=1
        for i in range(n-1):
            tmp=fib_i
            fib_i=fib_ii
            fib_ii=tmp+fib_i
        return fib_ii
#Complexity is O(n)
"""Complexity of Recursive Fibonacci"""
def fib_recur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_recur(n-1)+fib_recur(n-1)
#complexity is O(2^n)
"""Example when the input is a list"""
def sum_list(L):
    total=0
    for e in L:
        total+=total
    return total
#complexity is O(len(L))