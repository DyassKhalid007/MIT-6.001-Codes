# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 12:17:38 2018

@author: Dyass
"""
"""
    Topics:
        Classes of Tests
"""
"""
    Set yourself up for easy testiing and debugging:
        From the start,design code to ease this part
        
        Break problems into modules that can be tested and
        debugged immediately
        
        Document Constraints on modules
            What do you think the input to be?the output to be
            
        Document assumptions behind code design
"""
"""
    When are you ready to test:
        Ensure code runs
            remove syntax errors
            remove static semantic errors
            Python interpreter can usually find these for you
        have a set of expected results
            an input set
            for each input the expected output
"""
"""
    Classes of Tests:
        Unit testing:
            Validate each piece of program
            Testing each function separately
        Regression Testing:
            Add tests for bugs as you find them in a function
            Catch reintroduced errors that were previously fixed
        Integration Testing:
            Does overall program work?
            Tend to rush to do this
"""
"""
    Testing Approaches:
        Intuition about natural boundaries to the problem
        def is_biggest(x,y):
                Assumes x and y are ints
                Returns True if y is less than x.,else false
            
            Can you come up with some natural partitions
        If no natural partition,might do random testing
            Probability that the code is correct increases with more tests
            better options below
        Black box testing:
            Explore paths through specification
        Glass Box testing:
            Explore paths through code
"""
"""
    Black Box Testing:
        Designed without looking at the code
        Can be done by someone other than the implementer to avoid
        some implementer biases
        Testing can be reused if implementation changes
        Paths through specification:
            Build test cases in different natural space partitions
            Also consider the boundary conditions(empty lists,singleton,large.small numbers)
"""
"""Glass Box Testing:
        Use code directly to guid design of test cases
        Called path-complete if every potential path through code is tested
        at least once
        What are some drawbacks of this type of testing?
            Can go through loops arbitrary many times
            missing paths
        Guidelines:
            Branches
            for loops
            while loops
"""

            