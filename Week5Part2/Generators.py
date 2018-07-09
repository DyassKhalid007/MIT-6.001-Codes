# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:21:51 2018

@author: Dyass
"""

"""
    Topics:
        Generator
"""
"""
    Any procedure or method with yield statement
    is called a generator
    def genTest():
        yield 1
        yield 2
"""
def genTest():
    yield 1
    yield 2
#print(genTest())#see console it is agenerator object
"""
    Generators have a next() method which starts/resumes
    execution of the procedure.Inside of generator:
        Yield suspends execution and returns a value.
        Returning from a generator raises a StopIteration
        exception
"""
#foo=genTest()
#print(foo.__next__())
#print(foo.__next__())
#print(foo.__next__())#stop iteration exception
"""
    Use of generators in loops:
        Can use a generator inside a looping structure
        as it will continue until it gets a StopIteration
        exception:
            for n in genTest():
                print(i)
"""
#for n in genTest():
#    print(n)
"""Fibonaci Numbers Example"""
def genFib():
    fibn_1=1#fib(n-1)
    fibn_2=0#fib(n-2)
    while True:
        #fib(n)=fib(n-1)+fib(n-2)
        nextt=fibn_1+fibn_2
        yield nextt
        fibn_2=fibn_1
        fibn_1=nextt
fib=genFib()
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
"""
    Why Generators:
        Generators seperates the concept of computing a very
        long sequence of objects,from the actual process of computing
        them explicitly.
        
        Allows one to generate each new objects as needed as
        part of another computation(rather than computing
        a very long sequence only to throw most of it away
        while you do something on an element,then repeating the
        process)
        
        Have already seen this idea in range
"""

        