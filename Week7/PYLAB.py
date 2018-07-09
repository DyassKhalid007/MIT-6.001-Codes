# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 03:06:28 2018

@author: Dyass
"""
"""
    Topics:
        Pylab
"""
"""
    Visualizing Results:
        Earlier saw examples of different orders of
        growth of procedures.
        Used graphs to provide an intuitive sense of differences
        Example of leveraging an existing library,rather than
        writing procedures from scratch.
        Python provides libraries:
            graphing
            numerical computation
            stochastic computation
        Want to explore idea of using existing library proedures to
        guid processing and exploration of data
"""
"""
    Using pylab:
        can import library into computing environment
            import pylab as plt
            allows me to reference any library procedure as 
            plt.<procName>
        
        provides acess to existing set of graphing/plotting procedures
        
        here will just show some simple examples;lots of additional information
        available in documentation associated with pylab
        
        will see many other examples and details of these ideas if you opt
        to take 6.002x
"""
import pylab as plt
"""
    Simple example:
        Basic function plots two lists as x and y values.
"""
mySamples=[]
myLinear=[]
myQuadratic=[]
myCubic=[]
myExponential=[]
for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
#To generate a plot call
plt.figure("Linear")
plt.xlabel("Sample Inputs")
plt.ylabel("Linear Function")
plt.plot(mySamples,myLinear)
#arguments are list of values(for now)
#list must be of same length
#calling function in ipython console
#will generate plots within that console
#calling function in a python console will
#a seperate window in which plot is displayed
plt.figure("Quadratic")
plt.xlabel("Sample Inputs")
plt.ylabel("Quadratic Fuction")
plt.plot(mySamples,myQuadratic)

plt.figure("Cubic")
plt.xlabel("Sample Inputs")
plt.ylabel("Cubic Function")
plt.plot(mySamples,myCubic)

plt.figure("Exponential")
plt.xlabel("Sample Inputs")
plt.ylabel("Exponential Function")
plt.plot(mySamples,myExponential)

#plt.figure("Quadratic")
#plt.ylabel("Hello")
"""Adding Titles and clearing windows"""
plt.figure("Linear")
plt.title("Linear")
plt.clf()

plt.figure("Quadratic")
plt.title("Quadratic")
plt.clf()

plt.figure("Cubic")
plt.title("Cubic")
plt.clf()

plt.figure("Exponential")
plt.title("Exponential")
plt.clf()