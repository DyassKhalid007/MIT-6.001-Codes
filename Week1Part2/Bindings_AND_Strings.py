# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
     Topics: Bindings
             Strings
"""
"""
    Variables are names to which we can assosiate
    values.
    Name should be descriptive,meaningful,helps you re-read the code
    and cannot be key-words.
    Value is information stored and can be updated"
    = is the assignment operator
"""
#x=2 #x has value 2
#print(x)
#x=x*x #x has value 4
#print(x)
#y=x+1 #y has value 5
#print(y)
"""Example of how swapping is done"""
#x=2
#y=5
#temp=x
#x=y
#y=temp
#print(x,y)
"""
    Strings are letters,special characters,spaces,digits.
    They are enclosed in quotation marks or single quotes"
    Concatenation of strings is possible with the + operator
    + is called as over-loaded operator
"""
#hi="hello"
#hp='hp'
#print(hi,hp)
"""Example of concateneation"""
#name="Eric"
#greet="hi"
#print(name+" "+greet)
"""Operations on strings:
    Concatenation
    Successive Concatenation
    Length of strings using len function
    String indexing starts with 0 not with 1
    String slicing is possible.
    string[i:j] will give string starting from inde i to j-1 index.
    Another variant is with step size string[i:j:k]. Here k represent the
    step size.
"""
"""Example of concateneation"""
#name="Eric"
#greet="hi"
#print(name+" "+greet)
"""Example of successive concatenation"""
#name='dyass'
#print(name*3)#here * is overloaded for string type
"""Example of length function"""
#name ="dyass"
#print(len(name))#spaces are also included
#name="dyass khalid"
#print(len(name))#should print 12 because of space
"""Example of string indexing"""
#name="dyass"
#print(name[0])
#print(name[-1])#print the last index i.e s
#print(name[5])#should print an error message of index out of range
"""Example of string slicing"""
#name="dyass khalid"
#print(name[0:8])#should print dyass k
#print(name[3:])#print from 3rd index to onward
#print(name[:5]) #print till 5-1 or j-1 index
"""Example of advanced string slicing with step size"""
#name="dyass khalid"
#print(name[0:8:2])#should print dask
#print(name[0:len(name)-1:3])#should print dskl


    

