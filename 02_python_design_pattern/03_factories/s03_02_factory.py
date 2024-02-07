# ============================================ FACTORY START ============================================
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point():
     def __init__(self, x, y) -> None:
          self.x = x
          self.y = y

class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
         return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
         return Point(rho * cos(theta), rho * sin(theta))

# ============================================ FACTORY END ============================================
if __name__ == '__main__':
     # Python has no private class, so it cannot shield anyone using `__init__` method
     p = Point(2, 3)
     p2 = PointFactory.new_cartesian_point(4, 5)
     p3 = PointFactory.new_polar_point(10, 30)

     print(p)
     print(p2)
     print(p3)


# in most cases, a factory is a separated class
# if you want to get rid of default `__init__`
# ============================================ Inner class FACTORY START ============================================
class Point():
     def __init__(self, x, y) -> None:
          self.x = x
          self.y = y

     class PointFactory:
         def new_cartesian_point(self, x, y):
              return Point(x, y)
     
         def new_polar_point(self, rho, theta):
              return Point(rho * cos(theta), rho * sin(theta))
# ============================================ Inner class FACTORY END ============================================
if __name__ == '__main__':
     # Python has no private class, so it cannot shield anyone using `__init__` method
     p = Point(2, 3)
     p2 = Point.PointFactory.new_cartesian_point(4, 5)
     p3 = Point.PointFactory.new_polar_point(10, 30)


# you can also make it like singleton
# ============================================ Inner class FACTORY START ============================================
class Point():
     def __init__(self, x, y) -> None:
          self.x = x
          self.y = y

     class PointFactory:
         def new_cartesian_point(self, x, y):
              return Point(x, y)
     
         def new_polar_point(self, rho, theta):
              return Point(rho * cos(theta), rho * sin(theta))
         
     point = PointFactory()
# ============================================ Inner class FACTORY END ============================================
if __name__ == '__main__':
     # Python has no private class, so it cannot shield anyone using `__init__` method
     p = Point(2, 3)
     p2 = Point.point.new_cartesian_point(4, 5)
     p3 = Point.point.new_polar_point(10, 30)