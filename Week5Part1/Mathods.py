# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 12:57:45 2018

@author: Dyass
"""
"""
    Topics:
        Methods
"""
"""
    What is a Method:
        Procedural attribute,like a function
        that works only with class.
        Python always passes the actual objects as the first
        argument,convention is to use self as the name of the
        first argument of all methods.
        The "."operator is used to access any attribute:
            a data attribute of an object
            a method of an object
"""
"""
    Example of a method for the coordinate class"""
#class Coordinate(object):
#    def __init__(self,x,y):
#        self.x=x
#        self.y=y
#    def distance(self,other):
#        x_diff_sq=(self.x-other.x)**2
#        y_diff_sq=(self.y-other.y)**2
#        return (x_diff_sq+y_diff_sq)**0.5
#c=Coordinate(3,4)
#origin=Coordinate(0,0)
#print(c.distance(origin))
#print(Coordinate.distance(c,origin))
#The above two lines are same
"""
    Other than self and dot notation,methods behave
    just like functions(take params,do operations,return value)
"""
"""
    Print representation of an object:
        c=coordinate(3,4)
        print(c)
    uninformative print representation by default
    Define a __str__method for a class
    Python class the __str__method when used with
    print on your class object
    You choose what it does!Say that when we print a Coordinate Object
    ,we want to show:
        print(c)
        <3,4>
"""
class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def __sub__(self,other):
        return (self.x-other.x,self.y-other.y)
    
c=Coordinate(3,4)
origin=Coordinate(0,0)
#print(c)
"""
    Wrapping your head around types and classes:
        can ask for the type of an object instance:
            c=Coordinate(3,4)
            print(c)
            print(type(c))
        this makes sense since
            print(Coordinate,type(Coordinate))
        use isinstance()to chack if an object is a Coordinate:
            print(isinstance(c,Coordinate))
"""
#print(type(c))
#print(Coordinate,type(Coordinate))
#print(isinstance(c,Coordinate))
"""
    Special Operators:
        +,-,==,<,>,len(),print and many others
        like print,can overide these to work with your class
        define them with double underscore before/after:
            __add__(self,other)->self+other
            __sub__(self,other)->self-other
            __eq__(self,other)->self==other
            __it__(self,other)->self<other
            __len__(self)->len(self)
            __str__(self)->print(self)
            ... and others
"""
foo=c-origin
print(foo)