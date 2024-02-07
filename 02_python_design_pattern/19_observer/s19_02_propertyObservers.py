from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # item is each function inside the list
        for item in self:
            item(*args, **kwds)

class PropertyObservable:
    def __init__(self) -> None:
        self.property_changed = Event()

class Person(PropertyObservable):
    def __init__(self, age=0) -> None:
        super().__init__()
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    # if age is different, we send a notification
    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed('age', value) # invoke all fucntion in the list with variable ('age', value)


class TrafficAuthority:
    def __init__(self, person: Person) -> None:
        self.person = person
        self.person.property_changed.append( # add the function to subscribe person's property changes
            self.person_changed
        )
    
    def person_changed(self, name, value):
        if name == 'age':
            if value < 16:
                print('sorry, you still cannot drive\n')
            else:
                print('Okay, you can drive now\n')
                self.person.property_changed.remove(
                    self.person_changed
                    )
        



# make sure whenever a person falls ill, a doctor gets called
if __name__ == '__main__':
    """
        1. Person.age.setter()
        2. Person.age.setter().property_changed()
        3. Event().__call__()
            - iterator all function inside
        4. TrafficAuthority.person_changed()
    """
    p = Person()
    ta = TrafficAuthority(p)

    for age in range(14, 20):
        print(f'Setting age to {age}')
        p.age = age