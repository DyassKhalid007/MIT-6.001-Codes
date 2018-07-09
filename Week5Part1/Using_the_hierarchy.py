# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:41:15 2018

@author: Dyass
"""

"""
    Topics:
        Using the hierarchy
"""
"""
    Hierarchies:
        Parent Class(superclass)
        Child Class(subclass):
            inherits all data and behaviours of parent class
            add more info
            add more behaviour
            override behaviour
"""
class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,age):
        self.age=age
    def set_name(self,name=""):
        self.name=name
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
"""
    Added new functionality with speak()
        Instance of Cat can be called with new methods
        Instance of Animal throws error if called with new
        methods.
"""
jelly=Cat(1)
print(jelly.get_name())
jelly.set_name("JellyBelly")
print(jelly)
print(Animal.__str__(jelly))
blob=Animal(1)
print(blob)
blob.set_name()
print(blob)
class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:"+str(self.name)+":"+str(self.age)
peter=Rabbit(5)
jelly.speak()
peter.speak()
#blob.speak()#error no method speak for animal
class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friends=[]
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello")
    def age_diff(self,other):
        diff=self.get_age()-other.get_age()
        if self.age>other.age:
            print(self.name,"is",diff,"years older than",other.name)
        else:
            print(self.name,"is",-diff,"years older than",other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
eric=Person("eric",45)
john=Person("john",55)
eric.speak()
eric.age_diff(john)
john.age_diff(eric)