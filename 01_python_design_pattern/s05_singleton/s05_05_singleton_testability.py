# Purpose:
#   (1) to make sure we only have 1 instance of Database

from typing import Any
import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
            .__call__(*args, **kwds)
        
        return cls._instances[cls]
    
class Database(metaclass = Singleton):
    def __init__(self) -> None:
        self.population = {}
        f = open('/Users/runzhou/git/python-design-pattern/s05_singleton/capitals.txt', 'r')
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i + 1].strip())
        f.close()

class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
        # ========= DANGEROUS =========
        # we're running on live databases
            result += Database().population[c]
        # ========= DANGEROUS =========
        return result

# ===================== Inject database start =====================
class ConfigurableRecordFinder:
    def __init__(self, db) -> None:
        self.db = db
    
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result
    
class DummyDatabase:
    population = {
        'alpha' : 1,
        'beta' : 2,
        'gamma' : 3
    }

    def get_population(self, name):
        return self.population[name]
# ===================== Inject database end =====================



class SingletonTests(unittest.TestCase):
    # (1) test singleton
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    # (2) test total population
    def test_singlton_total_population(self):
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(17500000+17400000, tp)

    ddb = DummyDatabase()
    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(3, crf.total_population(['gamma']))

if __name__ == '__main__':
    unittest.main()