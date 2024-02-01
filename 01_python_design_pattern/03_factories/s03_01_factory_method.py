# using initializer

from enum import Enum
from math import cos, sin


# ============================================ START ============================================

# this violate open/ closed principle, better add new functionaly via extension rather than modfication
# class CoordinateSystem(Enum):
#     CARTESIAN = 1
#     POLAR = 2

# class Point:
#     def __init__(self, a, b, system=CoordinateSystem.CARTESIAN) -> None:
#         if system == CoordinateSystem.CARTESIAN:
#             self.x = a
#             self.y = b
#         elif system == CoordinateSystem.POLAR:
#             self.x = a * cos(b)
#             self.y = a * sin(b)
# ============================================ END ============================================



# ============================================ FACTORY START ============================================
class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    def __init__(self, a, b) -> None:
            self.x = a
            self.y = b

    @staticmethod
    def new_cartesian_point(x, y):
         return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
         return Point(rho * cos(theta), rho * sin(theta))
    
    def __str__(self) -> str:
         return '{{x: {}, y: {}}}'.format(self.x, self.y)
# ============================================ FACTORY END ============================================


if __name__ == '__main__':
    # Python has no private class, so it cannot shield anyone using `__init__` method
     p = Point(2, 3)
     p2 = Point.new_cartesian_point(4, 5)
     p3 = Point.new_polar_point(10, 30)

     print(p)
     print(p2)
     print(p3)