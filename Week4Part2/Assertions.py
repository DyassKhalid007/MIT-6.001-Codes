# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 22:11:04 2018

@author: Dyass
"""
"""
    Topics:
        Assertions
"""
"""
    Assertions:
        Want to be sure that assumptions on state
        of computation are as expected.
        
        Use an assert statement to raise an AssertError
        exception if assumptions are not meet.
        
        an example of good defensive programming.
"""
def avg(grades):
    assert not len(grades)==0,'no grades'
    return sum(grades)/len(grades)
avg([])
"""
    Assertions as Defensive Programming:
        Assertions don't allow a programmer to control
        response to unexpected condition.
        
        Ensure that execution halts whenever an expected
        condition is not met.
        
        Typically used to check inputs to function procedures,
        but can be used anywhere.
        
        Can be used to check inputs to functions procedures,
        but can be used anywhere.
        
        Can be used to check outputs of a function to avoid
        propagating bad values.
        
        Can make it easier to locate a source of bug.
"""