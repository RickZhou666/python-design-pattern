from typing import Any
from unittest import TestCase
import unittest


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
            iterate from rat1 -> rat2 -> rat3
        """
        for item in self:
            item(*args, **kwds)

class Game():
    def __init__(self):
        self.rat_enters = Event()
        self.rat_dies = Event()
        self.notify_rat = Event()


class Rat:
    def __init__(self, game):
        """
            initialize a new rat
            add for notification
            and check # of rats
        """
        self.game = game
        self.attack = 1

        game.rat_enters.append(self.rat_enters)
        game.notify_rat.append(self.notify_rat)
        game.rat_dies.append(self.rat_dies)

        # pass rat3 into __call__ function, and traverse each method with variable rat3
        self.game.rat_enters(self)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rat_dies(self)

    def rat_enters(self, which_rat):
        """
            if game.rat_enters has more than 1 rat
            the later compare to the first will be different, then we increase later rat number by 1

            and we need increase the which rat attack as well
        """
        if which_rat != self:
            self.attack += 1 # increase rat1
            self.game.notify_rat(which_rat) # notify rat3

    def notify_rat(self, which_rat):
        if which_rat == self:
            self.attack += 1
    
    def rat_dies(self, which_rat):
        self.attack -= 1

class Evaluate(TestCase):
    # def test_single_rat(self):
    #     game = Game()
    #     rat = Rat(game)
    #     self.assertEqual(1, rat.attack)

    # def test_two_rats(self):
    #     game = Game()
    #     rat = Rat(game)
    #     rat2 = Rat(game)
    #     self.assertEqual(2, rat.attack)
    #     self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)
        # after end of this with clause, it will trigger __exit__ function, which is rat_dies

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        
if __name__ == '__main__':
    unittest.main()
