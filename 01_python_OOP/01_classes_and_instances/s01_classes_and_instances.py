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
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

        

emp_1 = Employee('Corey', 'Schafer', 50_000)
emp_2 = Employee('Test', 'User', 60_000)

print(emp_1.email)
print(emp_2.email)

# print('{:<30s} {:20s}'.format(emp_1.first, emp_1.last))
# print(f'{emp_1.first}  {emp_2.last}')
print(emp_1.fullname())
print(Employee.fullname(emp_1)) # pass the instance