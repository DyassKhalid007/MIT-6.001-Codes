# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:43:01 2018

@author: Dyass
"""
"""
    Define your own types:
        Use the class keyword to define a new type
        
        class Coordinate(object):
            <define attributes here>
        Similar to def,indent code to indicate
        which statements are part of the class definitions
        
        The word object means that Coordinates is a python
        object and inherits all its attributes.
            Coordinates is a subclass of object
            Objects is a superclass of coordinate.
"""
"""Example of coordinate class"""
#class Coordinate(object):
#    #<define attributes here>
"""
    What are attributes?:
        Data and procedures that belong to the class
        Data attributes:
            Think of data as other objects that make up the class
            for example a coordinate is made up of two numbers
        Procedural attributes(methods):
            Think of methods as functions that only work with this class
            For example you can define a distance between two coordinate objects
            but there is no meaning to a distance between two list objects.
"""
"""
    Defining how to create an instance of the class:
        First have to define how to create an instance of object.
        Use a special method called _init_ to initialize some data attributes
            class Coordinate(object):
                def __init__(self,x,y):
                    self.x=x
                    self.y=y
"""
"""Example of a coordinate class"""
#class Coordinate(object):
#    def __init__(self,x,y):#This is a double underscore
#        self.x=x
#        self.y=y
#c=Coordinate(3,4)
#origin=Coordinate(0,0)
#print(c.x,c.y)
#Argument for self is automatically supplied
#by python
"""
    Data attributes of an instance are called instance variables.
    Dont provide argument for self.Python does that automatically
"""
                    
