# Module 10: Basic Introduction to Classes and Objects 
## Object Oriented Programming
- Paradigm that models a problem in terms of objects.
- Objects has their own attributes(data) and behaviour(methods).
- Methods are used to modify the attrbutes instead of directly modifying them.
Some key Features of OOP:
- Class: Blueprint defining the attributes and methods of an objects.
- Object: Instance of a class.
- Encapsulation: process of hiding the implementation details. Expose only the necessary information.
- Abstraction: Process of representing the complex real-world entities in a simplified manner.
- Inheritance: Process of craeting a new class that has the attributes and behaviour of base class.
- Polymorphism: Polymorphism is the ability of an object to take many forms.
- Constructor: A constructor is a special method that is called to create an object.
- Destructor: A destructor is a special method that is called when an object is destroyed.
- Method Overloading: There can be many methods of same name but with varying parameters. It can't be realized in python as other OOP languages. However, it can be realized in python using default arguments and conditional statements.
- Mehod overriding: Ability of a subclass to provide its own implementation of a method already defined in parent class.
## Python Class
- class keyword is used in python to create a class.
- \_\_new__ is called to create object.It must return an object.
- \_\_del__ is called to destroy oject.
- \_\_init__ is called to initialize the objects. It can't return anything.

## Python Inheritance
### Single inheritence
```
>>> class Person:
...     pass
...
>>> class Employee(Person):
...     pass
...
>>>
```
### Multilevel iheritence
- A class is derrived from a derrived class.
```
>>> class BClass1:
...     pass
...
>>> class BClass2(BClass1):
...     pass
...
>>> class DClass(BClass2):
...     pass
...
>>>
```
### Multiple Inheritence
- Derrived class inherits from multiple classes.
```
>>> class Color:
...     pass
...
>>> class Shape:
...     pass
...
>>> class Circle(Color,Shape):
...     pass
...
>>>
```
### Hierarchial Inheritence
- Many derrived class can have same parent class.
```
>>> class Shape:
...     pass
...
>>> class Circle(Shape):
...     pass
...
>>> class Square(Shape):
...     pass
...
>>>
```
## Super keyword
- In order to call a method that was overwritten in subclass super() is used.
- Python maintains the priotiy to select which method needs to be executed, also known as method resolutuon order or MRO. The mro can be viewed as `<class_name>.mro()`
- super() can take class name and object as the arguments. Python will resolve the method that occurs after the passed class as argument in the MRO.
```
class A:
    def print(self):
            print("This is from class A")

class B(A):
    def print(self):
            print("This is from class B")

class C(B):
    def print(self):
            print("This is from class C")

class D(C):
    def print(self):
            print("This is from class D")

class E(D):
    def print(self):
            print("This is from class E")
            super(D,self).print()

print("MRO of E",E.mro())
E().print()

MRO of E [<class '__main__.E'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
This is from class E
This is from class C
```
