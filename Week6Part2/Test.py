# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:43:52 2018

@author: Dyass
"""

def bubble_sort(L):
    swap=False
    while not swap:
        swap=True
        for i in range(1,len(L)):
            if L[i-1]>L[i]:
                swap=False
                L[i-1],L[i]=L[i],L[i-1]
    return L
def s_sort(L):
    suffix=0
    while suffix!=len(L):
        for i in range(suffix,len(L)):
            if L[i]<L[suffix]:
                L[suffix],L[i]=L[i],L[suffix]
        suffix+=1
    print(L)
