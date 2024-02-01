class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }
    
    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'
# ============================== Monostate start ==============================
# this ensure that we have same shared data
class Monostate:
    __shared_state = {}
    
    def __new__(cls, *args, **kwargs):
        # construct the object
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        # copy the initial state
        obj.__dict__ = cls.__shared_state
        return obj

class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'
    
# ============================== Monostate end ==============================


if __name__ == '__main__':
    # ============================== CEO START ==============================
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 77 # it's shared state, it will change both 
    ceo2.name = 'rick'
    print(ceo1)
    print(ceo2)
    # >> Steve is 55 years old
    # >> Steve is 77 years old
    # >> Steve is 77 years old
    # ============================== CEO END ==============================


    # ============================== CFO START ==============================
    # cfo1 = CFO()
    # cfo1.name = 'Eve'
    # cfo1.money_managed = 1
    # print(cfo1)

    # cfo2 = CFO()
    # cfo2.name = 'Ruth'
    # cfo2.money_managed = 10
    # print(cfo1, cfo2, sep='\n')
    # ============================== CFO END ==============================