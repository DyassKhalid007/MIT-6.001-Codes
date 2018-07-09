# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 11:40:10 2018

@author: Dyass
"""

"""
    Topics:
        Program Efficency
"""
"""
    Want to understand efficiency of
    Programs:
        Computers are fast and getting faster-so maybe
        efficient programs don't matter?
            But data sets can be very large
            Thus,simple solutions may simply not scale
            with size in acceptable manner
        So how could we decide which option for program is most
        efficienct?
        
        Seperate time and space efficiency of a program
        
        Tradeoff between them-will focus on time efficiency
"""
"""
    Challenges in understanding efficiency of a solution
    to a computational problem:
        A program can be implemented in many different ways
        You can solve a problem using only a handful of different
        algorithms.
        Would like to separate choices of implementations from
        choices of more abstract algorithm.
"""
"""
    How to evaluate efficiency of programs:
        Measure with a timer
        Count the operations
        Abstract notion of order of growth
"""
"""
    Timing a program:
        Use time module
        Recall the importing means to bring in that class
        into your own file.
        Start a clock
        Call function
        Stop Clock
"""
import time
def c_to_f(c):
    return c*9/5+32
t0=time.clock()
c_to_f(100000)
t1=time.clock()-t0        
print("t=",t0,":",t1,"s,")
"""
    Timing programs is inconsistent
    Goal:To evaluate different algorithms
    Running time varies between algorithms.
"""
"""
    Counting Operations:
        Assume the steps take constant time:
            Mathematical operations
            Comparisons
            Assignments
            Accesing objects in memory
        Then count the number of operations
        executed as function of size of innput
"""
def c_to_f(c):
    return c*9.0/5+32
def mysum(x):
    total=0
    for i in range(x+1):
        total+=i
    return total
"""
    Counting operations is better but still...
        count depends on algorithm
        count depends on implementation
        count independent of computers
        no real definitions of which operations to count
        
        count varies for different inputs and can
        come up with a relationship between inputs and the
        count
"""
"""
    Still need abetter way:
        Timing and counting evaluate implementation
        timing evaluates machines
        want to evaluate algorithm
        want to evaluate scalability
        want to evaluate in terms of input size
"""
"""
    Need to chose which input to use to evaluate
    a function:
        Want to express efficiency in terms of input,so need
        to decide what your input is
        Could be an integer:
            mysum(x)
        Could be length of list:
            list_sum(L)
        you decide when multiple parameters to a function:
            search_for_elmt(L,e)
"""
"""
    Different inputs cahnge how the program runs:
        a function that searches for an element in a list:"""
def search(L,e):
    for i in L:
        if i==e:
            return True
    return False
"""
    When e is the first element in the list:Best Case
    When e is not in the list:Worst Case
    When look through half of the elements in 
    list:Average Case
    Want to meaure this in a general way
"""
"""
    Best,Average,Worst Cases:
        Suppose you are given a list L of some length len(L)
        Best Case:minimum running time over all possible inputs
        of a given size,len(L):
            constant for search_for_elmt
            first element in any list
        Average case:average running time over all possible inputs
        of a given size,len(L):
            practical measure
        Worst Case:Maximum running time over all possible inputs
        of a given size,len(L):
            Linear in length of list for search_for_elmt
            Must search entrie list and not find it
"""
"""
    Orders of growth:
        Goals:
            Want to evaluate program's efficiency when input
            is very big.
            Want to express the growth of programs's run time
            as input size grows.
            Want to put an upper bound on growth.
            Do not need to be precise:order of not exact growth
            We will look at largest factor in run time(which section of
            the program will take the longest time to run?)
"""
"""
    Types of orders of growth:
        Constant
        Linear
        Quadratic
        Logarithmic
        nlogn
        Exponential
"""
