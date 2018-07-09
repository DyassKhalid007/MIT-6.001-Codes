# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 18:25:17 2018

@author: Dyass
"""
"""
    Topics:
        Exceptions as contol flow
"""
"""
    Exceptions as Contol Flow:
        Don't return special value when an error
        occured and then check whether error value
        was returned
        
        Instead,raise an exception when unable to produce a
        result consistent with function's specification.
        
        raise <exceptionName>(<arguments>)
        raise ValueError("something is wrong")
"""
"""Example raising an exception"""
#def get_ratios(L1,L2):
#    ratios=[]
#    for index in range(len(L1)):
#        try:
#            ratios.append(L1[index]/float(L2[index]))
#        except ZeroDivisionError:
#            ratios.append(float('NaN'))
#        except:
#            raise ValueError('get_ratios called with bad arg')
#    return ratios 
#L1=[1,2,3,4]
#L2=[5,6,7,8]
#print(get_ratios(L1,L2))
#L3=[5,6,7]
##print(get_ratios(L1,L3))
#L4=[5,6,7,0]
#print(get_ratios(L1,L4))
"""
    Examples of Exceptions:
        Assume we are given a class list for a subject:each entry
        is a list of two parts:
            A list of first and last name for a student
            A list of grades of assignments.
"""
def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats 

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('No Grades Data')
        return 0.0

#test_grades=[[['peter','parker'],[80.0,70.0,85.0]],[['bruce','wayne'],[100.0,80.0,74.0]]]
#print(get_stats(test_grades))
test_grades1 = [[['peter', 'parker'], [10.0, 5.0, 85.0]], 
           [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
           [['captain', 'america'], [8.0,10.0,96.0]],
           [['deadpool'], []]]
print(get_stats(test_grades1))




