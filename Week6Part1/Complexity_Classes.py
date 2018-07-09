# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 17:05:28 2018

@author: Dyass
"""
"""
    Constant Complexity:
        Complexity:
            Independent of inputs.
            Very few interesting algorithms in this
            class but can often have pieces that fit this class.
            Can have loops or recursive calls but number of class
            or iterations are independent of size of input.
"""
"""
    Logarithmic Complexity:
        Complexity grows as log of size of one of its inputs.
        Example:
            bisection search
            binary search of a list
"""
"""Example of logarithmic complexity"""
def intToStr(i):
    digits='0123456789'
    if i==0:
        return '0'
    result=''
    while i>0:
        result=digits[i%10]+result
        i=i//10
    return result
"""
    Linear Complexity:
        Searching a list in sequence to see if an element is
        present.
        Add characters of a string,assumed to be composed
        of decimal digits.
"""
def addDigits(s):
    val=0#constant
    for c in s:
        val+=int(c)
    return val#constant
#Order of complexity is O(len(s))
def fact_iter(n):
    prod=1
    for i in range(1,n+1):
        prod*=i
    return prod
#Order of complexity is O(n)
def fact_recur(n):
    if n<=1:
        return 1
    else:
        return n*fact_recur(n-1)
#Order of complexity is O(n)




        
        