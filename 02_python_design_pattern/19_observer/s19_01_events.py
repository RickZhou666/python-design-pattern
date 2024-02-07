from typing import Any

class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # get variables from upper stack
        # applied it to all functions that added to the list
        for item in self:
            item(*args, **kwds)


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        # we pass variable to list
        self.falls_ill(self.name, self.address)

def call_doctor(name, address):
    print(f'{name} needs a doctor at {address}')

def cook_me_chiken(name, address):
    print(f'{name} needs a sichuan chicken at {address}')

# make sure whenever a person falls ill, a doctor gets called
if __name__ == '__main__':
    """
        1. append a function into list
        2. we can append a lambda function as well
    """
    person = Person('Sherlock', '221B Baker St')

    person.falls_ill.append(
        lambda name, address: print(f'{name} falls ill')
    )
    person.falls_ill.append(call_doctor)
    person.falls_ill.append(cook_me_chiken)
    person.catch_a_cold()

    print('============================== after remove the call_doctor function ==============================')
    # remove subscriptions
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()