class Car:
    def __init__(self, driver) -> None:
        self.driver = driver

    def drive(self):
        print(f'Car is being driven by {self.driver.name}')

# don't allow driver under 18
        
class CarProxy:
    """
        designed for access control
        on top of original layer
    """
    def __init__(self, driver) -> None:
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 18:
            self._car.drive()
        else:
            print(f'driver is too young to drive')


class Driver:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

if __name__ == '__main__':
    driver = Driver('John', 16)
    car = Car(driver)
    car.drive()

    print('\n------------ proxy ------------')
    car_proxy = CarProxy(driver)
    car_proxy.drive()
