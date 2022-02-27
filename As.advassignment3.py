#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1) What is the concept of an abstract superclass?
# abstract superclass is can be considered as a blueprint for other classes. It allows you to create a set of methods that
#must be created within any child classes built from the abstract class. A class which contains one or more abstract methods
#is called an abstract class.
#Whereas an abstract method is a method that has a declaration but does not have an implementation


# In[ ]:


from abc import ABC,abstractmethod
class Polygon(ABC): # Abstract Class
    @abstractmethod
    def noofsides(self): # Abstract Method
        pass
class Triangle(Polygon):
    def noofsides(self):  # overriding abstract method in child class Triangle
        print("I have 3 sides")
class Pentagon(Polygon):
    def noofsides(self): # overriding abstract method in child class Pentagon
        print("I have 5 sides")


# In[ ]:


Triangle.noofsides(89)
Pentagon.noofsides(88)


# In[ ]:


#2)What happens when a class statement's top level contains a basic assignment statement?
#When a Class statement's top level contains a basic assignment statement, its usually treated as a class attribute or
#class level variable.
#where as assignment statements inside methods are treated as instance attributes or local attributes.


# In[ ]:


#example
class employees:
    groupname = 'AVIATORS' # class attribute
    def __init__(self,name,gender):
        self.name = name # instance attributes
        self.gender = gender


# In[ ]:


#3) Why does a class need to manually call a superclass's init method?
# if a child class has __init__ method, then it will not inherit the __init__ method of the parent class.So,the __init__
# method of the child class overrides the __init__ method of the parent class.
# so we have to manually call a parent superclass's __init__ using super() method


# In[2]:


#example()
class superman():
    def __init__(self,version,y):
        self.version=version
        self.y=y
class spiderman(superman):
    def __init__(self,version,y,realname,age):
        super().__init__(version,y)
        self.realname= realname
        self.age= age
man= spiderman(2.2,1986,'superman',36)
print(man.__dict__)       


# In[ ]:


#4)How can you augment, instead of completely replacing, an inherited method?
#super() method can be used to augment, instead of completely replacing, an inherited method.


# In[ ]:


#example()
class superman():
    def __init__(self,version,y):
        self.version=version
        self.y=y
class spiderman(superman):
    def __init__(self,version,y,realname,age):
        super().__init__(version,y)
        self.realname= realname
        self.age= age
man= spiderman(2.2,1986,'superman',36)
print(man.__dict__)  


# In[ ]:


#5)How is the local scope of a class different from that of a function?
# A Variable which is defined inside a function is local to that function. 
# it is accesible from the point at which it is defined until the end of the function, 
# and exists for as long as the function is existing.

#Similary a variable inside of a class also has a local variable scope. 
#Variables which are defined in the class body (but outside all methods) are called as class level variables or class attributes.
#they can be referenced by there bare names within the same scope, but they can also be accessed 
#from outside this scope if we use the attribute access operator (.). on a class or an instance of the class.


# In[3]:


#example
def hello(name):
    name = name
    print(f'you\'re name is {name}')
hello('achutha')
try:
    name
except NameError:
    print('Name varible is not available outside hello function scope')

class Person:
    employee = "audi"
    def __init__(self):
        pass
print(Person.employee) # Accessing species using class name
Male = Person()
print(Male.employee) # Accessing species using instance of class


# In[ ]:




