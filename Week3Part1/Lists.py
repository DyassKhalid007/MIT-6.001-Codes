# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 22:09:33 2018

@author: Dyass
"""
"""
    Topics:
        Lists:
            An ordered sequence of information, accessible by index.
            
            A list is denoted by square brackets.
            
            A list contain elements usually homogeneous i.e all integers
            but can contain mixed types (not common).
            
            List element can be changed so that list is mutable
"""
"""Example of lists"""
#a_list=[]#empty list
#b_list=[2,"a",4,True]#A hetrogeneous list
#L=[2,1,3] #A homogeneous list
#print(len(L))#evaluates to 3
#print(L[0])#evaluates to 2
#print(L[2]+1)#evaluates to 4
#print(L[3])#Invalid index gives an error
"""
    Use of variables to acess index:
        Index can bea variable or expression must evaluate to an int
"""
"""Example of accessing List elements by variable as an index"""
#L=[1,2,3]
#i=2
#print(L[i-1])#will print 2
"""
    Changigng elements in a list:
        Lists are mutable
        
        Assignning to an element at an index changes the value.
        
        L=[1,2,3]
        L[0]=5
        Now list is L=[5,2,3]
        Note that this is the same object
        
"""
"""Example of changing an elemnt by index"""
#L=[1,2,3]
#L[0]=3
#print(L)#evaluates to [3,2,3]
"""
    Iterating over a list:
        See the example below
"""
"""Example of iterating:Method 1"""
#L=[1,2,3,4,5]
#sum=0
#for ele in L:
#    sum+=ele
#print(sum)
"""Example of iterating:Mathod 2"""
#L=[1,2,3,4,5]
#sum=0
#for i in range(len(L)):
#    sum+=L[i]
#print(sum)
            

