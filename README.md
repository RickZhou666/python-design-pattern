# python-design-pattern
udemy course for python design parttern

[link](https://www.udemy.com/course/design-patterns-python)

- Introduction
    - design patterns are common architectural approaches
    - popularized by the Gang of Four book (1994)
        - smalltalk & C++
    - Translated to manny OOP languages
        - C#, Java, C++, ...
    - Universally relevant
        - internalized in some programming languages
        - libraries
        - your own code

<br><br><br>

- Solid design principles
    - Creational
        - Builder
        - Factories
            - abstract factory
            - factory method
        - prototype
        - singleton
    - Structural
        - adapater
        - bridge
        - composite
        - decorator
        - facade
        - flyweight
        - proxy
    - Behavioral
        - chain of responsibility
        - command
        - interpreter
        - iterator
        - mediator
        - memento
        - observer  
        - state
        - strategy
        - template method
        - visitor

<br><br><br>

- organization
    - 100% practical
    - hands-on coding
    - end-of-section coding exercises
    - latest version of python
    - code generation & refactoring IDE features
    - liberal use of decorators and metaclasses
    - external packages used liberally

<br><br><br>

- pre-requisites
    - understanding of object-oritented programming
    - good understanding of python
    - topics mentioned in the course
        - sequence processing (streams, Rx)
        - concurrency
        - dependency injection  



<br><br><br>



- env setup

```bash
# check python versions
$ pyenv versions

# switch to 3.10.4
$ pyenv local 3.10.4

# setup virtual env
$ python3.10 -m venv .venv

# select interpreter

# recheck version
$ python3 --version
```


<br><br><br>

## Tips
1. yield vs return
     - similar but different
     - yield is a generator object
     - return is a single value
    
2. API - application programming interface

3. abc package - abstract base classes

4. when traverse Enum class
```python
class AvailableDrink(Enum):
    TEA = auto()
    COFFEE = auto()

for d in AvailableDrink:
    print('{}, {}'.format(d.name, d.value))
# output
>> TEA, 1
>> COFFEE, 2
```

5. eval()
[link](https://stackoverflow.com/questions/3451779/how-to-dynamically-create-an-instance-of-a-class-in-python)
 - it's dangerous, due to code injections
```python
# return a class 
eval(factory_name)

# return a class instance
eval(factory_name)()
```

<br><br><br><br><br><br>

# 1. The solid design principles

## 1.1 Single responsibility principle (SRP)
- aka, SOC (separation of concerns)
- if you have some common function for each class. when there comes a change, you have to change all the classes.

- anti-pattern
    - god object
        - one class that does everything
        - hard to maintain
        - hard to test
        - hard to extend
        - hard to reuse
        - hard to read
        - hard to debug

<br><br><br>


## 1.2 Open-closed principle (OCP)
1. when you add new functionality, you add it via extension, not modification
2. `OCP = open for extension, closed for modification`
3. simply **extend things**

<br><br><br>

## 1.3 Liskov Subsitution Principle (LSP)
- a principle in object-oriented programming that states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.


<br><br><br>

## 1.4 Interface Segregation Principle (ISP)
1. you dont want to stick too many elements too many methods into an interface
2. implement a inteface with a lot of methods is not ideal, as you are forcing your client to define the methods which they dont need


<br><br><br>

## 1.5 Dependency Inversion Principle (DIP)
1. high level classes or high level modules should not depend on low level modules. instead they should depend on abstractions.
    - abstract class
    - class with abstract methods
    - depends on interfaces instead of concrete implementations

2. e.g. you are working on a unit test, you dont want to real pull data from database, you can create a fake database class, all of the data will be in memory. you will expose this data to unit test in a predictable fashion. 


- `this is not Depdenency Injection`


<br><br><br>

## 1.6 Summary

1. Single Responsibility Principle
    - a class should only have one reason to change
    - Separation of concerns - different classes handling different, independent tasks/ problems

2. Open-Closed Principle
    - classes should be open for extension, but closed for modification

3. Liskov Substitution Principle
    - you should be able to substitute a base type for a subtype

4. Interface Segregation Principle
    - dont put too much into an interface, split into separate interfaces
    - YAGNI - you ain't going to need it

5. Dependency Inversion Principle
    - high-level modules should not depend upon low-level ones, use abstractions


<br><br><br><br><br><br>

# 2. Builder

## 2.1 Gamma Categorization
1. design patterns are typically split into three categories
2. this is called Gamma Categorization after Erich Gamma, one of GoF authors
    - creational
        - deal with the creation (construction) of objects
        - Explicit(constructor) vs. implicity(DI, reflection, etc)
        - wholesale (single statement) vs piecewise (step-by-step)
    - structural
        - concerned with the structure (e.g., class members)
        - many patterns are wrappers that mimic the underlying class' interface
        - stress the importance of good API design
    - behavioral
        - they are all different; no central theme

<br><br><br>

## 2.2 Builder
1. motivation
    - some objects are simple and can be created in a single initializer call
    - other objects require a lot of ceremony to create
    - having an object with 10 initializer arguments is not productive
    - instead, opt for piecewise construction
    - builder provides an API for constructing an object step-by-step

2. formal definition 
    - when piecewise object construction is complicated, provide an API for doing it succinctly

<br><br><br>

## 2.3 builder facet
1. if a object is too complicated to build, and need involve multiple builders to anticipate

<br><br><br>

## 2.4 builder inheritance

<br><br><br>

## 2.5 Summary
1. A builder is a separate component for building an object
2. can either give builder an initializer or return it via a static function
3. to make builder fluent, return self
4. different facets of an object can be built with different builders working in tandem via a base class

<br><br><br><br><br><br>

# 3. Factories

## 3.1 Overview
- what is factory in general?
    - `a component responsible solely for the wholesale (not piecewise) creation of objects`
1. Object creation logic becomes too convoluted
2. Initializer is not descriptive
    - name is always __init__
    - cannot overload with same sets of arguements with different names
    - can turn into 'optional parameter hell'

3. Wholesale object creation(non-piexewise, unlike Builder) can be outsourced to
    - a separate method (factory method)
    - that may exist in a separate class (factory)
    - can create hierarchy of factories with abstract factory

<br><br><br>

## 3.2 Factory Method
1. if you define your system in Enum, every time you add a new member, you need modify enum and init method (constructor)
2. use static method to create instance
```python
class Point:
    def __init__(self, a, b) -> None:
            self.x = a
            self.y = b

    @staticmethod
    def new_cartesian_point(x, y):
         return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
         return Point(rho * cos(theta), rho * sin(theta))
    
    def __str__(self) -> str:
         return '{{x: {}, y: {}}}'.format(self.x, self.y)
```

<br><br><br>

## 3.3 Factory
1. if there is too many methods in a class, you can move and group them into another entity separately which is a class
    - single responsibility principle
    - 

## 3.4 Abstract Factory
1. you need a factory to prepare those instance for you
2. in python, you dont really define abstact base class, in other strong type(java) language you will need to
    - `but we suggest to keep it this way`
3. steps to build
    1. create your product in a hierarchical way
    2. create a factory for each product
    3. create an abstract factory that will create all the factories
    4. use input string -> get the factory -> get the product


## 3.5 Summary
1. a factory method is a statis method that creates objects
2. a factory is any entity that can take care of object creation
3. a factory can be external or reside inside the object as an inner clas
4. hierarchies of factories can be used to create related objects