# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 00:09:19 2018

@author: Dyass
"""

"""
    Topics:
        Functions:
            Reusable piece of code.
            Characterisitcs:
                has a name
                has parameter(zero or more)
                has a body
"""
"""Example of a function to find if a number is even or not"""
def is_even(i):
    if i%2==0:
        return True
    else:
        return False
"""Example of a function to find if a number is odd or not"""
def is_odd(i):
    if i%2!=0:
        return True
    else:
        return False
x=int(input("Please enter a number:"))
print(is_even(x))
print(is_odd(x))