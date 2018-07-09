# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:00:52 2018

@author: Dyass
"""
"""
    Topics:
        Bisection Search
"""
"""Linear Search on Sorted List"""
def search(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i]>e:
            return False
    return False
#Complexity is O(len(L))
"""
    Use Bisection Search:
        Pick an index i that divides the list in half
        Ask if L[i]==e
        If not ask if L[i] is larger or smaller than e
        Depending on answer,search left or right hald of L
        for e
        
    A new version of divide and conquer algorithm:
        Break into smaller version of problems plus some
        single operations.
        Answer to smaller version is answer to orignal
        problem.
    Complexity is O(nlog(n))
"""
#def bisect_search(L,e):
#    if L==[]:
#        return False
#    elif len(L)==1:
#        return L[0]==e
#    else:
#        half=len(L)//2
#        if L[half]>e:
#            return bisect_search(L[:half],e)
#        else:
#            return bisect_search(L[half:],e)
"""Bisection Search Implementation 2->O(log(n))"""
#def bisect_search(L,e):
#    def bisect_search_helper(L,e,low,high):
#        if high==low:
#            return L[low]==e
#        mid=(low+high)//2
#        if L[mid]==e:
#            return True
#        elif L[mid]>e:
#            if low==mid:
#                return False
#            else:
#                return bisect_search(L,e,low,mid-1)
#        else:
#            return bisect_search(L,e,mid+1,high)
#    if len(L)==0:
#        return False
#    else:
#        return bisect_search_helper(L,e,0,len(L)-1)

        
