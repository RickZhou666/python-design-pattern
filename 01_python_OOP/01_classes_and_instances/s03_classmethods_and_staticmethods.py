import datetime
import time


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        
        # Employee(first, last, pay)
        # use cls to replace Employee, and it's the same thing
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """return whether it's a workday
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

        
emp_1 = Employee('Corey', 'Schafer', 50_000)
emp_2 = Employee('Test', 'User', 60_000)

# before change
print('------------------------------ before change ------------------------------')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# before change
print('------------------------------ after change ------------------------------')
Employee.set_raise_amt(1.20) # we are working with class method to adjust class attribute
# Employee.raise_amount = 1.20 # equavilent
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)



print('------------------------------ build a constructor change ------------------------------')
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Rick-Zhou-150000'
emp_str_3 = 'Eve-Jiang-100000'
emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
emp_5 = Employee.from_string(emp_str_3)
print(emp_3.__dict__)
print(emp_4.__dict__)
print(emp_5.__dict__)

print('------------------------------ test datetime ------------------------------')
print(datetime.date.fromtimestamp(1706589138))
print(datetime.date.today())


print('------------------------------ test static method ------------------------------')
my_date = datetime.date(2024, 1, 28)
print('{} is a weekday: {}'.format(my_date, Employee.is_workday(my_date)))
my_date = datetime.date(2024, 1, 29)
print('{} is a weekday: {}'.format(my_date, Employee.is_workday(my_date)))