import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # unambiguous representation of an object
    # print out string that we can recreate this object
    def __repr__(self) -> str:
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # more readble version of object
    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)



print('------------------------------ print object will print __str__ with high priority ------------------------------')
print(emp_1)
print(repr(emp_1))
print(str(emp_1))


print('------------------------------ print object will print __str__ with high priority ------------------------------')
print(emp_1.__repr__())
print(emp_1.__str__())


print('------------------------------ int dunder add ------------------------------')
print(1 + 2)
print(int.__add__(1, 2))


print('------------------------------ str dunder add ------------------------------')
print(str.__add__('a', 'b'))


print('------------------------------ object dunder add ------------------------------')
print(emp_1 + emp_2)

print('------------------------------ dunder len function ------------------------------')
print(len('test'))
print('test'.__len__())

print('------------------------------ override len function to print customized object length ------------------------------')
print(len(emp_1))


print('------------------------------ override len function to print customized object length ------------------------------')
datetime