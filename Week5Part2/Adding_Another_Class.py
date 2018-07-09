# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 13:12:50 2018

@author: Dyass
"""
"""
    Topics:
        Adding Another Class
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
class Student(MITPerson):
    pass
class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year=classYear
    def getClass(self):
        return self.year
    def speak(self,utterance):
        return MITPerson.speak(self,"Dude: "+utterance)
class Grad(Student):
    pass
def isStudent(obj):
#    return isinstance(obj,UG)or isinstance(obj,Grad)
    return isinstance(obj,Student)
s1=UG('Matt Damon',2017)
s2=UG('Ben Affleck',2017)
s3=UG('Lin Manuel Miranda',2018)
s4=Grad('Leonardo di Caprio')
print(s1)
print(s1.getClass())
print(s1.speak('Where is the quiz?'))
print(s2.speak('I have no clue'))
class TransferStudent(Student):
    pass
s5=TransferStudent("Dyass Khalid")
print(s5)
    