from abc import ABC
from cmath import sqrt
from enum import Enum, auto
import math
import unittest

import numpy


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        val_1 = (-b + sqrt(b**2 - 4 * a * c )) / 2 * a
        val_2 = (-b - sqrt(b**2 - 4 * a * c )) / 2 * a
        return [val_1, val_2]


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return [float('nan'), float('nan')]
        



class DiscriminantFormat(Enum):
    ORDINARY = auto()
    REAL = auto()


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        ans = None
        if b**2 - 4 * a * c >= 0:
            self.set_discriminant(DiscriminantFormat.ORDINARY)
            ans = self.strategy.calculate_discriminant(a, b, c)
        else:
            self.set_discriminant(DiscriminantFormat.REAL)
            ans = self.strategy.calculate_discriminant(a, b, c)
        
        return ans

    def set_discriminant(self, strategy):
        if strategy == DiscriminantFormat.ORDINARY:
            self.strategy = OrdinaryDiscriminantStrategy()
        elif strategy == DiscriminantFormat.REAL:
            self.strategy = RealDiscriminantStrategy()


class DiscriminantTests(unittest.TestCase):
    qes = QuadraticEquationSolver(DiscriminantFormat.ORDINARY)
    def test_negative(self):
        a, b, c = 4, 3, 4
        val1, val2 = self.qes.solve(a, b, c)

        # (1) use numpy
        # https://stackoverflow.com/a/51728554/7163137
        check = numpy.isnan(val1) and numpy.isnan(val2)
        self.assertTrue(check)

        # (1) use math
        # https://stackoverflow.com/a/51728554/7163137
        # self.assertTrue(math.isnan(val1) and math.isnan(val2))
    
    
    def test_positive(self):
        a, b, c = 4, 10, 4
        val1, val2 = self.qes.solve(a, b, c)
        self.assertIsNotNone(val1)
        self.assertIsNotNone(val2)


if __name__ == '__main__':
    unittest.main()