from typing import Any


class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwds)
        return cls._instances[cls]

# it's already lazy loading, when we need it, we instantiate it
class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)