# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 13:47:06 2018

@author: Dyass
"""
"""
    Topics:
        Using Inherited Methods
"""
"""
    Add a Professor class of Objects:
        Also a kind of MIT Person
        but has different behaviours
    Use as an example to see how once can
    leverage methods from other classes in
    the hierarchy
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
#        return (self.getLastName()+" says: "+utterance)
        return (self.name+" says: "+utterance)
class Professor(MITPerson):
    def __init__(self,name,department):
        MITPerson.__init__(self,name)
        self.department=department
    def speak(self,utterance):
        new='In course '+self.department+' we say '
        return MITPerson.speak(self,new+utterance)
    def lecture(self,topic):
        return self.speak('It is obvious that '+topic)
faculty=Professor('Doctor Arrogant','six')
print(faculty.speak('hi there'))
print(faculty.lecture('hi there'))
