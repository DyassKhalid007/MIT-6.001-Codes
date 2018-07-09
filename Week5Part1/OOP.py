# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:14:25 2018

@author: Dyass
"""
"""
    Topics:
        Object Oriented Programming
"""
"""
    Objects:
        Python supports many different kinds of data
        1234
        3.14159
        "Hello"
        [1,5,7,11,13]
        {"CA":"California,"MA":"Massachusetts"}
        Each is an instance of an object and every object has:
            a type
            an internal data representation
            a set of procedures for interaction with the object
        Each instance is a particular type of object:
            1234 is an instance of an int
            a="hello"
            a is an instance of a string
"""
"""
    Everything in python is an object and has a type
    Objects are data abstraction that capture:
        internal representation through data attributes
        interface for interacting with object through
        methods,defines behaviour but hides the implementation
    Create new instance of objects
    Can destroy objects:
        explicitly using del or just forget about them
        Python system will reclaim destroyed or inacessible objects
        -called garbage collection.
"""
"""
    Creating and using your own objects with classes:
        Make a distinction between creating a class and using
        an instance of the class.
        Creating the class involves:
            defining the class name
            defining the class attributes
            for example someone wrote code to implement a list
            class.
        Using the class involves:
            creating new instances of objects
            doing operations on the instances
            for example L=[1,2] and len(L)
"""
"""
    Advantages of OOP:
        Bundle data into packages together with procedures
        that work on them through well defined interfaces
        Divide and conquer development:
            implement and test behaviour of each class separately
            increased modularity reduces complexity
        Classes make it easy to reuse code:
            Many python modules defines new classes
            Each class has a separate environment(no collision on functions names)
            Inheritance allows subclasses to redefine or extend a selected subset of a 
            superclass' behavior.
"""
            
    