# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:02:22 2018

@author: Dyass
"""

"""
    Topics:
        Tuples:
            An ordered sequence of elements,can mix element types
            
            Immutable,cannot change element values but can add new tuples
            
            represented with parenthesis
            
"""
"""Example of empty and new elements added to the tuple example"""
#te=()#empty tuple
#t=(2,"one",3)
#print(t[0])#will print the element at index 0
#print(t+(5,6))
#t=t+(5,6)#we can add new values to the tuple but cannot modify the existing ones
#print(t)
"""Example of slicing and changing values in a tuple"""
#t=(2,"one",3)
#print(t[1:2])#slice tuple evaluates to ("one",) The extra comma tells us that it is indeed a tuple
#print(t[1:3])#slice tuple evaluates to ("one",3)
#t[1]=4#will result in an error since tuples are immutable
"""Use of tuples to swap values"""
#x=2
#y=3
#te=(x,y)
#print(te)
#te=(y,x)
#print(te)
"""Use of tuple to return more than one value from the function"""
#def quotient_and_remainder(x,y):
#    quotient=x//y
#    remainder=x%y
#    return (quotient,remainder)
#(quot,rem)=quotient_and_remainder(9,3)
#print((quot,rem))
#"""Example of iterating over tuples"""
#tup=(1,("two",2),3,"four")
#for ele in tup:
#    print(ele) #will print the elements in a tuple on a new line
"""How to add a new string tuple and int tuple in an tuple"""
#tup=("one",2,"three",4)
#emp=()
"""How to iterate over a tuple"""
#for ele in tup:
#    emp+=(ele,)#see the epecific syntax here
#print(emp)
    



