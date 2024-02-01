import random


class Database:
    _instance = None

    def __init__(self) -> None:
        id = random.randint(0, 100)
        print('id = ', id)
        # print('Loading a database from file!')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)
        return cls._instance
    
if __name__ == '__main__':
    # ============ compare whether it's same database start ============
    d1 = Database()
    d2 = Database()
    print(d1 == d2) # althogh the instance only one copy but __init__  called every time

    # `__init__` was called, whatever happened
    # >>Loading a database from file!
    # >>Loading a database from file!
    # >>True
    # ============ compare whether it's same database end ============