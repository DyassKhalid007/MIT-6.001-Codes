# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 23:38:08 2018

@author: Dyass
"""

"""
    Topics:
        Selection Sort
"""
def selection_sort(L):
    suffixSt=0
    while suffixSt!=len(L):
        for i in range(suffixSt,len(L)):
            if L[i]<L[suffixSt]:
                L[suffixSt],L[i]=L[i],L[suffixSt]
        suffixSt+=1
    return L
L=[99,1,3,111,20,4,100]
print(selection_sort(L))
#Complexity is O(n^2)
                
            