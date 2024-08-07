from helper import d
# Object Orientated Programming and Classes - OOP
# Create multiple objects of the same class
#OOP = empty list is an object ex .append is a (f) inside a class
#revolves around blueprints that help us create mult objects with similiar attributes and behaviors
#Why use OOP - can do almost anything with OOP- custom classes - Modularity and better organization - reuse code - inheritance - polymorphism - data hiding 
#(Classes and objects) - class is a blueprint for creating objects - objects are instances of classes
#Reusable code - classes can be used to create many objects - objects can store data using attributes - objects can perform actions using methods
#Scalable code - classes allow for more complex, reusable code - large programs can be written in terms of classes and objects
##Maintain compatibility - classes make it easier to maintain and update code - updating a class automatically updates all objects - easier to update specific instances of an object rather than modifying an entire database or entire code base
#WHat are classes and objects -  classes are bluprints that outline the attributes and functionalities of an object - objects are instances of a class that can store data and perform actions
#We have been wokring with classes and objects all this time - 

num = 2
print(type(num))
str1 = str()  #created an empty string using the class constructor
print(type(str1))
str1 += ' I just concatanated this to str1'
print(str1)
d()
list1 = list()
print(type(list1))
d()
dictionary1 = dict()
print(type(dictionary1))
d()

# Let's create our own class!
# Naming convention for user defined classes: Always capitalize the first letter
class Car():# my car = Car() - my car is an object of the class Car

d()
my_car = Car()
print(type(my_car))

d()

bugati = Car()
my_other_car = Car()
d()




