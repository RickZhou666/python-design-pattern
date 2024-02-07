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
    def can_vote(self):
        return self._age >= 18

    @property
    def age(self):
        return self._age
    
    # if age is different, we send a notification
    @age.setter
    def age(self, value):
        """
            1. cache old can_vote
            2. compare with new changed age
            3. then decide whether to trigger it

            but it's not scalable, works well when you have only one property
        """
        if self._age == value:
            return
        
        old_can_vote = self.can_vote

        self._age = value
        self.property_changed('age', value) # invoke all fucntion in the list with variable ('age', value)
        
        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)

# make sure whenever a person falls ill, a doctor gets called
if __name__ == '__main__':
    """
    """
    def person_changed(name, value):
        if name == 'can_vote':
            print(f'Voting ability changed to {value}')

    p = Person()
    p.property_changed.append(
        person_changed
    )
    for age in range(16, 21):
        print(f'Changing age to {age}')
        p.age = age