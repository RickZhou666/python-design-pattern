import copy


class Addresses:
    def __init__(self, street_address, city, country) -> None:
        self.city = city
        self.street_address = street_address
        self.country = country
    
    @property
    def full_addr(self):
        return self.street_address + ' ' + self.city + ' ' + self.country
    
    @full_addr.setter
    def full_addr(self, addr):
        street_address, city, country =  addr.split(' ')
        self.street_address = street_address
        self.city = city
        self.country = country
    
    def __str__(self) -> str:
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} lives at {self.address}'
    

john = Person('John', Addresses('123 London Road', 'London', 'UK'))
print(john)

print('\n------------------ deep copy ------------------')
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.street_address = '123B Winchester Ave'
print(jane)
print(john)

print('\n ------------------ shallow copy ------------------')
tom = copy.copy(john) # shallow copy
tom.name = 'Tom'
tom.address.city = 'Manchester'
print(tom)
print(john)