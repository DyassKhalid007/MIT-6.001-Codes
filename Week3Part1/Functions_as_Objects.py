# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:31:50 2018

@author: Dyass
"""
"""
    Functions as Objects:
        Have Types
        Can be elements of data sructures like lists
        Can appear in expressions:
            as part of an assignment statement
            as an argument to a function
        Particularly useful to use functions as arguments
        when coupled with lists:
            aka higher order programming
"""
"""Example of applying functions to a list"""
#def fact(x):
#    if(x==1):
#        return 1
#    else:
#        return x*fact(x-1)
#def applyToEach(L,f):
#    for i in range(len(L)):
#        L[i]=f(L[i])
#L=[1,-2,3.4]
#applyToEach(L,abs)
#print(L)
#applyToEach(L,int)
#print(L)
#applyToEach(L,fact)
#print(L)
"""Example of list of functions"""
#def applyFuns(L,x):
#    for f in L:
#        print(f(x))
#applyFuns([abs,int,fact],4)
"""
    Generalization of HOPS:
        Python provides a general purpose HOP,map
        
        Simple form-a unary function and a collection of 
        suitable arguments:
            map(abs,[1,-2,3,-4])
"""
"""Example of map"""
#L=[1,2,-4,-99,0]
#for e in map(abs,L):
#    print(e)
"""Example of a general form of an n-ary functions and n collection of arguments"""
#L1=[1,28,36]
#L2=[2,57,9]
#for e in map(min,L1,L2):
#    print(e)




