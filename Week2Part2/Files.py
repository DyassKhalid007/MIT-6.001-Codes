# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:14:01 2018

@author: Dyass
"""
"""
    Topics:
        Files
"""
"""
    Modules and Files:
        Have assumed that all our code is stored in one file
        
        Cumbersome for large collections of code, or for code that
        should be used by many different other pieces of programming
        
        a module is a .py file containing a collection Python definitions
        and statements
"""
"""
    Example of Module:
        The file circle.py contains
        pi=3.14159
        def area(radius):
            return pi*(radius**2)
        def circumference(radius):
            return 2*pi*radius
        
        Then we can import and use this module
        
        import circle
        pi=3
        print(pi)
        print(circle.pi)
        print(circle.area(3))
        print(circle.circumference(3))
        
        Results in the following being printed:
            3
            3.14159
            28.27431
            18.849539999999998
"""
"""
    Other importing:
        If we don't want to refer to functions and variables by their module
        and names don't collide with other bindings then we can use:
            
            from circle import *
            
            #This means form the module circle import everything
            
            print(pi)
            print(area(3))
            
            This has the effect of creating bindings within the current scope
            for all objects defined within circle
            
            Statements within a module are executed only the first
            time a module is imported
"""
"""
    How to write to a file:
        nameHandle=open("kids","w")
        for i in range(2):
            name=input("Enter name:")
            nameHandle.write(name+'\')
        nameHandle.close()
"""
"""
    How to open a file:
        nameHandle=open("kids","r")
        for line in nameHandle:
            print(line)
        nameHandle.close()
"""
"""Example of writing to a file"""
#nameHandle=open("DyassInfo","w")
#for i in range(2):
#    name=input("Enter your name")
#    nameHandle.write(name+'\n')
#nameHandle.close()
"""Example of reading to a file"""
#nameHandle=open("DyassInfo","r")
#for line in nameHandle:
#    print(line)
#nameHandle.close()
"""Example of importing from a file named: Dyass.py"""
#import Dyass
#print(Dyass.pi)
#print(Dyass.area(103))
#print(Dyass.circumference(1))
"""Example of importing everything from a module and without using the module name"""
#from Dyass import *
#print(area(3))
#print(pi)
#print(circumference(2))

