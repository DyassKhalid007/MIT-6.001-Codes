# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:18:22 2018

@author: Dyass
"""

"""
    Topics:
        Why OOP
"""
"""
    The power of OOP:
        Bundle together objects that share:
            common attributes and
            procedures that operate on those attributes
        Use abstraction to make a distinction between how to
        implement an object vs how to use the object
        
        Build layers of object abstraction that inherit behaviors
        from other classes of objects
        
        Create our own classes of objects on top of python's
        basic classes
"""
"""
    Implementing the class versus Using the class:
        Write code from two different perspectives
        All class examples we have seen so far were numerical
        
        Implementing a new object type with a class:
            define the class
            define data attributes
            define methods
        Using the new object type in code:
            create instances of the object type
            do operations with them
"""
class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,age):
        self.age=age
    def set_name(self,name=""):
        self.name=name
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
myanimal=Animal(3)
print(myanimal)
myanimal.set_name("foobar")
print(myanimal)
print(myanimal.get_age())


