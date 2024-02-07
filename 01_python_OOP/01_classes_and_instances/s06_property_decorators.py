class Employee:

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def  __str__(self) -> str:
        return '{}, {}, {}'.format(self.first, self.last, self.email)


emp_1 = Employee('Corey', 'Schafer')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


print('------------------------------ change the name add @property ------------------------------')
emp_1.first = 'Tompson'
print(emp_1.email)
print(emp_1.fullname)

print('------------------------------ set the attributes ------------------------------')
emp_1.fullname = 'Rick Zhou'
print(emp_1)


print('------------------------------ delete the attributes ------------------------------')
del emp_1.fullname