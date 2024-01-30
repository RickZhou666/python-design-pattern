
# Tips
1. what is namespace
    - A namespace is a declarative region that provides a scope to the identifiers (the names of types, functions, variables, etc) inside it. Namespaces are used to organize code into logical groups and to prevent name collisions that can occur especially when your code base includes multiple libraries [link](https://www.google.com/search?q=namespace&oq=namespace&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDINCAEQABiDARixAxiABDINCAIQABiDARixAxiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDEwNDNqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8)

2. check wether a year leap year
```python
return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

3. return doc
```python
@staticmethod
def is_workday(day):
    """return whether it's a workday
    """
    if day.weekday() == 5 or day.weekday() == 6:
        return False
    return True
```

<br><br><br>

# Tutorial 1: classes and instances
- link: https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&ab_channel=CoreySchafer

1. create a class 
    - so we can create instance from it
    - blueprint to create employee
    - instead of doing the assignup manually we can assign the value we when create it

2. create instance from the class
    - `self` is passing automatically
    - each method in class, automatically take the instance as the first argument
    - need call `emp1.fullname()` instead of ``emp1.fullname`
    -
     ```python
    print(emp_1.fullname())
    print(Employee.fullname(emp_1)) # pass the instance
    ```

<br><br><br><br><br><br>

# Tutorial 2: classes variables
1. when you create a class attribute, its instance able to adjust by instance.class_variable. but only limit to it's own namesapce
2. use can use below to print out all atrributes or methods
    - `__dict__`
    ```python
    Employee.__dict__
    emp_1.__dict__
    ```


<br><br><br><br><br><br>

# Tutorial 3: classes variables

1. regular method automatically take the instance as the first argument
2. to create a `class method`, use decorator
    - we received the class as our first argument instead of the instance
    - `cls` is the class
    ```python
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    ```

3. static class dont pass anything automatically
    - it's nothing to do with instance or class
    - but it is need to be placed inside the class


<br><br><br><br><br><br>

# Tutorial 4: inheritance - creating subclasses
1. inheritance
```python
class Employee:
    pass

class Developer(Employee):
    pass
```

2. method resolution order
    - places where python searches for attributes and method
    - every class in python inherits from `builtins.object` class
```bash
    Help on class Developer in module __main__:

class Developer(Employee)
 |  Developer(first, last, pay) -> None
 |  
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
 |  
 |  Methods inherited from Employee:
 |  
 |  __init__(self, first, last, pay) -> None
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  apply_raise(self)
 |  
 |  fullname(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Employee:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Employee:
 |  
 |  raise_amount = 1.04
```


3. it's easy to maintance
```python
class Developer(Employee):
    raise_amount = 1.10

    # let super class to handler its attributes
    def __init__(self, first, last, pay, pro_lang) -> None:
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) # this can do the same thing
        self.pro_lang = pro_lang
```

4. `isinstance` will tell us if an object is an instance of a class
```python
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
>>True
>>True
>>False
```

5. `issubclass` will tell us if an class is a subclass of another class
```python
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
>>True
>>True
>>False
```

6. HTTPException -> Exception -> BaseException -> object


<br><br><br><br><br><br>

# Tutorial 5: special (magic/dunder) methods
1. dunder method
    - surrond by double underscore
    ```python
    def __init__(self):
        pass
    ```

2. `repr` should be unambiguous representation of an object
    - if we only overwrite 

3. `str` should be more readble version of object

4. `__add__` 

5. [emulating numeric types](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

<br><br><br><br><br><br>

# Tutorial 6: Property Decorators - Getters, Setters, and Deleters
1. we define our email as a method, but we able to access it like a `attribute`
```python
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
```

2. delete attribute
```python
@fullname.deleter
def fullname(self):
    print('Delete Name!')
    self.first = None
    self.last = None


del emp_1.fullname
```