# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:27:41 2018

@author: Dyass
"""
"""
    Measuring Order of Growth:
        Big OH Notation:
            Big Oh measures an upper bound on the
            asymptotic growth,often called order of growth.
            
            Big Oh or O() is used to describe worst case.
                Worst case occurs often and is the bottleneck
                when a program runs
                
                Express rate of growth of program relative to the
                input size.
                
                Evaluate algorithm not machine or implementation.
                
"""
"""Example"""
def fact_iter(n):
    answer=1
    while n>1:
        answer*=n
        n-=1
    return answer
"""
    Computes factorial
    Number of steps
    Worst case asymptotic complexity:
        Ignore additive constants
        Ignore multiplicative constants
    1+5n+1 steps in fact_iter
    O(n) ignoring additive and multiplcative constants.
"""
"""
    Simplification Examples:
        Drops constants and multiplicative factors.
        Focus on dominant terms:
            n^2+2n+2->O(n^2)
            n^2+1000n+3^1000->O(n^2)
            log(n)+n+4->O(n)
            0.0001*n*log(n)+300n->nlog(n)
            2*n^30+3^n->O(3^n)
"""
"""
    Analyzing Programs and Their Complexity:
        Combine complexity classes:
            Analyze statements inside functions
            Apply some rules,focus on dominant terms
        Law of addition for O():
            Used with sequential statements
            O(f(n))+O(g(n)) is O(f(n)+g(n))
            for example:
                for i in range(n):
                print('a')
                for j in range(n*n):
                print(b)
        The order is O(n)+O(n^2)=O(n^2+n)
        =O(n^2)
        
        Law of multiplication for O():
            Used with nested statements/loops:
                O(f(n))+O(g(n)) is O(f(n)*g(n))
                for example:
                    for i in range(n):
                        for j in range(n):
                            print('a')
                is O(n)*O(n)=O(n*n) because the outer loop goes n
                times and inner loop goes n times for every outer loop iter
"""

"""