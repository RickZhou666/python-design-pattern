class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self) -> str:
        return f'{self.name} born on {self.date_of_birth} ' + \
                f'works as {self.position}'
    
    @staticmethod
    def new():
        return PersonBuilder()
    
class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder): # inherit
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder): # inherit
    def works_as_a(self, position):
        self.person.position = position
        return self


# every single one of these builders is open for extension through inheritance but closed for modification
class PersonBirthDateBuilder(PersonJobBuilder): # inherit
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self
    
pb = PersonBirthDateBuilder()
me = pb\
    .called('Rick')\
    .works_as_a('Software Engineer')\
    .born('05/05/1995')\
    .build()

print(me)

