
# make it abstract base casee ABC

from abc import ABC
from enum import Enum, auto


# ======================== INSTANCE START ========================
class HotDrink(ABC):
     def consume(self):
          pass


class Tea(HotDrink):
     def consume(self):
          print('This tea is delicious')


class Coffee(HotDrink):
     def consume(self):
          print('This coffee is fantastic')
# ======================== INSTANCE END ========================

# ======================== FACTORY START ========================
# use abstract base case to have some APIs


class HotDrinkFactory(ABC):
     def prepare(self, amount):
          pass


class TeaFactory(HotDrinkFactory):
     def prepare(self, amount):
          print(f'Put in the tea bag, boil water,'
               f' pour {amount}ml, enjoy')
          return Tea()


class CoffeeFactory(HotDrinkFactory):
     def prepare(self, amount):
          print(f'Grind some beans, boil water,'
               f' pour {amount}ml, enjoy')
          return Coffee()
# ======================== FACTORY END ========================


# ======================== MAKE DRINK START ========================
def make_drink(entry: str, amount):
     if entry.lower() == 'tea':
          return TeaFactory().prepare(amount)
     elif entry.lower == 'coffee':
          return CoffeeFactory().prepare(amount)
     return None
# ======================== MAKE DRINK END ========================

# ======================== HOT DRINK MACHINE START ========================
# (1) initialize coffee or tea factories into list, we dont need repeated create factory
# (2) create instance via factory

class HotDrinkMachine():
     class AvailableDrink(Enum):
          TEA = auto()
          COFFEE = auto()

     factories = []
     initialized = False

     def __init__(self):
          if not self.initialized:
               self.initialized = True
               for d in self.AvailableDrink:
                    name = d.name[0] + d.name[1:].lower()
                    factory_name = name + 'Factory'
                    factory_instance = eval(factory_name)()
                    self.factories.append((name, factory_instance))

     def make_drink(self):
          print('Available drinks:')
          for f in self.factories:
               print(f[0])

          s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
          idx = int(s)
          s = input(f'Specify amount: ')
          amount = int(s)
          return self.factories[idx][1].prepare(amount)


# ======================== HOT DRINK MACHINE END ========================


if __name__ == '__main__':
     # entry = input('What kind of drink would you like?')
     # drink = make_drink(entry, 200)
     # drink.consume()
     hdm = HotDrinkMachine()
     hot_drink = hdm.make_drink()
     hot_drink.consume()