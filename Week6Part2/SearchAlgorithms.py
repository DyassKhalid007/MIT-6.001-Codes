# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 21:37:26 2018

@author: Dyass
"""
"""
    Topics:
        Search Algorithms
"""
"""
    Search Algorithms:
        Method for finding an item or group
        of items with specific properies within
        a collection of items.
        
        Collection could be implicit.
            Example:
                Find square root as a search problem:
                    Exhaustive ennumeration
                    Bisection Search
                    Newton Raphson
        Collection could be explicit:
            example-is a student record in a stored
            collection of data?
"""
"""
    Search Algortihms:
        Linear Search:
            Brute force search
            List does not have to be sorted
        Bisection Search:
            List must be sorted to give correct answer
            Will see two different implementation of the 
            algorithm
"""
"""Linear Search on Unsorted List"""
def linear_search(L,e):
    found=False
    for i in range(len(L)):
        if e==L[i]:
            found=True
    return found
#must look through all elements
#O(len(L))
#Constant time list acess
    
        