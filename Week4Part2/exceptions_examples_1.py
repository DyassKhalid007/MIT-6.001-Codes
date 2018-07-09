# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:49:28 2018

@author: Dyass
"""

"""
    Topics:
        Exceptions Examples 1
"""
#while True:
#    try:
#        n=input("Please enter an integer")
#        n=int(n)
#        break
#    except ValueError:
#        print("Input not an integer:try again")
#print("Correct input as an integer")
##ValueError:Operands are okay but value is illegal
##TypeError:Operands are illegal
"""Example:Control Input"""
data=[]
file_name=input("Provide a name of a file of data")
try:
    fh=open(file_name,'r')
except IOError:
    print("cannot open",file_name)
else:
    for new in fh:
        if new!="\n":
            addIt=new[:-1].split(',')#remove trailing
            data.append(addIt)
finally:
    fh.close()#close file even if fail

