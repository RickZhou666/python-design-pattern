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