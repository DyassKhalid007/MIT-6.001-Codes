# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:53:34 2018

@author: Dyass
"""
"""
    Topics:
        Visualizing Hierarchy
"""
import datetime
class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName
        
    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    
    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    # other methods

    def __str__(self):
        """return self's name"""
        return self.name
class MITPerson(Person):
    nextIdNum=0
    
    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum=MITPerson.nextIdNum
        MITPerson.nextIdNum+=1
    def getIdNum(self):
        return self.idNum
    def __lt__(self,other):
        return self.idNum<other.idNum
    def speak(self,utterance):
        return (self.getLastName()+" says "+utterance)
"""First Example"""
#m3=MITPerson('Mark Zuckerberg')
#Person.setBirthday(m3,5,14,84)
#m2=MITPerson('Drew Houston')
#Person.setBirthday(m2,3,4,83)
#m1=MITPerson('Bill Gates')
#Person.setBirthday(m1,10,28,55)
#print()
#MITPersonList=[m3,m2,m1]
#print(m1)
#print(m3)
#print()
#print(m1.speak('hi,there'))
#print()
#for e in MITPersonList:
#    print(e)
#print()
#MITPersonList.sort()#on the basis of id number
#for e in MITPersonList:
#    print(e)
"""Second Example"""
p1=MITPerson('Eric')
p2=MITPerson('John')
p3=MITPerson('John')
p4=Person('John')
print(p1<p2)#calls p1 lt method
print(p4<p1)#calls p4 lt method
print(p1<p4)#calls p2 lt method

    


        
