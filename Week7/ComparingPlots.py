# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 19:37:07 2018

@author: Dyass
"""

"""
    Topics:
        Comparing Plots
"""
"""
    Comparing Plots:
        Now suppose we would like to compare
        different plots.
        
        In particular,the scales on the graphs are
        very different.
        
        One option is to explicitly set limits on the 
        axis or axes
        
        A second option is to plot multiple functions on
        the same display
"""
import pylab as plt
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
#plt.figure("Lin")
#plt.clf()
#plt.ylim(0,1000)
#plt.plot(mySamples,myLinear)
#plt.figure("Quad")
#plt.clf()
#plt.ylim(0,1000)
#plt.plot(mySamples,myQuadratic)
#plt.figure("Lin")
#plt.title("Linear")
#plt.figure("Quad")
#plt.title("Quadratic")
"""Overlaying Plots"""
plt.figure("lin quad")
plt.clf()
plt.plot(mySamples,myLinear,'b-',label="Linear",linewidth=4.0)
plt.plot(mySamples,myQuadratic,'ro',label="Quadratic",linewidth=5.0)
plt.legend()

plt.figure("cube exp")
plt.clf()
plt.plot(mySamples,myCubic,'g^',label="Cubic",linewidth=2.0)
plt.plot(mySamples,myExponential,'r--',label="Exponential",linewidth=3.0)
plt.legend()

plt.figure("lin quad")
plt.title("Linear vs Quadratic")

plt.figure("cube exp")
plt.title("Cubic vs Exponential")
"""
    Controlling Display Parameters:
        Now suppose we want to control details of the display
        themselves.
        Examples:
            Changing color or style of data sets.
            Changing color of lines of display.
            Using subplots
"""