# store singleton into dictionary whenever people want it or initiazlied only once for each

# this is a decorator we created
# ==================== decorator start ====================
def singleton(class_):
    instances = {}

    def get_intance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    
    return get_intance
# ==================== decorator end ====================

@singleton
class Database:
    def __init__(self) -> None:
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
    
    # now it's only call __init__ once
    # >>Loading database
    # >>True


# =============== another test with different name start ===============
def singleton(any_name):
    instances = {}
    def wrapper(*args, **kwargs):
        if any_name not in instances:
            print(any_name)         # any_name = <class '__main__.Database'>
            print(type(any_name))   # <class 'type'>
            instances[any_name] = any_name(*args, **kwargs) 

        return instances[any_name]
    return wrapper

@singleton
class Database:
    def __init__(self) -> None:
        print('Loading database')


db1 = Database()
db2 = Database()
print(db1 == db2)
# =============== another test with different name end ===============