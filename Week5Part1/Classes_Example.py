# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:12:32 2018

@author: Dyass
"""
"""
    Topics:
        Fractions
"""
"""
    Create a new type to represent number as a fraction
    Internal representation is two integers
        numerator
        denominator
    Interface a.k.a methods a.k.a how to interact with
    fraction objects:
        print representation
        add,dubtract
        convert to a float
"""
#class fraction(object):
#    def __init__(self,numer,denom):
#        self.numer=numer
#        self.denom=denom
#    def __str__(self):
#        return str(self.numer)+"/"+str(self.denom)
#    def getNumer(self):#getter function
#        return self.numer
#    def getDenom(self):#getter function
#        return self.denom
#    def __add__(self,other):
#        numerNew=self.getNumer()*other.getDenom()+other.getNumer()*self.getDenom()
#        denomNew=self.getDenom()*other.getDenom()
#        return fraction(numerNew,denomNew)
#    def __sub__(self,other):
#        numerNew=self.getNumer()*other.getDenom()-other.getNumer()*self.getDenom()
#        denomNew=self.getDenom()*other.getDenom()
#        return fraction(numerNew,denomNew)
#    def convert(self):
#        return self.getNumer()/self.getDenom()
#oneHalf=fraction(1,2)
#twoThirds=fraction(2,3)
#print(oneHalf)
#print(twoThirds)
#print(oneHalf.getNumer())
#print(oneHalf.getDenom())
#new=oneHalf+twoThirds
#print(new)
#threeQuarters=fraction(3,4)
#print(threeQuarters)
#secondNew=twoThirds-threeQuarters
#print(secondNew)
#print(secondNew.convert())
"""
    Example set of integers:
        Create a new type to represent a collection of
        integers:
            initially the set is empty
            a particular integer appears only once in a set:
                representation invariant enforced by the code
        internal data representation:
            use a list to store the elements of a set
        interface:
            insert(e) insert integer e into set if not there
            member(e) return True if integer e is in set else False
            remove(e)-remove integer e from set,error if not present
"""
#class intSet(object):
#    def __init__(self):
#        self.vals=[]
#    def insert(self,e):
#        if e not in self.vals:
#            self.vals.append(e)
#    def member(self,e):
#        return e in self.vals
#    def remove(self,e):
#        try:
#            self.vals.remove(e)
#        except:
#            raise ValueError(str(e)+' not found')
#    def __str__(self):
#        self.vals.sort()
#        result=""
#        for e in self.vals:
#            result=result+str(e)+","
#        return "{"+result[:-1]+"}"
#s=intSet()
#print(s)
#s.insert(3)
#s.insert(4)
#s.insert(99)
#print(s)
#print(s.member(3))
#print(s.member(6))
#print(s.member(94))
#s.remove(3)
#print(s)
#s.insert(6)
#print(s)
#s.remove(100)
#print(s)

 
        
