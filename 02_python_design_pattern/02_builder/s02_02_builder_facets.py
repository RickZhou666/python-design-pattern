class Person:
    def __init__(self) -> None:
        # to have two builder 
        # address
        self.street_address = None
        self.postcode = None
        self.city = None

        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    
    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' + \
                f'Employed at {self.company_name} as a {self.position} earning {self.annual_income}'
    
# serve as base class
class PersonBuilder:        # initialize as blank instance
    def __init__(self, person = Person()):
        self.person = person
    
    # sub builder
    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person
    
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person) # this will go back to super class with instance as parameter

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self
    
    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self
    
pb = PersonBuilder()
person = pb\
    .lives\
        .at('123 London Road')\
        .in_city('London')\
        .with_postcode('SW12BC')\
    .works\
        .earning(12300)\
        .as_a('Egineer')\
        .at('Fabrikam')\
     .build()
    

print(person)