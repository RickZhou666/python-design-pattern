from typing import Any


class factory:
    def __init__(self, name) -> None:
        self.name = name


# this is way to make sure class to be created in single fashion
class SingletonFactory(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonFactory, cls)\
                .__call__(*args, **kwds)
        return cls._instances[cls]
    
class SingletonHat(metaclass = SingletonFactory):
    def __init__(self) -> None:
        pass

class NonSingletonHat():
    def __init__(self) -> None:
        pass

def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    hat1 = SingletonHat() 
    hat2 = SingletonHat()
    print(hat1 == hat2)

    hat3 = NonSingletonHat() 
    hat4 = NonSingletonHat()
    print(hat3 == hat4)

is_singleton('test')