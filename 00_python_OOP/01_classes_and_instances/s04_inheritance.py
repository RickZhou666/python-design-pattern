# we want to have different type of Employee


from http.client import HTTPException


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

class Developer(Employee):
    raise_amount = 1.10

    # let super class to handler its attributes
    def __init__(self, first, last, pay, pro_lang) -> None:
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) # this can do the same thing
        self.pro_lang = pro_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)
        if Employee is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

print('------------------------------ before change ------------------------------')
dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'Employee', 60000)

print(dev_1.email)
print(dev_2.email)


print('------------------------------ after inheritance ------------------------------')
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
print(dev_1.email)
print(dev_2.email)

print('------------------------------ after help() ------------------------------')
# print(help(Developer))


print('------------------------------ before change raise_amount ------------------------------')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print('------------------------------ after change raise_amount in Employee and Developer class ------------------------------')

print('raise_amount only happened in Developer class')
print('created from Developer class')
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


print('created from Employee class')
dev_1 = Employee('Corey', 'Schafer', 50000)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


print('------------------------------ Manager class ------------------------------')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

# remove employee
print('----- Remove Employee -----')
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print('------------------------------ isinstance() ------------------------------')
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print('------------------------------ issubclass() ------------------------------')
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))


HTTPException
BAD_REQUEST