# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 12:31:39 2018

@author: Dyass
"""
"""
    Dictionary:
        so far,can store using seperate lists for
        every info
        names=['Ana','John','Denise','Katy']
        grade=['B','A+','A','A']
        course=['CS100','CS200','CS201','CS300']
        
        A seperate list for each item
        
        Each list must have the same length
        
        HOW TO UPDATE/RETRIVE STUDENT INFO:
            def get_grade(student,name_list,grade_list,course_list):
                i=name_list.index(student)
                grade=grade_list[i]
                course=course_list[i]
                return (course,grade)
        
        Messy if have a lot of different info to keep track of
        
        Must maintain many lists and pass them as arguments
        
        Must always use index using integers
        
        WHAT IS A BETTER AND CLEANER WAY:
            A DICTIONARY:
                nice to index item of interests directly(not always int)
                
                nice to use one data structure,no seperate lists
                
            A python Dictionary:
                store pairs of data:
                    key
                    value
            Syntax:
                my_dict={}#empty dictionary
                grades={'Ana':'B','John':'A+','Denise':'A','Katy':'A'}
                
""" 
"""Example of a dictionay"""
#my_dict={}#empty dictionary
#my_dict={'Dyass':'A','Farhan':'B-','Momin':'A-'}
"""
    Dictionary Lookup:
        Similar to indexing into a list
        
        Looks up the key
        
        Returns the value assosiated with the key
        
        If key isn't found,get an error
"""
"""Example of dictionary lookup"""
#grades={'Dyass':'A','Farhan':'B-','Momin':'A-'}
#print(grades['Dyass'])
#print(grades['Farhan'])
#print(grades['Momin'])
#print(grades['hi'])#evaluates to Key error
"""
    Dictionary Operations
"""
"""Example of adding an entry"""
grades={'Ana':'B','John':'A+','Denise':'A','Katy':'A'}
grades['Sylvan']='A'
print(grades)
"""Example of testing if a key is in dictionart"""
print('John' in grades)
print('Dyass' in grades)
"""Example of deleting an entry"""
del(grades['Ana'])
print(grades)
"""How to get all the keys of a dictionary"""
print(grades.keys())
"""How to get all the values of a dictionary"""
print(grades.values())
"""
    Dictionary Keys and Values:
        Values:
            Any type(immutable and mutable)
            can be duplicates
            dictionary values can be lists,even other dictionaries
        Keys:
            Must be unique
            Immutable type:
                Actually need an object that is hashable,but thinks of as immutables
                as all immutable types are hashable
            Careful with float type as a key
            No order to key or values
"""