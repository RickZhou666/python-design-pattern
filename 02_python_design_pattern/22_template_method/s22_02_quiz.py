from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        # todo
        self.hit(self.creatures[c1_index], self.creatures[c2_index])
        if self.creatures[c1_index].health > 0 and self.creatures[c2_index].health > 0\
            or self.creatures[c1_index].health < 0 and self.creatures[c2_index].health < 0 :
            return -1
        elif self.creatures[c1_index].health < 0:
            return c2_index
        else:
            return c1_index


    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    # todo
    def __init__(self, creatures):
        super().__init__(creatures)

    def hit(self, attacker, defender):
        self.creatures[defender].health -= self.creatures[attacker].attack
        if self.creatures[defender].health > 0:
            self.creatures[defender].health += self.creatures[attacker].attack


class PermanentDamageCardGame(CardGame):
    def __init__(self, creatures):
        super().__init__(creatures)

    def hit(self, attacker, defender):
        self.creatures[defender].health -= self.creatures[attacker].attack
        