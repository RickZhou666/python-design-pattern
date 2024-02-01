class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self) -> str:
        return 'name: {}, id: {}'.format(self.id, self.name)

# once initialized, it will always be there
class PersonFactory:
    id = 0

    def create_person(self, name):
        person = Person(self.id, name)
        self.increase_id()
        return person

    def increase_id(cls):
        cls.id += 1

    
if __name__ == '__main__':
    person_factory = PersonFactory()
    p1 = person_factory.create_person('Rick')
    p2 = person_factory.create_person('Eve')
    p3 = person_factory.create_person('Ava')
    p4 = person_factory.create_person('Dunn')

    print(p1)
    print(p2)
    print(p3)
    print(p4)