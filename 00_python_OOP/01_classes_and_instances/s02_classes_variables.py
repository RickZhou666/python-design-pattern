# represent employee via python

# even if you don't initialize attributes,  you can still assign it
# class Employee:
#     pass

# emp_1 = Employee()
# emp_2 = Employee()

# emp_1.first = 'Jim'
# emp_1.last = 'Corey'

# print(emp_1.first)
# print(emp_1.last)

# ------------------------------------------------------------------------------------------------

class Employee:
    num_of_emps = 0 # each time we create a new instance from this class, we do incremental by 1
    # class variables
    raise_amount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 # every time use this class, we increase 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount) # NameError: name 'raise_amount' is not defined
                                                # we need access it via instance or class 
        self.pay = int(self.pay * self.raise_amount)
        

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50_000)
emp_2 = Employee('Test', 'User', 60_000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount
# Employee.raise_amount

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# if it's class variable, how can we access via instance 
# (1) first check if instance contains the attriabute
# (2) then check if any super class it inherits of containing the attribute
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print namesapce

# ----
# print(emp_1.__dict__) n
# instace doesn't contain class attributes
# {'first': 'Corey', 'last': 'Schafer', 'pay': 50000, 'email': 'Corey.Schafer@company.com'}


# ----
# print(Employee.__dict__) 
# python class contain class attributes
# {'__module__': '__main__',
#  'raise_amount': 1.04, 
#  '__init__': <function Employee.__init__ at 0x10631d900>,
#  'fullname': <function Employee.fullname at 0x10631e680>,
#  'apply_raise': <function Employee.apply_raise at 0x10631e830>,
#  '__dict__': <attribute '__dict__' of 'Employee' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Employee' objects>,
#  '__doc__': None}



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------
# adjust class attributes
# Employee.raise_amount = 1.2
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


#------------
# adjust class attributes from instance
# emp_1.raise_amount = 1.2
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_1.__dict__)
# print(emp_2.raise_amount) # we didn't setup class attribute, so emp_2 still falls back on class attribute value


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(Employee.num_of_emps)
# >> 2 # as we iniatiate twice