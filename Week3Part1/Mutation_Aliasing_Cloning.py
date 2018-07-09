# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:26:02 2018

@author: Dyass
"""
"""
    Topics:
        Mutation
        Aliasing
        Cloning
"""
"""
    Lists in memory:
        Lists are mutable
        
        Behave differently than immutable types
        
        Is an object in memory
        
        Variable name point to object
        
        Any variable pointing to that object
        is affected.
        
        Key phrase to keep in mind when working with
        lists is side effects.
"""
"""Example of aliases"""
#warm=['red','yellow','orange']
#hot=warm
#print(hot)
#hot.append('pink')
#print(hot)
#print(warm)
#see how mutation is occuring through aliases
"""
    Print is not ==:
        If two lists print the same thing. does not mean they
        are the same structure
        
        Can test by mutating one and checking
"""
cool=['blue','green','grey']
chil=['blue','green','grey']
#The lists point to different structures
#but they have same values
#print(cool)
#print(chil)
#chil[2]='blue'
#print(cool)
#print(chil)
#since they print different things they are different objects
"""
    Cloning a list:
        Create a new list and copy element
        using chill=cool[:]
"""
#cool=['blue','green','grey']
#chill=cool[:]#creates a new copy 
##Both point to dfferent structures
#chill.append('black')
#print(chill)
#print(cool)
##see the print to check the result
"""
    Sorting Lists:
        Calling sort() mutates the list,it returns nothing
        
        Calling sorted() does not mutate list, must assign result
        to a variable
"""
#warm=["red","yellow","orange"]
#sortedwarm=warm.sort()#sort function returns none so none is assigned to it
#print(warm)
#print(sortedwarm)#will print None
#
#cool=['grey','green','blue']
#sortedcool=sorted(cool)#sorted return a new sorted list
#print(cool)
#print(sortedcool)#will print the sorted list
"""
    Lists of lists of lists of...:
        Can have nested lists
        
        Side effects still possible after mutation
"""
#warm=['yellow','orange']
#hot=['red']
#brightcolors=[warm]
#print(brightcolors)#list of list
#brightcolors.append(hot)
#print(brightcolors)#now hot is also added
#hot.append("pink")
#print(hot)
#print(brightcolors)#why>Pink because of aliases sideffects
#print(hot+warm)
#print(hot)#nothing changed with concatenation 


