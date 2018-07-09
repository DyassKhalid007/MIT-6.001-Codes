# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 18:00:10 2018

a@uthor: Dyass
"""

"""
    Test File
"""
"""
x=15
guess=0
epsilon=0.01 #the error 
increment=0.001 #the number of steps 
num_guesses=0
while abs(guess**2-x)>=epsilon and guess<=x:
    num_guesses+=1
    guess+=increment
print("Number of guesses are:",num_guesses)
if abs(guess**2-x)>=epsilon:
    print("Method failed to find the square root")
else:
    print(guess,"is square root of,",x)
"""
"""
    Bisection search to compute square root
    x=25.0
high=x
low=1.0
guess=(high+low)/2.0
epsilon=0.00001
num_guesses=0
while abs(guess**2-x)>=epsilon:
    num_guesses+=1
    if guess**2>x:
        high=guess
    else:
        low=guess
    guess=(low+high)/2.0
print("Number of guesses are:",num_guesses)
if abs(guess**2-x)>=epsilon:
    print("Method failed to find the square root")
else:
    print(guess,"is square root of,",x)
"""
"""
    Newton-Raphson Method
    x=54
guess=x/2.0
num_guesses=0
increment=0.001
while abs(guess**2-x)>=epsilon:
    num_guesses+=1
    guess=guess-(guess**2-x)/(2*guess)
print("Number of guesses are:",num_guesses)
print(guess,"is square root of",x)
"""


    
    
    