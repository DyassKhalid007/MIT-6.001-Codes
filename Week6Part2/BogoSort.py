# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:24:30 2018

@author: Dyass
"""
"""
    Topics:
        Bogo Sort
"""
import random
def bogo_sort(L):
    while L != sorted(L):
        random.shuffle(L)
    return L
L = [9,7,5,3,1,0,99,1,2,4]
print(bogo_sort(L))