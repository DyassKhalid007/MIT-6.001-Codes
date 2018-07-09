# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:17:25 2018

@author: Dyass
"""

"""
    Topics:
        Recursion:
            A way to design solutions to problem by
            divide and conquer or decrease and conquer
            
            A programming technique where a function calls
            itself
            
            in programming, goal is to not have an infinite recursion
            must have one or more base cases that are easy to solve
            
            must solve the same problem on some other input with the goal
            pf simplifying the larger problem input 
            
"""
"""
    Iterative Algorithms so far:
        Looping constructs(while and for loops)lead tp iterative
        algorithms
        
        can recapture computation in a set of state variables
        that update on each interation through loop
        
"""
"""Multiplication-Iterative Solution"""
#def mult_iter(a,b):
#    result=0
#    while b>0:
#        result+=a
#        b-=1
#    return result
#print(mult_iter(7,4))
"""Multiplication-Recursive Solution"""
#def mult(a,b):
#    if(b==1):
#        return a
#    else:
#        return a+mult(a,b-1)
#print(mult(3,4))
#print(mult(8,4))
"""Factorial Function Recursive"""
#def factorial(a):
#    if(a==1):
#        return 1
#    else:
#        return a*factorial(a-1)
#print(factorial(5))
"""Factorial Function Iterative"""
#def factorial_iterative(a):
#    answer=1
#    while(a>1):
#        answer*=a
#        a-=1
#    return answer
#print(factorial_iterative(4))
#print(factorial_iterative(100))
"""
    Some Observations:
        Each recursive call to a function
        creates its own scope/environment
        
        Binding of variables in a scope is not
        changed by recursive call
        
        Flow of control passes back to previous
        scope once function call returns value
"""

"""Recursive Power Calculation"""
#def recurPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
# 
#    returns: int or float, base^exp
#    '''
#    # Your code here
#    if exp==0:
#        return 1
#    else:
#        return base*recurPower(base,exp-1)
"""Iterative Power Calculation"""
#def iterPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
# 
#    returns: int or float, base^exp
#    '''
#    # Your code here
#    ans=1;
#    while exp>0:
#        ans*=base
#        exp-=1
#    return ans


        