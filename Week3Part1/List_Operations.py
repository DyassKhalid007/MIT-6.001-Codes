# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:41:11 2018

@author: Dyass
"""
"""
    Topics:
        Operations on Lists:
            Add:
                Add elements to end of list with L.append(element)
                
                Mutates the list
"""
"""Example of append function"""
#L=[1,2,3,4]
#L.append(99)
#print(L)#99 is added to the end of the list
"""
    What is this dot in L.append(element):
        Lists are python objects. Everything in python is an object
        
        Objects have data
        
        Objects have methods and functions
        
        Access this information by object.do_something()
        
"""
"""
    How to combine lists together:
        Use concatenation, + operator
"""
"""Example of cincatenation of lists"""
#L1=[1,2,3]
#L2=[4,5,6]
#L3=L1+L2
#print(L3)
"""
    How to mutate list with L.extend(some_list)
"""
"""Example of mutating list with L.extend(some_list)"""
#L=[1,2,3,4,5]
#L.extend([5,6,7])
#print(L)
"""
    Operations on Lists-Remove:
        Delete elements at a specific index del(L[index])
        
        Remove elements at end of list with L.pop(),returns the removed element
        
        Remove a specific set of element with L.remove(element):
            Looks for the element and remove it
            If element occurs multiple times,remove the first occurence
            If element not in the list,gives an error
"""
"""Example of Lists-Remove function"""
#L=[2,1,3,6,3,7,0]
#L.remove(2)
#print(L)
#L.remove(3)
#print(L)
#del(L[1])
#print(L)
#print(L.pop())
#print(L)
"""
    Convert strings to lists and back:
        Convert string to list with list(s),returns a list with every character
        form an element in L
        
        Can use s.split() to split a string on a character parameter, splits on
        spaces if called without a parameter
        
        Use "".join(L) to turn a list of characters into a string.Can give a character in
        quotes to add char between every element.
"""
"""Example of the strings to lists and back operations"""
#s="I <3 CS"
#print(list(s))
#print(s.split("<"))
#L=["a","b","c"]
#L2="".join(L)
#print(L2)
#L3="_".join(L)
#print(L3)
"""
    Other list operation:
        sort()
        sorted()
        reverse()
"""
"""Example of sorted,.sort and .reverse methods"""
#L=[9,6,0,3]
#print(sorted(L))#return sorted list,does not mutate L
#L.sort()
#print(L)#Mutates L=[0,3,6,9]
#L.reverse()
#print(L)#Mutates L=[9,6,3,0]
"""
    Bringing together Loops,functions,range and Lists:
        Range is a special procedure
        
        Returns something that behave like a tuple
        
        Does not generate the elements at once but it generates the first element
        and then provides an iteration method by which subsequent elements are generated
        
        range(5) is equivalent to tuple (0,1,2,3,4)
        
        range(2,6) is equivalent to tuple (2,3,4,5)
        
        range of(5,2,-1) is equivalent to tuple (5,4,3)
        
        When use range in a for loop ,what the loop variable iterates over behave like a list
        
        for var in range(5):
            <expression>
        behind the scenes gets converted to something that will behave like:
            for var in (0,1,2,3,4):
                <expression>
"""