# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:40:14 2018

@author: Dyass Khalid(20-10-0004)
"""

"""Topics:
    Control Flow
"""
"""
    Conditional:
        The simplest branching statement is a conditional.
        A test that evaluates to True or False.
        A block of code to execute if the test is true.
        An optional block of code to execute if the test
        is false.
"""
#x=9
#if(x==9):
#    print("Value of x:"+str(x))
#else:
#    print("Value is not 9")

"""
    Comparision operators on Int's and Float's:
        i>j
        i>=j
        i<j
        i<=j
        i==j  equality test evaluates to true if the condition is true
        i!=j  inequality test evaluates to true if the condition is true
"""
#i=6;
#j=9;
#print(i>j)#print False
#print(i>=j)#print False
#print(i<j)#print True
#print(i<=j)#print True
#print(i==j)#print False
#print(i!=j)#print True
"""
    Logic Operations on Bools:
        not a:True if a is False
              False if a is True
        a and b:True if both are true
        a or b: True if either is true or both are true
"""
"""Example of not a"""
#a=True
#print(not a)#print False
#b=False
#print(not b)#print True
"""Example of a and b"""
#a=True
#b=True
#if(a and b):
#    print("Both are true so the condition is evaluated")#This will be evaluated
#else:
#    print("Either condition is false")
#c=True
#d=False
#if(c and d):
#    print("If both are true than this will be evaluated")
#else:
#    print("If either is false or both are false than this condition will be evaluated")
"""Example of a or b"""
#a=True
#b=False
#if(a or b):
#    print("Either is true or both are true")
#else:
#    print("Both are false so this will be evaluated")
"""
    Simple Conditional:
        if<condition>:
            <expression>
            <expression>
"""
"""Example of simple conditional"""
#a=9
#if(a==9):
#    print("Value of a:"+str(a))
"""
    Type 2 Conditional:
        if<condition>:
            <expression>
            <expression>
        elif<condition>:
            <expression>
            <expression>
"""
#b=int(input("Enter a number:"))
#if(b==8):
#    print("Value of b is:"+str(b))
#elif(b!=8):
#    print("Value of b is not 8.")
"""
    Type 3 Conditional:
        if<condition>:
            <expression>
            <expression>
        elif<condition>:
            <expression>
            <expression>
        else:
            <expression>
            <expression>
"""
#a=int(input("Enter a number:"))
#if(a>9):
#    print("Value of a is greater than 9")
#elif(a<6):
#    print("Value of a is less than 6")
#else:
#    print("Value of a is between 9 and 6 exclusive")
"""
    Control using while loop:
        while<condition>:
            <expression>
            <expression>
        <condition> evaluates to a boolean.
        If <condition> is True, do all the steps in the while code 
        block.
        Check the <condition> again.
        Repeat untill <condition> is False.
"""
"""Example of a while loop"""
#n=0
#while(n<50):
#    print(n)
#    n+=1
"""
    Control using a for loop:
        for<variable> in range(<some_num>):
            <expression>
            <expression>
        Each time through the loop, the variable takes a value.
        First time the variable starts at the smallest value
        Next time the variable gets the previous value plus 1.
        Range returns a sequence of integers starting at 0 to argument of range minus 1
        Range(start,stop,step):
            Default values are start=0 and step=1 and are optional.
            Loop until the value is stop minus 1.
"""
"""Example of for and range function"""
#for i in range(10):
#    print(i)#print 0 to 10 on a new line
#for i in range(-1):
#    print(i)#will not print anything since range starts from 0
"""Example of for and range function when the starting value is not 0"""
#my_sum=0
#for i in range(7,10):
#    my_sum+=i
#print(my_sum)#print 7+8+9=24
"""Example of for and range function when there is starting,stopping and step size"""
#for i in range(0,10,2):
#    print(i)#should print 0,2,4,6,8 each on a new line
"""
    Break Statement:
        Immediately exits whatever loop it is in.
        Skips remaining expression in code block.
"""
"""Example of break statement in a for loop to find the first odd number starting from 10"""
#odd=0
#for i in range(10,20):
#    if i%2!=0:
#        odd=i
#        break
#print(odd)#will print 11
"""For loop vs While loop:
    For Loop:
        Known number of iterations.
        Can end early via break.
        Uses a counter.
        Can re-write a for loop using a while loop.
    While loop:
        Unbounded number of iterations.
        Can end early via break.
        Can use a counter but must initialize before loop and increment it inside
        the loop.
        May not be able to re-write a while loop using a for loop.
"""

    



        
    

    


        