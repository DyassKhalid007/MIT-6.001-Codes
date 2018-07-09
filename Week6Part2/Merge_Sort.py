# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 00:44:08 2018

@author: Dyass
"""
"""
    Topics:
        Merge Sort
"""
"""
    Merge Sort:
        Use a divide and conquer approach.
        1:If a list is of length 0 or 1 already sorted
        2:If list has more than one element,split into two lists,
          and sort each
        3:Merge sorted sublists:
            1:Look at first element of each,move smaller to end of the
            result
            2:When one lists empty just copy rest of the other list
"""
def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left)and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
def merge_sort(L):
#    print(L)
    if(len(L)<2):
        return L[:]
    else:
        
        middle=len(L)//2
        left=merge_sort(L[:middle])
        right=merge_sort(L[middle:])
        return merge(left,right)
L=[99,1,0]
print(merge_sort(L))
            