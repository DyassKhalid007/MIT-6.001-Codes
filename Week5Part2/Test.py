# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:17:52 2018

@author: Dyass
"""

def genPrimes():
    primes=2
    yield primes
    while(True):
        primes+=1
        for i in range(2,primes):
            if primes%i==0:
                break
        else:
            yield primes
p=genPrimes()
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())



        